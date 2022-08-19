import dash_bootstrap_components as dbc
from dash import html

P_FONT_STYLE = {'font-family': 'assets/landing_page/Barlow Condensed/BarlowCondensed-Medium.ttf', 'font-size' : '25px', 'text-align' : 'justify'}

#################################################### Content ####################################################
OVERVIEW_p1 = ''' Caption generation is a challenging artificial intelligence problem where a textual description must be generated for a given photograph.It requires both methods from computer vision to understand the content of the image and a language model from the field of natural language processing to turn the understanding of the image into words in the right order.'''
OVERVIEW_p2 = '''the image is first divided into n parts, and we compute with a Convolutional Neural Network (CNN) representations of each part h1,…, hn. When the RNN is generating a new word, the attention mechanism is focusing on the relevant part of the image, so the decoder only uses specific parts of the image.'''
OVERVIEW = dbc.Col([
            html.Div(
                children = [
                    html.Ul([
                            html.Li(OVERVIEW_p1),
                            html.Li(OVERVIEW_p2),
                    ]) ,   
                ]        
            ),
        ], className=' my-auto text-left ', style = P_FONT_STYLE)

####################################################################################################################
DATASET = dbc.Col([
            html.P('What is COCO ?', className = 'font-weight-bold', style =  {'font-size' : '35px', 'font-family': 'assets/landing_page/Barlow Condensed/BarlowCondensed-Medium.ttf'}),
            html.P('''The MS COCO dataset is maintained by a team of contributors, and sponsored by Microsoft, Facebook, and other organizations. MS COCO is composed of several datasets created in different years\n each one focuses on a different computer vision task, such as:  ''',style = P_FONT_STYLE),
            html.Div(
                children = [
                    html.Ul([
                            html.Li("Object segmentation"),
                            html.Li("Keypoint tracking"),
                            html.Li("Image captioning"),
                    ]) ,   
                ]        
            ),
            html.P('''The image captioning training dataset consists of more than 100, 000 images with five independent human generated captions are be provided for each image.''')
        ], className=' my-auto pl-2 text-left text-justify', style = P_FONT_STYLE)


####################################################################################################################

encoder_p = ''' It's a convolutional neural network that takes in an image and extracts the most important features and landmarks from it.\n
            Later, this feature map is passed to the decoder, which relies on it to generate a caption that fits that image.'''
vgg_p1 = ''' It's an innovative object-recognition model that supports up to 19 layers. Built as a deep CNN\n 
            Here we used VGG16 which is one of the most popular algorithms for image classification and is easy to use with transfer learning. '''
ENCODER = dbc.Col([
            html.P('Encoder ?', className = 'font-weight-bold',  style =  {'font-size' : '35px', 'font-family': 'assets/landing_page/Barlow Condensed/BarlowCondensed-Medium.ttf'}),
            html.P(encoder_p),
            html.P('VGG ?', className = 'font-weight-bold', style =  {'font-size' : '35px', 'font-family': 'assets/landing_page/Barlow Condensed/BarlowCondensed-Medium.ttf'}),
            html.P(vgg_p1),
        ], className=' my-auto ml-3 px-5 text-left text-justify ml-3', style = P_FONT_STYLE)

####################################################################################################################

embedding_p1 = ''' It’s a layer that studies the captions' vocabulary words and gives them a numerical representation.\n
            This numerical representation encodes the meaning of the word such that the words that are closer in the vector space are said to be similar in meaning. '''
embedding_p2 = ''' Word embeddings are basically a form of word representation that bridges the human understanding of language to that of a machine. Word embeddings are distributed representations of text in an n-dimensional space.'''
EMBEDDING =  dbc.Col([
            html.P('Why do we need word embedding ?', className = 'font-weight-bold',  style =  {'font-size' : '35px', 'font-family': 'assets/landing_page/Barlow Condensed/BarlowCondensed-Medium.ttf'}),
                    html.Ul([
                            html.Li(embedding_p1),
                            html.Li(embedding_p2),
                    ])   

        ], className=' my-auto ml-3 px-5 text-left text-justify ml-3', style = P_FONT_STYLE)
####################################################################################################################

attention_p1 = ''' The attention mechanism was introduced to address the bottleneck problem that arises with the use of a fixed-length encoding vector, where the decoder would have limited access to the information provided by the input.'''
attention_p2 = ''' This module takes in the feature map of the image along with the previous decoder's hidden state and tries to learn the relationship between them using a fully connected network.\n
                   Later, this relationship will tell the decoder which parts of the image to focus on in order to generate the next word. '''
ATTENTION = dbc.Col([
            html.P('What is the attention mechanism ?', className = 'font-weight-bold',  style =  {'font-size' : '35px', 'font-family': 'assets/landing_page/Barlow Condensed/BarlowCondensed-Medium.ttf'}),
            html.P(attention_p1),
            html.P(attention_p2),
        ], className=' my-auto ml-3 px-5 text-left text-justify ml-3', style = P_FONT_STYLE)

####################################################################################################################

decoder_p = ''' It's a recurrent neural network that consists of GRU cells that generate a word at each time step.\n
              These GRU cells help the model learn long sequences at a low computational cost.\n
              At each time step, the decoder uses the attention module to focus on specific parts of the image and generates a new word. '''

gru_p = ''' It's a gating mechanism in recurrent neural networks utilises different ways of gating information to prevent vanishing gradient problems.\n'''
gru_li1 = '''Controls the flow of information without having to use a memory unit.\n'''
gru_li2 = '''Just exposes the full hidden content without any control.''' 
gru_li3 = '''Computationally efficient.'''
DECODER_p1 = dbc.Col([
    html.P('Decoder ?', className = 'font-weight-bold',  style =  {'font-size' : '35px', 'font-family': 'assets/landing_page/Barlow Condensed/BarlowCondensed-Medium.ttf'}),
    html.P(decoder_p),
    html.P('GRU ?', className = 'font-weight-bold', style =  {'font-size' : '35px', 'font-family': 'assets/landing_page/Barlow Condensed/BarlowCondensed-Medium.ttf'}),
        html.P(gru_p),
        html.Div(
                children = [
                    html.Ul([
                            html.Li(gru_li1),
                            html.Li(gru_li2),
                            html.Li(gru_li3),
                    ])   
                ], style = P_FONT_STYLE
        )
], className=' my-auto ml-3 px-5 text-left text-justify ml-3 ', style = P_FONT_STYLE)
