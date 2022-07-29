import dash
from dash import Dash, html, dcc, callback, Input

dash.register_page(__name__)

<<<<<<< HEAD
layout = html.Div([
    dcc.Textarea(
        id = 'suggestions-box',
        value = 'Type your suggestions here.',
        style={'width': '100%', 'height': 300},
    ),
    ##html.Button('Submit', id='textarea-state-example-button', n_clicks=0),
    html.Div(id='suggestions-box', style={'whiteSpace': 'pre-line'})
=======
layout = html.Div(children=[
    html.H1(children='This is our suggestions page'),
    dcc.Link(html.Button("Return home"), href="/home", refresh=True)

>>>>>>> d896c346346d01356c5ff9945c171a477579ddb7
])
