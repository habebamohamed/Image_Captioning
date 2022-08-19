from turtle import width
from dash import html
import dash_bootstrap_components as dbc

# from style import * 
from content import *
from styles import * 

#################################################### Cards ####################################################
CARD_IMG = {'width' : '50%', 'margin-bottom' : '1rem'}
CARD_BTN = "btn btn-outline-light text-black position-sticky sticky-top d-block"
CARD_FONT = {'font-size' :'30px','font-family': 'assets/landing_page/Barlow Condensed/BarlowCondensed-Medium.ttf', 'font-weight': 'bold'}

card_content0 = [
    html.Div([
        html.Img(src = 'assets/landing_page/dataset.png', style= CARD_IMG),
            html.A(id='b-1',  children="Dataset", href ="#dataset_id", className = CARD_BTN, style = CARD_FONT),
    ])
]    
card_content1 = [
    html.Div([
        html.Img(src = 'assets/landing_page/encoder.png', style= CARD_IMG),
        html.A(id='b-2', children="Encoder", href ="#cnn_id", className = CARD_BTN, style = CARD_FONT),
    ])
]    
card_content2 = [
    html.Div([
        html.Img(src = 'assets/landing_page/word.png', style= CARD_IMG),
        html.A(id='b-3',children="Embedding",href ="#embedding_id", className = CARD_BTN, style = CARD_FONT),
    ])
]    
card_content3 = [
    html.Div([
        html.Img(src = 'assets/landing_page/attention.png', style= CARD_IMG),
        html.A(id='b-4',children="Attention", href ="#attention_id",className = CARD_BTN, style = CARD_FONT),
    ])
]   
card_content4 = [
    html.Div([
        html.Img(src = 'assets/landing_page/decoder.png', style= CARD_IMG),
        html.A(id='b-5',children="Decoder", href ="#rnn_id",className = CARD_BTN, style = CARD_FONT),
    ])
]    


landing_page_layout = dbc.Container([ 
#################################################### HEADER ####################################################
    dbc.Container([
                html.Div(
                    style = DARK_OVERLAY,
                    children = [
                       dbc.Row([
                            dbc.Col([
                                html.H1('Image Captioning',className='display-2 pt-5'),
                                html.H3('A way to see the world better',className=' mx-5')
                            ], className='my-auto'),
                            dbc.Col([
                                html.A( 'Try it now !',className='btn btn-danger btn-lg ', style={'margin-top': '100px', 'width' : '200px'}, href='/Image_Captioning')
                            ], className='my-auto ')
                       ],className='p-5 text-center text-white my-auto')
                    ]
                )
    ],fluid= True, style = BG_STYLE),

    
#################################################### OVERVIEW ####################################################
    
    dbc.Container([
        html.H1("Overview",className='display-3 text-center text-dark my-3 p-2'),
            dbc.Row([
                dbc.Col([html.Img(src="assets/landing_page/Model_Arch.png", className ='img-fluid mx-3 mb-3 bg-dark', style={'width' : '85%'})]),
                dbc.Col([html.P( OVERVIEW, style = P_FONT_STYLE), 
                ], className='my-auto px-4 text-left text-justify col-sm-12 col-md-6'),
            ])
    ],fluid =True, className='my-4 py-3'),
    
    
#################################################### ARE U READY ####################################################
    dbc.Container([
            html.Div(
                children = [
                    html.Div(
                        style = DARK_OVERLAY,
                        children = [
                           dbc.Row([
                                html.H1('Are You Ready To Get Started?', className='text-center'),
                                html.P('Now we will get a little deep on our architecture.',className='lead')
                           ],className='p-3 text-center text-white my-3')
                        ]
                    )
                ]
            ),
        ],fluid =True,className='mb-3', style= R_U_READY_STYLE),

#################################################### CARDS ####################################################
  
    dbc.Container([
        dbc.Row([
                    dbc.Col(dbc.Card(card_content0, className='text-center p-2 text-black w-100 border border-white', style = {'cursor' : 'pointer'})),
                dbc.Col(dbc.Card(card_content1, className='text-center p-2 text-black w-100 border border-white', style = {'cursor' : 'pointer'})),
                dbc.Col(dbc.Card(card_content2, className='text-center p-2 text-black w-100 border border-white', style = {'cursor' : 'pointer'})),
                dbc.Col(dbc.Card(card_content3, className='text-center p-2 text-black w-100 border border-white', style = {'cursor' : 'pointer'})),
                dbc.Col(dbc.Card(card_content4, className='text-center p-2 text-black w-100 border border-white', style = {'cursor' : 'pointer'})),
                # navbar
            ],justify='center'),
    ],fluid =True, className="my-4 "),

#################################################### BODY ####################################################

######################### DATASET #########################    
    
    dbc.Container([
                html.H1("Dataset",className='display-3 text-center card text-black mb-3 p-3 border border-white'),
                html.Hr(style={'border': '0.0625rem solid #b0aeae', 'margin':'auto', 'margin-bottom':'2rem', 'margin-top':'1.5rem', 'width':'100%'}),

                dbc.Row([
                        DATASET,
                        dbc.Col([
                            # html.Img(src="assets/landing_page/sponsers.png",className='img-fluid w-75 pt-5 mr-4 mt-5 d-flex align-items-end'),

                            html.Img(src="assets/landing_page/COCO.jpg",height='450px', className='d-inline')],className = 'col-sm-12 col-md-7 justify-content-center d-flex align-items-center'),
                ],className = ''),
             ],fluid =True,className='mb-5 px-5 pb-3', id = 'dataset_id'),

######################### ENCODER #########################    
    
    dbc.Container([
                html.H1("Encoder ( CNN ) ",className='display-3 text-center card text-black mb-3 p-3 border border-white'),
                html.Hr(style={'border': '0.0625rem solid #b0aeae', 'margin':'auto', 'margin-bottom':'2rem', 'margin-top':'1.5rem', 'width':'100%'}),

                dbc.Row([
                     dbc.Col([html.Img(src="assets/landing_page/VGG.png",height='450px')],className = 'col-sm-12 col-md-6 justify-content-center d-flex align-items-center'),
                     ENCODER
                ]),
             ],fluid =True,className='mb-5 px-5 pb-3', id = 'cnn_id'),
    
    
    
######################### WORD EMBEDDING #########################    
    
    dbc.Container([
                html.H1("Word Embedding",className='display-3 text-center card text-black mb-3 p-3 border border-white'),
                html.Hr(style={'border': '0.0625rem solid #b0aeae', 'margin':'auto', 'margin-bottom':'2rem', 'margin-top':'1.5rem', 'width':'100%'}),

                dbc.Row([
                    EMBEDDING,
                     dbc.Col([html.Img(src="assets/landing_page/embedding.png",height='450px')],className = 'col-sm-12 col-md-6 justify-content-center d-flex align-items-center'),
                ]),
             ],fluid =True,className='mb-5 px-5 pb-3',id = 'embedding_id'),


######################### ATTENTION #########################    
    
    dbc.Container([
                html.H1("Attention",className='display-3 text-center card text-black mb-3 p-3 border border-white'),
                html.Hr(style={'border': '0.0625rem solid #b0aeae', 'margin':'auto', 'margin-bottom':'2rem', 'margin-top':'1.5rem', 'width':'100%'}),

                dbc.Row([
                     dbc.Col([html.Img(src="assets/landing_page/localAttention.png",height='450px')],className = 'col-sm-12 col-md-6 justify-content-center d-flex align-items-center'),
                     ATTENTION,
                ]),
             ],fluid =True,className='mb-5 px-5 pb-3',id = 'attention_id'),
    
    
    
######################### DECODER #########################    
    dbc.Container([
                html.H1("Decoder ( RNN )",className='display-3 text-center card text-black mb-3 p-3 border border-white'),
                html.Hr(style={'border': '0.0625rem solid #b0aeae', 'margin':'auto', 'margin-bottom':'2rem', 'margin-top':'1.5rem', 'width':'100%'}),

                dbc.Row([
                     DECODER_p1,
                    #  DECODER_p2,
                     dbc.Col([html.Img(src="assets/landing_page/GRU.png", height='450px')], className = 'col-sm-12 col-md-6 justify-content-center d-flex align-items-center'),
                ]),
             ],fluid =True,className='mb-5 px-5 pb-3', id = 'rnn_id'),

 
], fluid=True )   



