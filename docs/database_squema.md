T# 📌 Database Schema Metadata - Agricultural Management System

## 1️⃣ USERS TABLE
- **Description:** Stores information about users (farm owners and workers).
- **Primary Key:** `user_id`
- **Relationships:** `user_id` → `farms` (1:M)

### Columns:
| Column Name  | Data Type        | Constraints | Description |
|-------------|----------------|-------------|-------------|
| `user_id`    | `SERIAL`        | `PRIMARY KEY` | Unique identifier for each user. |
| `name`       | `VARCHAR(100)`  | `NOT NULL` | Full name of the user. |
| `email`      | `VARCHAR(100)`  | `UNIQUE NOT NULL` | Unique email address. |
| `role`       | `VARCHAR(50)`   | `CHECK (role IN ('owner', 'worker'))` | Role in the system. |
| `created_at` | `TIMESTAMP`     | `DEFAULT CURRENT_TIMESTAMP` | Account creation date. |

---

## 2️⃣ FARMS TABLE
- **Description:** Represents farms owned by users.
- **Primary Key:** `farm_id`
- **Relationships:** `farm_id` → `fields` (1:M), `farm_id` → `transactions` (1:M)

### Columns:
| Column Name  | Data Type       | Constraints | Description |
|-------------|---------------|-------------|-------------|
| `farm_id`    | `SERIAL`       | `PRIMARY KEY` | Unique identifier for each farm. |
| `user_id`    | `INT`          | `REFERENCES users(user_id) ON DELETE CASCADE` | Owner of the farm. |
| `name`       | `VARCHAR(100)` | `NOT NULL` | Farm name. |
| `location`   | `TEXT`         | `NOT NULL` | Location (GPS coordinates or address). |
| `size`       | `DECIMAL(10,2)`| `CHECK (size > 0)` | Total farm size in hectares. |

---

## 3️⃣ FIELDS TABLE
- **Description:** Stores data about different fields within farms.
- **Primary Key:** `field_id`
- **Relationships:** `field_id` → `crops`, `irrigation`, `fertilization`, `sensor_data` (1:M)

### Columns:
| Column Name  | Data Type       | Constraints | Description |
|-------------|---------------|-------------|-------------|
| `field_id`   | `SERIAL`       | `PRIMARY KEY` | Unique identifier for each field. |
| `farm_id`    | `INT`          | `REFERENCES farms(farm_id) ON DELETE CASCADE` | Farm that owns the field. |
| `name`       | `VARCHAR(100)` | `NOT NULL` | Field name or number. |
| `area`       | `DECIMAL(10,2)`| `CHECK (area > 0)` | Field size in hectares. |

---

## 4️⃣ CROPS TABLE
- **Description:** Tracks the crops grown in each field.
- **Primary Key:** `crop_id`
- **Relationships:** `field_id` → `crops` (1:M)

### Columns:
| Column Name  | Data Type      | Constraints | Description |
|-------------|--------------|-------------|-------------|
| `crop_id`    | `SERIAL`      | `PRIMARY KEY` | Unique crop identifier. |
| `field_id`   | `INT`         | `REFERENCES fields(field_id) ON DELETE CASCADE` | Field where the crop is planted. |
| `crop_type`  | `VARCHAR(50)` | `CHECK (crop_type IN ('wheat', 'corn', 'rice', 'soybean', 'potato', 'barley', 'cotton', 'sunflower'))` | Type of crop. |
| `planting_date` | `DATE`     | `NOT NULL` | Date of planting. |
| `harvest_date` | `DATE`     | `NULL` | Expected/actual harvest date. |
| `status`     | `VARCHAR(20)` | `CHECK (status IN ('planted', 'growing', 'harvested'))` | Crop growth stage. |

---

## 5️⃣ SENSOR DATA TABLE
- **Description:** Stores sensor readings for fields.
- **Primary Key:** `sensor_id`
- **Relationships:** `field_id` → `sensor_data` (1:M)

### Columns:
| Column Name  | Data Type      | Constraints | Description |
|-------------|--------------|-------------|-------------|
| `sensor_id`  | `SERIAL`      | `PRIMARY KEY` | Unique sensor reading ID. |
| `field_id`   | `INT`         | `REFERENCES fields(field_id) ON DELETE CASCADE` | Related field. |
| `sensor_type`| `VARCHAR(50)` | `CHECK (sensor_type IN ('temperature', 'humidity', 'soil_moisture', 'pH', 'EC'))` | Type of sensor. |
| `value`      | `DECIMAL(10,2)` | `NOT NULL` | Recorded value. |
| `timestamp`  | `TIMESTAMP`   | `DEFAULT CURRENT_TIMESTAMP` | Time of recording. |

---

## 6️⃣ TRANSACTIONS TABLE
- **Description:** Records financial transactions related to the farm.
- **Primary Key:** `transaction_id`
- **Relationships:** `farm_id` → `transactions` (1:M)

### Columns:
| Column Name  | Data Type      | Constraints | Description |
|-------------|--------------|-------------|-------------|
| `transaction_id` | `SERIAL`  | `PRIMARY KEY` | Unique transaction ID. |
| `farm_id`        | `INT`     | `REFERENCES farms(farm_id) ON DELETE CASCADE` | Related farm. |
| `amount`         | `DECIMAL(10,2)` | `NOT NULL` | Transaction value. |
| `type`           | `VARCHAR(20)` | `CHECK (type IN ('expense', 'income'))` | Transaction type. |
| `category`       | `VARCHAR(50)` | `NOT NULL` | Expense/income category. |
| `transaction_date` | `DATE` | `DEFAULT CURRENT_DATE` | Date of transaction. |

---

## 📌 Final Notes:
- **Indexes:** Add indexes on foreign keys for performance.
- **Normalization:** The schema follows **3rd Normal Form (3NF)** to avoid redundancy.
- **Data Integrity:** `ON DELETE CASCADE` ensures referential integrity.

---

This metadata document provides **a structured, professional, and formal overview** of the database schema, making it useful for **developers, analysts, and database administrators**. 🚀

