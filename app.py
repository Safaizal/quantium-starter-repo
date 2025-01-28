import pandas as pd
import dash
from dash import Dash, dcc, html
import plotly.express as px
import datetime

data = pd.read_csv('data/final_df.csv')
data['date'] = pd.to_datetime(data['date'])

app = Dash(__name__)

fig = px.line(data, x='date', y='sales', color='region', title='Sales data for pink morsels', labels={'sales':'Sales', 'date':'Date'})

fig.add_hline(y=data['sales'].mean(), line_dash='dash', line_color='red', annotation_text='Average sales', annotation_position='bottom right')

app.layout = html.Div([
    html.H1('Sales data for pink morsels'),
    dcc.Graph(figure=fig),
])

if __name__ == '__main__':
    app.run_server(debug=True)

# df = pd.read_csv('data/final_df.csv')

# df['date'] = pd.to_datetime(df['date'])

# print(df.dtypes)
# print(df.head())