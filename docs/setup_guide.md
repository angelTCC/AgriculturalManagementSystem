## 👅 Setup & Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
# Clone the repository to your local machine
git clone https://github.com/yourusername/AgriDataHub.git  
cd AgriDataHub
```

### 2. Set Up Python Environment

Create a virtual environment and install the necessary dependencies:

```bash
# Create a virtual environment
python3 -m venv .env 

# Activate the environment (Linux)
source .env/bin/activate

# Install required Python dependencies
pip install -r requirements.txt
```

### 3. Set Up PostgreSQL Database

Make sure you have PostgreSQL running. Then, create the `farm_management` database:

```bash
# Create the database
psql -U postgres -c "CREATE DATABASE farm_management;"
```

### 4. Apply Database Schema

Run the SQL schema to set up the tables and constraints:

```bash
# Apply schema to the database
psql -U postgres -d farm_management -f sql/schema.sql
```

Exactly! You're right — the `admin` role, if it's set as a **superuser**, automatically has all privileges, including access to sequences. So there's no need to explicitly grant sequence permissions to `admin`.

Here’s the revised and cleaner version:

### 5. Set Up Roles, Users, and Permissions

Run the SQL script to create roles and assign appropriate permissions:

```bash
psql -U postgres -d farm_management -f sql/authorization.sql
```

#### ⚠️ Sequence Permissions

Tables with auto-incrementing IDs (e.g., `crops`, `fields`, `transactions`) use **sequences**.  
To allow non-superuser roles like `worker` and `owner` to insert data, you must grant them access to these sequences:

```bash
# Grant sequence access to roles that insert data
psql -U postgres -d farm_management -c "GRANT USAGE, SELECT ON SEQUENCE crops_crop_id_seq TO worker, owner;"
psql -U postgres -d farm_management -c "GRANT USAGE, SELECT ON SEQUENCE fields_field_id_seq TO worker, owner;"
psql -U postgres -d farm_management -c "GRANT USAGE, SELECT ON SEQUENCE transactions_transaction_id_seq TO worker, owner;"
```

> 🔐 No need to grant these permissions to `admin` if it's a superuser — it already has full access.

### 6. Generate Synthetic Data

Run the Python script to generate synthetic data and store it in the `data` directory:

```bash
# Generate synthetic data (CSV files)
python3 ./scripts/synthetic_data.py
```

### 7. Load Initial Data Into the Database

Load the synthetic data (in CSV format) into the database:

```bash
# Load initial data into the database
psql -U postgres -d farm_management -f sql/seed_data.sql
```

### 8. Fix Sequence for Auto-Increment

To avoid issues with the auto-incrementing fields, reset the sequence:

```bash
# Set the sequence for the crops table
psql -U postgres -d farm_management -c "SELECT setval('crops_crop_id_seq', (SELECT MAX(crop_id) FROM crops));"
```

### 9. Run the Flask Application

Start the Flask application. By default, the `worker` user will be logged in.

```bash
# Run the Flask application
python3 app.py
```

### 10. Example: Making a POST Request to the API

Once the Flask app is running, you can test the POST `/api/crops` endpoint with the following cURL command:

```bash
# Example of implementing POST API for crops under the worker user
curl -X POST http://localhost:5000/api/crops -H "Content-Type: application/json" -d '{"field_id": 3, "crop_type": "rice", "planting_date": "2025-04-05", "harvest_date": "2025-07-20", "status": "planted"}'
```

For more details about the API, refer to the documentation in `/docs/api_documentation.md`.
