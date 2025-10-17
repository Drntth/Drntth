-- Create table
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(50),
    salary NUMERIC
);

-- Insert (Create)
INSERT INTO
    employees (name, position, salary)
VALUES
    ('Alice', 'Engineer', 70000),
    ('Bob', 'Manager', 90000);

-- Read (Select all)
SELECT
    *
FROM
    employees;

-- Read (Select with condition)
SELECT
    name,
    salary
FROM
    employees
WHERE
    position = 'Engineer';

-- Select with sorting
SELECT
    *
FROM
    employees
ORDER BY
    salary DESC;

-- Select with limit
SELECT
    *
FROM
    employees
LIMIT
    1;

-- Select distinct values
SELECT
    DISTINCT position
FROM
    employees;

-- Aggregate functions
SELECT
    COUNT(*)
FROM
    employees;

SELECT
    AVG(salary)
FROM
    employees;

SELECT
    MAX(salary)
FROM
    employees;

-- Group by
SELECT
    position,
    AVG(salary)
FROM
    employees
GROUP BY
    position;

-- Update
UPDATE
    employees
SET
    salary = 75000
WHERE
    name = 'Alice';

-- Delete
DELETE FROM
    employees
WHERE
    name = 'Bob';

-- Add new column
ALTER TABLE
    employees
ADD
    COLUMN email VARCHAR(100);

-- Rename column
ALTER TABLE
    employees RENAME COLUMN position TO job_title;

-- Delete column
ALTER TABLE
    employees DROP COLUMN email;

-- Simple join (assuming departments table exists)
-- CREATE TABLE departments (id SERIAL PRIMARY KEY, name VARCHAR(100));
-- ALTER TABLE employees ADD COLUMN department_id INT;
SELECT
    e.name,
    d.name AS department
FROM
    employees e
    JOIN departments d ON e.department_id = d.id;

-- Truncate table (delete all rows, keep structure)
TRUNCATE TABLE employees;

-- Rename table
ALTER TABLE
    employees RENAME TO staff;

-- Drop table
DROP TABLE staff;