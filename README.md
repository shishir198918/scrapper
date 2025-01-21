#Web Scrapper API documentation
----------------------------------
This API retrieving a text data from web-page 
-------------------------------------------------------------------------
##1-Get metadata for a webpage

Endpoint: "GET /metadata?url=% %"

Parameter:URL(url of webpage)

Response:(JSON)
```json
metadata{
    {
    "title": "title of Webpage",
    "List of content":["Content1","Content2","Content3","...""ContentN"]
    }
}
```

##2-Get text content for webpage

Endpoint: "GET /content?url=% %"

Parameter:URL(url of webpage)

Response:(JSON)
```json
content{
    {
 "title":"title of Webpage",
 "Content 1":"Text in content",
 "Content 2":"Text in content 2"

}
}
```


