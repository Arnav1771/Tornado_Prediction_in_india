import json
import random

# Read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# List of Indian states
indian_states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
                 "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
                 "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
                 "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]

# Iterate through each feature and update 'st' and 'StName'
for feature in data['features']:
    feature['properties']['st'] = "IN"
    feature['properties']['StName'] = random.choice(indian_states)

# Write the updated data back to the JSON file
with open('output_file.json', 'w') as output_file:
    json.dump(data, output_file, indent=2)

print("Processing completed.")

