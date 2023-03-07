import dash
from dash import dcc as dcc
from dash import html as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
import keplergl

app = dash.Dash()
server = app.server

df1 = pd.read_csv('max_muni_total_ONLY.csv')
df2 = pd.read_csv('highest_contributing_factors.csv')
df3 = pd.read_csv('max_index_overtime.csv')

# DATA

#2D Bubble Chart
data1 = [go.Scatter(x = df1['Average MAX'],
                   y = df1['MAX Score'],
                  text=df1['Municipality'],
                  mode = 'markers',
                  marker = dict(size=df1['MAX Score']/150, 
                                color = df1['Average MAX'],
                                colorscale = 'deep', # set color of bubbles
                                showscale=True))]
#Pie Chart
data2 = [go.Pie(labels=['Bike Lanes','Bus Headways','Level of Service','Volume to Capacity', 
                       'TIP Projects','Trails','Sharrow','Micromobility', 'Bus Rapid Transit',
                       'Bus Stops', 'Walkability'],
                             values=[5841.75,7023.75,5398.50,6391.50,2752.50,4202.25,935.00,247.75,305.25,5502.25,4318.00])]
#3D Bubble Chart
data3 = px.scatter_3d(df1, x='Average MAX', 
                     y='MAX Score', 
                     z='Walkability',
                     color='Walkability',
                     hover_data=['Municipality'], #allows municipality to be shown in chart
                     color_continuous_scale="Viridis",  
                     size='MAX Score', 
                     size_max=75, 
                     opacity=0.8)
# Line Graph
data4 = [go.Scatter(x=df3['Date'],
                    y = df3['MAX Score'],
                    line_color = "#20d37e",
                    mode='lines+markers')]


# LAYOUTS

#2D Bubble Chart
layout1 = go.Layout(title='MAX Index Performance by Municipality',
                   title_x = 0.5, # Title Alignment
                   title_font_size = 20, #set font size
                   title_font_color = 'rgb(233,233,233)', #title colour
                   paper_bgcolor= '#112330', # set the background colour
                   font=dict(color='rgb(233,233,233)'),
                   xaxis = dict(title = 'Average MAX Score',
                                title_font_size=16, 
                                title_font_color = 'rgb(233,233,233)',
                                gridcolor = 'grey',
                                zerolinecolor="grey",
                                color = 'rgb(233,233,233)',
                                ),
                   yaxis = dict(title = 'Sum of MAX Points for Municipality',
                                title_font_size=16, 
                                title_font_color = 'rgb(233,233,233)',
                                gridcolor = 'grey',
                                zerolinecolor="grey",
                                color = 'rgb(233,233,233)'),
                    
                   width = 475,
                   height = 450,
                   hovermode='closest')

#Pie Chart
layout2 = go.Layout(title = """Largest Contributing Factors to Countywide MAX Score""", # Graph title
                    title_font_size = 16,
                    title_font_color = 'rgb(233,233,233)',
                    font_color = 'rgb(233,233,233)',
                    width = 475,
                    height = 450,
                    paper_bgcolor='#112330', # set the background colour
)

#3D Bubble Chart
layout3 = data3.update_layout(
                    scene= dict(
                    xaxis = dict(
                        range=[0,16],
                        title='Average MAX Score', 
                        color = 'rgb(233,233,233)',
                        backgroundcolor="#20d37e",
                        gridcolor="grey",
                        showbackground=True,
                        zerolinecolor="white",),
                   
                     yaxis = dict(
                        range=[0,16000],
                        title='Total MAX Score',
                        color = 'rgb(233,233,233)',
                        backgroundcolor="#b2ed4c",
                        gridcolor="grey",
                        showbackground=True,
                        zerolinecolor="white"),
    
                     zaxis = dict( 
                        range=[0,1600],
                        title='Total Walkability', 
                        color = 'rgb(233,233,233)',
                        backgroundcolor="#40abf4",
                        gridcolor="grey",
                        showbackground=True,
                        zerolinecolor="white",),
                                   
                        camera = dict(eye = dict(x = -2.5, y =-1, z = 2),),),
                           
                            font=dict(color='rgb(233,233,233)'),
                            width = 460,
                            height = 450,
                            paper_bgcolor='#112330',
                            margin=dict(l=0, r=0, b=0, t=0),)

# Line Graph
layout4 = go.Layout(title = 'MAX Index Average Over Time', # Graph title
                    title_x = 0.5, # Title Alignment
                    title_font_color = 'rgb(233,233,233)',
                    title_font_size = 20,
                    paper_bgcolor='#112330', 
                    xaxis = dict(title = 'Date MAX Index Was Calculated',
                                title_font_size=16,
                                title_font_color = 'rgb(233,233,233)',
                                gridcolor="grey",
                                zerolinecolor="grey",
                                color = 'rgb(233,233,233)'), # x-axis label
                    yaxis = dict(title = 'Countywide Average',
                                title_font_size=16,
                                title_font_color = 'rgb(233,233,233)',
                                zerolinecolor="grey",
                                gridcolor="grey",
                                color = 'rgb(233,233,233)'), # y-axis label
                    width = 460,
                    height = 450
)

# FIGURES

fig1 = go.Figure(data = data1, layout = layout1) # 2D bubble Chart
fig2 = go.Figure(data=data2, layout=layout2) # Pie Chart
fig3 = go.Figure(data = data3, layout = layout3) # 3D Bubble Chart
fig4 = go.Figure(data = data4,layout = layout4) # Line Graph
fig5 = html.Iframe(srcDoc = open('MAXkepler.gl.html').read(), height='895', width='890') # Kepler Map

# DASH LAYOUT

app.layout = html.Div(

          children=[
              
                  dbc.Container([


                              dbc.Row(
                                       dbc.Col(html.H1("FORWARD PINELLAS MAX INDEX DASHBOARD",
                                       style={'textAlign':'center', 'font-size':36, 'font-weight': 'bold', 
                                              'font-family' : 'math',
                                              'color' : 'rgb(233,233,233)', 
                                              'padding-top' : 5, 'padding-bottom':0,
                                              'background-color': '#112330',  
                                              'margin-block-start': 1,
                                              'margin-block-end': 1, 
                                              'margin-inline-start': 25, # edits width left of margin
                                              'margin-inline-end': 23}, # edits width right of margin
                                       className='text-center'),
                                       )),
    
                              dbc.Row([ 
        
                                       dbc.Col([ # 2D Bubble
                                                 dcc.Graph(id='MAXBubblechart',figure = fig1)
                                                ],xs=12, sm=12, md=12, lg=5, xl=5),
        
                                       dbc.Col([ #Pie Chart
                                               dcc.Graph(id='MAXPieChart', figure = fig2)
                                               ],xs=12, sm=12, md=12, lg=5, xl=5)
                                               ],style={'width':'auto','height':'auto',
                                                 'display':'inline-block', 'verticalAlign': 'top',
                                                 'padding-left':25,'padding-right':0, 
                                                 'padding-top': 5, 'padding-bottom':0,}),
                             dbc.Row([ # Kepler Model
                                       dbc.Col([
                                                 fig5
                                               ],xs=12, sm=12, md=12, lg=5, xl=5),
                                               ],style={'width':'auto','height':'auto',
                                                 'display':'inline-block', 'verticalAlign': 'top', 
                                                 'border': 'black',
                                                 'padding-left':5,'padding-right':5, 
                                                 'padding-top': 5, 'padding-bottom':0,
                                                 }),
    
                             dbc.Row([
        
                                       dbc.Col([# 3D Bubble
                                               dcc.Graph(id='MAX3DBubblechart', figure = fig3)
                                               ],xs=12, sm=12, md=12, lg=5, xl=5),
        
                                       dbc.Col([# Line Graph
                                               dcc.Graph(id='MAXLineGraph', figure = fig4)
                                               ],xs=12, sm=12, md=12, lg=5, xl=5)
                                               ], style={'width':'auto', 'height':'auto',
                                                         'display':'inline-block','verticalAlign': 'top',
                                                         'padding-left':0,'padding-right':0, 
                                                         'padding-top': 5, 'padding-bottom':0,})
    
                            ],)], style= {'background-color': '#09101d', 'padding-left':0,
                                          'padding-right':0, 'padding-top': 25, 'padding-bottom':20,})


if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=False)
