import pandas as pd

def run_pipeline():

    df = pd.read_csv("data/orders_raw.csv")

    df = df.drop_duplicates()

    df["order_date"] = pd.to_datetime(df["order_date"])

    df["revenue"] = df["price"] * df["quantity"]

    df["gst"] = df["revenue"] * 0.18

    df["total_amount"] = df["revenue"] + df["gst"]

    revenue_city = df.groupby("city")["revenue"].sum().reset_index()

    category_sales = df.groupby("category")["revenue"].sum().reset_index()

    df.to_csv("output/clean_orders.csv", index=False)

    revenue_city.to_csv("output/revenue_by_city.csv", index=False)

    category_sales.to_csv("output/category_sales.csv", index=False)

if __name__ == "__main__":
    run_pipeline()
