#Follower Notification for Livecoding.tv
A channel follower notification utility I wrote for livecoding.tv.  It will pop open a notification on the configured streaming display and play a random sound from a list of sound files in a directory.

## Requirements

*  OSX (tested on Yosemite)
*  Growl ($3.99 @ Appstore)
*  Some sound clips
*  Feedparser (pip install feedparser)
*  Pandas (pip install pandas)


### Configuration
Edit the live_notify.py file and update your key, and edit the paths to match the directories with your sound files, and then configure Growl!

The only thing you need to do is schedule the python file.  I use GNU watch with a delay of 10 seconds, but you cna use cron.  Test the configureation first and run it form the comnand line before you schedule it to make siure it works.
