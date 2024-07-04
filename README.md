# 파이썬 팀 과제설명

1. **`Member`** 클래스와 **`Post`** 클래스를 정의하세요.
2. **`Member`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    - 회원 이름 (**`name`**)
    - 회원 아이디 (**`username`**)
    - 회원 비밀번호 (**`password`**)
3. **`Member`** 클래스에는 다음과 같은 메소드를 가지고 있어야 합니다.
    - 회원 정보를 print해주는 `display` (회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됩니다!)
4. **`Post`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    - 게시물 제목 (**`title`**)
    - 게시물 내용 (**`content`**)
    - 작성자 (**`author`**) : 회원의 `username` 이 저장되어야 함!
5. 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요
    1. members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다). 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
    1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
    2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요
  
**추가 도전 과제:**

1. input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
2. post도 터미널에서 생성할 수 있게 해주세요.
3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.

# 코드 설명

### 1. Member 클래스 안에 있는 __init__ 메소드다. hashlib 라이브러리를 통해 비밀번호를 암호화 한 뒤 저장했다.
>
    import hashlib

    def __init__(self, name, username, password):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode('UTF-8'))
        hash_pwd = sha256_hash.hexdigest()
        self.name = name
        self.username = username
        self.password = hash_pwd
        self.add_to_members()

### 2.Member 클래스 생성, add_to_members 메소드를 통해 인스턴스 생성 후 바로 members 리스트에 추가되도록 했다.
>
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
        
### 3. create_member 함수 생성, 터미널에서 member 추가할 수 있도록 함수를 만들었다.
>
    def create_member():
        name = input("생성할 member의 이름을 입력해 주세요.")
        username = input("생성할 member의 ID를 입력해 주세요.")
        password = input("생성할 member의 PW를 입력해 주세요.")
        new_member = Member(name, username, password)
        print('새로운 member가 추가 되었습니다.')

### 4. Post 클래스 생성, 구조는 Member 클래스와 거의 비슷하다.
>
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

### 5. write_username 함수 생성, 유저의 ID를 입력하는 함수를 생성했다.
>
    def write_username():
        input_username = input("ID를 입력하세요.")
        return input_username

### 6. write_pwd 함수 생성, 유저의 pwd를 입력하는 함수를 생성했다. 이 함수에도 비밀번호를 암호화하는 기능을 추가해서 로그인기능에서 패스워드값을 비교할수있게 만들었다.
>
    def write_pwd():
        input_pwd = input("비밀번호를 입력하세요.")
        sha256_hash = hashlib.sha256()
        sha256_hash.update(input_pwd.encode('UTF-8'))
        hash_input_pwd = sha256_hash.hexdigest()
        return hash_input_pwd

### 7. create_post 함수 생성, members 리스트 안에 있는 데이터를 이용해 post를 새로 작성하게 만들고 싶어서 로그인기능을 추가하였다.
>
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

### 8. 터미널에서 멤버 생성 및 post 작성 메뉴 코드, 반복문을 이용해서 메뉴를 구성해봤다. 반복문이 종료되면 members, posts 리스트들을 출력하게 했다.
>
    while True:
        choice = input("member 생성은 1번 / post 작성은 2번 / 종료는 3번을 눌러주세요.")
        if choice == '1':
            create_member()
        elif choice == '2':
            create_post()
        elif choice == '3':
            break
        else:
            print("1,2,3중 하나만 입력하세요.")
    print("")
    
    print("member 리스트")
    for member in members:
        member.display()
    print("")
    
    print("post 리스트")   
    for post in posts:
        post.display()
