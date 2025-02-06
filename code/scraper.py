from urllib.request import urlopen,Request

from bs4 import BeautifulSoup as BS4,SoupStrainer,NavigableString

from pprint import pprint
import json 

url="https://en.wikipedia.org/wiki/Feudalism"
url1="http://css.maxdesign.com.au/selectutorial/tutorial_step2.htm"
url2="https://en.wikipedia.org/wiki/Maria_Sharapova#Filmography"
url3="https://medium.com/@ahmadfarag/http-in-depth-dfdac806c2c0"
url4="https://beautiful-soup-4.readthedocs.io/en/latest/"
url5="https://en.wikipedia.org/wiki/Prakash_Shukla"
url6="https://en.wikipedia.org/wiki/Sachin_Tendulkar"
url_med="https://medium.com/myp-magazine-16/wunderland-mia-im-interview-c4f0df0ba603"
url_med2="https://medium.com/@spaw.co/beautifulsoup-user-agents-in-python-73f1ce49deb1"
def connection(url):
    """Return Stringfy HTML"""
    req=Request(url,headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0"},method="GET")
    page=urlopen(req) #return response object
    html_bytes=page.read()
    html=html_bytes.decode("utf-8")
    return html
     

title_tags_only=SoupStrainer(["h1","h2","h3","h4"]) # only parse title tags 
footer_tags=SoupStrainer("script",attrs={"type":"application/ld+json"})

script=BS4(connection(url1),"html.parser",parse_only=footer_tags)
title_soup=BS4(connection(url4),"html.parser",parse_only=title_tags_only)
content=BS4(connection(url_med2),"html.parser",parse_only=SoupStrainer(["body","main"]))



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



'''comment--> not in use '''
def dates(tag):
    date_dic=json.loads(tag.string)
    date={}
    date["datePublished"]=date_dic["datePublished"]
    date["dateModified"]=date_dic["dateModified"]
    return date

def clean_text(tag):
    string=""
    for child in tag.descendants:
        if child.string:
            if child.name in ["h1","h2","h3","h4","h5"]:
                break
            else:
                string=string+child.string
    return string            


def ancestors(tag):
    return tag.parent.parent


def tag_text_content(tag_name):
    obj={}
    obj[tag_name.string]=[]
    count=1
    break_indicator=False
    

    for friend in (tag_name.parent.next_siblings):
        if not break_indicator:
            if not friend.name:
                continue
            #print(friend.name)

            if friend.name in ["header","script","nav","noscript","style"]:
                continue
            
            if  hasattr(friend,"text"):
                
                string="".join(friend.text)
                #string=clean_text(friend)
                obj[tag_name.string].append(string.replace('\n'," "))
        

            if friend.name=="img":
                    obj[tag_name.string].append("".join(f"image->{count} {friend['src']}"))
                    count=count+1
            if friend.name=="figure":
                    obj[tag_name.string].append(({friend.figcaption.text:("".join(friend.text)).replace('\n'," ")}))
                        
            #if friend.name in ["h3","h4","h5"]:
                    #obj[tag_name.string].append({friend.text:tag_text_content(friend)})
            
  
            for child in friend.descendants:

                if not child.name:
                    continue
                
                if child.name in ["header","script","nav","noscript","style"]:
                    continue
               
                if child.name=="img":
                    obj[tag_name.string].append("".join(f"image->{count} {child['src']}"))
                    count=count+1
                if child.name=="figure":
                    obj[tag_name.string].append(({child.figcaption.string:("".join(child.text)).replace("\n"," ")}))
                
                if child.name=="table":
                    pass

                if child.name in ["h3","h4","h5"]:
                    obj[tag_name.string].append({child.text:tag_text_content(child)})

                if child.name==tag_name.name:
                    break_indicator=True
                    break    
                else:
                    continue
        else:
            break        
    return obj       


def heading_text(main_object):
    title_headings=main_object.find("h1")
    obj={}
    obj[title_headings.string]=[]
    count=1
    break_indicator=False
    for friend in title_headings.parent.next_siblings:                   
        if not break_indicator:
            if not friend.name:
                continue
            if friend.name in ["header","script","nav","noscript","style"]:
                continue
            
            
            if hasattr(friend,"text"):                
                for child in friend.contents:
                    if child.name in ["header","script","nav","noscript","style"]:                
                        continue
                        
                    if break_indicator:

                        break
                                            
                    if  hasattr(child,"text")  and  not isinstance(child,NavigableString):
                        for grandchild in child.descendants:

                            if grandchild.name in ["h1","h2","h3","h4","h5","h6"]:
                                break_indicator=True
                                break
                            if hasattr(grandchild,"string") and grandchild.name=="p":
                                string=("".join(grandchild.text)).replace('\n',"")
                                obj[title_headings.string].append((string))

                            if grandchild.name=="img":
                                obj[title_headings.string].append((f"image->{count} {grandchild['src']}"))
                                count=count+1
                            if grandchild.name=="figure":    
                                obj[title_headings.string].append(({grandchild.figcaption.string:("".join(grandchild.text)).replace("\n","")}))

        else:
            break            
    return obj            

     

def text_content(main_object):
    contents=[]
    contents.append(heading_text(main_object))
    for heading in main_object.find_all(["h1"]):           
        contents.append(tag_text_content(heading))
    return contents    


#pprint(text_content(content.body))



                
                






