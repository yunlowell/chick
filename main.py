class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"Name: {self.name}, Username: {self.username}")

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

members = []
members.append(Member("파카", "코딩하는파카", "1234"))
members.append(Member("카트만", "코딩하는카트만", "1234"))
members.append(Member("카일", "코딩하는카일", "1234"))

for member in members:
    member.display()

posts = []
posts.append(Post("제목 파카1", "파카1의 post", "파카"))
posts.append(Post("제목 파카2", "파카2의 post", "파카"))
posts.append(Post("제목 파카3", "파카3의 post", "파카"))
posts.append(Post("제목 카트만1", "카트만1의 post", "카트만"))
posts.append(Post("제목 카트만2", "카트만2의 post", "카트만"))
posts.append(Post("제목 카트만3", "카트만3의 post", "카트만"))
posts.append(Post("제목 카일1", "카일1의 post", "카일"))
posts.append(Post("제목 카일2", "카일2의 post", "카일"))
posts.append(Post("제목 카일3", "카일3의 post", "카일"))

for post in posts:
    if post.author == "파카":
        print(post.title)
        continue
    else:
        print()
        break

word = "카트만"
for post in posts:
    if word in post.content:
        print(post.title)

