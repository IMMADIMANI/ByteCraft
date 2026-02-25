class Profile:
    def __init__(self,username):
        self.followers=0
        self.username=username
    def follow(self):
        print("someone followed you")
        self.followers+=1
    def update_username(self,new):
        print("New user is created")
        self.username=new

p1=Profile("maneesh_reddy")
p1.follow()
print(p1.followers)
p1.update_username("mani")
print(p1.username)