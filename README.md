# Shower Thoughts Pwnagotchi Modification

## Introduction

This modification displays random r/showerthoughts headlines on your pwnagotchi when the device is waiting. It is a fun way to add some personality to your pwnagotchi and keep you entertained.

To do the modification, follow the instructions in the configuration section. 

You will need internet to the Pwnagotchi for these steps to work. And every time it needs to download the RSS feed. (It will wait until the internet is restored to perform the download.)

First, get a shared internet connection via BT or through your host machine. 

If you are running a Pi3 or 4 and have an ETH port just connect that port to your router and follow along. 

Copy the commands here and paste them in order in a terminal window. (just right click in the terminal window to paste from clipboard)

## Configuration

[command] <~~~ [explanation]

1. SSH to your Pwnagotchi. <~~~Self explanatory. if you need help with this do not proceed further this modification might not be for you.
2. Sudo su <~~~ go superuser
3. curl --silent https://www.reddit.com/r/showerthoughts/.rss --user-agent 'Mozilla' --output /root/showerthoughts.rss <~~~Download Showerthoughts RSS feed to root.
4. wget -P /usr/local/bin https://raw.githubusercontent.com/NoxiousKarn/Showerthoughts/main/remove_long_titles.py <~~~Downloads remove_long_titles.py to the right spot
5. python /usr/local/bin/remove_long_titles.py <~~~run the script we just saved to remove long headlines right away.
6. wget -P /usr/local/lib/python3.7/dist-packages/pwnagotchi/ https://raw.githubusercontent.com/NoxiousKarn/Showerthoughts/main/voice.py <~~~ Saves modified voice.py as voice.py.1
7. mv /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py.old ; mv /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py.1 /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py <~~~This command will first rename voice.py to voice.py.old and then rename voice.py.1 to voice.py.
8. (echo "0 */4 * * * curl --silent https://www.reddit.com/r/showerthoughts/.rss --user-agent 'Mozilla' --output showerthoughts.rss" ; echo "0 */4 * * * /usr/bin/python3 /usr/local/bin/remove_long_titles.py >/dev/null 2>&1") | crontab -
 <~~~ Sets cronjobs to download the RSS every 4 hours, then run remove_long_titles.py to remove long Headlines in the feed file every 4 hours.
9. touch /root/.pwnagotchi-auto && systemctl restart pwnagotchi <~~~this will reboot your Pwnagotchi.

Once loaded in auto mode you should see new phrases appear regularly.

## Usage
It's just gonna run by itself. every 4 hours it will DL the RSS and then remove the long headlines by itself, if you don't have internet after the 4-hour mark it will wait for the internet and download the feed then. 
(this can cause an error where the RSS displays headlines longer than 68 characters because the cronjob that runs remove_long_titles.py may have already run and has an out-of-sync timer. a simple reboot can correct this problem.
it is recommended to use this modification with Default memtemp and gps plugins turned off. We need their screen real estate. 

## Uninstalling
If you want to undo what we did SSH in.
Then we will type a command to remove voice.py and then rename voice.py.old to voice.py effectively undoing our modification. Delete the script and delete the RSS file remove the cronjobs and reboot.
1. sudo su <~~~ Superuser
2.  rm /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py ; mv /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py.old /usr/local/lib/python3.7/dist-packages/pwnagotchi/voice.py <~~~ removes voice.py then renames voice.py.old to voice.py
3. rm /usr/local/bin/remove_long_titles.py <~~~ Removes our custom python code that removes long headlines
4. rm /root/showerthoughts.rss <~~~ Removes showerthoughts.rss file from our root folder
5. rm /root/shortshowerthoughts.rss <~~~ Removes shortshowerthoughts.rss file from our root folder. **skip if reinstalling or updating to keep your headlines**
6. crontab -e
7. Delete the lines we added
8. Save and exit Hit: CTRL+O, [ENTER], CTRL+X 
9. Reboot

   There all gone and back to normal!

## License
The plugin is licensed under the GPLv3 license.

3. Reboot
