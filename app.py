from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash


app = Dash(__name__, use_pages=True)



app.layout = html.Div(
	children = [
	html.H1('BOSS CLUB', style = {'display': 'inline-block', 'margin-left': '4%', 'margin-right':'4%'}),
	dcc.Link(html.Button("Calendar"), href="/calendar", refresh=True, style = {'margin-left': '4%', 'margin-right':'4%'}),
	dcc.Link(html.Button("About"), href="/about", refresh=True, style = {'margin-left': '4%', 'margin-right':'4%'}),
	dcc.Link(html.Button("Suggestions"), href="/suggestions", refresh=True, style = {'margin-left': '4%', 'margin-right':'4%'}),
	dcc.Link(html.Button("Contact"), href="/contact", refresh=True, style = {'margin-left': '4%', 'margin-right':'4%'}),
	dcc.Link(html.Button("Profile"), href="/profile", refresh=True, style = {'margin-left': '4%', 'margin-right':'4%'}),
	html.A([
            html.Img(
                src='https://upload.wikimedia.org/wikipedia/commons/5/58/Instagram-Icon.png',
				style={
					'height' : '2%',
                    'width' : '2%',
					'margin-left' : '3%'}),
    ], href="https://www.instagram.com/wl_boss/?hl=en", target="_blank"),
	html.A([
            html.Img(
                src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Facebook_Logo_%282019%29.png/800px-Facebook_Logo_%282019%29.png',
				style={
					'height' : '2%',
                    'width' : '2%',
					'margin-left' : '1%'}),
    ], href="https://www.youtube.com/watch?v=MADvxFXWvwE", target="_blank"),
	html.A([
            html.Img(
                src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANAAAADyCAMAAAALHrt7AAAAYFBMVEUAvPL///8AuPEAufHW8/z8//8Sv/Pf9v3q+P4hwvPt+v72/f/q+v47xfQAv/Lc9P1cy/Wx5vqM2vii4fny/P7C6/uS2/hgzvV41Pds0fa76fvQ8PxezfXI7ftGx/Su5Pq/uoI0AAAH4UlEQVR4nO2diZajKBRA9ZGYmJSVRRPNZv7/Lxu1TAKCS+CB2twzp2dO1xnkFoKsD89vZ7ldrxajYbdOlh0Z9uQ/Sh7nNCIwMkh0Pz+S4ULJM6cuxBshRb7yp8xJLHTKx+nyhsD+0VvoGoLt/PYBomsvoVs0CZ0CiHadQsvLZHQKIONbPU7oFkzKhxoFuzaheGI6BRDLhbIJ+lCjo0xoWtXnDWRiofvIPz1yIBUJXSbrw5TRS2ia9afmXY9qoSm2b5/AgRXaTdyHdu5Wn0LLwHZ+1Ak+haZdgSrI8S00/ReuoHrpSqHIdl60QPJa6DGLAqIt3e1PaB4FRMkrodtMCogW0a4USifc52EhWSG0nY0PZUmFDrN54+g7d6VC83nj6Dt3oUK2M6GVwPfm0UuogbV3mNEbR9+5k3ecl9DZS23nQSvk4unu9wTB7y/9p/ij+K/GQKv66+qP4t+aH59rTs8jW5+Fy3HA/Vj3Zz3UmxwVWrMZ5sfCATcXvRl7FXZCTsgwTsgJGcYJOSHDOCEnZBgYKjS6GYCQ5ZcXitifR7zQL5eAbZ+W/XbfYX3pbXZCXVsmnZATckJOyAk5ISfkhJzQeIU0+9gX+uHgS2zHwQtw//vGuhBhaYxYPfb4D/+KboBLwLYPz+zmFJyQEzKME3JChnFCTsgwTsgJGaa5PsTkmIx/fShiCTec0H3PcOeFQi4B2z7zG7HOTmh2kyROyAk5ISfkhJyQE3JC/5GQZh/7QksOPoMDf25fiGPwENxONvszeIvm2OcUZjdJ4oSckGGckBMyjBNyQoZxQqMX4pdTJi+02jIkvFDC/nw1diGHw+FwOBw9GN8OcQUIhPnlEtm8CoKAl9/zUE8WIPup+pmHyJYSuSyqLDzVr6QgwceA4Gxl7xREq3cWjqpZCJnoXVcLRmTPDDgUf6mwYlLzT8aNSMrmwN+rvPgk41Lzn4aNqpDGn6xVcsAXkG88NnfAB6zzfaWgeI3UDC8alhGaOVTCSjbKm2Jy1AxnQQZUhEJBegbDP0OjCqsKEVGCxpq6RgNXkSkIiV5hipmAydwH6IXKzmFyFKdp4t4LkPhs1Z4tTtTA5whEDVLBValRIqJmpkwW2Uj2vvm+YiwjWEjSxW0Z4CLzUWkSSvjYsS8wb1cASd3V8dRmd65m5WF9Yrl7uT7Y6kj9JEs9CXGMXnfvNNFzjdValvxyj/LaiT9+BZpGmMIOUIXyALIBRBvp03RVWxB3QUrUvgqCZ0mbN52rY/JKSsdbWq/SFHavazRG0wPxXaEly1SbEfFanuPre07xqOa9mm909ewgbw5P3+geKsurKv0i6bjylEi7WSXap9AEg3umkFQrLOTSr0OB/t4w4QNgsiQXJSXiia6/fYPRF+4w8nfp10oQtDSjWD7dRv46+2aRgkD4bE8XbYTcaeRv4wgGPZwAyWQDFHQf+viwtWWoiukcQc+CIuCl7VWnBHN0TIK21rtmc7gEHbekEwKQH299joJgL3l0viAVP6fj3qNWfGnRvwCA8BLfugu7BP0e37Z+Hc92cY2PaR5UIvRbFt2z8/PW+sFhWSMNuRije8/f7adZsv7ZJMPPGunuy4sh/F3caBhb6Rjy2n3PwuCt66Jb7XWjfzDcrtTaNVZnYXzJnYTyuQxlllbu8IV0QPs7iINnJ/YKIcfhLXg3D62zFMMAT3t7t8jtRsYhXqyzlBY4U5cDlY59eqx9OFkunRqoNxcpoWNnkjaKUafam3dTm5NAgEB6Sr60WRyDsekU0BFCHjf30nSwPWWjtPmDQJA9e1eo7eOcdwxtR0A5us4Oj3Vbpdqur+d7CMNmVGxSWHlBfjmf4zh+Hmqezzg+Z/coKII8Y5QM9s6qwosPYI0agzrSfsGsZVLvbjsLWiHHuV3SfJjZNdqwmNlF597crqLfU6F0Ru8ciamQmd2JZoAVFdJ9M7dNIp8K+ZfZGJFnKbSYzTtHlqWQ2tb7EVHuGiyEMLcmmoQkf0IzKaJqI0optJpFEVWbY6t92XPoocL1Q2h0YeqGU29S/BOafuCJOjZIfRTA9Ek03UC9ovg622B4AVAz8NqQ8j6sYWXNTBMfi9gfp0/Qt2yg8bne+3mcZqplxGwyYM4HTbMeAbOhiz3wNMG2DrhtLdwJrlUwsQ8SpNwGosaRtElVJBI0Ts40z9jtRrLO2Q2IdrOIDg2erAa36AuBs2jBUHwK8paScRcTQPQU776THevcHvZe372wZiFFfBL5ymdLAPDlLc5yAgMZ+DsYlj7xwn32bN162x3RPPlZDeBnWCspPw35LdpDtA86tdQMZ6GMfqEhETbItxsb5OgXGjBZLj9Q+j0IQr0PN8tCASiBIdS3GkUYz0YR6leNQNemNAYUoV7VCHqcS/kCHKEew3n5mXk1kIT4iLpNWo5jK4Ek1Dldzl94oQ0soY7Dui0BBhRBE2pdXW87wa4InlBbNZKGBVEHT8iX71ERxETTBqKQtBqhnj7CFJIEEJFEvNIEqtBWWI34KO96QRUSboGQRj7SA66Q4FAt9skwZKFGyEt5yCtNYAs1qhHGCapPsIW4+IeSAHwaQRdiqhF2BfJNCPn5qxohzFo1MCCUvEtI/6xVAwNCr91ebdGOtGFC6G/tFmXWqoERoaoaocxaNTAjVFyByd9MhIQZIf8ESLNWDQwJ+RneoJvFlFDzZlkk/gHG1Xq2jL2ofgAAAABJRU5ErkJggg==',
				style={
					'height' : '1.7%',
                    'width' : '1.7%',
					'margin-left' : '1%'}),
    ], href="https://web.groupme.com/join_group/70908100/CzPh7pDT", target="_blank"),
	dash.page_container
], style = {'margin-top' : '3%'})

if __name__ == '__main__':
	app.run_server(debug=True)
