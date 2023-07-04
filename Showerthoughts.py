import subprocess
import re
import random
import os
import pwnagotchi.plugins as plugins


class ShowerThoughtsPlugin(plugins.Plugin):
    __author__ = 'Noxiouskarn & GPT3'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Display random shower thoughts rss headlines when waiting. '

    def __init__(self):
        self.rss_url = self.options['rss_url']
        self.saved_rss = self.options['saved_rss']
        self.max_title_length = self.options['max_title_length']
        self.make_file_writeable = true
        self.download_rss_feed()

    def on_wait(self, agent, seconds):
        headline = self.get_random_headline()
        agent.display.write(headline)
    
    def download_rss_feed(self):
        command = "curl --silent {} --user-agent 'Mozilla' --output {}".format(self.rss_url, self.saved_rss)
        subprocess.run(command, shell=True)
        
        if self.make_file_writeable:
            # Make the saved RSS file writeable
            saved_rss_path = self.options['saved_rss']
            make_file_writeable(saved_rss_path)
            
    def remove_long_titles(self):
        with open(self.saved_rss, 'r') as f:
            data = f.read()

        title_regex = r'<title>(.*?)</title>'
        long_titles = re.findall(title_regex, data)

        for title in long_titles:
            if len(title) > self.max_title_length:
                data = data.replace("<title>{}</title>".format(title), '')

        with open(self.saved_rss, 'w') as f:
            f.write(re.sub(title_regex, '', data))

    def get_random_headline(self):
        self.remove_long_titles()

        with open(self.saved_rss, 'r') as f:
            data = f.read()

        title_regex = r'<title>(.*?)</title>'
        headlines = re.findall(title_regex, data)

        return random.choice(headlines)


plugins.register(ShowerThoughtsPlugin())
