
from instagramy import InstagramUser
 
user = InstagramUser("minabonino")

file = open(f"{user.username}.csv", "w", encoding="utf-8")
# Formatting the data
file.write("User")
file.write("\tFollowers")
file.write("\tFollowing")
file.write("\tFollows Viewer")
# file.write("\n" + str(user.username))
file.write("\t" + str(user.number_of_followers))
file.write("\t" + str(user.number_of_followings))
file.write("\t" + str(user.is_verified))
file.close()