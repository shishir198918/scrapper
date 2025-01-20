#Web Scrapper API documentation
----------------------------------
This API retiving a text data from wikipedia or similar structure website
-------------------------------------------------------------------------
##1-Get text data from website

Endpoint: GET/text_content

Parameter:URL(wikipedia)

Response:(JSON)
{
    {'Title':title1 },
    {'List of content':Content1,content2,content3,...contentn},
    {'Content1':Text of content1},
    {'content2':Text of content2},
    .
    .
    .
    {'Content n':Text of Content n }
}
