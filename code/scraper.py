from urllib.request import urlopen

from bs4 import BeautifulSoup as BS4,SoupStrainer

from pprint import pprint
import json 

url="https://en.wikipedia.org/wiki/Prakash_Shukla"
url2="https://en.wikipedia.org/wiki/Purulia_arms_drop_case"
url3="https://en.wikipedia.org/wiki/Potato"



def connection(url):
    """Return Stringfy HTML"""
    page=urlopen(url) #return response object
    html_bytes=page.read()
    html=html_bytes.decode("utf-8")
    return html

content_tags_only=SoupStrainer(["h1","h2","h3","img","p","ul","ol","a","span","b","cite","i","th","td"])
title_tags_only=SoupStrainer(["h1","h2","h3"]) # only parse title tags 
header_tags=SoupStrainer(["head.meta['property']"])
footer_tags=SoupStrainer("script",attrs={"type":"application/ld+json"})

script=BS4(connection(url),"html.parser",parse_only=footer_tags)
title_soup=BS4(connection(url),"html.parser",parse_only=title_tags_only)
soup=BS4(connection(url3),"html.parser",parse_only=content_tags_only)

def list_of_content(title_soup,script):
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

    content.append(obj)

    content.append(dates(script))        
                     
    return content 


  



def text_content(soup):
    content = {}
    headings = soup.find_all(["h1","h2","h3"])
    
    for heading in headings:
        section_title = heading.text.strip()  
        content[section_title] = ""  
        
        
        for sibling in heading.find_next_siblings():
            count=1
            if sibling.name in ["h1","h2","h3"]:
                break  
            
            
            if sibling.name =="img" and "src" in sibling.attrs:
                content[section_title] = content[section_title]+ f"\nImage{sibling.sourceline}:->{count} {sibling['src']}"
                count=count+1
            

            #elif sibling.name in ["p","ul","ol","a"]:                
                #content[section_title] = content[section_title]+f"\n{sibling.get_text(strip=True)}"
            else:
                pass    
    
    return content


def dates(tag):
    date_dic=json.loads(tag.string)
    date={}
    date["datePublished"]=date_dic["datePublished"]
    date["dateModified"]=date_dic["dateModified"]
    return date

print(list_of_content(title_soup,script))


                
                






