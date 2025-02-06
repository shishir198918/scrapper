from flask import Flask,request,make_response,jsonify
import urllib.parse
from urllib.request import urlopen,Request
import scraper
import medium
from bs4 import BeautifulSoup as BS4,SoupStrainer

title_tags_only=SoupStrainer(["h1","h2","h3"])
content_tags_only=SoupStrainer(["main"])
footer_tags=SoupStrainer("script",attrs={"type":"application/ld+json"})

app=Flask(__name__)


def connection_xml(url):
    """Return Stringfy HTML"""
    header={
            "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Content-Type": "application/xml"
            }

    req=Request(url,headers=header,method="GET")
    page=urlopen(req) #return response object
    html_bytes=page.read()
    html=html_bytes.decode("utf-8")
    return html

@app.route("/metadata/", methods=["GET"])
def metadata():
    url=urllib.parse.unquote(request.args.get("url"))
    
    if url[7:14]=="/medium":
        parsed_html=BS4(connection_xml(url),"html.parser")

        return make_response(jsonify(medium.list_of_headings(parsed_html)),200)
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

@app.route("/sitemap",methods=["GET"])
def extract_link():
    url=urllib.parse.unquote(request.args.get("url"))

    list_url=[]
    if url[-3::1]=="xml":        
        xml_raw=BS4(connection_xml(url),"xml")        
        for loc in (xml_raw.find_all("loc")):
            list_url.append(loc.text)
        return make_response(jsonify(list_url))
    


if __name__ =="__main__":
    app.run()


