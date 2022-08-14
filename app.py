from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash
from flask import Flask, render_template, url_for, redirect
from authlib.integrations.flask_client import OAuth
import os
from dash.dependencies import Input, Output, State
import sqlite3
from db import init_db_command
# from users import User

app = Dash(__name__, use_pages=True)
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

# try:
#     init_db_command()
# except sqlite3.OperationalError:
#     # Assume it's already been created
#     pass


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
    print(redirect_uri);
    print(GOOGLE_CLIENT_ID);
    return oauth.google.authorize_redirect(redirect_uri)

@server.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, 0)

    print(type(token));
#return redirect('/')
    return user.name

if __name__ == '__main__':
	app.run_server(debug=True,port=5000)
