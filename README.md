# The Better Boulder Bureau
The Better Boulder Bureau (TBBB) helps rock climbers find outdoor places to boulder around the Bay Area. It allows users to search for climbing locations and specific routes by name, as well as displaying all current locations on a map.  TBBB keeps track of site specific information, such as directions, descriptions, latitude and longitude and route difficulty. Users can add a star rating and comments on a particular route or boulder.  Users are able to keep track of the routes they have rated on their dashboard.


## Table of Contents
* [Technologies Used](#technologiesused)
* [How to use The Better Boulder Bureau](#use)

## <a name="technologiesused"></a>Technologies Used

* Python
* Flask
* Postgres SQL
* SQL Alchemy
* JavaScript
* jQuery
* HTML
* CSS
* Bootstrap
* AJAX/JSON
* Jinja2
* Chart.js
* MapBox API
* rateYo.js
* import.io


## <a name="use"></a>How to use The Better Boulder Bureau

###When the main page loads all bouldering locations
All locations will appear as clusters of map pins.
Click on a pin to see the name of the location.
 
![The Better Boulder Bureau Main page](/static/main_page.png)

###Searching for the name of a location
Search results will appear as clusters of map pins.
Non-mappable locations will be listed on the side.
Click on a pin to see the name of the location.

![The Better Boulder Bureau Search](/static/main_page_search.png)
![The Better Boulder Bureau Map Flag](/static/map_flag.png)

###The Boulder Page
The Boulder page shows the location plotted on a map
It also show a graph of the difficulty rating break down of all the climbing routes for that boulder.
For a user that is not logged in Boulder star ratings shown are the average star rating and is shown in green.

![The Better Boulder Bureau Boulder page](/static/boulder_page_1.png)

There is also location specific information about the boulder as well as the names and ratings of it's climbing routes.

![The Better Boulder Bureau Boulder page](/static/boulder_page_2.png)

Comments the users have entered about the location are listed at the bottom.

![The Better Boulder Bureau Boulder page](/static/boulder_page_3.png)

###The Route Page
Shows route specific information as well as other routes that are on the same boulder. 
It will also list if there are any other near by boulders.
Any user comments will also appear.

![The Better Boulder Bureau Route page](/static/route_page.png)

###The User Page
When a user has logged in they are taken to their user page.
On the user page they can search for locations.

![The Better Boulder Bureau User page](/static/user_page_1.png)

They also can see a table of all the climbing routes they have completed.

![The Better Boulder Bureau User page](/static/user_page_2.png)

###The Boulder Page 'User View'
When a user is logged in they have the ability to rate the location or add comments.
If they have not rated the particulare location they will see the average rating for that location, also in green.

![The Better Boulder Bureau User View Boulder page ](/static/user_view_boulder.png)

###The Route Page 'User View'
When a user is logged in they have the ability to rate the route or add comments.
If they have rated the climbing route they will see their rating for that location, also in blue.

![The Better Boulder Bureau User View Route page ](/static/user_view_route.png)

## <a name="author"></a>Author
Aiden Ward is a software engineer in San Francisco, CA.