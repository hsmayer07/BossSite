from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash


app = Dash(__name__, use_pages=True)



app.layout = html.Div(
	children = [

	html.H1('BOSS CLUB', style = {'display': 'inline-block', 'margin-left': '125px', 'margin-right':'150px'}),
	dcc.Link(html.Button("Calendar"), href="/calendar", refresh=True, style = {'margin-left': '50px', 'margin-right':'50px'}),
	dcc.Link(html.Button("About"), href="/about", refresh=True, style = {'margin-left': '50px', 'margin-right':'50px'}),
	dcc.Link(html.Button("Suggestions"), href="/suggestions", refresh=True, style = {'margin-left': '50px', 'margin-right':'50px'}),
	dcc.Link(html.Button("Contact"), href="/contact", refresh=True, style = {'margin-left': '50px', 'margin-right':'50px'}),
	dcc.Link(html.Button("Profile"), href="/profile", refresh=True, style = {'margin-left': '50px', 'margin-right':'50px'}),

	dash.page_container
])

if __name__ == '__main__':
	app.run_server(debug=True)
