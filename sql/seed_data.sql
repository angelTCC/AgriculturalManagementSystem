TRUNCATE TABLE users, farms, fields, crops, irrigation, fertilization, sensor_data, transactions CASCADE;


-- Load data into users table
\copy users(user_id, name, email, role, created_at) FROM './data/users.csv' DELIMITER ',' CSV HEADER;

-- Load data into farm table
\copy farms(farm_id, user_id, name, location, size) FROM './data/farms.csv' DELIMITER ',' CSV HEADER;

-- Load data into fields table
\copy fields(field_id, farm_id, name, area) FROM './data/fields.csv' DELIMITER ',' CSV HEADER;



-- Load data into crops table
\copy crops(crop_id, field_id, crop_type, planting_date, harvest_date, status) FROM './data/crops.csv' DELIMITER ',' CSV HEADER;

-- Load data into irrigation table
\copy irrigation(irrigation_id, field_id, water_volume, method, date) FROM './data/irrigations.csv' DELIMITER ',' CSV HEADER;

-- Load data into sensor table
\copy sensor_data(sensor_id, field_id, sensor_type, value, reading_time) FROM './data/sensor_data.csv' DELIMITER ',' CSV HEADER;

-- Load data into transactions table
\copy transactions(transaction_id, farm_id, amount, type, category, transaction_date) FROM './data/transactions.csv' DELIMITER ',' CSV HEADER;

-- Load data into fertilization table
\copy fertilization(fertilization_id, field_id, fertilizer_type, quantity, application_date) FROM './data/fertilizations.csv' DELIMITER ',' CSV HEADER;
