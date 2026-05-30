import pandas as pd
product_cost = pd.read_csv("cost_per_material.csv")
global_supply = pd.read_csv("global_supply.csv")

print(product_cost.head(10))
print(global_supply.head(10))