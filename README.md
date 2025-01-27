#Web Scrapper API documentation
----------------------------------
This API retrieving a text data from web-page 
-------------------------------------------------------------------------
##1-Get metadata for a webpage

Endpoint: "GET /metadata?url=% %"

Parameter:URL(url of webpage)

Response:(JSON)
```json
{
"metadata" :   {
    "title": "title of Webpage",
    "List of content":["Content1","Content2","Content3","...""ContentN"]
    }
}
```

**errors**:

**status**: `400 Bad request`
```json
{
    "error": "Malformed URL,changes require"
}
```


**status**: `404 Not Found`
```json
{
    "error": "Server did not found any valid page."
}
```


**status**: `403 Forbidden`
```json
{
    "error": "Authorization required for Page"
}
```



**status**: `413 Request Entity Too Large`
```json
{
    "error": "URL is too long to proceed"
}
```

**status**: `500 Internal Server Error`
```json
{
    "error": "The server encountered an unexpected condition which prevented it from fulfilling the request"
}
```

##2-Get text content for webpage

Endpoint: "GET /content?url=% %"

Parameter:URL(url of webpage)

Response:(JSON)
```json
{
 "content" :  {
 "title":"title of Webpage",
 "Content 1":"Text in content",
 "Content 2":"Text in content 2"

}
}
```
**errors**:

**status**: `400 Bad request`
```json
{
    "error": "Malformed URL,changes require"
}
```


**status**: `404 Not Found`
```json
{
    "error": "Server did not found any valid page."
}
```


**status**: `403 Forbidden`
```json
{
    "error": "Authorization required for Page"
}
```



**status**: `413 Request Entity Too Large`
```json
{
    "error": "URL is too long to proceed"
}
```

**status**: `500 Internal Server Error`
```json
{
    "error": "The server encountered an unexpected condition which prevented it from fulfilling the request"
}
```










