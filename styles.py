#################################################### Styles ####################################################
################################################# landing page #################################################

DARK_OVERLAY = {
    'background': 'rgba(0, 0, 0, 0.5)',
    'position': 'absolute',
    'top': '-10',
    'left': '0',
    'width': '100%',
    'height': '100%'
}

BG_STYLE = {
    'position': 'relative',
    'background': 'url("assets/landing_page/BG.png")',
    'background-repeat': 'no-repeat',
    'background-size' : '100% 100%',
    'min-height': '300px' 
}

R_U_READY_STYLE = {
    'position': 'relative',
    'min-height': '150px',
    'background':' url(assets/landing_page/lights.jpg)',
    'background-size' : '100% 100%',
    'background-attachment': 'fixed',
    'background-repeat': 'no-repeat',
    'text-align': 'center',
    'color': '#fff'
}
P_FONT_STYLE = {'font-family': 'assets/landing_page/Barlow Condensed/BarlowCondensed-Medium.ttf', 'font-size' : '25px'}
################################################# Image Captioning page #################################################

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    'margin-left': '6.25rem',
    'margin-right': '0rem',
    "top": 0,
    "bottom": 0,
    "padding": "2rem",
    "background-color": "#424141",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.

THUMBNAIL_STYLE = {
    'border': '0.0625rem solid #ddd',
    'border-radius': '0.25rem',
    'padding': '0.3125rem',
    'width': '95%',
    'height': '4rem',
    'object-fit': 'cover',
    'cursor': 'pointer'
}

THUMB_COL_STYLE = {'margin-top': '0.625rem'}


MAIN_IMG_STYLE = {
    'height': '25rem',
    'max-width': '100%',
    'max-height': '41.75rem',
    'margin': 'auto',
    'padding': 'auto',
    'borderWidth': '0.0625rem',
    'borderStyle': 'dashed',
    'borderRadius': '0.3125rem',
    'border-color': 'gray',
    'object-fit': 'cover'
}


PLOT_IMG_STYLE = {
    'width' : '100%',
    'margin' : '-20px'
}