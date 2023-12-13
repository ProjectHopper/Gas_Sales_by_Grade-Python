from dash import html, dcc, Output, Input
import plotly.express as px

def render(app,data):
    @app.callback(
            Output("pie-chart","children"),
            [
                Input("year_dropdown","value"),
                Input("month_dropdown","value"),
                Input("category_dropdown","value"),
            ]
    )
    def update_pie_chart(years, month, categories):
        filtered_data = data.query("year in @years and month in @month and category in @categories")
        if filtered_data.shape[0]==0:
            html.Div("No data selected", id="pie-chart")
        fig = px.pie(  
            filtered_data,
            values = 'amount', 
            names = "category",
            title = "Revenue"
        )
        return html.Div(dcc.Graph(figure=fig), id="pie-chart")
    return html.Div( id="pie-chart")