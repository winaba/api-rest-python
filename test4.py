from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/todo/api/v1.0/tasks', methods=['POST'])

def create_task():

    arquivo = open('arq01.txt','w')
    arquivo.write(request.data.decode("utf-8") + '\n')
    arquivo.close()
    return 'Sucesso!\n\n'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
