import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

############# Make changes here


app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Plotly Dash - the best way to visualize your data!'),
    dcc.Graph(
        id='this_is_an_id',
        figure={
            'data': [
                {'x': ['Africa', 'Asia', 'World'], 'y': [10, 4, 7], 'type': 'bar', 'name': 'Animals'},
                {'x': ['Africa', 'Asia', 'Wrold'], 'y': [5, 0, 8], 'type': 'bar', 'name': 'Natural'},
            ],
            'layout': {
                'title': "Endangered Animals",
                'xaxis':{'title':'Choice of data visualization'},
                'yaxis':{'title':'Approval rating by average data scientist'},
            }
        }
    )]
)


###### Don't change anything here



if __name__ == '__main__':
    app.run_server()
