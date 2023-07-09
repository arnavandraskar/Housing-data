# Housing Data API

This project implements a REST API using Python and Flask to store and retrieve housing data in a PostgreSQL database. The API provides endpoints to store the data, calculate average sale prices, and retrieve maximum and minimum sale prices.

## Prerequisites

- Python 3.x
- PostgreSQL database

## Installation

1. Clone the repository:

```cmd
git clone https://github.com/your-username/housing-data-api.git
```

2. Install the required dependencies:

```cmd
pip install -r requirements.txt
```

## Configuration

1. Open the `config.py` file and update the database connection details (`db_host`, `db_name`, `db_user`, `db_password`) with your actual PostgreSQL database credentials.

## Database Setup

1. Create a PostgreSQL database named `housing_data_db`.

2. Execute the following SQL query to create the `housing_data` table in the database:

```sql
CREATE TABLE housing_data (
    id SERIAL PRIMARY KEY,
    bedrooms INTEGER,
    bathrooms NUMERIC,
    square_footage INTEGER,
    location VARCHAR(255),
    sale_price INTEGER
);
```

## Usage

Run the Flask application:

```cmd
python app.py
```
