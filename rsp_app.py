from flask import Flask, render_template, request, redirect, url_for, session
import random
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # 세션 사용을 위한 비밀 키 설정

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
    return render_template('rsp_game.html', data=None)


@app.route('/play', methods=['POST'])
def play():
    options = ['가위', '바위', '보']

    player_choice = request.form.get('choice')
    computer_choice = random.choice(options)

    # 유저 게임 룰
    if player_choice == computer_choice:
        result = '무승부입니다.'
    elif (player_choice == '가위' and computer_choice == '보') or \
            (player_choice == '바위' and computer_choice == '가위') or \
            (player_choice == '보' and computer_choice == '바위'):
        result = '이겼습니다.'
    else:
        result = '졌습니다.'

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

    if result == '이겼습니다.':
        user_game_score.win += 1
    elif result == '무승부입니다.':
        user_game_score.draw += 1
    else:
        user_game_score.loss += 1

    db.session.commit()

    # 세션에 최신 게임 결과 저장
    session['player_choice'] = player_choice
    session['computer_choice'] = computer_choice
    session['result'] = result

    # PRG 패턴 적용: 리디렉션
    return redirect(url_for('show_result'))


@app.route('/result')
def show_result():
    # 세션에서 플레이 결과 불러오기
    player_choice = session.pop('player_choice', None)
    computer_choice = session.pop('computer_choice', None)
    result = session.pop('result', None)

    # 최신 게임 결과 가져오기
    latest_game_result = GameResult.query.order_by(GameResult.id.desc()).first()
    user_game_score = UserGameScore.query.first()

    game_result_list = GameResult.query.all()

    context = {
        'player_choice': latest_game_result.player_choice,
        'computer_choice': latest_game_result.computer_choice,
        'result': latest_game_result.result,
        'win': user_game_score.win,
        'draw': user_game_score.draw,
        'loss': user_game_score.loss,
        'game_result_list': game_result_list
    }

    return render_template('rsp_game.html', data=context)


@app.route('/delete', methods=['POST'])
def delete():
    db.drop_all()
    db.create_all()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
