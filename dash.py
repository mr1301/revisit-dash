import os
import pandas
import plotly
from plotly import graph_objs

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)
    
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

    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "revisit-dash", csv_filename)

    csv_data = pandas.read_csv(csv_filepath)
    # CALCULATIONS
    monthly_total = csv_data["sales price"].sum()

    top_sellers = top_selling_products(csv_data)

    # OUTPUTS

    print("-----------------------")
    print("MONTH: March 2018") # TODO: get month and year

    print("-----------------------")
    print("CRUNCHING THE DATA...")

    print("-----------------------")
    print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

    print("-----------------------")
    print("TOP SELLING PRODUCTS:")
    for d in top_sellers:
        print("  " + str(d["rank"]) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))

    print("-----------------------")
    print("VISUALIZING THE DATA...")