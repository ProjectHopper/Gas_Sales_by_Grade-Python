from dash import html,dcc,Input,Output
import dash_bootstrap_components as dbc

def render(app,data):
    all_months = data["month"].unique()
    options = [{"label":month, "value":month} for month in all_months]
    @app.callback(
        Output("month_dropdown","value"),
        Input("month_button","n_clicks")
    )
    def select_all_months(n):
        return all_months
    return html.Div([
            html.H6("Month"),
            dcc.Dropdown(
                options=options,
                multi=True,
                id = "month_dropdown"
            ),
            html.Button(
                ["Select All"],
                n_clicks = 0,
                id = "month_button"
            )
    ])