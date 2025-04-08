# Agricultural Management System 🌱

A smart **Agricultural Management System** built with **PostgreSQL** and **Flask** to efficiently manage and track farms, crops, sensors, and transactions. This system aims to streamline agricultural operations through structured data management and role-based access control.

## 🚀 Project Overview

### Context:
AgriTech Solutions, a mid-sized agricultural management company, faced challenges managing farm operations through spreadsheets and CSV files. As the company grew, data inconsistencies, duplicated records, and inefficient workflows became significant hurdles. The company also began adopting IoT sensors for monitoring environmental factors like soil moisture, temperature, and humidity, but integrating this data into their workflow proved difficult.

### Goals:
The company transitioned to a structured database system with the following objectives:
1. **Centralized Data Management**: Migrate all historical data from CSV files to a robust PostgreSQL database.
2. **Role-Based Access Control (RBAC)**: Implement user roles with specific privileges to secure data.
3. **Comprehensive Documentation**: Ensure all database structures, scripts, and processes are well-documented and replicable.

### Approach:
- Designed and implemented a **relational database schema** in PostgreSQL, ensuring data integrity through tables, relationships, and constraints.
- Migrated data from CSV files and utilized **Python’s Faker library** to generate synthetic test data.
- Established a **role-based access control system** to ensure secure management of users and their respective permissions.

## 💡 Database Schema
The system uses a relational database with key tables, including:

- **Users**: Manages farm owners, workers, and auditors.
- **Farms**: Stores farm-related information.
- **Fields**: Represents specific field divisions within farms.
- **Crops**: Tracks planting, growth, and harvesting data.
- **Irrigation**: Logs irrigation schedules and details.
- **Fertilization**: Records fertilizer applications.
- **Transactions**: Stores financial transaction records.
- **Sensor Data**: Stores environmental data from IoT sensors.

## 🔐 User Roles & Permissions
The database includes a **role-based access control (RBAC)** system to manage user permissions efficiently.

| Privilege           | Admin | Owner | Worker (Limited) | Auditor |
|---------------------|:-----:|:-----:|:----------------:|:-------:|
| CREATE TABLE        | ✅    | ❌    | ❌               | ❌      |
| DROP TABLE          | ✅    | ❌    | ❌               | ❌      |
| INSERT DATA         | ✅    | ✅    | ✅               | ❌      |
| UPDATE DATA         | ✅    | ✅    | ✅               | ❌      |
| DELETE DATA         | ✅    | ✅    | ❌               | ❌      |
| SELECT DATA         | ✅    | ✅    | ✅               | ✅      |
| ALTER TABLE         | ✅    | ❌    | ❌               | ❌      |
| MANAGE USERS        | ✅    | ✅    | ❌               | ❌      |

**Role Definitions**:
- **Admin**: Full control over the database (superuser).
- **Owner**: Full CRUD (Create, Read, Update, Delete) access to system data.
- **Worker**: Limited access (Read, Insert, and Update for specific tables).
- **Auditor**: Read-only access to all system data.

## 🛠️ Setup and Installation
For detailed instructions on setting up the project, refer to the [setup guide](docs/setup_guide.md).

## 🚧 Future Implementations
In future iterations, the project will be expanded to include:
- **Dockerization**: Containerize both the Flask API and PostgreSQL database for improved scalability and portability.
- **Performance Optimization**: Implement query optimization strategies to enhance system efficiency.
