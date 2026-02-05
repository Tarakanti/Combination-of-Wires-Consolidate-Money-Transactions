import pandas as pd
from datetime import datetime

DATA_FOLDER = r"C:\Users\tarak\OneDrive\Desktop\project"

today = datetime.now().date()
input_file = f"{DATA_FOLDER}\\transactions_{today}.csv"
output_file = f"{DATA_FOLDER}\\report_{today}.csv"

df = pd.read_csv(input_file)

df['Date'] = pd.to_datetime(df['Date']).dt.date

summary = (
    df.groupby(['Customer_ID', 'Date'])
      .agg(Total_Amount=('Amount', 'sum'),
           Num_Transactions=('Transaction_ID', 'count'))
      .reset_index()
)

summary.to_csv(output_file, index=False)

print(f" Report saved to: {output_file} with {len(summary)} rows")
