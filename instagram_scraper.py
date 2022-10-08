# Get instance
import instaloader
import os

def print_profile(user):
    file.write("\n" + str(user.username))
    file.write("\t" + str(user.followers))
    file.write("\t" + str(user.followees))
    file.write("\t" + str(user.full_name))
    # file.write("\t" + str(user.biography.replace("\n", "")))

L = instaloader.Instaloader()

# Login or load session
username = input("Type your instagram mail: ")
password = input("Type your instagram password: ")
L.login(username, password)  # (login)
os.system('cls')
account_to_scrape = input("Paste the username you want to scrape: ")

# Obtain profile metadata
primary_user = instaloader.Profile.from_username(L.context, account_to_scrape)
file = open(f"{primary_user.username}.csv", "w", encoding="utf-8")
# Formatting the data
file.write("User")
file.write("\tFollowers")
file.write("\tFollowing")
file.write("\tFull Name")


count = 0
for followee in primary_user.get_followees():
    primary_user = instaloader.Profile.from_username(L.context, followee.username)
    if count >= 199:
        break
    print_profile(primary_user)
    print(primary_user.username)
    count += 1

file.close()