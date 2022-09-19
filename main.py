from flask import *
import json, time, requests, random, os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    adult_query = str(request.args.get('adult'))
    year = str(request.args.get('year'))
    page = random.randint(1, 500)
    api_url = f'https://api.themoviedb.org/3/discover/movie?api_key={get_Env()}&include_adult={adult_query}&page={page}&year={year}'
    response = requests.get(api_url)
    data = json.dumps(response.json())
    y = json.loads(data)
    z = y["results"]
    random_number = random.randint(1,len(z))-1
    return response.json()

def get_Env():
    return os.getenv('PYTHON_API_MOVIE')

if __name__ == '__main__':
    app.run(port=7777)