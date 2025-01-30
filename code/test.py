import scraper as sc
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS4,SoupStrainer,NavigableString
from pprint import pprint
url=sc.url
main_filter=SoupStrainer(["main"])
content=BS4(sc.connection(url),"html.parser",parse_only=main_filter)

def list_of_children(content):
    l1=content.main.contents
    print(f"contents list-->{len(l1)}")
    l2=list(content.main.descendants)
    print(f"descendants list-->{len(l2)}")
    print(f"find_all-->{len(content.main.find_all(True))}")

def structure(tag_name):

    l1=[]    
    for tag in tag_name.children:
        #print(type(tag))
        #count=0
        if isinstance(tag,NavigableString):
                #print(f"NavigableString{count}")
                #count=count+1
                continue    #passing to next node
        if  not tag.contents:
             #print(f"Contents{count}")
             #count=count+1
             l1.append(tag.name)
                 
        else:
            #print(f"structure{count}")
            #count=count+1
            l1.append({tag.name:structure(tag)})
    return l1    

#pprint(structure(content.main))  

def content_data(tag_name):
    l1=[] 
    image_counter=1   
    for tag in tag_name.children:
        print(len(list(tag_name.children)))

        if  tag.name=="img":
            l1.append({f"image link{image_counter}":tag["src"]})
            image_counter=image_counter+1

        #if not isinstance(tag,NavigableString) or not tag.strip():
            #continue
            
        if  tag.text:
            l1.append({tag.name:tag.text.strip()}) 
        
        else:
            l1.append({tag.name:structure(tag)})
    return l1        
                 
pprint(content_data(content.main))               
#print((content.header.string))
     
     


 