import os
import sys
import time
import script
import analysis
import visualize

def run_pipeline():
  print("="*40)
  print("RESTAURANT ANALYTICS PIPELINE")
  print("="*40)
  start_time = time.time()

  # Step 1: Data Generation
  print("\n[1/3] Generating synthetic data...")
  script.generate_sales_data(num_orders=12000)

  # Step 2: Analysis
  print("\n[2/3] Performing ETL and calculating metrics...")
  try:
    results = analysis.run_analysis("outputs/restaurant_sales.csv")
    analysis.save_csvs(results)
  except Exception as e:
    print(f"Analysis failed: {e}")
    return

  # Step 3: Visualization
  print("\n[3/3] Generating executive dashboard...")
  visualize.create_dashboard()

  end_time = time.time()
  duration = round(end_time - start_time, 2)
  print(f"\n{'='*40}")
  print(f"Pipeline finished successfully in {duration}s")
  print("Outputs available in the /outputs/ folder.")
  print('='*40)

if __name__ == "__main__":
  run_pipeline()