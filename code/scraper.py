from urllib.request import urlopen

from bs4 import BeautifulSoup as BS4,SoupStrainer

url="https://en.wikipedia.org/wiki/Prakash_Shukla"
url2="https://en.wikipedia.org/wiki/Web_scraping"
url3="https://en.wikipedia.org/wiki/Market_research"

def connection(url):
    """Return Stringfy HTML"""
    page=urlopen(url) #return response object
    html_bytes=page.read()
    html=html_bytes.decode("utf-8")
    return html

content_tags_only=SoupStrainer(["h1","h2","h3","img","p","ul","ol","a","span","b","cite","i"])
title_tags_only=SoupStrainer(["h1","h2","h3"]) # only parse title tags 
title_soup=BS4(connection(url),"html.parser",parse_only=title_tags_only)
soup=BS4(connection(url3),"html.parser",parse_only=content_tags_only)

def list_of_content(title_soup):
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
                     
    return content 


  



def text_content(soup):
    content = {}
    headings = soup.find_all(["h1","h2","h3"])
    
    for heading in headings:
        section_title = heading.text.strip()  
        content[section_title] = ""  
        
        
        for sibling in heading.find_next_siblings():
            if sibling.name in ["h1","h2","h3"]:
                break  
            
            
            if sibling.name =="img" and "src" in sibling.attrs:
                content[section_title] = content[section_title]+ f"\nImage: {sibling['src']}"
            

            elif sibling.name in ["p","ul","ol","a"]:
                
                content[section_title] = content[section_title]+f"\n{sibling.get_text(strip=True)}"
    
    return content
print(text_content(soup)) 




                
                






