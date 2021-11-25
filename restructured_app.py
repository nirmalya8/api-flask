from flask import Flask, json, jsonify,request
#import request
app = Flask(__name__) 

menucard = [{'Item' : 'Rice', 'Price':10},{'Item': 'Dal','Price':15},{'Item':'Chicken','Price':20},{'Item':'Mutton', 'Price':25},{'Item':'Fish','Price':20},{'Item':'IceCream','Price':10}]
orders = []

@app.route('/') 
def hello_world():
    response = jsonify('Hello world!')
    response.status_code = 200
    return response

@app.route('/showmenu')
def show_menu():
    response = jsonify({'Menu':menucard})
    response.status_code = 200
    return response

@app.route('/orders', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def order():
    if request.method == 'GET':
        response = ' '
        if len(orders)==0:
            response = jsonify({'Your orders':'Haven\'t ordered anything yet'} )
            response.status_code = 404
        else :
            response = jsonify({'Your orders':orders})
            response.status_code = 200
        return response
        # retrieve order
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

'''
Curl command
curl -H "Content-Type: application/json" --request POST -d '{"id":2}' http://127.0.0.1:5000/orders/
curl -X GET http://127.0.0.1:5000/orders
curl -X GET http://127.0.0.1:5000/showmenu
curl -H "Content-Type: application/json" --request PUT -d '{"item1":{"Item" : "Curd", "Price":10}}' http://127.0.0.1:5000/orders/
curl -H "Content-Type: application/json" --request DELETE -d '{"id":2}' http://127.0.0.1:5000/orders/
'''