import hashlib
class Member:  #멤버 클래스
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"Name: {self.name}, Username: {self.username}")


    def _hash_password(self, password):
        # 비밀번호를 해시화하여 반환하는 함수
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

class Post: #게시글 클래스
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

# ----- 코드 실행 ------
members = []
posts = []

#멤버 인스턴스 생성 및 members 리스트에 append
members_list = [
    ("가나다", "ABC", "1234"),
    ("라마바", "DEF", "5678"),
    ("사아자", "GHI", "9012")
]

for name, username, password in members_list:
    members.append(Member(name, username, password))

# 사용자 입력을 통해 멤버 인스턴스 생성 및 members 리스트에 append
print("아래의 요건에 맞춰 정보를 입력하세요.")
while True:
    name = input("이름을 입력하세요.: ")
    username = input("닉네임을 입력하세요.: ")
    password = input("비밀번호를 입력하세요.: ")
    members.append(Member(name, username, password))
    break

#회원들의 이름 모두 프린트
for member in members:
    member.display()


#게시글 인스턴스 생성 및 posts 리스트에 append
posts_data = [
    ("post1", "동해물과 백두산이", "ABC"),
    ("post2", "마르고 닳도록", "DEF"),
    ("post3", "하느님이 보우하사", "GHI"),
    ("post4", "우리나라 만세", "ABC"),
    ("post5", "무궁화 삼천리 화려 강산", "DEF"),
    ("post6", "대한 사람 대한으로", "GHI"),
    ("post7", "길이 보전하세", "ABC"),
    ("post8", "무궁화 꽃이 피었습니다.", "DEF"),
    ("post9", "배고파", "GHI")
]

for title, content, author in posts_data:
    posts.append(Post(title, content, author))


# 특정 회원이 작성한 게시글의 제목 모두 출력
a_author = "ABC"
print(f"{a_author} 회원님이 작성한 게시글:")
for post in posts:
    if post.author == a_author:
        print(post.title)

# 특정 단어가 content에 포함된 게시글의 제목 모두 출력
a_word = "무궁화"
print(f"{a_word}(이)가 내용에 포함된 게시글:")
for post in posts:
    if a_word in post.content:
        print(post.title)

# 사용자 입력을 통해 포스트 생성 및 Post 리스트에 append
print("게시글을 작성해주세요.")
while True:
    title = input("제목을 입력하세요.: ")
    content = input("내용을 입력하세요.: ")
    author = input("닉네임을 입력하세요.: ")
    members.append(Member(title, content, author))
    break