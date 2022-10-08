# Get instance
import instaloader
from instagramy import InstagramUser

def print_profile(user):
    file.write("\n" + str(user.username))
    file.write("\t" + str(user.number_of_followers))
    file.write("\t" + str(user.number_of_followings))
    file.write("\t" + str(user.is_verified))
    file.write("\t" + str(user.biography.replace("\n", "")))

L = instaloader.Instaloader()

# Login or load session
username = input("Type your instagram mail: ")
password = input("Type your instagram password: ")
L.login(username, password)  # (login)
account_to_scrape = input("Paste the username you want to scrape: ")

# Obtain profile metadata
primary_user = instaloader.Profile.from_username(L.context, account_to_scrape)
user = InstagramUser(account_to_scrape)
file = open(f"{primary_user.username}.csv", "w", encoding="utf-8")
# Formatting the data
file.write("User")
file.write("\tFollowers")
file.write("\tFollowing")
file.write("\tVerified")
print_profile(user.username)


count = 0
for followee in primary_user.get_followees():
    if count >= 300:
        break
    user = InstagramUser(followee.username)
    print_profile(user)
    print(user.username)
    count += 1

file.close()

# tbetan508@gmail.com
# 35rnpZ8YfFGHTyT