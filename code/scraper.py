from urllib.request import urlopen

from bs4 import BeautifulSoup as BS4,SoupStrainer

from pprint import pprint
import json 


url1="http://css.maxdesign.com.au/selectutorial/tutorial_step2.htm"
url2="https://en.wikipedia.org/wiki/Maria_Sharapova#Filmography"
url3="https://en.wikipedia.org/wiki/Potato"


def connection(url):
    """Return Stringfy HTML"""
    page=urlopen(url) #return response object
    html_bytes=page.read()
    html=html_bytes.decode("utf-8")
    return html

title_tags_only=SoupStrainer(["h1","h2","h3","h4"]) # only parse title tags 
footer_tags=SoupStrainer("script",attrs={"type":"application/ld+json"})

script=BS4(connection(url1),"html.parser",parse_only=footer_tags)
title_soup=BS4(connection(url3),"html.parser",parse_only=title_tags_only)
content=BS4(connection(url1),"html.parser",parse_only=SoupStrainer(["main"]))



def list_of_headings(title_soup):
    content=[]
    obj={}
    for title in title_soup.find_all("h2"):        
        if title.next_sibling and title.next_sibling.name !="h2":
            obj[title.text]=[]
            for sub_title in title.next_siblings:
                if sub_title.name=="h3":
                    obj[title.text].append(sub_title.text)
                elif sub_title.name=="h2":
                    
                    break
                else:
                    pass
        else:
            content.append(title.text)                                                                      
    return content 




def dates(tag):
    date_dic=json.loads(tag.string)
    date={}
    date["datePublished"]=date_dic["datePublished"]
    date["dateModified"]=date_dic["dateModified"]
    return date

def ancestors(tag):
    return tag.parent.parent


def tag_text_content(tag_name):
    obj={}
    obj[tag_name.text]=[]
    count=1
    break_indicator=False
    

    for friend in (tag_name.parent.next_siblings):
        if not break_indicator:
            if not friend.name:
                continue
            #print(friend.name)

            if friend.name in ["header","script","nav","noscript","style"]:
                    continue
            
            if  hasattr(friend,"text") and friend.text:
                
                string="".join(friend.text)
                obj[tag_name.text].append((string))
        

            if friend.name=="img":
                    obj[tag_name.text].append("".join(f"image->{count} {friend['src']}"))
                    count=count+1
            if friend.name=="figure":
                    obj[tag_name.text].append("".join({friend.figcaption.text:friend.text}))
                        
            if friend.name in ["h3","h4","h5"]:
                    obj[tag_name.text].append({friend.text:tag_text_content(friend)})
            
  
            for child in friend.descendants:

                if not child.name:
                    continue
                
                if child.name in ["header","script","nav","noscript","style"]:
                    continue
               
                if child.name=="img":
                    obj[tag_name.text].append((f"image->{count} {child['src']}"))
                    count=count+1
                if child.name=="figure":
                    obj[tag_name.text].append(({child.figcaption.text:child.text}))
                
                if child.name=="table":
                    pass

                if child.name in ["h3","h4","h5"]:
                    obj[tag_name.text].append({child.text:tag_text_content(child)})

                if child.name==tag_name.name:
                    break_indicator=True
                    break    
                else:
                    continue
        else:
            break        
    return obj       
                                      

def text_content(main_object):
    contents=[]
    for heading in main_object.find_all(["h2"]):
        
        contents.append(tag_text_content(heading))
    return contents    

pprint(text_content(content.main))



                
                






