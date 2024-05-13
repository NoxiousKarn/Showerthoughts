# Shower Thoughts Pwnagotchi Modification

<img src="doc/attachments/showerthoughts.gif" width="631" height="272"/>
## IMPORTANT!! Verifiy the location of your voice.py file location as it's based on the version of python your unit is running.



## Introduction

This modification displays random r/showerthoughts headlines on your pwnagotchi when the device is waiting. 

It is a fun way to add some personality to your pwnagotchi and keep you entertained.

NOTE: All other phrases used by pwnagotchi will still display as normal, but waiting...(x Sec), etc... is replaced with a call to read a modified copy of the official r/showerthoughts rss feed. 
It is modified by a Python program that only saves valid headlines to an RSS file called shortshowerthoughts.rss in append mode. (Append = add to the file don't overwrite) 
This means once you have some headlines you won't need the internet for them to display and your list of phrases will grow every time a valid (Less then 68 characters long) headline is posted to r/showerthoughts RSS feed.


To do the modification, follow the instructions in the configuration section. 
You will need internet to the Pwnagotchi for these steps to work and every time it needs to download the RSS feed for new phrases. 
It will wait until the internet is restored to perform the download from Reddit.

SSH into your Pi and follow the configuration below.

## Configuration
Copy the commands here and paste them in order in a terminal window. (just right click in the terminal window to paste from the clipboard)

Go superuser
```bash
sudo su
```
Download Showerthoughts RSS feed to root. 
```bash
curl --silent https://www.reddit.com/r/showerthoughts/.rss --user-agent 'Mozilla' --output /root/showerthoughts.rss
```
Downloads remove_long_titles.py to /usr/local/bin
```bash
wget -P /usr/local/bin https://raw.githubusercontent.com/NoxiousKarn/Showerthoughts/main/remove_long_titles.py
```
Run remove_long_titles.py
```bash
python /usr/local/bin/remove_long_titles.py
```
## Python Version 3.7 (only)

Download modified voice.py from this repo and place in /usr/local/lib/python3.7/dist-packages/pwnagotchi/ it should save as voice.py.1 (Work with older forks running python 3.7)
```bash
wget -P /usr/local/lib/python3.7/dist-packages/pwnagotchi/ https://raw.githubusercontent.com/NoxiousKarn/Showerthoughts/main/voice.py
```
Rename voice.py to voice.py.old and then rename voice.py.1 to voice.py.
```bash
mv /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py.old ; mv /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py.1 /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py
```
## Python 3.9 (only)

Download modified voice.py from this repo and place in /usr/local/lib/python3.p/dist-packages/pwnagotchi/ it should save as voice.py.1 (Work with older forks running python 3.9)
```bash
wget -P /usr/local/lib/python3.9/dist-packages/pwnagotchi/ https://raw.githubusercontent.com/NoxiousKarn/Showerthoughts/main/voice.py
```
Rename voice.py to voice.py.old and then rename voice.py.1 to voice.py.
```bash
mv /usr/local/lib/python3.9/dist-packages/pwnagotchi/voice.py /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py.old ; mv /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py.1 /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py
```

## Remaining steps are the same for all versions.

Set Cronjobs to download the RSS every 4 hours, then run remove_long_titles.py to remove long Headlines in the feed file every 4 hours
```bash
(echo "0 */4 * * * curl --silent https://www.reddit.com/r/showerthoughts/.rss --user-agent 'Mozilla' --output showerthoughts.rss" ; echo "0 */4 * * * /usr/bin/python3 /usr/local/bin/remove_long_titles.py >/dev/null 2>&1") | crontab -
```
Reboot Pwnagotchi
```bash
touch /root/.pwnagotchi-auto && systemctl restart pwnagotchi
```

Once loaded in auto mode you should see new phrases appear regularly.


## Usage
It's just gonna run by itself you don't need to do anything for the phrases to start. Every 4 hours it will DL the RSS and then remove the long headlines, if you don't have internet after the 4-hour mark it will wait for the internet and download the feed then. 


## Uninstalling
If you want to undo what we did SSH in.

Go Superuser
```bash
sudo su
```
## Choose the script that matches you Python version.

## Python 3.7
Remove voice.py then rename voice.py.old to voice.py
```bash
rm /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py ; mv /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py.old /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py
```

## Python 3.9
Remove voice.py then rename voice.py.old to voice.py
```bash
rm /usr/local/lib/python3.9/dist-packages/pwnagotchi/voice.py ; mv /usr/local/lib/python3.9/dist-packages/pwnagotchi/voice.py.old /usr/local/lib/python3.9/dist-packages/pwnagotchi/voice.py
```

Remove remove-long-titles.py
```bash
rm /usr/local/bin/remove_long_titles.py
```
Remove showerthoughts.rss file from our root folder
```bash
rm /root/showerthoughts.rss
```
Remove shortshowerthoughts.rss Skip this step if you want to keep already collected headlines for reinstall
```bash
rm /root/shortshowerthoughts.rss
```
Remove cronjobs from crontab manually Delete the lines we added and save
```bash
crontab -e
```
save
Ctrl+O
save as named
[enter]
Exit
Ctrl+X

Reboot Pwnagotchi
```bash
touch /root/.pwnagotchi-auto && systemctl restart pwnagotchi
```

   There all gone and back to normal!

## License
The plugin is licensed under the GPLv3 license.
