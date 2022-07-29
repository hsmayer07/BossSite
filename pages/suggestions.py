import dash
import smtplib
from dash.dependencies import Input, Output, State
from dash import Dash, html, dcc, callback, Input

dash.register_page(__name__,)
layout = html.Div([
    dcc.Textarea(
        id = 'suggestions_box',
        value = 'Type your suggestions here.',
        style={'width': '100%', 'height': 300},
        ),

    html.Button('Submit', id='submit_button', n_clicks=0),
    #html.Div(id='suggestions_box_output', style={'whiteSpace': 'pre-line'})
    ])

@callback(
        #Output('suggestions_box_output', 'children'),
        Output('suggestions_box', "value"),
        Input('submit_button', 'n_clicks'),
        State('suggestions_box', 'value')
        )

def update_output(n_clicks, value):
    if n_clicks > 0:

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            subject = 'New BOSS suggestion'
            smtp.login('mahadkhalid4955@gmail.com','etmwfqvkoeeaeval')
            msg = f'Subject: {subject}\n\n{value}'
            smtp.sendmail('mahadkhalid4955@gmail.com', 'mahadkhalid4955@gmail.com', msg)
            return 'Thanks for adding a suggestion!'



