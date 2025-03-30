-- USERS TABLE
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(50) CHECK (role IN ('owner', 'worker')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- FARMS TABLE
CREATE TABLE farms (
    farm_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    location TEXT NOT NULL,
    size DECIMAL(10,2) CHECK (size > 0)
);

-- FIELDS TABLE
CREATE TABLE fields (
    field_id SERIAL PRIMARY KEY,
    farm_id INT REFERENCES farms(farm_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    area DECIMAL(10,2) CHECK (area > 0)
);

-- CROPS TABLE
CREATE TABLE crops (
    crop_id SERIAL PRIMARY KEY,
    field_id INT REFERENCES fields(field_id) ON DELETE CASCADE,
    crop_type VARCHAR(50) CHECK (crop_type IN ('wheat', 'corn', 'rice', 'soybean', 'potato', 'barley', 'cotton', 'sunflower')),
    planting_date DATE NOT NULL,
    harvest_date DATE,
    status VARCHAR(20) CHECK (status IN ('planted', 'growing', 'harvested'))
);

-- IRRIGATION TABLE
CREATE TABLE irrigation (
    irrigation_id SERIAL PRIMARY KEY,
    field_id INT REFERENCES fields(field_id) ON DELETE CASCADE,
    water_volume DECIMAL(10,2) CHECK (water_volume > 0),
    method VARCHAR(50) CHECK (method IN ('drip', 'sprinkler', 'flood', 'manual')),
    date DATE DEFAULT CURRENT_DATE
);

-- FERTILIZATION TABLE
CREATE TABLE fertilization (
    fertilization_id SERIAL PRIMARY KEY,
    field_id INT REFERENCES fields(field_id) ON DELETE CASCADE,
    fertilizer_type VARCHAR(50) CHECK (fertilizer_type IN ('organic', 'chemical', 'compost', 'manure', 'biofertilizer')),
    quantity DECIMAL(10,2) CHECK (quantity > 0),
    application_date DATE DEFAULT CURRENT_DATE
);

-- TRANSACTIONS TABLE
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    farm_id INT REFERENCES farms(farm_id) ON DELETE CASCADE,
    amount DECIMAL(10,2) NOT NULL,
    type VARCHAR(20) CHECK (type IN ('expense', 'income')),
    category VARCHAR(50) CHECK (category IN ('equipment', 'labor', 'seeds', 'fertilizer', 'irrigation', 'harvest', 'sale', 'maintenance', 'other')),
    transaction_date DATE DEFAULT CURRENT_DATE
);

-- SENSOR_DATA TABLE (Attributes stored as rows)
CREATE TABLE sensor_data (
    sensor_id SERIAL PRIMARY KEY,
    field_id INT REFERENCES fields(field_id) ON DELETE CASCADE,
    sensor_type VARCHAR(50) CHECK (sensor_type IN ('temperature', 'humidity', 'soil_moisture', 'light_intensity')),
    value DECIMAL(10,2) NOT NULL,
    reading_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- INDEXES FOR PERFORMANCE
CREATE INDEX idx_farm_user ON farms(user_id);
CREATE INDEX idx_field_farm ON fields(farm_id);
CREATE INDEX idx_crop_field ON crops(field_id);
CREATE INDEX idx_irrigation_field ON irrigation(field_id);
CREATE INDEX idx_fertilization_field ON fertilization(field_id);
CREATE INDEX idx_transaction_farm ON transactions(farm_id);
CREATE INDEX idx_sensor_field ON sensor_data(field_id);
