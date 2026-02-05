import pandas as pd
import random
from datetime import datetime

SAVE_PATH = r"C:\Users\tarak\OneDrive\Desktop\project"
NUM_TRANSACTIONS = 5000
CLIENT_ID = "C001"
TXN_MODES = ['Wire', 'NEFT', 'RTGS', 'UPI']
STATUSES = ['Success', 'Failed'] 

today = datetime.now().date()
num_customers = random.randint(200, 300)
customer_ids = [f"U{str(i).zfill(4)}" for i in range(1, num_customers + 1)]

num_one_time = max(1, int(num_customers * 0.05))
one_time_customers = random.sample(customer_ids, num_one_time)
repeat_customers = list(set(customer_ids) - set(one_time_customers))

transactions = []
txn_id_counter = 1

for cust_id in one_time_customers:
    transactions.append({
        'Transaction_ID': f"T{txn_id_counter:06d}",
        'Client_ID': CLIENT_ID,
        'Customer_ID': cust_id,
        'Amount': random.randint(100, 10000),
        'Date': today,
        'Mode': random.choice(TXN_MODES),
        'Status': random.choices(STATUSES, weights=[90, 10])[0]
    })
    txn_id_counter += 1

remaining_txns = NUM_TRANSACTIONS - len(transactions)
for _ in range(remaining_txns):
    cust_id = random.choice(repeat_customers)
    transactions.append({
        'Transaction_ID': f"T{txn_id_counter:06d}",
        'Client_ID': CLIENT_ID,
        'Customer_ID': cust_id,
        'Amount': random.randint(100, 10000),
        'Date': today,
        'Mode': random.choice(TXN_MODES),
        'Status': random.choices(STATUSES, weights=[90, 10])[0]
    })
    txn_id_counter += 1

df = pd.DataFrame(transactions)
file_name = f"{SAVE_PATH}\\transactions_{today}.csv"
df.to_csv(file_name, index=False)

print(f" Dataset saved to: {file_name} with {len(df)} records and {len(customer_ids)} customers")
