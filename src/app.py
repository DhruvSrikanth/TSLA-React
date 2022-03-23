import random
from collections import deque

import app_settings as settings

import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html

import plotly
import plotly.graph_objs as go
  
X = deque(maxlen = 20)
X.append(1)
  
Y = deque(maxlen = 20)
Y.append(1)
  
app = dash.Dash(title=settings.TITLE,
                update_title=settings.UPDATE_TITLE)
  
app.layout = html.Div(
                        [
                            dcc.Graph(id = 'tsla-price-graph', 
                                      animate = True),
                            dcc.Interval(id = 'tsla-price-update',
                                         interval = settings.TSLA_PRICE_GRAPH_INTERVAL,
                                         n_intervals = 0)
                        ]
                    )
  
@app.callback(Output('tsla-price-graph', 'figure'),
             [Input('tsla-price-update', 'n_intervals')])
def update_tsla_price_graph(n):
    
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))
  
    data = plotly.graph_objs.Scatter(x=list(X),
                                     y=list(Y),
                                     name='Scatter',
                                     mode= 'lines+markers')
    
    live_dynamic_graph =  {
                            'data': [data],
                            'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),yaxis = dict(range = [min(Y),max(Y)]),)
                          }
    
    return live_dynamic_graph 
  
if __name__ == '__main__':
    app.run_server(debug=settings.DEBUG, 
                   port=settings.PORT)