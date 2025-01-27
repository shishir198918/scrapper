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
    "error": "The request could not be understood by the server due to    malformed syntax. The client SHOULD NOT repeat the request without
   modifications"
}
```
**status**: `400 Bad request`


```json
{
    "error": "The server has not found anything matching the Request-URI. No indication is given of whether the condition is temporary or
   permanent."
}
```
**status**: `404 Not Found`


```json
{
    "error": "The server understood the request, but is refusing to fulfill it.Authorization will not help and the request SHOULD NOT be repeated. And reason can mention"
}
```
**status**: `403 Forbidden`


```json
{
    "error": "The server is refusing to process a request because the request entity is larger than the server is willing or able to process. The server MAY close the connection to prevent the client from continuing the request"
}
```
**status**: `413 Request Entity Too Large`


```json
{
    "error": "The server is refusing to service the request because the Request-URI
   is longer than the server is willing to interpret. This rare
   condition is only likely to occur when a client has improperly
   converted a POST request to a GET request with long query
   information, when the client has descended into a URI 'black hole' of
   redirection (e.g., a redirected URI prefix that points to a suffix of
   itself), or when the server is under attack by a client attempting to
   exploit security holes present in some servers using fixed-length
   buffers for reading or manipulating the Request-URI."
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
    "error": "The server does not support the functionality required to fulfill the request. This is the appropriate response when the server does not recognize the request method and is not capable of supporting it for any resource."
}
```
**status**: `501 Not Implemented`


```json
{
    "error": "The server does not support, or refuses to support, the HTTP protocol
   version that was used in the request message. The server is
   indicating that it is unable or unwilling to complete the request
   using the same major version as the client, other than with this error message. The response SHOULD contain an entity describing why that version is not supported and what other protocols are supported by that server."
}
```
**status**: `505 HTTP Version Not Supported`




