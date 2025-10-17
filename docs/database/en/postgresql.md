# PostgreSQL

---

> :uk: English | [:hungary: Magyar](../hu/postgresql.md)

**Purpose**: PostgreSQL is a powerful, open-source object-relational database system. It is designed to handle a wide range of workloads, from single machines to large web services, and is known for its reliability, feature set, and extensibility. PostgreSQL supports advanced data types, full ACID compliance, and is highly customizable for various use cases.

---

## Key Concepts

### ACID Compliance

PostgreSQL is fully ACID compliant, meaning it guarantees Atomicity, Consistency, Isolation, and Durability for all transactions. This ensures that database operations are reliable: either all changes in a transaction are applied, or none are, and the database remains in a consistent state even in case of failures.

### Extensibility

PostgreSQL is highly extensible. You can define custom data types, operators, functions, and even procedural languages. Extensions such as `hstore`, `uuid-ossp`, and `pg_trgm` can be added to enhance functionality, making PostgreSQL adaptable to many use cases.

### MVCC (Multi-Version Concurrency Control)

MVCC allows multiple transactions to occur simultaneously without interfering with each other. Instead of locking the entire database, PostgreSQL keeps multiple versions of data, enabling high concurrency and performance for read and write operations.

### Schemas

Schemas are logical containers for database objects (tables, views, functions, etc.). They help organize data, manage permissions, and avoid naming conflicts, especially in large or multi-tenant databases.
See code example below.

### Indexes

Indexes are special lookup tables that the database search engine can use to speed up data retrieval. PostgreSQL supports several index types (B-tree, Hash, GiST, GIN, BRIN), each optimized for different query patterns and data types, improving performance for large datasets.
See code example below.

### Replication

PostgreSQL offers built-in support for both streaming and logical replication. Streaming replication keeps a standby server synchronized with the primary, while logical replication allows selective data replication between databases, supporting high availability and scaling.

### Foreign Data Wrappers (FDW)

FDWs allow PostgreSQL to connect to external data sources (other databases, files, etc.) and query them as if they were local tables. This enables data integration and federation across different systems.

---

## Installation

- **For Ubuntu**:  

  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  ```

This installs the PostgreSQL server and additional useful tools.

---

## Basic Usage

- **Start/Stop Service (Ubuntu)**:

  ```bash
  sudo systemctl start postgresql
  sudo systemctl stop postgresql
  sudo systemctl status postgresql
  ```

- **Access psql shell**:

  ```bash
  sudo -u postgres psql
  ```

- **Create a database and user**: See code example below.

- **Connect from Python (psycopg2) and perform basic database operations**: See code example below.

- **Basic SQL operations**: See code example below.

---

## Shortcuts

- `\l` - List databases in psql
- `\dt` - List tables in current database
- `\c dbname` - Connect to another database
- `\q` - Quit psql
- Arrow keys, Tab completion, and history navigation in psql shell

---

## Best Practices

- Use parameterized queries to prevent SQL injection. See code example below.
- Regularly back up your databases using `pg_dump` or `pg_basebackup`.
- Monitor performance with `EXPLAIN` and `pg_stat_statements`.
- Apply security updates and restrict network access.
- Normalize data but denormalize for performance where appropriate.
- Use connection pooling for web applications.
- Document schema changes and use migrations.

---

## Common Pitfalls

- **Not setting proper authentication**: Always configure `pg_hba.conf` and use strong passwords.
- **Ignoring backups**: Regularly schedule backups to avoid data loss.
- **Unindexed queries**: Missing indexes can lead to slow performance.
- **Resource limits**: Not tuning memory and connection settings for your workload.
- **Long-running transactions**: Can cause table bloat and lock contention.

---

## Example Code

- Example code for working with schemas can be found in the [code directory](../../../code/postgresql/schemas.sql).
- Example code for working with indexes can be found in the [code directory](../../../code/postgresql/indexes.sql).
- Example code for creating a database and user can be found in the [code directory](../../../code/postgresql/create_database_and_user.sql).
- Example code for connecting from Python and executing queries (SELECT, INSERT, UPDATE, DELETE, DDL) can be found in the [code directory](../../../code/postgresql/connect_from_python.py).
- Example code for basic sql operations can be found in the [code directory](../../../code/postgresql/basic_sql_operations.sql).
- Example code for using parameterized queries can be found in the [code directory](../../../code/postgresql/parameterized_queries.py).

---

## Sources

- [PostgreSQL Official Documentation](https://www.postgresql.org/docs/): Comprehensive reference and guides.
- [Postgres Guide](https://postgresguide.com/): Practical tips and explanations for everyday use.
- [psycopg2 Documentation](https://www.psycopg.org/docs/): Python client library for PostgreSQL.
- [DigitalOcean PostgreSQL Tutorials](https://www.digitalocean.com/community/tags/postgresql): Step-by-step guides for setup and management.

---

*Last updated at: 2025.10.16.*
