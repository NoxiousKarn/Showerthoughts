import re
import os
import logging

def remove_long_titles(filename):
    
    with open(filename, 'r') as f:
        data = f.read()

    
    title_regex = r'<title>(.*?)</title>'
    headlines = re.findall(title_regex, data)

    
    for headline in headlines:
        if len(headline) > 68 or headline.strip().lower() == "showerthoughts":
            data = data.replace("<title>{}</title>".format(headline), '')

    with open(filename, 'w') as f:
        f.write(data)

if __name__ == '__main__':
    filename = '/root/showerthoughts.rss'

    remove_long_titles(filename)

    logging.info('Finished removing long headlines from RSS feed.')
