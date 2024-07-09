## Project
Rock Scissors Paper Game
가위바위보 게임을 웹페이지에서 즐길 수 있다.

## Development Team
병아리(Chick)

## Pair Programing
윤율
- 문서 작성
- 가위 바위 보 게임의 입출력을 Flask와 HTML을 이용하도록 변경

이광열
- SQLite를 이용하여 가위바위보 게임 전적을 저장

남지민
- HTML에 승/무/패 통계와 게임 기록 표시

김영빈
- CSS/부트스트랩을 이용하여 화면 구성


## Development time
- 2024.07.08~2024.07.09

## Development Environment
- Programming Language: python 3.10.14
- Web Framework: Flask 3.0.3
- Database: SQLite
- IDE: Pycharm
- Version Control: Git, Github
- Communication: Zep, Notion
- 
### 사용하는 기술
    - Backend: Python, Flask
    - Frontend: HTML, CSS
    - Database: SQLite, SQLALchemy

## Requirements
**과제 내용:**

1.  앞서 진행했던 `가위 바위 보 게임` 의 입출력을 Flask 와 HTML 을 이용하도록 변경하세요.
    1. 과제2 에서는 `가위 바위 보 게임` 입출력을 콘솔(터미널)에서 진행했어요.
    2. 이번 과제에서는 HTML form 을 통해서 입력을 받으세요. 
    3. Flask 내부에서 로직을 처리한 후 HTML 에 출력되도록 구성해보세요.

**추가 도전 과제:**

1. sqlite 로 가위바위보 게임 전적을 저장하세요.
    - 예시
        
        `ChatGPT 웹개발` 4주차 강의를 참고하세요~!
        
        게임 전적
        
        | 게임 번호 | 1 |
        | --- | --- |
        | 컴퓨터 | 바위 |
        | 사용자 | 보 |
        | 결과 | 승 |
        
        - (힌트코드)
            
            
            ```python
            class GameHistory(db.Model):
                id = ...
                user_choice = ...
                computer_choice = ...
                result = ...
            ```
            
2. HTML 에 승/무/패 통계와 게임 기록을 표시하세요.
    - 예시
        
        **승무패 통계**
        
        ```python
        승 : 5회 | 무 : 6회 | 패 : 4회
        ```
        
        - 힌트
            
            <aside>
            💡 flask-sqlalchemy 의 filter_by 와 count 를 활용해보세요!
            
            </aside>
            
        
        **게임 기록**
        
        | # | 컴퓨터 | 사용자 | 결과 |
        | --- | --- | --- | --- |
        | 1 | 바위 | 가위 | 패 |
        | 2 | 보 | 보 | 무 |
        | 3 | 보 | 바위 | 패 |
        | 4 | 가위 | 바위 | 승 |
        - 힌트
            
            참고해보세요!
            
            - 3-14 강의의 영화 검색 사이트 만들기를 참고해보세요
            - HTML `table` 혹은 `li` 를 활용해보세요
        
3. css / 부트스트랩을 이용해서 내 취향대로 가위바위보 게임을 꾸며보세요.

### 평가
- html form 을 이용해서 사용자의 입력을 받을 수 있는가?
- input으로 받은 값을 flask 에서 사용할 수 있는가?
- input 으로 받은 값을 string에서 int로 바꿀 수 있는가?
- if문을 이용해서 조건에 따른 코드 실행을 바꿀 수 있는가?
- flask 에서 html 을 통해 원하는 값을 표시할 수 있는가?

## Wireframe
![image](https://github.com/yunlowell/chick/assets/173750800/d01b60e1-1f37-4cc6-8784-b4e72ccb79a1)

## 최종 결과물

![image](https://github.com/yunlowell/chick/assets/173750800/abc7adac-fc69-4500-9936-1dcc895f4543)
- 플레이어는 선택하세요 옆의 선택지에서 가위, 바위, 보 중 하나를 골라 선택한 후 플레이를 누른다.
- 컴퓨터는 랜덤으로 가위, 바위, 보 중 하나를 고른다.
- 플레이어가 이기면 '이겼습니다.', 컴퓨터가 이기면 '졌습니다.', 비기면 '비겼습니다.' 메시지가 표시된다.
- 밑에는 결과의 데이터가 쌓여 숫자로 표시 된다.
  
![image](https://github.com/yunlowell/chick/assets/173750800/b3d6e2fb-bce5-4456-b4c8-6527926226e8)
- 게임 기록 보기를 누르면 표로 정리되어 그동안의 게임기록을 보여준다.
  
![image](https://github.com/yunlowell/chick/assets/173750800/c6a40787-1ec2-4626-bbc9-13084e136768)
-게임으로 돌아가기를 누르면 표가 접어지고 다시 처음 화면으로 돌아간다.
