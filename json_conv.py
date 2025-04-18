import pandas as pd
import json

# Load the JSON data
with open("input_data/feverous_train_challenges.json", "r") as f:
    data = [json.loads(line) for line in f]

# Convert to DataFrame
df = pd.DataFrame(data)

# Filter for rows where label is exactly "SUPPORTS"
true_statements = df[df["label"] == "SUPPORTS"][["claim"]]

# Shuffle the rows
true_statements = true_statements.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
true_statements.to_csv("input_data/input.csv", index=False)