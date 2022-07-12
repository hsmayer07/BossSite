from dash import Dash, dcc, html, Input, Output, callback
from dash_labs.plugins import register_page
import plotly.express as px
import numpy as np

register_page(__name__)


layout = html.Div(
    [
    ]
)

#
# @callback(
#     Output("histograms-graph", "figure"),
#     Input("histograms-mean", "value"),
#     Input("histograms-std", "value"),
# )
# def display_color(mean, std):
#     data = np.random.normal(mean, std, size=500)
#     fig = px.histogram(data, nbins=30, range_x=[-10, 10])
#     return fig
