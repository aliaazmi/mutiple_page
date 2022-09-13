#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
import plotly.express as px
import plotly.io as pio
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from dash.dependencies import Output, Input
import plotly.figure_factory as ff
import plotly.graph_objs as go
from dash import Dash, html
import base64
from PIL import Image
from dash_table import DataTable

dash.register_page(__name__, order=3, title="Breast Cancer")

df = pd.read_csv('https://raw.githubusercontent.com/aliaazmi/databreast/main/Raw_data_breast_cancer_2.csv')

df_filterd1 = df[df['STAGE'].isin(['I', 'II', 'III', 'IV'])]
fig1 = px.pie(df_filterd1, values='Count', names='STAGE',
             title='<b>Stage (n=893)</b>',
             labels ='<b> STAGE </b>', hole=.3, color_discrete_sequence=px.colors.diverging.curl,)
fig1.update_traces(textposition='inside', textinfo='percent+label+value')

df_filterd7 = df[df['Tumor_Grade'].isin(['1','2','3'])]
fig7 = px.pie(df_filterd7, values='Count', names='Tumor_Grade',
             title='<b>Tumor Grade (n=604)</b>',
             labels ='Tumor_Grade', color_discrete_sequence=px.colors.diverging.Tropic)
fig7.update_traces(textposition='inside', textinfo='percent+label+value', )


columns = [dict(id='Year', name='Year'),
           dict(id='amount', name='Amount of Pt', type='numeric')]
data = [
    dict(Year='2019', amount=519),
    dict(Year='2020', amount=596),
    dict(Year='2021', amount=538),
    dict(Year='2022-August', amount=391),
    dict(Year='Total Pt', amount=2044)]
dr_table = DataTable(columns=columns,
                     data=data,
                     sort_action='native',
                     derived_virtual_data=data,
                     style_table={'minHeight': '40vh',
                                  'height': '40vh',
                                  'overflowY': 'scrool'},
                     style_cell={"whitespace": 'normal',
                                 'height': 'auto',
                                 'fontFamily': 'verdana'},
                     style_header={'textAlign': 'center',
                                   'fontSize': 20},
                     style_data={'fontSize': 18},
                     style_data_conditional=[{'textAlign': 'center',
                                              'cursor': "pointer"},
                                             {'if': {'row_index': 'odd'}, 'backgroundColor': '#E6E6FA'}],

                     )



fig6 = go.Figure()
fig6.add_trace(go.Bar(
    x=['TNBC, n=173, 15.8%', 'HR-ve/HER2+ve, n=187, 17.1%', 'HR+ve/HER2+ve, n=303, 27.6%', 'HR+ve/HER2-ve, n=433, 39.5%', ],
    y=[173, 187, 303, 433 ],
    name='Female',
    marker=dict(
        color='#1C4E80',
        line=dict(color='#1C4E80', width=2)
    )
))
fig6.update_traces(textposition='inside', selector=dict(type='bar'))
fig6.update_layout(title= go.layout.Title(text='<b>HR/HER2</b>', xref='paper', x=0),xaxis=dict(title_text='<b>HR/HER2</b>'),
        margin=dict(t=30, b=35) )

pie1_graph = dcc.Graph (figure=fig7,
                       style= {'gridArea': 'pie1'})
pie2_graph = dcc.Graph (figure=fig1,
                       style= {'gridArea': 'pie2'})
fig6_graph = dcc.Graph (figure=fig6)




container = html.Div([  pie1_graph, pie2_graph,],
                    style={'display': 'grid',
                          'gridTemplateAreas':'"pie1 pie2 " ',
                            'gridTemplateColumns': '45vw 55vw',
                           'columnGap': '2px',})

app = Dash(__name__)

title = html.H2 ("Beacon Hospital's Breast Cancer Statistic (2019-2022-August)",
                style={
                      'fontFamily': 'verdana',
                      'textAlign': 'center',
                      },
                        id='dashTitle',
                        className="titles")

layout = html.Div([
    html.H2(title), dr_table, container, fig6_graph,


])

