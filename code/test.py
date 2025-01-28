from urllib.request import urlopen
from bs4 import BeautifulSoup as BS4,NavigableString,SoupStrainer
from pprint import pprint





def connection(url):
    page=urlopen(url) #return response object
    html_bytes=page.read()
    html=html_bytes.decode("utf-8")
    return html

def obj_beautifulSoup(stringify_html):
    soup=BS4(stringify_html,"html.parser")
    return soup.prettify()

def response(obj_BS4):
    metadata={}
    metadata["title"]=str(obj_BS4.h1.string) 
    print(type(metadata['title']))

    res={}
    res['metadata']=metadata
    return res
       

url="https://en.wikipedia.org/wiki/Potato_grouper"
url1="https://medium.com/@ahmadfarag/http-in-depth-dfdac806c2c0"

page=connection(url)
soup=obj_beautifulSoup(page)
#t1=soup.h1.contents

#print(soup.prettify())
def list_of_sibling(stringfy_html):
    print(stringfy_html.h1.string)
    for sibling in stringfy_html.h1.next_siblings:
        if sibling=='\n':
            pass
        else:
            print(str(sibling))

#list_of_sibling(soup) 
                       
def filter_div(obj_beautifulSoup):
    for div in obj_beautifulSoup.find_all("div"):
        for tag in div.contents:
            if tag.name=="h2":
                print(tag.string+'\n')
            else:
                pass    
#filter_div(soup)
soup1=BS4(connection(url),"html.parser")
json=soup1.find_all("script",attrs={"type":"application/ld+json"})

def meta_data(page):
    meta_filter=SoupStrainer(["head"])
    meta=BS4(page,"html.parser",parse_only=meta_filter)
    
    
print(BS4(connection(url),"html.parser").head.find_all("meta",attrs={"property":"og:type","content":True}))



