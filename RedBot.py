import praw
import time

r = praw.Reddit(user_agent = "RedBot by /u/Dalmathus") # This supplies the decription to the API of your intentions on teh service
print("Logging in")
r.login('JamesRedBot', 'r2d2owns')	# log in to reddit, possible parameters are (Username, Password) if left blank it will prompt on login for those details, I left bank here to keep my details confidential

words_to_match = ['james', 'luxton'] # words im looking to match
cache = []

def run_bot():	# defining a function in python follow the next line with 4 spcaes per the python style guide
    print("Grabbing subreddit")
    subreddit = r.get_subreddit("test")	# this will assign our praw object with a subreddit to examie I hav selected r/test here
    print("Grabbing comments")
    comments = subreddit.get_comments(limit = 25) # api calls per minute i have set 25 limit is 200? line gets comments and stores in an array
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match) # are any words in comment string matchign any of the words in our list of words?
        if comment.id not in cache and isMatch:
            try:
                print("Match Found! Comment ID: " + comment.id)
                cache.append(comment.id)
                comment.reply('You said my name!')
                print("Reply succesful")                
            except:
                print ('Comment already replied to')
                pass

while True:
    run_bot()
    time.sleep(10)