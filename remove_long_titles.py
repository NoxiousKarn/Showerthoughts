import re
import os
import logging

def remove_long_titles(filename):

    with open(filename, 'r') as f:
        data = f.read()

    title_regex = r'<title>(.*?)</title>'
    headlines = re.findall(title_regex, data)

    short_headlines = []
    for headline in headlines:
        if len(headline) <= 68 and headline.strip().lower() != "showerthoughts":
            short_headlines.append(headline)

    with open(filename, 'w') as f:
        f.write(data)

    with open('/root/shortshowerthoughts.rss', 'a') as f:
        for headline in short_headlines:
            if headline not in f.read():
                f.write('<title>{}</title>'.format(headline))

if __name__ == '__main__':
    filename = '/root/showerthoughts.rss'

    remove_long_titles(filename)

    logging.info('Finished removing long headlines from RSS feed.')
