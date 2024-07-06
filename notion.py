@app.route('/v1/prices', methods=['GET'])
def get_prices():
product = request.args.get('product')
zone = request.args.get('zone')
if product in prices_data and zone in prices_data[product]:
return jsonify(prices_data[product][zone])
else:
return jsonify({"error": "Data not found"}), 404

if **name** == '**main**':
app.run(debug=True)
