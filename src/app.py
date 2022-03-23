import pandas as pd

import app_settings, data_settings
import data

import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

import plotly
import plotly.graph_objs as go
import plotly.express as px



resevoir = data.get_data(data_settings.LOOK_BACK)

app = dash.Dash(title=app_settings.TITLE,
                update_title=app_settings.UPDATE_TITLE)
  
app.layout = html.Div(children=[
                                    html.H1(children="Tesla's Stock Price"),

                                    html.Div(children='''TSLA Close Quote:'''),

                                    dcc.Graph(id = 'tsla-price-graph', 
                                              animate = True), 

                                    dcc.Interval(id = 'tsla-price-update',
                                                 interval = app_settings.TSLA_PRICE_GRAPH_INTERVAL,
                                                 n_intervals = 0)
                                ]
                     )
  
@app.callback(Output('tsla-price-graph', 'figure'),
             [Input('tsla-price-update', 'n_intervals')])
def update_tsla_price_graph(n):
    global resevoir

    price_window = data.get_data(data_settings.LOOK_BACK)
    resevoir = pd.concat([resevoir, price_window])
    X = resevoir["timestamp"].tolist()
    Y = resevoir["quote"].tolist()

    graph_data = plotly.graph_objs.Scatter(x=X,
                                           y=Y)
    
    live_dynamic_graph =  {
                            'data': [graph_data],
                            'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),yaxis = dict(range = [min(Y),max(Y)]))
                          }
    
    return live_dynamic_graph 
  
if __name__ == '__main__':
    app.run_server(debug=app_settings.DEBUG, 
                   port=app_settings.PORT)