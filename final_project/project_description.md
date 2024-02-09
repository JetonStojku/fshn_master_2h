# Project Description

## Description

This project aims to demonstrate data import, transformation, and insertion into a relational database using Python. The input data will be in JSON format or CSV, transformed as necessary, and then inserted into a relational database. The project includes database schema definition, data insertion scripts, and utility functions.

## Input Data

The input data will be in JSON format or CSV, representing various entities and their relationships. This data will be transformed and inserted into the database tables.

## Transformation

The input data will undergo normalization to ensure compliance with the principles of database normalization (NF1, NF2, NF3). This includes resolving many-to-one and many-to-many relationships and structuring the data into appropriate tables.

## Output Data

The output data will be structured and stored in a PostgreSQL database, following the defined schema.

## JSON Data

A JSON dataset will be provided or generated for importing into the database. It should contain diverse entities and relationships to demonstrate the full functionality of the project.

## Tables

The project will include at least 10 database tables, representing different entities and their relationships.

## Database Schema

The database schema will be defined either using an Object-Relational Mapping (ORM) library or raw SQL statements. It will reflect the structure of the input data and adhere to the principles of normalization.

## Project Structure

The project will be structured into at least three Python files:
- `db_schema.py` - Contains the definition of the database schema.
- `insert_data.py` - Includes scripts for importing and inserting data into the database.
- `utils.py` - Provides utility functions for data transformation and other common tasks.

## Implementation

Python will be used for importing, transforming, and inserting data into the database. Depending on the chosen approach, either ORM libraries like SQLAlchemy or raw SQL statements will be used for database interaction.

## Data Insertion

Data insertion into the database will be handled using either ORM methods or raw SQL queries, ensuring efficient and accurate data storage.

## Transformation

Input data will be transformed as necessary to meet the requirements of the database schema. Additional data may be derived or aggregated during this process to fulfill the schema's needs.
