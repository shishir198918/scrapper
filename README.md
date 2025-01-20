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
    "title": "title of content",
    "List of content":['Content1','Content2','Content3'...'ContentN']
}
```

