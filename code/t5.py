from flask import Flask,request,make_response,jsonify
import urllib.parse
import scraper
from bs4 import BeautifulSoup as BS4,SoupStrainer



markup = "<title><p>I want <b>pizza</b> and more <b>pizza</b>!</p></title>"
soup = BS4(markup, 'html.parser')
print(soup.title.text)


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
            

            elif sibling.name in ["p","ul","ol","a"]:                
                content[section_title] = content[section_title]+f"\n{sibling.get_text(strip=True)}"
            else:
                pass    
    
    return content