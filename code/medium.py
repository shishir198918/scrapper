from urllib.request import urlopen,Request

from bs4 import BeautifulSoup as BS4,SoupStrainer,NavigableString

from pprint import pprint
import json 


def connection(url):
    """Return Stringfy HTML"""
    req=Request(url,headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0"},method="GET")
    page=urlopen(req) #return response object
    html_bytes=page.read()
    html=html_bytes.decode("utf-8")
    return html
url="https://medium.com/@spaw.co/beautifulsoup-user-agents-in-python-73f1ce49deb1"

content=BS4(connection(url),"html.parser")

def nested_tag(tag):
    heading_obj=[]
    heading_obj.append(tag.string)
    for child in tag.descendants:    
        if child.name==tag.name:
            break
        if child.name in ["h2","h3","h4","h6"]:
            heading_obj.append({child.name:nested_tag(child)})
    return heading_obj

def heading_list(html_object):
    obj={"heading":[]}
    for heading in html_object.find_all("h1"):
        obj["heading"].append(nested_tag(heading))
    return obj    




def list_of_headings(html_object):
    meta_obj={}
    for tag in html_object.html.find_all("meta"):
        '''for name attribute'''
        if hasattr(tag,"name"):
            for value in tag.get_attribute_list('name'):                
                if value in ["description","title","author"]:
                    meta_obj[value]=tag['content']
        if hasattr(tag,"property"):
            for value in tag.get_attribute_list('property'):
                if value in ['article:published_time','article:modified_time']:
                    meta_obj[value]=tag['content']
    meta_obj.update(heading_list(html_object))
    return meta_obj  



def content(html_object):
    contents={}
    head=html_object.find("h1")
    contents[head.string]
    for tag in head.parent.next_siblings:
        for sub_tag in tag.descendants:
            if hasattr(sub_tag,"text"):
                contents

        


#print(list_of_headings(content))        
        

