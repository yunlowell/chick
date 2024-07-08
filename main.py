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
    username = write_username()

    for member in members:
        if username == member.username:
            while True:
                password = write_pwd()
                if password == member.password:
                    print("로그인 성공")
                    print(member.username)
                    title = input("작성할 post의 제목을 입력해 주세요.")
                    content = input("작성할 post의 내용을 입력해 주세요.")
                    author = member.username
                    new_post = Post(title, content, author)
                    print("post 작성이 완료 되었습니다.")
                    return
                else:
                    print("비밀번호가 일치하지 않습니다. 비밀번호를 재입력하세요.")
    print("일치하는 ID가 없습니다.")


def write_username():
    input_username = input("ID를 입력하세요.")
    return input_username


def write_pwd():
    input_pwd = input("비밀번호를 입력하세요.")
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_pwd.encode('UTF-8'))
    hash_input_pwd = sha256_hash.hexdigest()
    return hash_input_pwd


# 특정 작성자가 작성한 게시물 제목 출력
def display_posts_by_author(author):
    for post in posts:
        if post.author == author:
            post.display()


# 특정 단어가 포함된 게시물 제목 출력
def display_posts_by_keyword(keyword):
    for post in posts:
        if keyword in post.content:
            post.display()


members = []
posts = []

# Member 클래스 객체 생성
member1 = Member(name="이광열", username="xman1215", password="1234")
member2 = Member('최준환', 'asd123', "123456")
member3 = Member(name="김남훈", username="gkgk55", password="6430")
# member4 = create_member()

# Post 클래스 객체 생성
post1 = Post('제목1', '내용1 파이썬', member1.username)
post2 = Post('제목2', '내용2 html', member1.username)
post3 = Post('제목3', '내용3 파이썬', member1.username)

post4 = Post('제목4', '내용4 html', member2.username)
post5 = Post('제목5', '내용5 ', member2.username)
post6 = Post('제목6', '내용6 자바', member2.username)

post7 = Post('제목7', '내용7 파이썬', member3.username)
post8 = Post('제목8', '내용8 자바', member3.username)
post9 = Post('제목9', '내용9 html', member3.username)


# # 추가된 회원 정보를 출력
# for member in members:
#     member.display()
#
# # 해싱된 회원들 비밀번호 출력
# for member in members:
#     member.show_password()
#
# # 특정 유저가 작성한 게시글의 제목 출력
# for member in members:
#     for post in posts:
#         if post.author == member.username:
#             print(f'{member.username}님이 작성한 게시글의 제목: {post.title}')
#
# # 특정 단어가 content에 포함된 게시글의 제목을 출력
# for post in posts:
#     if "파이썬" in post.content :
#         print(f'파이썬이 포함된 게시글의 제목: {post.title}')

def menu():
    while True:
        print("\n메뉴를 선택하세요:")
        print("1. 회원 추가")
        print("2. 게시물 추가")
        print("3. 특정 작성자(ID)의 게시물 보기")
        print("4. 특정 단어가 포함된 게시물 보기")
        print("5. 종료")
        choice = input("선택: ")

        if choice == '1':
            create_member()
        elif choice == '2':
            create_post()
        elif choice == '3':
            author = input("작성자 ID를 입력하세요: ")
            display_posts_by_author(author)
        elif choice == '4':
            keyword = input("검색할 단어를 입력하세요: ")
            display_posts_by_keyword(keyword)
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

        print("member 리스트")
        for member in members:
            member.display()
        print("")

        print("post 리스트")
        for post in posts:
            post.display()


# 프로그램 시작
menu()
