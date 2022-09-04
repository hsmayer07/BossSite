from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash
from flask import Flask, render_template, url_for, redirect
from authlib.integrations.flask_client import OAuth
import os
from dash.dependencies import Input, Output, State
import sqlite3
import db
from users import User
import smtplib

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)
server = app.server
server.secret_key = 'ertuyiokploiuygtfre'

'''
    Set SERVER_NAME to localhost as twitter callback
    url does not accept 127.0.0.1
    Tip : set callback origin(site) for facebook and twitter
    as http://domain.com (or use your domain name) as this provider
    don't accept 127.0.0.1 / localhost
'''

server.config['SERVER_NAME'] = '127.0.0.1:5000'
oauth = OAuth(server)

try:
	db.init_db_command();
except sqlite3.OperationalError:
	pass

#app.dump()
app.layout = html.Div(
	children = [
	dash.page_container
], style = {'margin-top' : '3%'})

@server.route('/google/')
def google():

    # Google Oauth Config
    # Get client_id and client_secret from environment variables
    # For developement purpose you can directly put it
    # here inside double quotes
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_AUTH_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_AUTH_CLIENT_SECRET')

    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    redirect_uri = url_for('google_auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@server.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, 0)
    if User.get_user_by_name(user.name) is None:
         print("not found!");
    return user.name

@app.callback(
	Output('suggestions_box', "value"),
	Input('submit_button', 'n_clicks'),
	State('suggestions_box', 'value'))
def handle_input(count, body):
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo();
		smtp.starttls();
		smtp.ehlo();
		subject = 'New BOSS suggestion';
		smtp.login('mahadkhalid4955@gmail.com','etmwfqvkoeeaeval');
		msg = f'Subject: {count}\n\n{body}';
		smtp.sendmail('mahadkhalid4955@gmail.com', 'mahadkhalid4955@gmail.com', msg);
		return 'Thanks for adding a suggestion!';


if __name__ == '__main__':
	app.run_server(debug=True,port=5000)
