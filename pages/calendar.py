import dash
from dash import html, dcc

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='This is our calendar page'),
    dcc.Link(html.Button("Return home"), href="/home", refresh=True),
    html.Iframe(src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FIndiana%2FIndianapolis&src=YXFoMW0zcmlhNHQyOWJsc2NjNDRtc2ZodmtAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&color=%233F51B5", style={'frameborder':'0', 'overflow':'hidden', 'overflow-x':'hidden','overflow-y':'hidden', 'height':'100%', 'width':'100%','position':'absolute', 'top':'0px', 'left': '0px', 'right':'0px', 'bottom':'0px', 'height':'100%', 'width':'100%'})
])

##, style={"border:solid 1px #777", 'width': '800%', 'height':'600', 'frameborder':'0','scrolling':'no'}

##style={'frameborder':'0''overflow':'hidden', 'overflow-x':'hidden','overflow-y':'hidden', 'height':'100%', 'width':'100%','position':'absolute', 'top':'0px', 'left': '0px', 'right':'0px', 'bottom':'0px', 'height':'100%', 'width':'100%'}

##style={'border':'solid 1px #777', 'width': '100%', 'height':'100%', 'frameborder':'0','scrolling':'no'}
