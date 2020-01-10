
import requests
import time
import json
import os



def get_comments_from_pushshift(numba, **kwargs):
    i = numba
    url = f"https://api.pushshift.io/reddit/search/submission?subreddit=dadjokes&size=500&score=>5&after={i}&before={i+86399}&fields=selftext,title"
    r = requests.get(url,params=kwargs)
    data = r.json()
    return data['data']

def get_all():

    xd = []
    unixtimes = range(1348444800,1569433429,86400)
    j = 1
    for i in unixtimes:
        print(f'{j}/2557')
        j = j + 1
        jeje = get_comments_from_pushshift(i)
        xd.extend(jeje)

    return xd



jaja = get_all()


balle = []
unixtimes = range(1569000000,1569423429,86400)
j = 1
for i in unixtimes:
    jeje = get_comments_from_pushshift(i)
    balle.extend(jeje)
tdict = {'data': balle}








url = "https://api.pushshift.io/reddit/search/submission?subreddit=dadjokes&size=500&score=>5&after=1566000000&before=1566086400&fields=selftext,title"
r = requests.get(url)
data = r.json()
#data = data['data']
tdict.update(data)


data.__class__.__name__
tdict

jaja = get_comments_from_pushshift()








#######################

file = open("testfile.txt","w")

for n in jaja:
    try:
        if n['selftext'] == "":
            continue
        if "[removed]" in n['selftext']:
            continue
        if "[deleted]" in n['selftext']:
            continue
        if len(n['selftext']) > 300:
            continue
        if "http" in n['selftext']:
            continue
        if "&amp;#x200B;" in n['selftext']:
            continue
        if "Edit" in n['selftext']:
            continue
        if "edit" in n['selftext']:
            continue
        if "E:" in n['selftext']:
            continue
        file.write("joke:\n")
        file.write(n['title'])
        file.write("\n")
        file.write(n['selftext'])
        file.write("\n\n")
    except (UnicodeEncodeError,KeyError) as e:
        continue


file.close()

###############################
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

file_len("dadjokes.txt")/5

###############################
## pushshift iosta https://api.pushshift.io/reddit/search/submission?subreddit=dadjokes&size=1000&fields=selftext,title,score
# https://api.pushshift.io/reddit/search/submission?subreddit=dadjokes&size=1000&fields=score,selftext,title&score=%3E10&score=%3C20
# toi hakee kaikki postit jol on 10-20 upvotee, toi ohjelma voi hakee max 500 kerrallaa, mut voit salee tehä jonku skriptin
# joka hakee intervallein mahd paljo postei

# https://www.reddit.com/r/pushshift/comments/9zhj0x/how_to_get_an_archive_of_all_your_comments_from/
# tuolt voit salee hakee infoo, salee looppi joka perustuu aikaan on paras




