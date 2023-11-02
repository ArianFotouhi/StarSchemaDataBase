from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def dormant():

    url = 'http://127.0.0.1:5000/get_table/User'
    response = requests.get(url)
    data = response.json()  # This will parse the JSON content of the response
    data_value = data.get('data')
    

    
    # return render_template('dormant.html')
    return str(data_value)


if __name__ == '__main__':
    app.run(debug=True,port=8000,host='0.0.0.0')