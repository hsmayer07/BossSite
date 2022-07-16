from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
	html.H1('Multi-page app with Dash Pages'),
	dcc.Link(html.Button("Calendar"), href="/calendar", refresh=True),
	dcc.Link(html.Button("About"), href="/about", refresh=True),
	dcc.Link(html.Button("Suggestions"), href="/suggestions", refresh=True),
	dcc.Link(html.Button("Contact"), href="/contact", refresh=True),
	dcc.Link(html.Button("Profile"), href="/profile", refresh=True),

	dash.page_container
])

if __name__ == '__main__':
	app.run_server(debug=True)
