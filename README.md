#Web Scrapper API documentation
----------------------------------
This API retrieving a text data from web-page 
-------------------------------------------------------------------------
##1-Get metadata for a webpage

Endpoint: "GET /metadata/?url=% %"

Parameter:URL(url of webpage)

Response:(JSON)
```json
{
"crawler":{
    "@context": "http://schema.org",
    "@type": "NewsArticle",
    "author": {
      "@type": "Person",
      "name": "Ahmad Farag",
      "url": "https://medium.com/@ahmadfarag"
    },
    "creator": [
      "Ahmad Farag"
    ],
    "dateCreated": "2018-03-31T09:27:42.135Z",
    "dateModified": "2018-07-23T16:55:25.543Z",
    "datePublished": "2018-03-31T09:27:42.135Z",
    "description": "From 1989, Tim Berners-Lee and his team at CERN , the European Nuclear Research Center in Switzerland, developed the Hypertext Transfer Protocol, together with the concepts of URL and HTML , which…",
    "headline": "HTTP In Depth - Ahmad Farag - Medium",
    "identifier": "dfdac806c2c0",
    "image": [
      "https://miro.medium.com/v2/resize:fit:1200/1*fFgr7pu2_c4jbKqULD2ahw.png"
    ],
    "mainEntityOfPage": "https://medium.com/@ahmadfarag/http-in-depth-dfdac806c2c0",
    "name": "HTTP In Depth - Ahmad Farag - Medium",
    "publisher": {
      "@type": "Organization",
      "logo": {
        "@type": "ImageObject",
        "height": 60,
        "url": "https://miro.medium.com/v2/resize:fit:544/7*V1_7XP4snlmqrc_0Njontw.png",
        "width": 272
      },
      "name": "Medium",
      "url": "https://medium.com/"
    },
    "url": "https://medium.com/@ahmadfarag/http-in-depth-dfdac806c2c0"
  }
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










