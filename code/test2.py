from urllib.request import urlopen
from bs4 import BeautifulSoup as BS4,NavigableString,SoupStrainer
import test 

url="https://en.wikipedia.org/wiki/Purulia_arms_drop_case"


stringfy_html=test.connection(url)

def body_content(string_html):
    """ all return a list of contents in a body tag""" 
    l1=BS4(string_html,"html.parser").body.contents

    for tag in l1:
        if tag.name is None:
            pass
        else:
            
            print(f"tag name->{tag.name},tag attributes->{tag.attrs},line number->{tag.sourceline}")
            count=0
            for tag1 in tag.descendants:
                
                if tag1.name is None:
                        pass
                else:
                    count=count+1
                    print(f"{tag1.name}--{count}??{tag1.sourceline}'\n'")
                 
def list_tag(parent_tag,child_tag):
    obj={}
    l2=[]
    l1=parent_tag.find_all(child_tag)
    if l1:
        for title in l1:
            l2.append(title.text)
        obj[parent_tag]=l2
        return obj     
l2=BS4(stringfy_html,"html.parser").find_all(True)
for tag in l2:
    print(tag.name)

        





