Project Overview
This project demonstrates a simple movie (or project) rating website built using Django and Docker.
Users can browse a list of movies, submit a 1-5 star rating for each movie, and view rating statistics such as the average score and rating details.

Key Components and Features
1. Model Structure (/movies/models.py)
Movie Model: Stores the title, description, and creation date of each movie. Provides a method to calculate the average score from related ratings.

Rating Model: Stores user ratings (1-5 stars) for each movie. Linked to the Movie model via a ForeignKey relationship (1:N).

2. Admin Page (/movies/admin.py)
MovieAdmin: Displays movies in the admin list view, showing title, average score, and creation date, sorted by average score in descending order.

RatingAdmin: Shows each rating entry with the associated movie, score, and date.

3. URL Routing (/movies/urls.py)
Movie list: /

Movie detail: /movie/<pk>/

Submit rating: /movie/<pk>/rate/

Rating result: /movie/<pk>/result/

4. View Functions (/movies/views.py)
Handles displaying the movie list, movie details, submitting ratings, and viewing results/statistics.

5. Templates
Provides user interfaces for the movie list, detail pages, rating submission form, and rating result views.

6. Docker Setup (/Dockerfile)
Uses a Python 3.10 base image.

Installs dependencies from requirements.txt.

Copies the project source code and runs the Django server.

