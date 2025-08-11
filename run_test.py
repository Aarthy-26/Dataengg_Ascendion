import pandas as pd

class CustomerTransactionProcessor:
    def load_customers(self, filepath: str) -> pd.DataFrame:
        customer_df=pd.read_csv(filepath)
        return customer_df

    def load_transactions(self, filepath: str) -> pd.DataFrame:
       return pd.read_csv(filepath)
    def clean_transaction_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.dropna()
        df = df.drop_duplicates()
        return df

    def merge_data(self, transactions: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
        merged_df = pd.merge(transactions, customers, on='CustomerID', how='inner')
        merged_df['TotalAmount'] = merged_df['Quantity'] * merged_df['Amount']
        return merged_df


    def calculate_total_by_membership(self, merged_df: pd.DataFrame) -> pd.DataFrame:
        result = merged_df.groupby('MembershipLevel')['TotalAmount'].sum().reset_index()
        result.rename(columns={'TotalAmount': 'TotalSpent'}, inplace=True)
        return result
