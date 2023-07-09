from flask import Flask, jsonify, request
import psycopg2
import json

app = Flask(__name__)

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="housing_db",
    user="postgres",
    password= "arnav")

cur = conn.cursor()

# Endpoint to store the JSON data in the PostgreSQL database
@app.route('/store_data', methods=['POST'])
def store_data():
    try:
        # Get the JSON data from the request
        data = json.loads(request.data)
        
        # Extract the "data" list from the JSON
        housing_data = data['data']
        
        # Iterate over the housing data and insert each record into the database
        for record in housing_data:
            bedrooms = record['Bedrooms']
            bathrooms = record['Bathrooms']
            square_footage = record['SquareFootage']
            location = record['Location']
            sale_price = record['SalePrice']
            
            # Execute the SQL INSERT query
            cur.execute("INSERT INTO housing_data (bedrooms, bathrooms, square_footage, location, sale_price) VALUES (%s, %s, %s, %s, %s)",
                        (bedrooms, bathrooms, square_footage, location, sale_price))
        
        # Commit the changes to the database
        conn.commit()
        
        return jsonify({'message': 'Data stored successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get the average sale price of the house overall
@app.route('/average_sale_price', methods=['GET'])
def get_average_sale_price():
    try:
        # Execute the SQL query to calculate the average sale price
        cur.execute("SELECT AVG(sale_price) FROM housing_data")
        average_sale_price = cur.fetchone()[0]
        
        return jsonify({'average_sale_price': round(float(average_sale_price), 4)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get the average sale price of the house per location
@app.route('/average_sale_price_per_location', methods=['GET'])
def get_average_sale_price_per_location():
    try:
        # Execute the SQL query to calculate the average sale price per location
        cur.execute('''SELECT location, AVG(sale_price) 
                        FROM housing_data 
                        GROUP BY location''')
        
        average_sale_prices = cur.fetchall()
        
        result = {}
        for row in average_sale_prices:
            location = row[0]
            average_sale_price = row[1]
            result[location] = round(float(average_sale_price), 4)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get the max sale price
@app.route('/max_sale_price', methods=['GET'])
def get_max_sale_price():
    try:
        # Execute the SQL query to calculate the max sale price
        cur.execute("SELECT MAX(sale_price) FROM housing_data")
        max_sale_price = cur.fetchone()[0]
        
        return jsonify({'max_sale_price': round(float(max_sale_price), 4)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get the min sale price
@app.route('/min_sale_price', methods=['GET'])
def get_min_sale_price():
    try:
        # Execute the SQL query to calculate the min sale price
        cur.execute("SELECT MIN(sale_price) FROM housing_data")
        min_sale_price = cur.fetchone()[0]
        
        return jsonify({'min_sale_price': round(float(min_sale_price), 4)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
