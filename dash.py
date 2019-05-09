import os
import pandas
import plotly
from plotly import graph_objs

def top_selling_products(sales_data):
    product_totals = sales_data.groupby(["product"]).sum()
    product_totals = product_totals.sort_values("sales price", ascending=False)
    top_sellers = []
    rank = 1
    for i, row in product_totals.iterrows():
        d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
        top_sellers.append(d)
        rank = rank + 1
    return top_sellers


if __name__ == "__main__":
    # INPUTS

    csv_filename =input("please input file name in this format, sales-201710.csv" )  # allow user to specify

    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", csv_filename)

    csv_data = pandas.read_csv(csv_filepath)
    # CALCULATIONS
    monthly_total = csv_data["sales price"].sum()

    top_sellers = top_selling_products(csv_data)