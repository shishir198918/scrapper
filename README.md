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

```json
{
    "error": "Malformed syntax,changes require"
}
```
**status**: `400 Bad request`


```json
{
    "error": "Server not found any HTML."
}
```
**status**: `404 Not Found`


```json
{
    "error": "Could not Scrap for URI"
}
```
**status**: `403 Forbidden`


```json
{
    "error": "URL is too long to proceed"
}
```
**status**: `413 Request Entity Too Large`


```json
{
    "error": "Request-URI Too Long"
}
```
**status**: `414 Request-URI Too Long`


```json
{
    "error": "The server encountered an unexpected condition which prevented it from fulfilling the request"
}
```
**status**: `500 Internal Server Error`


```json
{
    "error": "Response only define for GET ."
}
```
**status**: `501 Not Implemented`


```json
{
    "error": "Only support HTTP/1.1 and HTTPS."
}
```
**status**: `505 HTTP Version Not Supported`




