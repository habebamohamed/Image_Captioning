import numpy as np
import tensorflow as tf

from PIL import Image
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import pickle
from classes import *

max_length = 30
attention_features_shape = 49

def img_reading(content):
    base64_code_start_idx = content.index(',')
    image_base64 = content
    image = Image.open(BytesIO(base64.b64decode(image_base64[base64_code_start_idx:])))
    image = np.array(image)
    return image

def img_preprocess(raw_img):
    img = tf.keras.layers.Resizing(224, 224)(raw_img)
    img = tf.keras.applications.vgg16.preprocess_input(img)
    img = tf.expand_dims(img, 0)
    return img
 
def fig2data ( fig ):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw ( )
    # Get the RGBA buffer from the figure
    w,h = fig.canvas.get_width_height()
    buf = np.fromstring ( fig.canvas.tostring_argb(), dtype=np.uint8 )
    buf.shape = ( w, h, 4 )
 
    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll ( buf, 3, axis = 2 )
    return buf
  
def fig2img ( fig ):
    """
    @brief Convert a Matplotlib figure to a PIL Image in RGBA format and return it
    @param fig a matplotlib figure
    @return a Python Imaging Library ( PIL ) image
    """
    # put the figure pixmap into a numpy array
    buf = fig2data ( fig )
    w, h, d = buf.shape
    return Image.frombytes( "RGBA", ( w ,h ), buf.tostring( ) )

def plot_attention(image, result, attention_plot):
    temp_image = np.array(image)

    fig = plt.figure(figsize=(10, 10))

    len_result = len(result)
    for i in range(len_result):
        temp_att = np.resize(attention_plot[i], (8, 8))
        grid_size = max(int(np.ceil(len_result/2)), 2)
        ax = fig.add_subplot(grid_size, grid_size, i+1)
        ax.set_title(result[i])
        img = ax.imshow(temp_image)
        ax.imshow(temp_att, cmap='gray', alpha=0.6, extent=img.get_extent())
        ax.get_yaxis().set_visible(False)
        ax.get_xaxis().set_visible(False)

    im = fig2img(fig)
    arr = np.array(im)
    y=0
    x=0
    h=im.height - 420
    w=im.width
    crop_image = arr[y:h, x:w]
    im = Image.fromarray(crop_image)
    
    return im

def evaluate(image, decoder, encoder, tokenizer, w_i, i_w):
    attention_plot = np.zeros((max_length, attention_features_shape))
    # figure = attention_plot
    hidden = decoder.reset_state(batch_size=1)

    img_tensor_val = tf.reshape(image, (image.shape[0],
                                                 -1,
                                                 image.shape[3]))

    features = encoder(img_tensor_val)
    dec_input = tf.expand_dims([w_i('<start>')], 0)
    result = []
    for i in range(tokenizer.get_config()['output_sequence_length']):
        predictions, hidden, attention_weights = decoder(dec_input,
                                                         features,
                                                         hidden)

        attention_plot[i] = tf.reshape(attention_weights, (-1, )).numpy()
        predicted_id = tf.argmax(predictions[0])
        predicted_word = tf.compat.as_text(i_w(predicted_id).numpy())
        result.append(predicted_word)
        if predicted_word == '<end>':
            return result, attention_plot

        dec_input = tf.expand_dims([predicted_id], 0)
    attention_plot = attention_plot[:len(result), :]
    return result, attention_plot


def standardize(inputs):
    inputs = tf.strings.lower(inputs)
    return tf.strings.regex_replace(inputs,
                                  r"!\"#$%&\(\)\*\+.,-/:;=?@\[\\\]^_`{|}~", "")

def img_captioning(preprocessed_img):
    # features extraction model
    image_model = tf.keras.applications.vgg16.VGG16(include_top=False,  input_shape=(224, 224, 3), weights='imagenet')
    new_input = image_model.input
    hidden_layer = image_model.layers[-1].output
    image_features_extract_model = tf.keras.Model(new_input, hidden_layer)
    features_of_img = image_features_extract_model(preprocessed_img)


    # load our tokenizer object
    pickle_tokenizer = pickle.load(open("tokenizer.pkl", "rb"))
    tokenizer = tf.keras.layers.TextVectorization.from_config(pickle_tokenizer['config'])
    tokenizer.set_weights(pickle_tokenizer['weights'])

    # Create mappings for words to indices and indices to words.
    word_to_index = tf.keras.layers.StringLookup(
        mask_token="",
        vocabulary=tokenizer.get_vocabulary())
    index_to_word = tf.keras.layers.StringLookup(
        mask_token="",
        vocabulary=tokenizer.get_vocabulary(),
        invert=True)

    # shapes
    embedding_dim = 256
    units = 512
    features_shape = 512
    attention_features_shape = 49

    # decoder_encoder creation
    encoder = CNN_Encoder(embedding_dim)
    decoder = RNN_Decoder(embedding_dim, units, tokenizer.vocabulary_size())

    optimizer = tf.keras.optimizers.Adam()
    loss_object = tf.keras.losses.SparseCategoricalCrossentropy(
    from_logits=True, reduction='none')

    checkpoint_path = "./checkpoints_08082022/train"
    ckpt = tf.train.Checkpoint(encoder=encoder,
                               decoder=decoder,
                               optimizer=optimizer)
    ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)

    ckpt.restore(ckpt_manager.latest_checkpoint)

    # evaluation
    result, attention_plot = evaluate(features_of_img, decoder, encoder, tokenizer, word_to_index, index_to_word)

    return result, attention_plot