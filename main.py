import hashlib


class Member:
    def __init__(self, name, username, password):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode('UTF-8'))
        hash_pwd = sha256_hash.hexdigest()
        self.name = name
        self.username = username
        self.password = hash_pwd
        self.add_to_members()

    def add_to_members(self):
        members.append(self)

    def display(self):
        print(f'회원 이름: {self.name}, 회원 아이디: {self.username}')

    def show_password(self):
        print(self.password)


def create_member():
    name = input("생성할 member의 이름을 입력해 주세요.")
    username = input("생성할 member의 ID를 입력해 주세요.")
    password = input("생성할 member의 PW를 입력해 주세요.")
    new_member = Member(name, username, password)
    print('새로운 member가 추가 되었습니다.')

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.add_to_posts()

    def add_to_posts(self):
        posts.append(self)

    def display(self):
        print(f'제목: {self.title} \n작성자: {self.author}\n내용: {self.content}')


def create_post():
    if
    title = input("작성할 post의 제목을 입력해 주세요.")
    content = input("작성할 post의 내용을 입력해 주세요.")
    author = ""
    new_post = Post(title, content, author)
    print("")



members = []
posts = []

# Member 클래스 객체 생성
member1 = Member(name="이광열", username="xman1215", password="1234")
member2 = Member('최준환','asd123',"123456")
member3 = Member(name="김남훈", username="gkgk55", password="6430")
member4 = create_member()

# Post 클래스 객체 생성
post1 = Post('제목1','내용1 파이썬',member1.username)
post2 = Post('제목2','내용2 html',member1.username)
post3 = Post('제목3','내용3 파이썬',member1.username)

post4 = Post('제목4','내용4 html',member2.username)
post5 = Post('제목5','내용5 ',member2.username)
post6 = Post('제목6','내용6 자바',member2.username)

post7 = Post('제목7','내용7 파이썬',member3.username)
post8 = Post('제목8','내용8 자바',member3.username)
post9 = Post('제목9','내용9 html',member3.username)


# 추가된 회원 정보를 출력
for member in members:
    member.display()

# 해싱된 회원들 비밀번호 출력
for member in members:
    member.show_password()

# 특정 유저가 작성한 게시글의 제목 출력
for post in posts:
    if post.author == member1.username:
        print(f'{member1.username}님이 작성한 게시글의 제목: {post.title}')

# 특정 단어가 content에 포함된 게시글의 제목을 출력
for post in posts:
    if "파이썬" in post.content :
        print(f'파이썬이 포함된 게시글의 제목: {post.title}')

