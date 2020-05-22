# project-103-dashboard-devs
project-103-dashboard-devs created by GitHub Classroom

Live site can be found here: https://dashboard-devs-t.herokuapp.com/

MyDash was created by @TildenWinston, @Don-Joel, @cfrymire98, and @simonmli for UVA CS3240. The goal was to create a dashboard for students that puts useful information in a single central location. The dashboard has four modules, weather, calendar, to-do list, and GPA calculator. The version here is the same as the final submitted version with the following major improvements:
* Site lands on proper dashboard page, not the todo module
  * Todo and dashboard URLs switched back to how they should be. Originally, the page located at /dashboard/ was from the todo module with the contents of the dashboard page
* The Todo list box on the dashboard page is now an iframe
  * Long todo lists have a scroll bar
* dashboard page can no longer be viewed when not logged-in
* API keys and other secrets have been properly removed and replaced
* /Todo/ was updated to match styling of weather

Other issues have also been fixed, but more, such as inconsistant styling with the calendar and GPA modules, still exist.


# Architecture
The website is written using Django and hosted on Heroku.


