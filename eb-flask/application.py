from flask import Flask
import requests
from bs4 import BeautifulSoup
from flask import Flask, request
from flask_cors import CORS

# ...

application = Flask(__name__)
CORS(application)

# print a nice greeting.
def say_hello(username="World"):
    return '<p>Hello %s!</p>\n' % username

# function to get the head tag content of a website
def get_head_tag_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            head_tag = soup.head
            if head_tag:
                return str(head_tag)
            else:
                return "No <head> tag found on the website."
        else:
            return "Failed to retrieve the website content."
    except:
        return "An error occurred while fetching the website content."

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: Append a URL to the URL (for example: <code>/https://www.switchcode.io</code>)
    to get the <head> tag content of a specific website.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a URL parameter appended to the site URL.
application.add_url_rule('/<path:url>', 'get_head', (lambda url:
    header_text + get_head_tag_content('https://' + url) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
