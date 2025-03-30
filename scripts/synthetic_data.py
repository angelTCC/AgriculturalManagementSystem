from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Define the number of records
num_users = 100
max_farms_per_user = 10
max_fields_per_farm = 10
max_fertilizations_per_field = 5
max_irrigations_per_field = 5
max_sensor_readings_per_field = 5
max_transactions_per_farm = 5
max_crops_per_field = 3

# Generate Users
users = []
for user_id in range(1, num_users + 1):
    users.append({
        'user_id': user_id,
        'name': fake.name(),
        'email': fake.unique.email(),
        'role': random.choice(['owner', 'worker']),
        'created_at': fake.date_time_this_decade()
    })

# Generate Farms
farms = []
farm_id_counter = 1
for user in users:
    num_farms = random.randint(1, max_farms_per_user)
    for _ in range(num_farms):
        farms.append({
            'farm_id': farm_id_counter,
            'user_id': user['user_id'],  # Foreign key reference
            'name': fake.company(),
            'location': fake.address(),
            'size': round(random.uniform(1.0, 50.0), 2),
        })
        farm_id_counter += 1

# Generate Fields
fields = []
field_id_counter = 1
for farm in farms:
    num_fields = random.randint(1, max_fields_per_farm)
    for _ in range(num_fields):
        fields.append({
            'field_id': field_id_counter,
            'farm_id': farm['farm_id'],
            'name': f"Field {field_id_counter}",
            'area': round(random.uniform(0.5, 10.0), 2)  # Random size between 0.5 and 10 hectares
        })
        field_id_counter += 1

# Generate Fertilization Data
fertilizations = []
fertilization_id_counter = 1
fertilizer_types = ['organic', 'chemical', 'compost', 'manure', 'biofertilizer']

for field in fields:
    num_fertilizations = random.randint(1, max_fertilizations_per_field)
    for _ in range(num_fertilizations):
        fertilizations.append({
            'fertilization_id': fertilization_id_counter,
            'field_id': field['field_id'],
            'fertilizer_type': random.choice(fertilizer_types),
            'quantity': round(random.uniform(10.0, 200.0), 2),  # Random quantity between 10 and 200 kg
            'application_date': fake.date_between(start_date='-2y', end_date='today')
        })
        fertilization_id_counter += 1

# Generate Irrigation Data
irrigations = []
irrigation_id_counter = 1
irrigation_methods = ['drip', 'sprinkler', 'flood', 'manual']

for field in fields:
    num_irrigations = random.randint(1, max_irrigations_per_field)
    for _ in range(num_irrigations):
        irrigations.append({
            'irrigation_id': irrigation_id_counter,
            'field_id': field['field_id'],
            'water_volume': round(random.uniform(100.0, 1000.0), 2),  # Random volume between 100 and 1000 liters
            'method': random.choice(irrigation_methods),
            'date': fake.date_between(start_date='-2y', end_date='today')
        })
        irrigation_id_counter += 1

# Generate Sensor Data
sensor_data = []
sensor_id_counter = 1
sensor_types = ['temperature', 'humidity', 'soil_moisture', 'light_intensity']

for field in fields:
    num_sensors = random.randint(1, max_sensor_readings_per_field)
    for _ in range(num_sensors):
        sensor_data.append({
            'sensor_id': sensor_id_counter,
            'field_id': field['field_id'],
            'sensor_type': random.choice(sensor_types),
            'value': round(random.uniform(10.0, 100.0), 2),  # Random sensor value
            'reading_time': fake.date_time_this_decade()
        })
        sensor_id_counter += 1

# Generate Transactions Data
transactions = []
transaction_id_counter = 1
transaction_types = ['expense', 'income']
transaction_categories = ['equipment', 'labor', 'seeds', 'fertilizer', 'irrigation', 'harvest', 'sale', 'maintenance', 'other']

for farm in farms:
    num_transactions = random.randint(1, max_transactions_per_farm)
    for _ in range(num_transactions):
        transactions.append({
            'transaction_id': transaction_id_counter,
            'farm_id': farm['farm_id'],
            'amount': round(random.uniform(100.0, 10000.0), 2),  # Random amount between 100 and 10,000
            'type': random.choice(transaction_types),
            'category': random.choice(transaction_categories),
            'transaction_date': fake.date_between(start_date='-2y', end_date='today')
        })
        transaction_id_counter += 1

# Generate Crops Data
crops = []
crop_id_counter = 1
crop_types = ['wheat', 'corn', 'rice', 'soybean', 'potato', 'barley', 'cotton', 'sunflower']
crop_statuses = ['planted', 'growing', 'harvested']

for field in fields:
    num_crops = random.randint(1, max_crops_per_field)
    for _ in range(num_crops):
        planting_date = fake.date_between(start_date='-2y', end_date='today')
        harvest_date = planting_date + timedelta(days=random.randint(90, 150))  # Harvest date 90 to 150 days after planting
        crops.append({
            'crop_id': crop_id_counter,
            'field_id': field['field_id'],
            'crop_type': random.choice(crop_types),
            'planting_date': planting_date,
            'harvest_date': harvest_date,
            'status': random.choice(crop_statuses)
        })
        crop_id_counter += 1

# Convert to DataFrames
df_users = pd.DataFrame(users)
df_farms = pd.DataFrame(farms)
df_fields = pd.DataFrame(fields)
df_fertilizations = pd.DataFrame(fertilizations)
df_irrigations = pd.DataFrame(irrigations)
df_sensor_data = pd.DataFrame(sensor_data)
df_transactions = pd.DataFrame(transactions)
df_crops = pd.DataFrame(crops)

# Save to CSV files
df_users.to_csv('./data/users.csv', index=False)
df_farms.to_csv('./data/farms.csv', index=False)
df_fields.to_csv('./data/fields.csv', index=False)
df_fertilizations.to_csv('./data/fertilizations.csv', index=False)
df_irrigations.to_csv('./data/irrigations.csv', index=False)
df_sensor_data.to_csv('./data/sensor_data.csv', index=False)
df_transactions.to_csv('./data/transactions.csv', index=False)
df_crops.to_csv('./data/crops.csv', index=False)

print('Data synthetic created!')

