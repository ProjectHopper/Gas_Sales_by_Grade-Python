from dash import Dash, html
import dash_bootstrap_components as dbc
from util import get_data
from layout import create_layout

PATH = "gas_sale.csv"
data = get_data(PATH)
print(data.head())
app = Dash(external_stylesheets=[dbc.themes.COSMO])
app.layout = create_layout(app,data)
app.run_server(debug=True)