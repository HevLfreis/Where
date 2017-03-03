# Where
Where is a web service to simulate finding nearest cars of taxi booking apps  
Location: http://where.seeleit.com/  

***

## What is this ?
Where is a web service to simulate finding nearest cars of taxi booking apps. Considering that we have an NxN grid, some points of the grid have already placed taxis. You are on one certain point on the grid and we'd like to find which taxi is the nearest to your location.

## How to use
I provide two ways to access the service:  
1. GET  
Example:  `http://where.seeleit.com/?lng=100&lat=100`  
2. POST  
In post method, your data in post request must contain the following two values: `{'lng': 100, 'lat':100}`  

### Deployed Environment
Server: Aliyun Ubuntu14.04, Core: 2, RAM: 4G
