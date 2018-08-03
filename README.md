# RoutesOptimizer

A Python Script that find alternative routes based on certain features
Specify which restaurant you want the most on the path. 
The algorithm will pick the path that has the most specified shop.
Very accurate results but is the algorithm is a little slow. O(N^2)

If the same shop is within 10 km of each other it will not inlude it in the shop frequency

## Tools
Yelp Search API

Google Map API

Zipcode Searcher

## Details
Finds the correct Route without add too much time to the route beacuase the lat and long of direction change
You can change after how many miles does the algorithm look. The samller the mile value, the faster the program

## Future
Going to add a option that finds the path with best weather Ex: path without storms, rain, etc.

