import dash
from dash import html, dcc

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='This is our profile page'),
    dcc.Link(html.Button("Return home"), href="/home", refresh=True)


])
