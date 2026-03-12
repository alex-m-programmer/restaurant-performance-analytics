import pandas as pd
import numpy as np
from faker import Faker
import random
import os

fake = Faker()

def generate_sales_data(num_orders=12000):
    # Menu with base prices
    menu = {
        "Burger": 12, "Pizza": 14, "Carbonara": 13, "Salad": 9,
        "Sushi": 18, "Tomahawk": 35, "Spring Rolls": 8,
        "Ice Cream": 7, "Coffee": 4, "Soda": 3
    }

    categories = {
        "Burger": "Main", "Pizza": "Main", "Carbonara": "Main",
        "Salad": "Appetizer", "Sushi": "Main", "Tomahawk": "Main",
        "Spring Rolls": "Appetizer", "Ice Cream": "Dessert",
        "Coffee": "Drink", "Soda": "Drink"
    }

    servers = ["Alice", "Bob", "Charlie", "Diana"]
    server_weights = [0.4, 0.3, 0.2, 0.1]

    orders = []

    for order_id in range(1, num_orders + 1):
        timestamp = fake.date_time_between(start_date="-3M", end_date="now")
        
        # Simulate peak hours
        if random.random() < 0.3:
            timestamp = timestamp.replace(hour=random.choice([12, 13, 19, 20]))

        dish = random.choice(list(menu.keys()))
        category = categories[dish]
        quantity = np.random.poisson(1) + 1
        
        base_price = menu[dish]
        price = round(base_price * random.uniform(0.9, 1.1), 2)
        cost = round(price * random.uniform(0.4, 0.7), 2)
        server_id = random.choices(servers, weights=server_weights, k=1)[0]

        orders.append([order_id, timestamp, dish, category, quantity, price, cost, server_id])

    df = pd.DataFrame(orders, columns=[
        "order_id", "timestamp", "dish_name", "category", "quantity", "price", "cost", "server_id"
    ])

    # Introduce messy data
    for _ in range(30):
        idx = random.randint(0, len(df) - 1)
        df.at[idx, "dish_name"] = np.nan
        df.at[idx, "price"] = np.nan

    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/restaurant_sales.csv", index=False)
    print(f"Dataset generated: outputs/restaurant_sales.csv ({num_orders} rows)")
    return df

if __name__ == "__main__":
    generate_sales_data()