#Web Scrapper API documentation
----------------------------------
This API retrieving a text data from web-page 
-------------------------------------------------------------------------
##1-Get metadata for a webpage

Endpoint: "GET /metadata"

Parameter:URL(url of webpage)

Response:(JSON)
```json
{
    "title": "title of Webpage",
    "List of content":["Content1","Content2","Content3","...""ContentN"]
}
```

##2-Get text content for webpage

Endpoint: "GET /content"

Parameter:URL(url of webpage)

Response:(JSON)
```json
{
 "title":"title of Webpage",
 "Content 1":"Text in content",
 "Content 2":"Text in content 2"

}
```
##3-Get image links

Endpoints: "GET/images"

Parameter:URL(url of webpage)

Response:(JSON)
```json
{
    "image1":"link of image 1",
    "image2":"link of image 2",
    "image3":"link of image 3"

}
```


