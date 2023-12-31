#python
# app.py

import pandas as pd
from dash import Dash, dcc, html

data = (
    pd.read_csv("avocado.csv")
    .query("type == 'conventional' and region == 'Albany'")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Paltas Analytics: Understand Your Paltas!"
server = app.server

#app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🥑  🥑", className="header-emoji"),
                html.H1(
                    children="Paltas Analytics", className="header-title"
                ),
                html.P(
                    children=(
                        "Analyze the behavior of paltas prices and the number"
                        " of paltas sold in the US between 2015 and 2018"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["AveragePrice"],
                                    "type": "lines",
                                    #"hovertemplate": (
                                    #    "$%{y:.2f}<extra></extra>"
                                    #),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Average Price of Paltas",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": True},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["Total Volume"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Avocados Sold",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ],
)

#app.layout = html.Div(
#    children=[
#        html.Div(
#            children=[
#                html.P(children="🥑", className="header-emoji"),
#                html.H1(
#                    children="Avocado Analytics", className="header-title"
#                ),
#                html.P(
#                    children=(
#                        "Analyze the behavior of avocado prices and the number"
#                        " of avocados sold in the US between 2015 and 2018"
#                    ),
#                    className="header-description",
#                ),
#            ],
#            className="header",
#        ),
#        dcc.Graph(
#            figure={
#                "data": [
#                    {
#                        "x": data["Date"],
#                        "y": data["AveragePrice"],
#                        "type": "lines",
#                    },
#                ],
#                "layout": {"title": "Average Price of Avocados"},
#            },
#        ),
#        dcc.Graph(
#            figure={
#                "data": [
#                    {
#                        "x": data["Date"],
#                        "y": data["Total Volume"],
#                        "type": "lines",
#                    },
#                ],
#                "layout": {"title": "Avocados Sold"},
#            },
#        ),
#    ]
#)

if __name__ == "__main__":
    app.run_server(debug=True)
