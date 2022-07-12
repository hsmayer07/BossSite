from dash_labs.plugins import register_page
from dash import dcc, html, Input, Output, callback
import plotly.express as px

register_page(__name__)


layout = html.Div(
    [
    ]
)

#
# @callback(Output("bar-chart", "figure"), Input("dropdown", "value"))
# def update_bar_chart(day):
#     mask = df["day"] == day
#     fig = px.bar(df[mask], x="sex", y="total_bill", color="smoker", barmode="group")
#     return fig
