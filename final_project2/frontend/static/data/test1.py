import pandas as pd
import random

# Read the CSV file into a DataFrame
df = pd.read_csv('df.csv')

# List of Indian states
indian_states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
                 "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
                 "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
                 "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]

# Update 'st' and 'stname' columns
df['st'] = "IN"
df['stname'] = df['stname'].apply(lambda x: random.choice(indian_states))

# Write the updated DataFrame back to a new CSV file
df.to_csv('output_file.csv', index=False)

print("Processing completed.")
