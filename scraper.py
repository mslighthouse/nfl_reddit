import praw
import time
import sqlite3

start = time.time()
print("Program Starting...") # Timekeeping

# connect to sqlite database
conn   = sqlite3.connect('nfl.db')
cursor = conn.cursor()

# reddit authorization
reddit = praw.Reddit("NFL Superbowl 50 /r/nfl threads scraper 1.0 by /u/mslighthouse")

# game thread (1st quarter 44o48r) (2nd quarter 44ogft) (halftime 44onej) (3rd quarter 44orca) (4th quarter 44ow9l)
submission = reddit.get_submission(submission_id='44onej')
submission.replace_more_comments(limit=None, threshold=0)

# comment tree
commentlist = praw.helpers.flatten_tree(submission.comments)

for comment in commentlist:

    #author
    auth = comment.author
    if auth is None:
        auth = "None"
    else:
        auth = str(comment.author)
    #author flair
    flair_text = comment.author_flair_text
    if flair_text is None:
        flair_text = "None"

    #comment bodies
    if comment.body is None:
        body = "None"
    else:
        body = comment.body.encode('ascii', 'ignore')

    #time created (UTC)
    created = comment.created_utc

    #gilded
    if comment.gilded > 0:
        gilded = "TRUE"
    else:
        gilded = "FALSE"

    #score
    score = comment.score

    #insertion to DB CHANGE QUARTER TABLES
    cursor.execute("INSERT INTO halftime VALUES (?,?,?,?,?,?)", (auth, flair_text, body, created, gilded, score))

# commit DB changes
conn.commit()

# timekeeping
print("Program ended. Process time:" + str((time.time() - start)/60) + "Minutes")
print("Program ending")
