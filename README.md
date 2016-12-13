
# StringsAPI
It's a simple app wrote for fun which implements a below task.

## Task (this are requirements) 
Fun with Strings API
    
We are running a service which allows to have a lot of fun with strings.
To gain more customers we want to create an API to allow others to integrate it in their own applications.
    
The service supports following operations on strings which we want to expose over a RESTful API:
- get a random word (via Public API http://www.setgetgo.com/randomword/)
- return content of Wikipedia article about given word (https://www.mediawiki.org/wiki/API:Main_page)
- collect statistic for most popular words submitted to previous operation and return top N, where N is provided by user
- (optional) given a first and/or a last name as parameter, return a random joke from external API (http://www.icndb.com/api/),
if no name is provided, a Chuck Norris joke is returned
- (optional) perform a spell check on a given string via calling some external API for spell checking
    
Scope of the task:
- provide the implementation for the operations on strings
- create API endpoint(s) to expose all the operations
- design corresponding request/response format (XML, JSON etc.)
- it is enough to use simple data structure for statistic collection, no need to involve any data-store
- API should handle errors properly and return meaningful response to the user
- (optional) user authorization for our API
- no frameworks (especially no Django). Only bottle + request/gevent can be used


## How to run this app?
First, you need to install all required 3rd libs. In order to do please call below command:
```
pip install -r requirements.txt
```

Next, run app using below command:
```
python start.py
```

and you should see in console something like this:
```
Bottle v0.12.10 server starting up (using WSGIRefServer())...
Listening on http://localhost:8080/
Hit Ctrl-C to quit.
```
It's mean, server is up and running! Kudos for you!

## Error handling
All occurred errors should be served as it's presented below:
```
HTTP/1.0 400 Bad Request
Date: Tue, 13 Dec 2016 20:38:46 GMT
Server: WSGIServer/0.1 Python/2.7.10
Content-Length: 62
Content-Type: application/json

{
    "error_type": "TypeError",
    "error": "an integer is required"
}
```

## API endpoints

### Random word
This endpoint returns a meaning of random word fetched from Wikipedia in JSON format.

```
/random_word
```

+ Response 200 OK
```
{
    definition: "From an alternative name: This is a redirect from a title that is another name such as a pseudonym, a nickname, or a synonym of the target, or of a name associated with the target.",
    word: "cercarian",
    article_content: "The page you specified doesn't exist"
}
```

#### cURL request example
```
curl -i -H "Content-Type: application/json" -XGET "http://localhost:8080/random_word"
```

### Statistics
This endpoint returns a statistic of most popular randomly selected words.

```
/statistic/<limit:int>
```

+ Response 200 OK
```
{
    "statistic": {
        "crucify": 2,
        "gloriousness": 1,
        "lipography": 1,
        "microchromosome": 1
    }
}
```

### cURL request example
```
curl -i -H "Content-Type: application/json" -XGET "http://localhost:8080/statistic/10"
```


### Joke
This endpoint returns a random joke fetched from icndb.com

```
/joke?first_name=<string>&last_name=<string>
```
all request params are optional.

+ Response 200 OK
```
{
    "text": "Chuck Norris cannot love, he can only not kill."
}
```

### cURL request example
```
curl -i -H "Content-Type: application/json" -XGET "http://localhost:8080/joke"
```
