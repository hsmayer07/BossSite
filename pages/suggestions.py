import dash
from dash import Dash, html, dcc, callback, Input

dash.register_page(__name__)

layout = html.Div([
    dcc.Textarea(
        id = 'suggestions-box',
        value = 'Type your suggestions here.',
        style={'width': '100%', 'height': 300},
    ),
    ##html.Button('Submit', id='textarea-state-example-button', n_clicks=0),
    html.Div(id='suggestions-box', style={'whiteSpace': 'pre-line'})
])
