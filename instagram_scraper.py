# Get instance
import instaloader

def print_profile(user):
    file.write("\n" + str(user.username))   
    file.write("\t" + str(user.followers))
    file.write("\t" + str(user.followees))
    file.write("\t" + str(user.is_verified))
    # file.write("\t" + str(user.biography).replace("\n", ""))

L = instaloader.Instaloader()

# Login or load session
username = input("Type your instagram mail: ")
password = input("Type your instagram password: ")
L.login(username, password)  # (login)
account_to_scrape = input("Paste the username you want to scrape: ")

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, account_to_scrape)
file = open(f"{profile.username}.csv", "w", encoding="utf-8")
# Formatting the data
file.write("User")
file.write("\tFollowers")
file.write("\tFollowing")
file.write("\tVerified")
# file.write("\tBiography")
file.write("\n" + str(profile.username))
file.write("\t" + str(profile.followers))
file.write("\t" + str(profile.followees))
file.write("\t" + str(profile.is_verified))
# file.write("\t" + str(profile.biography).replace("\n", ""))

count = 0
for followee in profile.get_followees():
    if count >= 300:
        break
    profile = instaloader.Profile.from_username(L.context, followee.username)
    print_profile(profile)
    print(profile.username)
    count += 1

file.close()

# tbetan508@gmail.com
# 35rnpZ8YfFGHTyT