-- Remove existing roles to avoid duplication
DROP ROLE IF EXISTS admin, owner, worker, auditor;

-- Create roles
CREATE ROLE admin_farm WITH LOGIN PASSWORD 'admin_password' SUPERUSER;
CREATE ROLE owner WITH LOGIN PASSWORD 'owner_password';
CREATE ROLE worker WITH LOGIN PASSWORD 'worker_password';
CREATE ROLE auditor WITH LOGIN PASSWORD 'auditor_password';

-- Grant permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO owner;
GRANT SELECT, INSERT, UPDATE ON crops, irrigation, fertilization, sensor_data TO worker;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO auditor;

-- Ensure new tables inherit privileges
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO owner;

-- Revoke public access for security
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM public;

-- ✅ Create test users and assign roles
DROP USER IF EXISTS test_admin, test_owner, test_worker, test_auditor;

CREATE USER test_admin WITH PASSWORD 'test_admin_pass';
CREATE USER test_owner WITH PASSWORD 'test_owner_pass';
CREATE USER test_worker WITH PASSWORD 'test_worker_pass';
CREATE USER test_auditor WITH PASSWORD 'test_auditor_pass';

-- Assign roles to users
GRANT admin_farm TO test_admin;
GRANT owner TO test_owner;
GRANT worker TO test_worker;
GRANT auditor TO test_auditor;
