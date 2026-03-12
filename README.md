# 🍽️ Restaurant Performance Analytics Pipeline

![image alt](https://github.com/alex-m-programmer/restaurant-performance-analytics/blob/4005908f27459ef304a3c194d79dcaaf900fd1cc/executive_dashboard.png)

A data engineering and analytics pipeline that generates synthetic restaurant sales data, processes it through an ETL pipeline, and produces a business intelligence dashboard with revenue insights and forecasting.


## Overview

This project simulates a real-world analytics pipeline for a restaurant business.

It generates synthetic restaurant sales data, processes it through a **data engineering ETL pipeline**, and produces a **business intelligence dashboard** that highlights revenue trends, staff performance, and operational insights.

The goal of the project is to demonstrate how raw transactional data can be transformed into **actionable business insights** using Python-based analytics tools.

## 🎯 Project Goals

This project was built to demonstrate:

• Data engineering workflows (ETL pipelines)
• Data cleaning and validation
• Business analytics and metric design
• Automated dashboard generation
• Reproducible environments using Docker


## 🚀 Features

**Synthetic Data Generation**

• Uses Faker and NumPy to generate **12,000+ realistic restaurant transactions**
• Simulates peak hours, missing values, and data inconsistencies

**ETL Pipeline**

• Data cleaning and validation
• Removal of impossible records (e.g., cost higher than price)
• Handling of missing values and outliers

**Business Intelligence Metrics**

• Menu item profitability analysis
• Revenue contribution by category
• Server performance analysis (revenue vs order volume)
• Time-based performance (Lunch vs Dinner)

**Revenue Forecasting**

• Simple **7-day revenue projection** based on historical day-of-week trends

**Automated Dashboard**

• Generates a high-resolution **executive dashboard**
• Includes 6 different analytical visualizations

**Containerized Environment**

• Fully **Dockerized** for reproducible execution across systems



## 📊 Dashboard Insights

• Top 10 Dishes by Revenue
• Revenue Mix by Category
• Server Efficiency Analysis
• 7-Day Revenue Forecast
• Lunch vs Dinner Performance
• Hourly Sales Trends

*(Dashboard image generated in "outputs/executive_dashboard.png")*



## 🛠 Tech Stack

**Language**

• Python 3.10

**Libraries**

• Pandas
• NumPy
• Matplotlib
• Seaborn
• Faker

**Tools**

• Docker



## ⚙️ Data Pipeline

1. **Data Generation**

  • Faker creates realistic restaurant orders
  • NumPy introduces variability and outliers

2. **Data Cleaning**

  • Remove invalid records
  • Handle missing values
  • Validate pricing logic

3. **Feature Engineering**

  • Profit calculation
  • Time segmentation (Lunch/Dinner)
  • Server performance metrics

4. **Visualization**

  • Dashboard generated using Matplotlib



## 🚦 Getting Started

### Prerequisites

• Docker installed
  OR
• Python 3.10+



### Option 1: Run with Docker (Recommended)

Build the image:

```bash
docker build -t restaurant-analytics .
```

Run the container:

On Mac or Linux:
```bash
docker run -v $(pwd)/outputs:/app/outputs restaurant-analytics
```

On Windows (Command Prompt/CMD):
```bash
docker run -v %cd%/outputs:/app/outputs restaurant-analytics
```

On Windows (PowerShell):
```bash
docker run -v ${PWD}/outputs:/app/outputs restaurant-analytics
```

### Option 2: Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python main.py
```

---

## 📁 Project Structure

```
project/
│
├── main.py          # Pipeline orchestrator
├── script.py        # Synthetic data generator
├── analysis.py      # Data cleaning and metric calculations
├── visualize.py     # Dashboard generation
│
└── outputs/
    ├── sales_data.csv
    └── executive_dashboard.png
```

## 📌 Purpose of the Project

Restaurants generate large amounts of operational data, but many businesses do not analyze it effectively.

This project demonstrates how a simple **data pipeline + analytics workflow** can transform raw sales data into useful insights such as:

• Best-selling dishes
• Peak revenue hours
• Staff efficiency
• Revenue forecasting
