from flask import Flask, flash, jsonify, request, render_template
from flask_cors import CORS
import config
import json
import text_processor

print('********************************')
print('Setting up Flask API\n')


app = Flask(__name__)
CORS(app)


@app.route("/nlp/sentiment",methods=['POST' ])
def get_sentiment():
    try:

        data = request.get_json()
        text = data['data']

        print('** /nlp/sentiment **')
        print('** Received text **')
        print(text)
        print('*********************')

        sentiment = text_processor.get_sentiment(text)
        response = jsonify({'data': sentiment, 'success': True})
        response.headers.add('Access-Control-Allow-Origin', '*')

    except Exception as e:
        print('Error encountered.')
        print(e)

        response = jsonify({'success': False, 'error': str(e)})
        response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    app.run(config.HOST,config.PORT)
