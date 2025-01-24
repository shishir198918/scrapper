from flask import Flask,request,make_response,jsonify
import urllib.parse
import scraper
from bs4 import BeautifulSoup as BS4,SoupStrainer

title_tags_only=SoupStrainer(["h1","h2","h3"])

app=Flask(__name__)

@app.route("/metadata/", methods=["GET"])
def metadata():
    url=urllib.parse.unquote(request.args.get("url"))
    title_BS4=BS4(scraper.connection(url),"html.parser",parse_only=title_tags_only)
    meta={}
    meta["title"]=str(title_BS4.h1.text) 
    meta["content"]=scraper.list_of_content(title_BS4)

    res={}
    res['metadata']=meta
    return make_response(jsonify(res),200)

if __name__ =="__main__":
    app.run()


