-- Create a new schema
CREATE SCHEMA company;

-- Create a table in the new schema
CREATE TABLE company.employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(50)
);

-- Insert data into the schema's table
INSERT INTO
    company.employees (name, position)
VALUES
    ('Bob', 'Manager');

-- Query data from the schema's table
SELECT
    *
FROM
    company.employees;