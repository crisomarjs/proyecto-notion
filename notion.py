curl --location --request POST 'https://api.notion.com/v1/databases/<database_id>/query' \
--header 'Authorization: Bearer <secret_bot>' \
--header 'Content-Type: application/json' \
--data '{
    "start_cursor": "33e19cb9-751f-4993-b74d-234d67d0d534"
}'

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
