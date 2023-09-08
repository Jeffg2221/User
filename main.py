from user import User

my_user = User("Mike", "Ross", "mikeross@icloud.com", 32)

my_user.display_info().enroll().display_info().spend_points(50).display_info()

my_user2 = User("Bobby", "Brown","bbrown@yahoo.com", 50)

my_user2.display_info().enroll().display_info().spend_points(80).display_info()
