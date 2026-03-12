import pandas as pd
import os

def load_and_clean_data(path: str) -> pd.DataFrame:
  df = pd.read_csv(path)

  df = df.dropna(subset=["dish_name", "price", "cost", "quantity", "timestamp"])
  df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
  df = df.dropna(subset=["timestamp"])

  # Remove impossible sales records
  df = df[
    (df["quantity"] > 0) &
    (df["price"] > 0) &
    (df["cost"] >= 0) &
    (df["cost"] <= df["price"])
  ]

  return df


def add_metrics(df: pd.DataFrame) -> pd.DataFrame:
  # Time features for demand analysis
  df["hour"] = df["timestamp"].dt.hour
  df["day_of_week"] = df["timestamp"].dt.day_name()
  df["month"] = df["timestamp"].dt.month

  # Profitability metrics
  df["profit"] = df["price"] - df["cost"]
  df["total"] = df["price"] * df["quantity"]
  df["total_profit"] = df["profit"] * df["quantity"]

  return df


def summarize_performance(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
  return (
    df.groupby(group_col).agg(
      Total_Revenue=("total", "sum"),
      Total_Profit=("total_profit", "sum"),
      Total_Quantity=("quantity", "sum"),
      Average_Profit_Per_Item=("profit", "mean"),
    ).sort_values("Total_Profit", ascending=False))

def performance_by_time_window(df: pd.DataFrame, start_hour: int, end_hour: int) -> pd.DataFrame:
  window_df = df[(df["hour"] >= start_hour) & (df["hour"] < end_hour)]
  return summarize_performance(window_df, "dish_name")


def expected_revenue_by_day_hour(df: pd.DataFrame, days: int = 7) -> pd.DataFrame:
  baseline = (df.groupby(["day_of_week", "hour"])["total"].mean().reset_index(name="expected_revenue"))
  future_days = pd.date_range(
    start=pd.Timestamp.today().normalize(),
    periods=days
  )

  rows = []
  for day in future_days:
    pattern = baseline[baseline["day_of_week"] == day.day_name()]
    for _, row in pattern.iterrows():
      rows.append({
        "date": day.date(),
        "hour": row["hour"],
        "expected_revenue": row["expected_revenue"],
      })

  return pd.DataFrame(rows)


def run_analysis(data_path: str):
  df = load_and_clean_data(data_path)
  df = add_metrics(df)

  results = {
    "menu_performance": summarize_performance(df, "dish_name"),
    "lunch_performance": performance_by_time_window(df, 12, 15),
    "dinner_performance": performance_by_time_window(df, 19, 22),
    "category_performance": summarize_performance(df.dropna(subset=["category"]), "category"),
    "server_performance": (df.groupby("server_id").agg(
      Total_Revenue=("total", "sum"),
      Total_Profit=("total_profit", "sum"),
      Number_of_Orders=("order_id", "nunique"),
      Average_Profit_Per_Order=("total_profit", "mean"),
    ).sort_values("Total_Revenue", ascending=False)),
    "revenue_by_hour": df.groupby("hour")["total"].sum().sort_index(),
    "expected_revenue": expected_revenue_by_day_hour(df),
  }

  return results

def save_csvs(results):
  for name, df in results.items():
    if isinstance(df, pd.DataFrame):
      df.to_csv(f"outputs/{name}.csv", index=True)


if __name__ == "__main__":
  results = run_analysis("outputs/restaurant_sales.csv")
  save_csvs(results)
  print("All CSVs saved in outputs/ folder.")