from flask import Flask,request,make_response,jsonify
import urllib.parse
import scraper
from bs4 import BeautifulSoup as BS4,SoupStrainer

title_tags_only=SoupStrainer(["h1","h2","h3"])
content_tags_only=SoupStrainer(["main"])
footer_tags=SoupStrainer("script",attrs={"type":"application/ld+json"})

app=Flask(__name__)

@app.route("/metadata/", methods=["GET"])
def metadata():
    url=urllib.parse.unquote(request.args.get("url"))
    title_BS4=BS4(scraper.connection(url),"html.parser",parse_only=title_tags_only)
    script=BS4(scraper.connection(url),"html.parser",parse_only=footer_tags)
    meta={}
    meta["title"]=str(title_BS4.h1.text) 
    meta["content"]=scraper.list_of_headings(title_BS4)
    meta["dateOfPublication"]=scraper.dates(script)["datePublished"]
    meta["dateOfModification"]=scraper.dates(script)["dateModified"]
    res={}
    res['metadata']=meta
    return make_response(jsonify(res),200)

@app.route("/content/",methods=["GET"])
def content():
    url=urllib.parse.unquote(request.args.get("url"))
    content_BS4=BS4(scraper.connection(url),"html.parser",parse_only=content_tags_only)
    meta={}
    meta["content"]=scraper.text_content(content_BS4.main)
    return make_response(jsonify(meta),200)

@app.route("/sitemap/medium")
def extract_link():
    file=open("../data/sitemap.xml","r")
    xml_content=file.read()
    file.close()
    xml_raw=BS4(xml_content,"xml")
    list_url=[]
    # for loc in (xml_raw.find_all("loc")):
    #     list_url.append(loc.string)
    for loc in (xml_raw.find_all("loc")):
         list_url.append(loc.text)
    return make_response(jsonify(list_url))

if __name__ =="__main__":
    app.run()


