import dash
from dash import html, dcc


dash.register_page(__name__, path='/')



layout = html.Div(children = [
            html.Div(children =[
                html.H1(children='BOSS CLUB'),
                html.H3(children='MAKE GOOD CHOICES, BE GOOD PEOPLE'),
                ], style = {'margin-top':'37%', 'margin-left': '4%', "border":"2px black solid", 'width':'30%', 'padding-left':'3%'}
            ),
            html.Div(children = [
                html.H1(children = "Upcoming Event"),
                html.H3(children = "FOOD FINDERS")
            ], style = {'display' : 'inline-text', 'float' : 'right', "border":"2px black solid", 'width':'30%', 'padding-left':'3%'})

    ]
)
