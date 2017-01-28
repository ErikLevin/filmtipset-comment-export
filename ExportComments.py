import re
import sys
import urllib.request
from datetime import datetime

user_id = sys.argv[1]
base_url = 'http://www.filmtipset.se/yourpage.cgi?page=commented_movies&member=' + user_id + '&offset='
offset = 0

with open('Filmtipset_comments.csv', 'wb') as output_file:
    while True:
        site_url = base_url + str(offset)
        print('Opening ' + site_url)
        response = urllib.request.urlopen(site_url)
        website_html = response.read()
        html_str = website_html.decode('iso-8859-1')

        comment_re = 'class=favoritetext>(.*?)</div>'
        title_re = '<b><i>Originaltitel:</i></b> (.*?)</div>'
        date_re = '<span title="(\d{2}:\d{2} \d{1,2}/\d{1,2} \d{4})">'
        comment_matches = re.findall(comment_re, html_str, re.DOTALL)
        title_matches = re.findall(title_re, html_str, re.DOTALL)
        date_matches = re.findall(date_re, html_str, re.DOTALL)

        # If we did not get equal number of titles, comments, and dates, something went wrong.
        assert (len(comment_matches) == len(title_matches) == len(date_matches))

        if (len(comment_matches) == 0):
            break  # This page was empty, we are done
        else:
            offset += 20  # Next iteration we will take next page (next 20 comments)

        for i in range(len(comment_matches)):
            comment_matches[i] = comment_matches[i].replace('\r\n',
                                                            ' ')  # Since we're making a csv, we can't really support newlines inside the elements...
            foo = datetime.strptime(date_matches[i], '%H:%M %d/%m %Y')
            output_file.write(
                (title_matches[i] + "\t" + comment_matches[i] + '\t' + str(foo) + '\n').encode('iso-8859-1'))

print('Done!')
