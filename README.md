# Agricultural Management System 🌱

A smart **agriculture management system** using **PostgreSQL** and **Django** to efficiently track farms, crops, sensors, and transactions.

## 🚀 Project Overview
For years, AgriTech Solutions, a mid-sized agricultural management company, has relied on spreadsheets and CSV files to track farm operations. Initially, this method worked well for managing field data, crop cycles, and financial transactions. However, as the company expanded, inefficiencies in data handling became evident.

Farm managers often struggled with inconsistent records, duplicated data, and difficulties in accessing information quickly. Employees had to manually consolidate reports from multiple spreadsheets, a time-consuming process prone to human error. The company also began adopting IoT sensors to monitor environmental factors such as soil moisture, temperature, and humidity, but integrating this data into their existing workflow proved challenging.

Recognizing these limitations, the company decided to transition to a structured database system. Their goals were clear:

1. **Data Centralization**: Migrating all historical data from CSV files into a robust PostgreSQL database.
2. **User Roles & Permissions**: Implementing a role-based access control (RBAC) system to manage data securely.
3. **Query Optimization**: Enhancing performance by reducing query execution time.
4. **Comprehensive Documentation**: Ensuring all database structures and scripts are well-documented and replicable.

### Approach:
- Designed the **database schema** using **draw.io**.
- Implemented the schema in **PostgreSQL**, creating tables, relationships, and constraints.
- Imported existing data from CSV files and used **Python's Faker library** to generate synthetic data for testing.
- Focused on **query optimization**, indexing, and improving database performance.
- Established **user roles and privileges** to maintain data security and integrity.

## 🛠️ Tech Stack
- **Database:** PostgreSQL
- **Backend:** Django, Python
- **Data Handling:** Pandas, Faker (for synthetic data generation)
- **Containerization:** Docker, Docker Compose
- **Visualization & Documentation:** Draw.io, Markdown

## 📌 Features
- 🌾 Manage farms, fields, and crops.
- 🚜 Track irrigation and fertilization activities.
- 💰 Record financial transactions.
- 🛁 Store environmental sensor data (humidity, temperature, soil moisture, etc.).
- 🔍 Optimize performance with **indexing and query optimization**.
- 🔑 Secure role-based access control (RBAC).

## 💊 Database Schema
The system utilizes a **relational database** with the following key tables:
- **Users**: Manages farm owners, workers, and auditors.
- **Farms**: Stores details about different farms.
- **Fields**: Represents specific field divisions within farms.
- **Crops**: Tracks planting, growth, and harvesting.
- **Irrigation**: Logs irrigation schedules and details.
- **Fertilization**: Records fertilizer applications.
- **Transactions**: Stores financial records.
- **Sensor Data**: Stores environmental sensor readings.

📚 **[View Full Database Documentation](docs/database_schema.md)**  
📚 **[Schema Diagram (draw.io)](https://drive.google.com/file/d/1mV3-faYCJ_EjsKRXoJhrw-YT_99Kelk7/view?usp=sharing)**

## 🔹 User Roles & Permissions
The database includes a **role-based access control system** to manage permissions effectively.

| Privilege           | Admin | Owner | Worker (Limited) | Auditor |
|---------------------|:-----:|:-----:|:---------------:|:-------:|
| CREATE TABLE       | ✅    | ❌    | ❌              | ❌      |
| DROP TABLE         | ✅    | ❌    | ❌              | ❌      |
| INSERT DATA        | ✅    | ✅    | ✅              | ❌      |
| UPDATE DATA        | ✅    | ✅    | ✅              | ❌      |
| DELETE DATA        | ✅    | ✅    | ❌              | ❌      |
| SELECT DATA        | ✅    | ✅    | ✅              | ✅      |
| ALTER TABLE        | ✅    | ❌    | ❌              | ❌      |
| MANAGE USERS       | ✅    | ✅    | ❌              | ❌      |

**Roles & Permissions:**
- **Admin**: Full control over the database (superuser).
- **Owner**: Full CRUD (Create, Read, Update, Delete) access.
- **Worker**: Limited permissions (Read, Insert, and Update for specific tables).
- **Auditor**: Read-only access to all tables.

## 👅 Setup & Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/AgriDataHub.git  
cd AgriDataHub

# Start PostgreSQL and create the database
psql -U your_user -d your_db -f sql/schema.sql
```

## 🐢 Deployment (Using Docker)
```bash
# Build and start the PostgreSQL container
docker-compose up -d

# Apply migrations (if using Django ORM)
python manage.py migrate
```

## 📂 Project Structure
```
AgriDataHub/  
│── sql/  
│   ├── schema.sql          # Tables, constraints, indexes, views  
│   ├── triggers.sql        # Triggers for automation  
│   ├── transactions.sql    # Example transactions  
│   ├── seed_data.sql       # Initial data for testing  
│   ├── queries.sql         # Sample queries (reports, analytics, etc.)  
│   ├── authorization.sql   # User roles & permissions  
│  
│── docs/  
│   ├── ERD.png             # Entity-Relationship Diagram  
│   ├── api_docs.md         # API documentation  
│   ├── setup.md            # How to set up the project  
│  
│── .gitignore  
│── README.md  
│── requirements.txt        # Python dependencies  
│── docker-compose.yml      # Optional: PostgreSQL container  
│── manage.py  
```

## 📊 Example Queries (Optimized)
```sql
-- Retrieve all crops for a specific farm with optimized indexing
SELECT c.* FROM crops c
JOIN fields f ON c.field_id = f.id
JOIN farms fa ON f.farm_id = fa.id
WHERE fa.name = 'Farm A';

-- Get total revenue for a farm
SELECT SUM(amount) as total_revenue FROM transactions
WHERE farm_id = (SELECT id FROM farms WHERE name = 'Farm A');
```

---
## 🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request.

---
## 🚀 Future Improvements
- Implement **Django ORM** for better database interactions.
- Integrate a **REST API** for seamless frontend-backend communication.
- Improve **real-time analytics and reporting** features.

---
Feel free to contribute or suggest improvements! 🎯

