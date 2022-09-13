#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)

layout = html.Div([
    html.H1('Beacon Hospital Cancer Pt Statistic 2019-2022'),

    dcc.Dropdown(id='year-choice',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.Year.unique())],
                 value='2019', style={'width': '50%'}
                 ),
    dcc.Graph(id='my-graph')
])


@app.callback(
    Output(component_id="my-graph", component_property="figure"),
    Input(component_id="year-choice", component_property="value"),

)
def interactive_graphing(value_year):
    dff = df[df.Year == value_year]
    fig = px.pie(dff, values='Count', names='Cancer',
                 title='Beacon Hospital Cancer Pt Statistic 2019-2022',
                 labels='Cancer')
    fig.update_traces(textposition='inside', textinfo='percent+label+value')
    return fig

