from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('rsp_game.html')

@app.route('/play', methods=['POST'])
def play():
    options = ['가위', '바위', '보']
    player_choice = request.form['choice']
    computer_choice = random.choice(options)

    context = {
        'player_choice': player_choice,
        'computer_choice': computer_choice
    }

    return render_template('rsp_game.html', data=context)

if __name__ == '__main__':
    app.run(debug=True)
