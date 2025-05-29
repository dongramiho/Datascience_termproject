import pandas as pd

# 1. CSV 파일 불러오기
df = pd.read_csv("train.csv")

# 2. ID 기준으로 내림차순 정렬
df_sorted = df.sort_values(by="past_waste_kg")

# 3. 정렬된 결과를 다시 CSV로 저장
df_sorted.to_csv("train_sorted_by_past_waste_kg.csv", index=False)