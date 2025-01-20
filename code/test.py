from urllib.request import urlopen


def connection(url):
    page=urlopen(url) #return response object
    html_bytes=page.read()
    print(html_bytes)
    html=html_bytes.decode("utf-8")
    return html


url="https://en.wikipedia.org/wiki/Web_scraping"
page=connection(url)