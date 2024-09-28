from datetime import datetime
from flask import Flask, render_template, request
import requests


app = Flask(__name__)

API_KEY = '038292ba9b9ffe6684831017b6b680ed'
BASE_URL = 'https://rekrutacja.teamwsuws.pl'

@app.route('/')
def index():
    tag = request.args.get('tag')

    if tag:
        response = requests.get(f"{BASE_URL}/events/filter/?tag={tag}", headers={"api-key": API_KEY})
    else:
        response = requests.get(f"{BASE_URL}/events/", headers={"api-key": API_KEY})

    events = response.json()
    if response.status_code != 200 or 'detail' in events:
    # API zwróciło błąd lub tag nie został znaleziony
        events = []
        error_message = 'Tag nie został znaleziony.'
    else:
        error_message = None
    

    return render_template('index.html', events=events, tag=tag, error_message=error_message)


@app.route('/event/<int:event_id>')
def event_detail(event_id):
    response = requests.get(f"{BASE_URL}/events/{event_id}", headers={"api-key": API_KEY})
    event = response.json()
    return render_template('event_detail.html', event=event)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

