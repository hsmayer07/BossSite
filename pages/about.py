import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
dash.register_page(__name__,)


                #'backgroundColor':'darkslategray',

layout = html.Div([
        html.Div([
            html.H1("About BOSS"),
            dcc.Link(html.Button("Return home"), href="/", refresh=True),
        ]),
        html.Div(children=[
            html.H3("Who We Are"),
            html.H3("Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.")
        ],className="box1",
            style={
                'height':'100px',
                'margin-left':'10px',
                'width':'30%',
                'height':'500%',
                'display':'inline-block',
                "border":"2px black solid"
                }),
        html.Div(children=[
            html.H3("Our Purpose"),
            html.H3("Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. ")
        ],className="box1",
            style={
                'height':'100px',
                'margin-left':'10px',
                'width':'30%',
                'height':'500%',
                'display':'inline-block',
                "border":"2px black solid"
                }),
        html.Div(children=[
            html.H3("Our History"),
            html.H3("Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club.  ")
        ],className="box1",
            style={
                'height':'100px',
                'margin-left':'10px',
                'width':'30%',
                'height':'500%',
                'display':'inline-block',
                "border":"2px black solid"
                }),

], style = {"text-align" : "center", "height":"100%"})
