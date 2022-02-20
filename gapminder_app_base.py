from dash import Dash, dcc, html, Input, Output

gapminder_app = Dash(__name__, external_stylesheets='https://codepen.io/chriddyp/pen/bWLwgP.css'])

gapminder_app.layout = html.Div([
    dcc.Input(id='widget-1'),
    dcc.Textarea(id='widget-2')])
    #'This is my dropdown',
    #dcc.Dropdown(
    #    options=[{'label': 'Africa', 'value': 'Africa'},
    #             {'label': 'Americas', 'value': 'Americas'},
    #             {'label': 'Asia', 'value': 'Asia'},
    #             {'label': 'Europe', 'value': 'Europe'},
    #             {'label': 'Oceania', 'value': 'Oceania'}],
    #    placeholder='Select a city...'
    #)])

@gapminder_app.callback(
    Output('widget-2', 'value'),
    Input('widget-1', 'value'))
def update_output(input_value):
    return input_value

if __name__ == '__main__':
    app.run_server(debug=True)
