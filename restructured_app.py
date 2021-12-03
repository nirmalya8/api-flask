from flask import Flask, jsonify,request
#import request
app = Flask(__name__) 

menucard = [{'Item' : 'Rice', 'Price':10},{'Item': 'Dal','Price':15},{'Item':'Chicken','Price':20},{'Item':'Mutton', 'Price':25},{'Item':'Fish','Price':20},{'Item':'IceCream','Price':10}]
orders = []

'''
Curl commands for each method:
curl -H "Content-Type: application/json" --request POST -d '{"id":2}' http://127.0.0.1:5000/orders
curl --request GET http://127.0.0.1:5000/orders
curl --request GET http://127.0.0.1:5000/showmenu
curl -H "Content-Type: application/json" --request PUT -d '{"item1":{"Item" : "Curd", "Price":10}}' http://127.0.0.1:5000/orders
curl -H "Content-Type: application/json" --request DELETE -d '{"id":1}'
'''



@app.route('/') 
def hello_world():
    # The home route, which shows "Hello World"
    response = jsonify('Hello world!')
    response.status_code = 200
    return response

@app.route('/showmenu')
def show_menu():
    # This route will show the menucard
    response = jsonify({'Menu':menucard})
    response.status_code = 200
    return response



# The following route will handle all requests: GET, POST, PUT, and DELETE.
# We will access this using the cuRL command and pass data as payloads. 
@app.route('/orders', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def order():
    #GET Request for obtaining the list of already ordered items
    if request.method == 'GET':
        response = ' '
        if len(orders)==0:
            response = jsonify({'Your orders':'Haven\'t ordered anything yet'} )
            response.status_code = 404
        else :
            response = jsonify({'Your orders':orders})
            response.status_code = 200
        return response

    # POST Method to add an item to orders
    elif request.method == 'POST':
        response = {}
        payload = request.get_json()
        id1 = int(payload['id'])
        if id1<len(menucard) and menucard[id1] not in orders:
            d = menucard[id1]
            d['Quantity'] = 1
            orders.append(d)
            response = jsonify({'Status':'Added','Item':d})
            response.status_code = 200
        elif id1>= len(menucard):
            response = jsonify({'Satus': 'Not in menu'})
            response.status_code = 404
        elif menucard[id1] in orders:
            for i in orders:
                if i['Item'] == menucard[id1]['Item']:
                    i['Quantity']+=1
            response = jsonify({'Status': 'Updated quantity','Item':menucard[id1]})
            response.status_code =200
        return response

    # PUT Method to add an item to the menucard(only for staff)
    elif request.method == 'PUT':
        response = {}
        payload = request.get_json()
        item = payload["item1"]
        f = False
        for i in menucard:
            if i ==item:
                f = True
        if not f:
            menucard.append(item)
            response = jsonify({'Status': 'Added','Item':item})
            response.status_code =201
        else:
            response = jsonify({'Status': 'Already There','Item':item})
            response.status_code =400
        return response
        
    #DELETE Method to delete an item from the menucard(only for staff)
    elif request.method == 'DELETE':
        response = {}
        payload = request.get_json()
        itemid = payload["id"]
        if itemid<len(menucard) and itemid>=0:
            item = menucard[itemid]
            del menucard[itemid]
            response = jsonify({'Status':'Deleted','Item':item})
            response.status_code = 200
            return response

        response = jsonify({'Status':'Not in Menu','ItemID':itemid})
        response.status_code = 404
        return response


if __name__ == "__main__":
    app.run(debug=True)
