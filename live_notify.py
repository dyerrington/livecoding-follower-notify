#!/Users/davidyerrington/virtualenvs/data/bin/python

import feedparser # pip install feedparser
import pandas as pd, logging, os, subprocess, time
import gntp.notifier

logging.basicConfig(level=logging.INFO)

rss_feed    =   "https://www.livecoding.tv/rss/dyerrington/followers/?key=[your key here]"
feed        =   feedparser.parse(rss_feed)

users       =   []

if feed.entries:
    for item in feed.entries:
        users.append({ 
            'username':  item.title, 
            'url':       item.links[0]['href']
        })
        
feed_df             =   pd.DataFrame(users)
serialized_file     =   './livecoding_followers.pkl'

# Read initial state
try:
    users_df        =   pd.read_pickle(serialized_file)

except: # additionally can catch IOError but lets catch everything
# Save initial state if none exists
    users_df = pd.DataFrame(users)
    users_df.to_pickle(serialized_file)


# test_new    =   pd.DataFrame([{'username': 'KaiserK13', 'url': 'Hh0h0h0h0'}, {'username': 'shanevrgr', 'url': 'assbandit'}, {'username': 'dardoneli', 'url': 'blalbalblablba'}])
# feed_df     =   feed_df.append(test_new)

new_users   =   (set(feed_df['username'].values) - set(users_df['username'].values))

growl = gntp.notifier.GrowlNotifier(
        applicationName = "livecoding.tv Awesome Notification Business HD",
        notifications = ["New Updates","New Messages"],
        defaultNotifications = ["New Messages"],
        # hostname = "computer.example.com", # Defaults to localhost
        # password = "abc123" # Defaults to a blank password
)
growl.register()


for username in new_users:
    
    growl.notify(
        noteType = "New Messages",
        title = "%s" % username,
        description = "Thanks for subscribing!",
        icon = "http://icons.iconarchive.com/icons/dryicons/valentine/128/heart-icon.png",
        sticky = True,
        priority = 1
    )

    subprocess.call(['./play_random.sh'])
    time.sleep(10)

# serialize new feed data if we've already displayed it
if len(new_users) > 0:
    print 'pickling new feed data..'
    feed_df.to_pickle(serialized_file)