import dash
import dash_labs as dl
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


app = Dash(
    __name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.BOOTSTRAP]
)



topbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),
    brand="Multi Page App Plugin Demo",
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [topbar, dl.plugins.page_container],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
