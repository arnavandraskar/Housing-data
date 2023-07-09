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

1. Create a PostgreSQL database named `housing_db`.

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

    python app.py
    

The API will be accessible at http://localhost:5000.
Use the following commands to execute requests to the API endpoints:

- POST /store_data: Store the JSON data in the PostgreSQL database.
    ```cmd
    curl -X POST -H "Content-Type: application/json" -d @housing_data.json http://localhost:5000/store_data
    ```
    
### Example
![store_data](https://github.com/arnavandraskar/Housing-data/assets/80948956/7f4cac5e-0507-4172-b06c-dba69a58446d)
![data_populate](https://github.com/arnavandraskar/Housing-data/assets/80948956/ad102443-8c43-4e01-98af-3fbe060823a4)


- GET /average_sale_price: Get the average sale price of the house overall.
    ```cmd
    curl http://localhost:5000/average_sale_price
    ```


- GET /average_sale_price_per_location: Get the average sale price of the house per location.
    ```cmd
    curl http://localhost:5000/average_sale_price_per_location
    ```


- GET /max_sale_price: Get the maximum sale price.
    ```cmd
    curl http://localhost:5000/max_sale_price
    ```


- GET /min_sale_price: Get the minimum sale price.
    ```cmd
    curl http://localhost:5000/min_sale_price
    ```

Make sure to set the appropriate headers and request body (if required) based on the endpoint you're accessing.
### Example
![image](https://github.com/arnavandraskar/Housing-data/assets/80948956/08c28fd0-9fb7-4adc-ba7e-366fa50029c9)

