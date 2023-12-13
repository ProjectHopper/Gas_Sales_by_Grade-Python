from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

def render(app, data):
    list_category=data["category"].unique()
    all_category=[{"label":c, "value":c} for c in list_category]
    
    @app.callback(
        Output("category_dropdown", "value"),
        Input("button", "n_clicks")
    )
    def update_all_categories(n):
        return list_category
    
    return html.Div(
        [
            html.H6("Select Categories"),
            dcc.Dropdown(
                options=list_category,
                multi=True,
                value="Premium",
                id="category_dropdown",
            ),
            dbc.Button(
                children=["Select all"],
                color="primary",
                n_clicks=0,
                id="button",
            )
        ]
    )