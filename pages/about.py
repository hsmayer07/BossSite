import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
dash.register_page(__name__,)


                #'backgroundColor':'darkslategray',

layout = html.Div([
    
    html.Div([
        html.Div(children="Who Are We",className="box1",
            style={
                'color':'lightsteelblue',
                'height':'100px',
                'margin-left':'10px',
                'width':'33%',
                'display':'inline-block'
                }),

        html.Div(children="Our Purpose",className="box2",
            style={
                'color':'lightsteelblue',
                'height':'100px',
                'margin-left':'10px',
                'width':'33%',
                'display':'inline-block'
                }),
        html.Div(children="Our History",className="box3",
            style={
                'color':'lightsteelblue',
                'height':'100px',
                'margin-left':'10px',
                'width':'33%',
                'display':'inline-block'
                }),

    ]),
])
