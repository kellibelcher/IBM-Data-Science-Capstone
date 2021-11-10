# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv('spacex_launch_dash.csv')
spacex_df.rename(columns={'class': 'Class'}, inplace=True)
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#000000',
                                               'font-size': 40}),

                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(id='site-dropdown',
                                             options=[
                                                 {'label': 'All Sites', 'value': 'ALL'},
                                                 {'label': 'Cape Canaveral Air Force Station (CCAFS LC-40)', 'value': 'CCAFS LC-40'},
                                                 {'label': 'Cape Canaveral Space Launch Complex (CCAFS SLC-40)', 'value': 'CCAFS SLC-40'},
                                                 {'label': 'Kennedy Space Center (KSC LC-39A)', 'value': 'KSC LC-39A'},
                                                 {'label': 'Vandenberg Air Force Base (VAFB SLC-4E)', 'value': 'VAFB SLC-4E'},

                                             ],
                                             value='ALL',
                                             placeholder='Select a Launch Site here',
                                             searchable=True),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P('Payload Range (kg):'),
                                # TASK 3: Add a slider to select payload range
                                # dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, max=10000, step=1000,
                                                marks={0: '0', 2500: '2,500', 5000: '5,000',
                                                       7500:'7,500', 10000:'10,000'},
                                                value=[min_payload, max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ], style={'font-family': 'verdana'})


# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='Class', names='Launch Site',
                     title='Total Successful Launches by Site')
        return fig
    else:
        # return the outcomes piechart for a selected site
        filtered_df = spacex_df.loc[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(filtered_df, names='Class',
                     title='Total Successful Launches for ' + entered_site)
        return fig



# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_plot(entered_site, payload):
    min, max = payload
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] > min) & (spacex_df['Payload Mass (kg)'] < max)]
    filtered_df['Class'] = ['Successful' if i == 1 else 'Unsuccessful' for i in filtered_df['Class']]
    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='Class',
                         color='Booster Version',
                         title='Correlation between Payload and Success for All Sites')
        return fig
    else:
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='Class',
                         color='Booster Version',
                         title='Correlation between Payload and Success for ' + entered_site)
        return fig


# Run the app
if __name__ == '__main__':
    app.run_server()