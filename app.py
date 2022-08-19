from dash import Dash, dcc, html, Input, State, Output, callback
from landing_page import landing_page_layout
from Image_Captioning_page import *
import dash_bootstrap_components as dbc
from dash import ctx
import requests

app = Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY],suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])

app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    
    html.Div(id='page-content')
])


@app.callback(Output('output-image-upload', 'children'),
              Output('caption', 'children'),
              Output('collapse-div', 'children'),
              Output('attention-card', 'children'),
              Input('upload-image', 'contents'),
              Input('upload-image','filename'),
              Input('drag-drop-uploader', 'contents'),
              Input('drag-drop-uploader','filename'),
              Input('im1', 'n_clicks'),
              Input('im2', 'n_clicks'),
              Input('im3', 'n_clicks'),
              Input('im4', 'n_clicks'),
              Input('im5', 'n_clicks'),
              Input('im6', 'n_clicks'),
              Input('im7', 'n_clicks'),
              Input('im8', 'n_clicks'),
              Input('im9', 'n_clicks'),
              Input('URL-btn', 'n_clicks'),
              State('im1', 'src'),
              State('im2', 'src'),
              State('im3', 'src'),
              State('im4', 'src'),
              State('im5', 'src'),
              State('im6', 'src'),
              State('im7', 'src'),
              State('im8', 'src'),
              State('im9', 'src'),
              State('URL-box', 'value'),
              prevent_initial_call=True)

def update_output(content_browse, filename_browse, content_drag_drop, filename_drag_drop, c1, c2, c3, c4, c5, c6, c7, c8, c9, c_url, s1, s2, s3, s4, s5, s6,
                  s7, s8, s9, s_url):
    triggered_id = ctx.triggered_id
    if triggered_id == 'upload-image':
        base64_code_start_idx = content_browse.index(',')
        image_base64 = content_browse
        image = Image.open(BytesIO(base64.b64decode(image_base64[base64_code_start_idx:])))
        children, caption, expanded, attention_image_browser = pass_img_to_model(content_browse, image)
        if filename_browse == 'my_developer__.jpeg':
                caption = "My developers \U0001F60D \U0001F60D"
                expanded = collapsed        
        return children, caption, expanded, attention_image_browser


    elif triggered_id == 'drag-drop-uploader':
        base64_code_start_idx = content_drag_drop.index(',')
        image_base64 = content_drag_drop
        image = Image.open(BytesIO(base64.b64decode(image_base64[base64_code_start_idx:])))
        children, caption, expanded, attention_image_browser = pass_img_to_model(content_browse, image)
        if filename_drag_drop == 'my_developer__.jpeg':
                caption = "My developers \U0001F60D \U0001F60D"
                expanded = collapsed
        return children, caption, expanded, attention_image_browser



    elif triggered_id == 'URL-btn':
        response = requests.get(s_url)
        image = Image.open(BytesIO(response.content))
        return pass_img_to_model(s_url, image)


    elif triggered_id == 'im1':
        image = Image.open(s1)
        return pass_img_to_model(s1, image)

    elif triggered_id == 'im2':
        image = Image.open(s2)
        return pass_img_to_model(s2, image)

    elif triggered_id == 'im3':
        image = Image.open(s3)
        return pass_img_to_model(s3, image)

    elif triggered_id == 'im4':
        image = Image.open(s4)
        return pass_img_to_model(s4, image)

    elif triggered_id == 'im5':
        image = Image.open(s5)
        return pass_img_to_model(s5, image)

    elif triggered_id == 'im6':
        image = Image.open(s6)
        return pass_img_to_model(s6, image)

    elif triggered_id == 'im7':
        image = Image.open(s7)
        return pass_img_to_model(s7, image)

    elif triggered_id == 'im8':
        image = Image.open(s8)
        return pass_img_to_model(s8, image)

    elif triggered_id == 'im9':
        image = Image.open(s9)
        return pass_img_to_model(s9, image)


@app.callback(
    Output("attention-collapse", "is_open"),
    [Input("attention-button", "n_clicks")],
    [State("attention-collapse", "is_open")],
    prevent_initial_call=True
)
def toggle_left(n_left, is_open):
    if n_left:
        return not is_open
    return is_open



# Update the index
@callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return landing_page_layout
    elif pathname == '/Image_Captioning':
        return Image_captioning_layout
    # You could also return a 404 "URL not found" page here

if __name__ == '__main__':
    app.run_server(debug=True, port= 8888)