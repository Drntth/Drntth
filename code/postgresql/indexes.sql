-- Create a table for demonstration
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(50),
    location POINT,
    tags TEXT [],
    salary NUMERIC
);

-- B-tree index (default, best for equality and range queries)
CREATE INDEX idx_employees_name ON employees(name);

-- Hash index (for simple equality comparisons)
CREATE INDEX idx_employees_name_hash ON employees USING HASH (name);

-- GiST index (for geometric types, range types, and full-text search)
CREATE INDEX idx_employees_location_gist ON employees USING GiST (location);

-- GIN index (for array, jsonb, and full-text search)
CREATE INDEX idx_employees_tags_gin ON employees USING GIN (tags);

-- BRIN index (for very large tables with naturally ordered data, e.g. timestamps)
CREATE INDEX idx_employees_salary_brin ON employees USING BRIN (salary);

-- Query that benefits from the B-tree or Hash index
SELECT
    *
FROM
    employees
WHERE
    name = 'Alice';

-- Query that benefits from the GiST index (geometric search)
SELECT
    *
FROM
    employees
WHERE
    location ~ = POINT(10, 20);

-- Query that benefits from the GIN index (array search)
SELECT
    *
FROM
    employees
WHERE
    tags @ > ARRAY ['remote'];

-- Query that benefits from the BRIN index (range search on large, ordered data)
SELECT
    *
FROM
    employees
WHERE
    salary > 50000;

-- Drop an index
DROP INDEX idx_employees_name;

DROP INDEX idx_employees_name_hash;

DROP INDEX idx_employees_location_gist;

DROP INDEX idx_employees_tags_gin;

DROP INDEX idx_employees_salary_brin;