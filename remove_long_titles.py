import re
import os

def remove_long_titles(filename):
    # This function removes long headlines from an RSS feed.

    # Open the RSS feed file in read mode.
    with open(filename, 'r') as f:
        data = f.read()

    # Use a regular expression to extract all the headlines from the file.
    title_regex = r'<title>(.*?)</title>'
    headlines = re.findall(title_regex, data)

    # Iterate over the headlines and remove any headlines that are longer than 68 characters or that are the word "showerthoughts".
    for headline in headlines:
        if len(headline) > 68 or headline.strip().lower() == "showerthoughts":
            data = data.replace("<title>{}</title>".format(headline), '')

    # Write the modified data to the file.
    with open(filename, 'w') as f:
        f.write(data)

if __name__ == '__main__':
    # Get the filename of the RSS feed.
    filename = '/root/showerthoughts.rss'

    # Remove long headlines from the file.
    remove_long_titles(filename)

    # Log the fact that the function has finished running.
    logging.info('Finished removing long headlines from RSS feed.')
