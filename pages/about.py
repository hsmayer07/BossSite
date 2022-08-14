import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
dash.register_page(__name__,)


                #'backgroundColor':'darkslategray',

layout = html.Div([
        html.H1("About BOSS"),
        html.Div(children=[
            html.H3("Who We Are"),
            html.H3("Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. ")
        ],className="box1",
            style={
                'height':'100px',
                'margin-left':'10px',
                'width':'30%',
                'display':'inline-block'
                }),
        html.Div(children=[
            html.H3("Our Purpose"),
            html.H3("Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. ")
        ],className="box1",
            style={
                'height':'100px',
                'margin-left':'10px',
                'width':'30%',
                'display':'inline-block'
                }),
        html.Div(children=[
            html.H3("Our History"),
            html.H3("Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. Boss is a club. ")
        ],className="box1",
            style={
                'height':'100px',
                'margin-left':'10px',
                'width':'30%',
                'display':'inline-block'
                }),

], style = {"text-align" : "center"})
