import praw
import re
import time
import random
reddit = praw.Reddit(user_agent='CoBBattleBot' ,
                     client_id='e_q5FCoE9tkAwA' ,
                     client_secret='DdT9siB75usVN1eDv7t3qa2IbpY' ,
                     password='Bushybushy101' ,
                     username='CoBBattleBot'
)

intro = random.randint(1,4)
if (intro == 1):
    print ("I'm afraid I can't do that Dave.")
    time.sleep(2)
    print ("Just kidding, I'm built to serve!\n\n")
elif (intro == 2):
    print ("Welcome dino! How can I help?\n\n")
elif (intro == 3):
    print ("I'm programmed to obey the three laws of robotics. I always forget what they are though.\n\n")
elif (intro == 4):
    print ("Guess you're not as clever as you thought if you need me to do all this maths.\n\n")
else:
    print ("Well... that didn't work as well as I thought.\n\n")


print("\nHow many MaA?\n")
maa = int(input(""))
print("\nHow many Levies?\n")
levies = int(input(""))
print("\nHow many hours will it take?\n")
timeTaken = float(input(""))

time.sleep(timeTaken)

title = "Movement Report"
selftext = "{} MaA and {} levies approach the northwest Stark hamlet!".format(maa, levies)
print (selftext)
reddit.subreddit("CenturyOfBloodMods").submit(title, selftext=selftext)
