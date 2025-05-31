import pandas as pd

df = pd.read_csv("train.csv")

df_sorted = df.sort_values(by="past_waste_kg")

df_sorted.to_csv("train_sorted_by_past_waste_kg.csv", index=False)
