import scraper as sc
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS4,SoupStrainer,NavigableString

from pprint import pprint
url=sc.url3
main_filter=SoupStrainer(["main"])
content=BS4(sc.connection(url),"html.parser",parse_only=main_filter)


def structure(tag):
    contents=[]
    for child in tag.children:
        if child.name in [None,"\n","header","script","nav","noscript"]:
            continue
        if child.text and child.text.strip():

            if hasattr(child,"children"):
                contents.extend({child.text:structure(child)})
            else:
                contents.append(child.text.strip())          
    return contents 
#pprint(structure(content.main))                


def grandparent(tag):
    return (tag.parent).parent

def title_tags(main_tag):
    content_title=content.main_tag.find_all(["h2","h3","h4","h5","h6"])
    return content_title

def title_list(content_list):
    title=[]
    heading=content_list[0].get_text()
    for index in range(1,len(content_list)-2,1):
        if grandparent(content_list[index])==grandparent(content_list[index+1]):


 
for title in content.main.div.next_siblings:
    print(title.name)