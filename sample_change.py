

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import os
import numpy as np

os.chdir("D:\\Dash")

df=pd.read_excel("dataset.xlsx")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#df1 = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

available_indicators = df['student_name'].unique()

app.layout = html.Div([
    html.Div([

        html.Div([
            html.H5(["Select Student names to comapare"]),
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='arun'
            ),
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            ),
            
        
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='arun'
            ),
            
            html.H5(["Select subjects to comapare"]),
            dcc.Dropdown(
                id='xaxis-column_sub',
                options=[{'label': i, 'value': i} for i in df.columns[3:9]],
                value='Maths_PT1(40)'
            ),
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            ),
             dcc.Dropdown(
                id='yaxis-column_sub',
                options=[{'label': i, 'value': i} for i in df.columns[3:9]],
                value='Maths_PT1(40)'
            ),
            html.H5(["Single subject overview"]),
            dcc.Dropdown(
                id='sub_over',
                options=[{'label': i, 'value': i} for i in df.columns[3:9]],
                value='Maths_PT1(40)',
               
            
            ),
            html.H5(["Single student overview"]),
            dcc.Dropdown(
                id='stu_over',
                options=[{'label': i, 'value': i} for i in df["student_name"]],
                value='arun',
               
            
            ),
             html.H5(["student vs subject comparision"]),
            dcc.Dropdown(
                id='stu_over_comp',
                options=[{'label': i, 'value': i} for i in df["student_name"]],
                value=['arun','balu'],
                multi=True
               
            
            ),
             html.H5(["subject vs student comparision"]),
            dcc.Dropdown(
                id='sub_over_comp',
                options=[{'label': i, 'value': i} for i in df.columns[3:9]],
                value=['Maths_PT1(40)'],
                multi=True
               
            
            ),
             html.H5(["Class wise plotting"]),
            dcc.Dropdown(
                id='class',
                options=[{'label': i, 'value': i} for i in df["class"].unique()],
                value='I'
                
               
            
            )
            
        ],style={'width': '24%',"height":"100%","float":"left",'display': 'inline-block',"position":"fixed","overflow":"scroll"})
    ]),
   html.Div([
   
    dcc.Graph(id='indicator-graphic'),
              
             
    dcc.Graph(id='indicator-graphic1'),
    
    dcc.Graph(id='sub-bar_over'),
    
    dcc.Graph(id='stu-bar_over'),
    
    dcc.Graph(id='stu-bar_over_comp'),
    
    dcc.Graph(id='sub-bar_over_comp'),
    
    dcc.Graph(id='class_plot'),
    
    
    ],style={'width': '70%','float':'right'}),

#    dcc.Slider(
#        id='year--slider',
#        min=df['year'].min(),
#        max=df['year'].max(),
#        value=df['year'].max(),
#        marks={str(year): str(year) for year in df['year'].unique()},
#        step=None
#    )
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
     Input('xaxis-type', 'value'),
     Input('yaxis-type', 'value'),
     
     
    ])
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 ):
   
#    dff = df[df['year'] == year_value]
#    df_x=df.loc[df['student_name'] == xaxis_column_name].iloc[:,3:9].T
#    df_y=df.loc[df['student_name'] == yaxis_column_name].iloc[:,3:9].T
#    df_x['student']=xaxis_column_name
#    df_y['student']=yaxis_column_name
    x_i=df[df['student_name']==xaxis_column_name].index
    y_i=df[df['student_name']==yaxis_column_name].index
    
    return {
            
        
        'data': [dict(
            
            x=df[df["student_name"]==xaxis_column_name].iloc[:,3:9].T[x_i[0]],
            
            y=df[df['student_name'] == yaxis_column_name].iloc[:,3:9].T[y_i[0]],
           
          
            text=df[df['student_name'] == yaxis_column_name].columns[3:9],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': dict(
            xaxis={
                'title': xaxis_column_name,
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name,
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            
            margin={'l': 0, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
            
            
            
        )
    }

@app.callback(
    Output('indicator-graphic1', 'figure'),
    [Input('xaxis-column_sub', 'value'),
     Input('yaxis-column_sub', 'value'),
     Input('xaxis-type', 'value'),
     Input('yaxis-type', 'value'),  
     
     
     
    ])
def update_graph1(xaxis_column_name1, yaxis_column_name1,xaxis_type1, yaxis_type1,
                 
                 ):

#    dff = df[df['year'] == year_value]
#    df_x=df.loc[df['student_name'] == xaxis_column_name].iloc[:,3:9].T
#    df_y=df.loc[df['student_name'] == yaxis_column_name].iloc[:,3:9].T
#    df_x['student']=xaxis_column_name
#    df_y['student']=yaxis_column_name
#    x_i=df[df['student_name']==xaxis_column_name].index
#    y_i=df[df['student_name']==yaxis_column_name].index
    
    return {
        'data': [dict(
            
            x=df[xaxis_column_name1],
            
            y=df[yaxis_column_name1],
           
          
            text=df["student_name"],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': dict(
            xaxis={
                'title': xaxis_column_name1,
                'type': 'linear' if xaxis_type1 == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name1,
                'type': 'linear' if yaxis_type1 == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }
        
@app.callback(
    Output('sub-bar_over','figure'),
    [Input("sub_over","value")])

def sub_bar(subject):

   
  
   return {
            'data': [dict(
                
                x=df["student_name"],
                
             
                y=df[subject],
                
               
               
              
#                text=df["student_name"],
                
                type='bar',
                mode='markers',
                color=df["student_name"],
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )],
            'layout': dict(
                xaxis={
                    'title': "Student names",
                    
                },
                yaxis={
                    'title': subject,
                    
                },
                margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
                hovermode='closest'
            )
        }
@app.callback(
    Output('stu-bar_over','figure'),
    [Input("stu_over","value")])

def stu_bar(student):


   data_stu=df[df["student_name"]==student].iloc[:,3:9].T
   data_stu.reset_index(inplace=True)
   data_stu.rename(columns={0:'marks'},inplace=True)
   title = '<b>{}</b> Overview'.format(student)
  
   return {
        'data': [dict(
            
            x=data_stu["index"],
            
         
            y=data_stu.iloc[:,1],
            
           
            
          
            text=student,
            
            type='bar',
            mode='markers',
            color=df["student_name"],
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': dict(
               
            xaxis={
                'title': "Student names",
                
            },
            yaxis={
                'title': "marks",
                
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            annotations= [{
            'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
            'xref': 'paper', 'yref': 'paper', 'showarrow': False,
            'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
            'text': title
        }],
            hovermode='closest'
        )
    }

@app.callback(
    Output('stu-bar_over_comp','figure'),
    [Input("stu_over_comp","value")])
def stu_bar_comp(stu):

    
    f=[]
    for i in stu:
        data_stu=df[df["student_name"]==i].iloc[:,3:9].T
        data_stu.reset_index(inplace=True)
        data_stu.rename(columns={0:'marks'},inplace=True)
        f.append(go.Bar(name=i, x=data_stu["index"], y=data_stu.iloc[:,1]))
    

    fig=go.Figure(data=f)
    fig.update_layout(barmode='group')
    return fig
       
@app.callback(
    Output('sub-bar_over_comp','figure'),
    [Input("sub_over_comp","value")])
def sub_bar_comp(sub):

    
    f=[]
    for i in sub:
#            data_stu=df[df["student_name"]==i].iloc[:,3:9].T
#            data_stu.reset_index(inplace=True)
#            data_stu.rename(columns={0:'marks'},inplace=True)
        f.append(go.Bar(name=i, x=df["student_name"], y=df[i]))
    

    fig=go.Figure(data=f)
    fig.update_layout(barmode='group')
    return fig

@app.callback(
    Output('class_plot','figure'),
    [Input("class","value")])
def class_plot(c):

    df_class=df[df["class"]==c]

    
    f=[]
    for i in df_class.columns[3:9]:
#            data_stu=df[df["student_name"]==i].iloc[:,3:9].T
#            data_stu.reset_index(inplace=True)
#            data_stu.rename(columns={0:'marks'},inplace=True)
        f.append(go.Bar(name=i, x=df_class["student_name"], y=df_class[i]))
    

    fig=go.Figure(data=f)
    fig.update_layout(barmode='group')
    return fig
   
    
    

if __name__ == '__main__':
    app.run_server()


