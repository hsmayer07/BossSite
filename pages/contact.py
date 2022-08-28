import dash
from dash import html, dcc

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='Contacts'),
    dcc.Link(html.Button("Return home"), href="/", refresh=True),
    html.H2("Mahad Faruqi (president): farqim@student.wl.k12.in.us"),
    html.H2("Nathan Park (vice president): parkn@student.wl.k12.in.us"),
    html.H2("Eric Pacheco (secretary): pachecoe@student.wl.k12.in.us"),
    html.H2("Exec Board: "),
    html.H2("  •  Albert Rajwa (rajwaa@student.wl.k12.in.us)"),
    html.H2("  •  Harry Forde (marchantfordeb@student.wl.k12.in.us)"),
    html.H2("  •  Max Hook (hookm@student.wl.k12.in.us)"),
    html.H2("  •  Malik Resheidat (resheidatm@student.wl.k12.in.us)"),
    html.H2("  •  Kirtan Patel (patelki@student.wl.k12.in.us)"),
    html.H2("  •  Yian Koh (kohy@student.wl.k12.in.us)"),
    html.H2("  •  Elijah Stenberg (stenberge@student.wl.k12.in.us)")


])
