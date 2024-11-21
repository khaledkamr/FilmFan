# FilmFan

FilmFan is a full-stack web application designed for movie and TV show enthusiasts to discover, rate, and review their favorite films and series. Inspired by platforms like IMDb, FilmFan aims to provide users with an engaging and interactive experience where they can explore featured movies, view new arrivals, stay updated with the latest news in the entertainment industry, and contribute their own ratings and reviews.

## Features

### General Features
- **Home Page**: Showcases featured movies and TV shows, highlighting the top-rated and most popular entries.
- **Movies Page**: Displays all the movies in the server.
- **TV Shows Page**: Displays all the TV shows in the server.
- **New Arrivals**: Displays the latest movies and TV shows added to the platform.
- **News Section**: Provides the latest news and updates about movies, TV shows, and the entertainment industry.
- **Sign up/ Sign in**: user can create his own account on the website and can login with it any time.

### Movie/TV Show Details
- **Detailed Information**: Includes comprehensive details about each movie or TV show, such as synopsis, release date, genres, and cast & crew information.
- **Rating and Reviews**: Displays the average rating and user reviews for each movie or TV show.
- **Cast & Crew**: Lists the stars and writers involved in the production.
- **User Ratings**: Registered users can rate movies and TV shows.

## Technologies Used

### Front-end
- **HTML/CSS**: For structuring and styling the web pages.
- **JavaScript**: For enhancing user interactions and dynamic content loading.

### Back-end
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
  - **Django Views**: Handle the logic for displaying the appropriate data and templates based on user requests.
  - **Django Templates**: Render HTML pages dynamically using Django's templating engine.
  - **Django Admin**: Provides a built-in interface for managing the database entries and user data.

### Database
- **SQLite**: The default database for Django, used for storing all the application data including user information, movie and TV show details, ratings, and reviews.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/khaledkamr/FilmFan.git
   cd FilmFan
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   pip install virtualenv
   virtualenv venv
   venv/Scripts/activate
   ```

3. **Install Django:**
   ```bash
   pip3 install Django
   ```

4. **Apply the migrations:**
   ```bash
   py manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   py manage.py runserver
   ```

6. **Access the application:**
   
   Open your web browser and navigate to `http://127.0.0.1:8000/` .
