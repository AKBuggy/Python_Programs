# Import necessary libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Sample dataset (transactions)
data = {
    'Transaction': [1, 1, 2, 2, 2, 3, 3, 4, 4, 4],
    'Item': ['Bread', 'Milk', 'Bread', 'Diaper', 'Beer', 'Bread', 'Milk', 'Bread', 'Diaper', 'Beer']
}

# Create a DataFrame from the dataset
df = pd.DataFrame(data)

# Encoding the items as binary variables
encoded_df = pd.get_dummies(df['Item'])

# Concatenate the transaction ID and the encoded items
df_encoded = pd.concat([df['Transaction'], encoded_df], axis=1)

# Find frequent itemsets using Apriori algorithm
frequent_itemsets = apriori(df_encoded.drop('Transaction', axis=1), min_support=0.2, use_colnames=True)

# Print frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# Print association rules
print("\nAssociation Rules:")
print(rules)
