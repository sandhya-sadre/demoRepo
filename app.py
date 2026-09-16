from flask import Flask, jsonify
import pandas as pd
app = Flask(__name__)
# function to find region with highest sales
@app.route('/highest_region', methods=['GET'])
def highest_region():
    df = pd.read_csv('sales_data.csv')
    region_revenue = df.groupby('region')['sales'].sum()
    highest_region = region_revenue.idxmax()
    return jsonify({'highest_region': highest_region})

@app.route('/total_revenue', methods=['GET'])
def total_revenue():
    # Read the sales csv file
    df = pd.read_csv('sales_data.csv')
    # Calculate total revenue
    total_revenue = (df['sales']).sum()
    return jsonify({'total_revenue calculated': int(total_revenue)})

if __name__ == '__main__':
    app.run(debug=True)

# Tesing line