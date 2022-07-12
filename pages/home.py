from dash_labs.plugins import register_page
from dash import dcc, html, Input, Output, callback
import plotly.express as px

register_page(__name__, path="/")


layout = html.Div(
    [

    ]
)

#
# @callback(Output("heatmaps-graph", "figure"), Input("heatmaps-medals", "value"))
# def filter_heatmap(cols):
#     fig = px.imshow(df[cols])
#     return fig
