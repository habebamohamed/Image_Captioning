import dash_bootstrap_components as dbc
from dash import dcc, html
from styles import * 
from main_functions import *


demos = [
    dbc.Row([
        dbc.Col(html.Img(src="assets/demos/10.jpg", style=THUMBNAIL_STYLE, id='im1'), style=THUMB_COL_STYLE),
        dbc.Col(html.Img(src="assets/demos/11.jpg", style=THUMBNAIL_STYLE, id='im2'), style=THUMB_COL_STYLE),
        dbc.Col(html.Img(src="assets/demos/8.jpg", style=THUMBNAIL_STYLE, id='im3'), style=THUMB_COL_STYLE),
    ], style={'margin': 'auto', 'padding': '0rem'}),

    dbc.Row([
        dbc.Col(html.Img(src="assets/demos/1.jpg", style=THUMBNAIL_STYLE, id='im4'), style=THUMB_COL_STYLE),
        dbc.Col(html.Img(src="assets/demos/20.jpeg", style=THUMBNAIL_STYLE, id='im5'), style=THUMB_COL_STYLE),
        dbc.Col(html.Img(src="assets/demos/21.jpeg", style=THUMBNAIL_STYLE, id='im6'), style=THUMB_COL_STYLE),
    ], style={'margin': 'auto', 'padding': '0rem'}),

    dbc.Row([
        dbc.Col(html.Img(src="assets/demos/7.jpg", style=THUMBNAIL_STYLE, id='im7'), style=THUMB_COL_STYLE),
        dbc.Col(html.Img(src="assets/demos/14.jpg", style=THUMBNAIL_STYLE, id='im8'), style=THUMB_COL_STYLE),
        dbc.Col(html.Img(src="assets/demos/9.jpg", style=THUMBNAIL_STYLE, id='im9'), style=THUMB_COL_STYLE),
    ], style={'margin': 'auto', 'padding': '0rem'}),

]

uploader = dcc.Upload(
    id='upload-image',
    children=html.Button('Browse', id='upload-btn', className="btn btn-info",
                         style={'width': '100%', 'height': '3rem', 'font-size': '140%'})
    ,
    style={
        'width': '85%',
        'height': '3rem',
        'textAlign': 'center',
        'margin': 'auto',
        'cursor': 'pointer',
    },
    # Allow multiple files to be uploaded
    multiple=False,
)

drag_drop = dcc.Upload(
    id='drag-drop-uploader',
    children=[
        html.Img(src="assets/demos/img_template.jpg", style=MAIN_IMG_STYLE),
        html.P('Drag and drop to upload an image.', className="form-text text-muted", id='drag-drop-p',
               style={'width': '100%', 'height': '100%', 'font-weight': '500', 'font-size': '140%',
                      'position': 'absolute', 'top': '100%', 'left': '50%', 'transform': 'translate(-50%, -55%)'})
    ],
    style={
        'width': '80%',
        'height': '25rem',
        'textAlign': 'center',
        'margin': 'auto',
        'padding': 'auto'
    },
    # Allow multiple files to be uploaded
    multiple=False,
    disable_click=True
)

sidebar = [

    dbc.Row(
        html.H3("Intelligent Scene Captioning", style={"text-align": "center", 'color': '#ffffff'}, className="h1")),
    dbc.Row(html.Hr(
        style={'border': '0.0625rem solid #b0aeae', 'margin': 'auto', 'margin-bottom': '2rem', 'margin-top': '1.5rem',
               'width': '70%'})),
    dbc.Row(html.H4("Demos", style={'color': '#ffffff', 'margin-bottom': '1rem'})),
    dbc.Row(demos, style={'text-align': '-webkit-center'}),
    dbc.Row(
        html.H4("Try a new image", style={'color': '#ffffff', 'margin-bottom': '1.625rem', 'margin-top': '3.125rem'})),
    dbc.Row(uploader),
    dbc.Row(html.P("- Or -", className='lead',
                   style={"text-align": "center", 'color': '#ffffff', 'margin-top': '5%', 'margin-bottom': '5%',
                          'font-size': '130%'})),
    dbc.Row([
        dbc.Col(
            dcc.Input(placeholder="Image URL",
                      id='URL-box',
                      style={'width': '95%',
                             'height': '3rem',
                             'margin-right': '0.3125rem',
                             'margin-left': '11%',
                             'font-size': '125%',
                             }, className='form-control')
            , width=8),

        dbc.Col(
            html.Button('Go', id='URL-btn', className="btn btn-success",
                        style={'width': '75%', 'height': '3rem', 'font-size': '140%', 'margin-left': '0rem'})
            , width=4)
    ])

]

collapsed = [
    dbc.Row(
        dbc.Button(
            "Show Attention Plot \U0001F447",
            id="attention-button",
            className="btn btn-success disabled",
            n_clicks=0,
            style={'font-size': '140%', 'width': '25%', 'margin': 'auto'}
        )
    ),

    dbc.Row(
        dbc.Collapse(
            dbc.Card("This is the left card!", id='attention-card', body=True),
            id="attention-collapse",
            is_open=False,
        )
    )

]

expanded = [
    dbc.Row(
        dbc.Button(
            "Show Attention Plot \U0001F447",
            id="attention-button",
            className="btn btn-success",
            n_clicks=0,
            style={'font-size': '140%', 'width': '25%', 'margin': 'auto'}
        )
    ),

    dbc.Row(
        dbc.Collapse(
            dbc.Card("Here is the attention plot!", id='attention-card', body=True, className='border-0'),
            id="attention-collapse",
            is_open=False,
            style={'width': '100%'}
        )
    )

]

content = [
    dbc.Row(drag_drop, style={'text-align': '-webkit-center', 'margin-top': '5%'}, id='output-image-upload'),
    dbc.Row(html.P("Your caption will appear here once you choose an image", id='caption',
                   style={'text-align': 'center', 'font-size': '140%'}),
            style={'margin': 'auto', 'margin-top': '3.125rem', 'width': '70%'},
            className="alert alert-dismissible alert-info"),
    dbc.Row(collapsed, id='collapse-div', style={'text-align': '-webkit-center', 'margin-top': '3.125rem'})
]

Image_captioning_layout = dbc.Row([
    dbc.Col(sidebar, style=SIDEBAR_STYLE, width=3),
    dbc.Col(content, id="page-content", width=8)
], style={'margin':'0rem', 'padding':'0rem', 'width':'100%', 'height':'100vh'})

def pass_img_to_model(img_src, image):
    pil_img = image
    image = np.array(image)
    image = img_preprocess(image)
    caption, attention_plot = img_captioning(image)
    data = plot_attention(pil_img, caption, attention_plot)
    attention_image_browser = html.Img(src=data, className='', style= PLOT_IMG_STYLE)
    children = [
        dcc.Upload(
            id='drag-drop-uploader',
            children=[
                html.Img(src=img_src, style=MAIN_IMG_STYLE),
            ],
            style={
                'width': '80%',
                'height': '25rem',
                'textAlign': 'center',
                'margin': 'auto',
                'padding': 'auto'
            },
            # Allow multiple files to be uploaded
            multiple=False,
            disable_click=True
        )
    ]
    caption = ' '.join(caption[1:-1])
    return children, caption, expanded, attention_image_browser