import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_dashboard():
    data_dir = "outputs"
    try:
        cat_perf = pd.read_csv(f"{data_dir}/category_performance.csv")
        menu_perf = pd.read_csv(f"{data_dir}/menu_performance.csv")
        server_perf = pd.read_csv(f"{data_dir}/server_performance.csv")
        lunch_perf = pd.read_csv(f"{data_dir}/lunch_performance.csv")
        dinner_perf = pd.read_csv(f"{data_dir}/dinner_performance.csv")
        expected_rev = pd.read_csv(f"{data_dir}/expected_revenue.csv")
        sales_df = pd.read_csv(f"{data_dir}/restaurant_sales.csv")
        
        sales_df['total'] = sales_df['price'] * sales_df['quantity']
        sales_df['timestamp'] = pd.to_datetime(sales_df['timestamp'])
        sales_df['hour'] = sales_df['timestamp'].dt.hour
    except FileNotFoundError:
        print("Error: Required CSV files not found. Run main.py first.")
        return

    # Theme
    sns.set_theme(style="whitegrid")
    fig = plt.figure(figsize=(22, 16))
    fig.patch.set_facecolor('#f4f4f4')
    plt.suptitle("Executive Restaurant Performance Dashboard", fontsize=30, fontweight='bold', y=0.98)

    # 1. Top Dishes (Revenue)
    ax1 = fig.add_subplot(3, 2, 1)
    top_dishes = menu_perf.sort_values('Total_Revenue').tail(10)
    sns.barplot(data=top_dishes, x='Total_Revenue', y='dish_name', hue='dish_name', palette="viridis", legend=False, ax=ax1)
    ax1.set_title('Top 10 Dishes by Revenue', fontsize=16)

    # 2. Category Mix (Pie Chart)
    ax2 = fig.add_subplot(3, 2, 2)
    ax2.pie(cat_perf['Total_Revenue'], labels=cat_perf['category'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    ax2.set_title('Revenue by Category', fontsize=16)

    # 3. Server Performance
    ax3 = fig.add_subplot(3, 2, 3)
    sns.barplot(data=server_perf, x='server_id', y='Total_Revenue', hue='server_id', palette="Blues_d", legend=False, ax=ax3)
    ax3_twin = ax3.twinx()
    sns.lineplot(data=server_perf, x='server_id', y='Number_of_Orders', color='red', marker='o', ax=ax3_twin)
    ax3.set_title('Server Revenue vs Order Volume', fontsize=16)

    # 4. 7-Day Forecast
    ax4 = fig.add_subplot(3, 2, 4)
    expected_rev['dt'] = pd.to_datetime(expected_rev['date']) + pd.to_timedelta(expected_rev['hour'], unit='h')
    sns.lineplot(data=expected_rev, x='dt', y='expected_revenue', color='darkorange', ax=ax4)
    ax4.set_title('7-Day Revenue Forecast', fontsize=16)
    plt.xticks(rotation=30)

    # 5. Lunch vs Dinner 
    ax5 = fig.add_subplot(3, 2, 5)
    lunch = lunch_perf.set_index('dish_name')['Total_Quantity'].head(5)
    dinner = dinner_perf.set_index('dish_name')['Total_Quantity'].head(5)
    pd.DataFrame({'Lunch': lunch, 'Dinner': dinner}).fillna(0).plot(kind='bar', ax=ax5, color=['#66c2a5', '#fc8d62'])
    ax5.set_title('Lunch vs Dinner: Top Dishes', fontsize=16)
    plt.xticks(rotation=0)

    # 6. Hourly Demand Trend
    ax6 = fig.add_subplot(3, 2, 6)
    hourly = sales_df.groupby('hour')['total'].sum()
    ax6.fill_between(hourly.index, hourly.values, color="purple", alpha=0.2)
    ax6.plot(hourly.index, hourly.values, color="purple", lw=3)
    ax6.set_title('Hourly Sales Trend', fontsize=16)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(f"{data_dir}/executive_dashboard.png", dpi=150)
    print(f"Executive Dashboard saved to: {data_dir}/executive_dashboard.png")

if __name__ == "__main__":
    create_dashboard()