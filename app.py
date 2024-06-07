from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = 'aff383143383395d19546ba1df0e1e07'  # Replace this with your new API key

@app.route('/movies')
def get_movies():
    try:
        response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=aff383143383395d19546ba1df0e1e07&query=3')
        data = response.json()
        print('Fetched data from TMDB:', data)  # Log the fetched data
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
