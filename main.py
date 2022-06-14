from user import User
from post import Post

app_user_one = User("mk@mk.com", "Marvin Korir", "pwd", "DevOps Engineer")
app_user_one.change_job_title("SRE")
app_user_two = User("wk@wk.com", "Wendy Korir", "pwd2", "Interior Designer")

app_user_one.get_user_info()
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_one.name)
new_post.get_post_info()