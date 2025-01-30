import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

data = pd.read_csv('data/final_df.csv')

data['date'] = pd.to_datetime(data['date'])

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Sales data for Pink morsels', style={'textAlign': 'center', 'color': '#000000', 'fontSize': '40px'}, id='header'),
    html.Label('Select region'),
    dcc.RadioItems(
        id = "region-filter",
        options = [
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north',},
            {'label': 'South', 'value': 'south'},
            {'label': 'East', 'value': 'east'},
            {'label': 'West', 'value': 'west'}
        ],
        value = 'all',
        inline = True,
        style = {'marginBottom': '20px'},
    ),

    dcc.Graph(id='sales-chart'),
])

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)

def update_chart(region):
    altered_df = data if region == 'all' else data[data['region'] == region]

    fig = px.line(altered_df, x='date', y='sales', color='region', title='Sales data for pink morsels', labels={'sales':'Sales', 'date':'Date'})

    fig.add_hline(y=altered_df['sales'].mean(), line_dash='dash', line_color='red', annotation_text='Average sales', annotation_position='bottom right')

    # fig.add_vline(x=datetime(2021, 1, 15), line_dash='dash', line_color='green', annotation_text='Price rise', annotation_position='top right')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

# df = pd.read_csv('data/final_df.csv')

# df['date'] = pd.to_datetime(df['date'])

# print(df.dtypes)
# print(df.head())
###############################################################################################################################################3
