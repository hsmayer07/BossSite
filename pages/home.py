import dash
from dash import html, dcc


dash.register_page(__name__,)



layout = html.Div(children = [
            html.Div(children =[
                html.H1(children='BOSS CLUB'),
                html.H3(children='MAKE GOOD CHOICES, BE GOOD PEOPLE'),
                ], style = {'margin-top':'550px', 'margin-left': '50px', "border":"2px black solid", 'width':'30%', 'padding-left':'5%'}
            )



    ]
)
