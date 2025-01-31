import scraper as sc
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS4,SoupStrainer,NavigableString

from pprint import pprint
url=sc.url
main_filter=SoupStrainer(["main"])
content=BS4(sc.connection(url),"html.parser",parse_only=main_filter)



def parse_content(main_content):
    return parse_tag(main_content)

def parse_tag(tag):
    contents=[]

    if hasattr(tag,"children"):
        for child in tag.children:
            contents.extend((parse_tag(child)))
    else:    
        contents.append((parse_tag_content(tag)))
    return {'content': (contents)}

def parse_tag_content(tag):
    return tag.text.strip()
pprint(parse_content(content.main))