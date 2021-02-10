import requests as re
import json
def  getMovieTitles(substr):
    url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title='
    result = re.get(url+substr)
    data = result.json()
    every = []
    final = []
    
    r = data['total_pages']
     
    for data in data['data']:
        every.append(data['Title'])
    
    
    for i in range(2,(r+1)):
        url ='https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}'.format(substr,i )
        result = re.get(url)
        data = result.json()
        for data in data['data']:
            every.append(data['Title'])
    every = sorted(every)
    substr = substr.title()
    print(substr+'is a fish')
    print(every)
    for ever in every:
        print(ever)
        if substr in ever:
            final.append(ever)
    print(final)

getMovieTitles('spiderman')
