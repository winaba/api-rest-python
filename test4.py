from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/todo/api/v1.0/tasks', methods=['POST'])

def create_task():

    arquivo = open('arq01.txt','w')
    arquivo.write(request.data.decode("utf-8") + '\n')
    arquivo.close()
    return 'Sucesso!\n\n'
     
#    if request.headers['Content-Type']=='application/json':
#        return 'Content-Type: '+ str(request.headers['Content-Type'])   
#    else:
#        return request.data    

#    task = {
#        'id': tasks[-1]['id'] + 1,
#        'title': request.json['title'],
#        'description': request.json.get('description', ""),
#        'done': False
#    }
#    tasks.append(task)

#    return jsonify({'task': request.json}), 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)