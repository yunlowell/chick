from flask import Flask, render_template, request
import random
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# 유저 게임 내용
class GameResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_choice = db.Column(db.String, nullable=False)
    computer_choice = db.Column(db.String, nullable=False)
    result = db.Column(db.String, nullable=False)


# 유저 게임 총 전적
class UserGameScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    win = db.Column(db.Integer, default=0)
    draw = db.Column(db.Integer, default=0)
    loss = db.Column(db.Integer, default=0)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('rsp_game.html')


@app.route('/play', methods=['POST'])
def play():
    options = ['가위', '바위', '보']
    player_choice = request.form['choice']
    computer_choice = random.choice(options)

    # 유저 게임 룰
    if player_choice == computer_choice:
        result = 'draw'
    elif (player_choice == '가위' and computer_choice == '보') or \
            (player_choice == '바위' and computer_choice == '가위') or \
            (player_choice == '보' and computer_choice == '바위'):
        result = 'win'
    else:
        result = 'lose'

    # 유저 게임 내용 db에 저장
    game_result = GameResult(player_choice=player_choice, computer_choice=computer_choice,
                             result=result)
    db.session.add(game_result)
    db.session.commit()

    # 유저 게임 총 전적 설정
    user_game_score = UserGameScore.query.first()
    if not user_game_score:
        user_game_score = UserGameScore(win=0, draw=0, loss=0)
        db.session.add(user_game_score)

    if result == 'win':
        user_game_score.win += 1
    elif result == 'draw':
        user_game_score.draw += 1
    else:
        user_game_score.loss += 1

    db.session.commit()

    context = {
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'result': result,
        'win': user_game_score.win,
        'draw': user_game_score.draw,
        'loss': user_game_score.loss
    }

    return render_template('rsp_game.html', data=context)


if __name__ == '__main__':
    app.run(debug=True)
