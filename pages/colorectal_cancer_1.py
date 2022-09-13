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

dash.register_page(__name__, order=2, title="Colorectal Cancer" )

df = pd.read_csv('https://raw.githubusercontent.com/aliaazmi/colorectal_site/main/Database_Colorectal_cancer3.csv')
df.head()

app = Dash(__name__)

# Using direct image file pathhttps://raw.githubusercontent.com/aliaazmi/data_lung_cancer/main/Lung_cancer.csv
image_path = 'assets/my-image.jpeg'

# Using Pillow to read the the image
pil_img = Image.open('assets/my-image.jpeg')

# Using base64 encoding and decoding
def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/jpeg;base64,' + base64.b64encode(image).decode('utf-8')


title = html.H2("Beacon Hospital's Colorectal Cancer Statistic (2019-2022)",
                style={
                    'fontFamily': 'verdana',
                    'textAlign': 'center',
                },
                id='dashTitle',
                className="titles")
columns = [dict(id='Year', name='Year'),
           dict(id='amount', name='Amount of Pt', type='numeric')]
data = [
    dict(Year='2019', amount=260),
    dict(Year='2020', amount=198),
    dict(Year='2021', amount=326),
    dict(Year='2022-July', amount=120),
    dict(Year='Total Pt', amount=904)]
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
fig3 = go.Figure()
fig3.add_trace(go.Bar(
    x=['<35', '36-50', '51-65', '65>', 'Total'],
    y=[13, 76, 150, 158, 397],
    name='Female',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=2)
    )
))
fig3.add_trace(go.Bar(
    x=['<35', '36-50', '51-65', '65>', 'Total'],
    y=[6, 79, 205, 212, 502],
    name='Male',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=2)

    )
))
fig3.update_layout(xaxis=dict(title_text='<b>Age</b>'),
                   margin=dict(t=5, b=85))

df_filterd1 = df[df['Stage_AJC'].isin(['I', 'II', 'III', 'IV'])]
fig1 = px.pie(df_filterd1, values='Count', names='Stage_AJC',
             title='<b>Stage for Colorectal Cancer Pt (n=436)</b>',
             labels ='Stage_AJC', hole=.3, color_discrete_sequence=px.colors.sequential.Magenta)
fig1.update_traces(textposition='inside', textinfo='percent+label+value')

pie1_graph = dcc.Graph(figure=fig1,
                       style={'gridArea': 'pie1'})

bar_graph = dcc.Graph(figure=fig3,
                      style={'gridArea': 'bar'})

dr_table.style = {'gridArea': 'tables'}
container = html.Div([bar_graph, pie1_graph],
                     style={'display': 'grid',
                            'gridTemplateAreas': '"tables tables " "pie1 bar"',
                            'gridTemplateColumns': '45vw 55vw',

                            'columnGap': '2px', })



layout = html.Div([
    html.H2(title), html.Img(src=pil_img), dr_table,
    container,
])

