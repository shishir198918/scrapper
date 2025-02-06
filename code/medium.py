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

parsed_html=BS4(connection_xml(url),"html.parser")

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
    for tag in html_object.find_all("meta"):
        '''for name attribute'''
        if hasattr(tag,"name"):
            for value in tag.get_attribute_list('name'):                
                if value in ["description","title","author"]:
                    meta_obj[value]=tag['content']
        if hasattr(tag,"property"):
            for value in tag.get_attribute_list('property'):
                if value in ['article:published_time','article:modified_time']:
                    meta_obj[value]=tag['content']
                elif value in ['og:type','og:description','og:url']:
                    meta_obj[value[3:]]=tag['content']    
    meta_obj.update(heading_list(html_object))
    return meta_obj  



def head_content_tag(head):
    contents={}
    string=""
    contents[head.string]=[]
    for tag in head.parent.next_siblings:        
        if head.name==tag.name:
            break
        if hasattr(tag,"string") and tag.string:
            contents[head.string].append(("".join(tag.text)).replace('\n'," "))
        if tag.name=="img":
            contents[head.string].append(f"Image-->{tag['src']}")
        if tag.name in ["h2","h3","h4"]:
            contents[head.string].append(head_content_tag(tag))
    return contents  


def text_content_tag(head):
    contents={}

    contents[head.string]=[]
    for tag in head.next_siblings:
        if hasattr(tag,"text") and tag.text:
            for sub_tag in tag.descendants:
                if head.name==tag.name:
                    break
                if hasattr(sub_tag,"string") and sub_tag.string:
                    contents[head.string].append(("".join(sub_tag.text)).replace("\n"," "))
                # if sub_tag.name=="img":
                #     contents[head.string].append(f"Image-->{sub_tag['src']}")
                if tag.name in ["h2","h3","h4"]:
                    contents[head.string].append(text_content_tag(sub_tag))
    return contents  



#pprint(text_content_tag(parsed_html.h1))



    

            


        


#print(list_of_headings(parsed_html))        
        

