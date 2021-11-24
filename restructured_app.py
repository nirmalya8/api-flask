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

@app.route('/orders/', methods = ['GET', 'POST', 'PUT', 'DELETE'])
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
        id = int(request.args.get('id'))
        if id<len(menucard) and menucard[id] not in orders:
            d = menucard[id]
            d['Quantity'] = 1
            orders.append(d)
            response = jsonify({'Status':'Added','Item':d})
            response.status_code = 200
        elif id>= len(menucard):
            response = jsonify({'Status': 'Not in menu'})
            response.status_code = 404
        elif menucard[id] in orders:
            for i in orders:
                if i['Item'] == menucard[id]['Item']:
                    i['Quantity']+=1
            response = jsonify({'Status': 'Updated quantity','Item':menucard[id]})
            response.status_code =200
        return response

if __name__ == "__main__":
    app.run(debug=True)