import pandas as pd

# Creating a simple dataset with 10 rows
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'LIMIT_BAL': [20000, 120000, 90000, 50000, 50000, 50000, 500000, 100000, 140000, 20000],
    'EDUCATION': [2, 2, 2, 2, 2, 1, 1, 2, 3, 3],
    'AGE': [24, 26, 34, 37, 57, 37, 29, 23, 28, 35],
    'PAY_0': [2, -1, 0, 0, -1, 0, 0, 0, 0, -2],
    'BILL_AMT1': [3913, 2682, 29239, 46990, 8617, 64400, 367965, 11876, 11285, 0],
    'PAY_AMT1': [0, 0, 1518, 2000, 2000, 2500, 55000, 380, 3329, 0],
    'default.payment.next.month': [1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
}

# Create a DataFrame
credit_card_data = pd.DataFrame(data)
student_df.to_csv('student_dataset.csv', index=False)
# Display the created dataset
print(credit_card_data)