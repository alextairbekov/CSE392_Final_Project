import praw
from snap import *

def add_new_user(user_name, user_dict, network):
    user_id = user_dict.get(user_name, -1)
    if user_id == -1:
        user_id = len(user_dict)
        user_dict[user_name] = user_id
        network.AddNode(user_id)
    return user_id

net = TNEANet.New()
users = {}

# assume author_name is already in users
# and comments are in a list sorted by creation date
def load_comment(edge_id, parent_name, author_name, created_utc, replies):
    replies.replace_more(limit=None)
    # edge_id measures established conversation
    
    timestamp = {}

    for reply in sorted(list(replies), key=lambda k: k.created_utc):
        reply_author = reply.author
        if reply_author is None:
            reply_author = ""
        else:
            reply_author = reply_author.name 
        if reply_author == author_name:
            load_comment(edge_id, parent_name, author_name, created_utc, reply.replies)
            continue
        if reply_author not in timestamp:
            timestamp[reply_author] = int(reply.created_utc)
        if reply_author == parent_name:
            net.AddIntAttrDatE(edge_id, timestamp[parent_name] - created_utc, str(int(created_utc)))
            load_comment(edge_id, author_name, parent_name, timestamp[parent_name], reply.replies)
        else:
            user_id = add_new_user(reply_author, users, net)
            new_edge_id = net.AddEdge(users[author_name], user_id)
            load_comment(new_edge_id, author_name, reply_author, reply.created_utc, reply.replies)


reddit = praw.Reddit(user_agent='linux:reds:v0.0.1 (by /u/anvils-reloaded)', client_id='7Rx0lKv3vHNvZA', client_secret='ys6ywb8ke4OKCF4JSC9mf82Dq3k')

submissions = reddit.subreddit('programming').new(limit=100)

for submission in submissions:
    
    submission_author = submission.author
    if submission_author is None:
        submission_author = ""
    else:
        submission_author = submission_author.name 
    author_id = add_new_user(submission_author, users, net)
    
    submission.comments.replace_more(limit=None)
    for comment in submission.comments:
        comment_author = comment.author
        if comment_author is None:
            comment_author = ""
        else:
            comment_author = comment_author.name
        user_id = add_new_user(comment_author, users, net)
        edge_id = -1
        if user_id != edge_id:
            edge_id = net.AddEdge(author_id, user_id) 
        load_comment(edge_id, submission_author, comment_author, comment.created_utc, comment.replies)

    # okay cool after this we've loaded all of our comments into the tree
    # now, for each edge, we know the stochastic process representing the distribution

    # calculate the mean and variance response times of each user for each "thread"
    # also aggregate the means and variances of vertices:

    # sort and build a distribution of means, variances 

    net.Dump()
