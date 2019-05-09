import os
import pandas
from dash import to_usd, top_selling_products

def test_to_usd():
    assert to_usd(5) == "$5.00"

    assert to_usd(3.889) == "$3.89"

    assert to_usd(3.8) =="$3.80"


def test_top_selling_products():
    csv_filename = "sales-201710.csv"
    csv_filepath = os.path.join(os.path.dirname(__file__), "revisit-dash", csv_filename)
    csv_data = pandas.read_csv(csv_filepath)
    results = top_selling_products(csv_data)