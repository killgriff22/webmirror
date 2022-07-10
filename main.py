from bs4 import BeautifulSoup
import flask, requests
from flask import Flask
app = Flask(__name__)
mirroraddr=""
@app.route('/')
def index():
    with open("index.htm", "r") as f:
        return f.read()
@app.route('/index.js')
def idxjs():
    with open("index.js", "r") as f:
        return f.read()
@app.route('/mirror')
def mirror():
    global mirroraddr
    try:
        mirroraddr = flask.request.args.get('mirroraddr')
        if not "http://" in mirroraddr:
            mirroraddr = "http://" + mirroraddr
        elif not "https://" in mirroraddr:
            mirroraddr = "https://" + mirroraddr
        baseaddr = mirroraddr.split("/")[2]
        content = requests.get(mirroraddr).text
        soup = BeautifulSoup(content, "html.parser")
        print(soup.prettify())
        content.replace("=\"/","=\"https://"+baseaddr+"/")
    except Exception as e:
        content = "COULD NOT CONNECT TO SITE TO MIRROR"
        print(e)
    return content
if __name__ == '__main__':
   app.run(host="webmirror.up.railway.app")