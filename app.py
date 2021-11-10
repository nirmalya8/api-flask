from flask import Flask, json, jsonify
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

@app.route('/order/<int:id>',methods=['GET','POST'])
def take_orders(id):
    response = {}
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

@app.route('/show',methods=['GET'])
def show_orders():
    response = ' '
    if len(orders)==0:
        response = jsonify({'Your orders':'Haven\'t ordered anything yet'} )
        response.status_code = 404
    else :
        response = jsonify({'Your orders':orders})
        response.status_code = 200
    return response

@app.route('/price', methods = ['GET'])
def show_price():
    response = {}
    if len(orders) == 0:
        response = jsonify({'Orders':'Haven\'t ordered yet','Price':0})
        response.status_code = 404
    else:
        p = 0
        for i in orders:
            p = p + i['Price']*i['Quantity']
        response = jsonify({'Orders':orders,'Price':p})
        response.status_code = 200
    return response

@app.route('/delete/<int:delid>',methods=['GET','POST'])
def delete_order(delid):
    response = {}
    if(delid<len(orders) and delid>=0):
        for i in range(len(orders)):
            if i == delid:
                orders[i]['Quantity']-=1
    
        for i in orders:
            if i['Quantity'] == 0:
                orders.remove(i)
        response = jsonify({'Status':'Successfully Deleted'})
        response.status_code = 200
    else:
        response = jsonify({'Status':'Wasn\'t in the menu'})
        response.status_code = 404
    return response

@app.route('/additem',methods=['GET','PUT'])
def add_to_menu():
    item = {'Item':'New Item','Price':15}
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


@app.route('/delitem',methods = ['GET','DELETE'])
def delete_from_menu(): 
    item = menucard[2]
    for i in menucard:
        if i == item:
            menucard.remove(i)
            response = jsonify({'Status':'Deleted','Item':item})
            response.status_code = 200
            return response

    response = jsonify({'Status':'Not in Menu','Item':item})
    response.status_code = 404
if __name__ == "__main__":
    app.run(debug=True)

