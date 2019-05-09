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

    expected_result = [
        {'rank': 1, 'name': 'Button-Down Shirt', 'monthly_sales': 5,464.20},
        {'rank': 2, 'name': 'Super Soft Sweater', 'monthly_sales': 2,249.85},
        {'rank': 3, 'name': 'Super Soft Hoodie', 'monthly_sales': 1800.00},
        {'rank': 4, 'name': 'Khaki Pants', 'monthly_sales': 1780.00},
        {'rank': 5, 'name': 'Vintage Logo Tee', 'monthly_sales': 526.35},
        {'rank': 6, 'name': 'Sticker Pack', 'monthly_sales': 283.50},
        {'rank': 7, 'name': 'Brown Boits', 'monthly_sales': 250.00}
    ]
