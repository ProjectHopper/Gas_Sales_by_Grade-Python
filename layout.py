from dash import Dash,html
import dash_bootstrap_components as dbc
from components import (
                    pie_chart, 
                    category_dropdown,
                    year_dropdown,
                   month_dropdown
                )

def create_layout(app,data):
    return dbc.Container(
        [
            dbc.Row(
                [
                    html.Div(html.H1("Gas Station Sales")),
                 ]
                ),
            dbc.Row(
                [
                    html.Div([
                        dbc.Col([
                            category_dropdown.render(app,data),
                            year_dropdown.render(app,data),
                            month_dropdown.render(app,data)
                    ],lg=4),
                        dbc.Col(pie_chart.render(app,data),lg=8)
                 ]),
                ]
            )
        ]
    )
