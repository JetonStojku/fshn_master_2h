# Lesson: Interacting with Databases Using Raw SQL

## Objectives:

- Understand the importance of using raw SQL for specific database interactions.
- Learn the fundamentals of executing raw SQL queries in Python.
- Gain practical experience by applying raw SQL queries to interact with databases.
- Develop skills for error handling and security considerations when working with raw SQL.

## Introduction:

While tools like SQLAlchemy provide a Pythonic way to interact with databases, there are situations where writing raw SQL queries becomes essential. This lesson focuses on understanding and implementing raw SQL queries for effective database interaction.

## Section 1: Why Raw SQL?

### When to Use Raw SQL:

- **Performance**: In scenarios where direct control over the SQL statement's performance is crucial.
- **Specific Database Features**: Utilizing database-specific functionalities not easily accessible through ORMs.
- **Migrations**: Executing complex database migrations or updates.

## Section 2: Executing Raw SQL Queries

### Using Database Connectors:

- Utilizing database-specific libraries (e.g., `psycopg2` for PostgreSQL, `sqlite3` for SQLite).

### Basic Query Execution:

```python
import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Execute a simple query
cursor.execute('SELECT * FROM users;')
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
connection.close()
```

## Section 3: Parameterized Queries

### Preventing SQL Injection:

- Use parameterized queries to prevent SQL injection attacks.

```python
# Parameterized query
user_id = 1
cursor.execute('SELECT * FROM users WHERE id=?;', (user_id,))
result = cursor.fetchone()
print(result)
```

## Section 4: Handling Transactions

### Transaction Management:

- Managing transactions explicitly for complex operations.

```python
# Begin a transaction
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

try:
    # Execute multiple queries
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?);', ('John Doe', 30))
    cursor.execute('UPDATE users SET age=? WHERE id=?;', (31, 1))

    # Commit the transaction
    connection.commit()

except Exception as e:
    # Rollback in case of an error
    connection.rollback()
    print(f"Error: {e}")

finally:
    # Close the connection
    connection.close()
```

## Section 5: Practical Examples

### Example 1: Retrieving Specific Data:

```python
# Connecting to a PostgreSQL database
import psycopg2

connection = psycopg2.connect('dbname=mydatabase user=user password=password host=localhost port=5432')
cursor = connection.cursor()

# Execute a query to retrieve specific data
cursor.execute('SELECT name, age FROM users WHERE age > 25;')
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
connection.close()
```

### Example 2: Performing Updates:

```python
# Connecting to a MySQL database
import mysql.connector

connection = mysql.connector.connect(user='user', password='password', host='localhost', database='mydatabase')
cursor = connection.cursor()

# Execute a query to update data
cursor.execute('UPDATE users SET age = age + 1 WHERE age < 30;')

# Commit the transaction
connection.commit()

# Close the connection
connection.close()
```

## Conclusion:

This lesson covered the fundamentals of interacting with databases using raw SQL queries. We discussed when to use raw SQL, executing queries, parameterized queries for security, and transaction management. While ORMs like SQLAlchemy offer a high-level abstraction, the knowledge of raw SQL is crucial for scenarios requiring precision and control.