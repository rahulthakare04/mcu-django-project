# MCU Django Project

This Django project is designed for Marvel Cinematic Universe (MCU) fans, providing information on movies, superheroes, fan stories, and more. It integrates MySQL and MongoDB for data storage and management.

## Project Overview
This project allows users to:
- View Marvel movies in sequence
- Search for Marvel superheroes
- Create their own superheroes
- Download Marvel movies
- Read fan stories
- Check upcoming Marvel movies

### Technologies Used
- **Django** - Web framework for Python
- **MySQL & MongoDB** - Databases for structured and unstructured data
- **HTML, CSS, JavaScript (AJAX), Bootstrap** - Frontend design

---
## Database Schema (MySQL Tables & MongoDB Collection)
This project uses MySQL for structured data and MongoDB for dynamic content. Below is the schema:

### MySQL Tables
#### Upcoming Marvel Movies
```sql
CREATE TABLE Upcoming_Marvel_Movies (
    MovieID INT NOT NULL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    ReleaseDate DATE NOT NULL,
    Director VARCHAR(255)
);
```

#### Fan Stories
```sql
CREATE TABLE fan_stories (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Movie Sequence
```sql
CREATE TABLE movie_sequence (
    movie_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    movie_name VARCHAR(255) NOT NULL,
    release_year YEAR NOT NULL,
    director VARCHAR(255) NOT NULL,
    imdb_rating DECIMAL(3,1) NOT NULL
);
```

#### Superheroes
```sql
CREATE TABLE superheroes (
    hero_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    hero_name VARCHAR(255) NOT NULL,
    real_name VARCHAR(255) NOT NULL,
    title VARCHAR(255),
    origin_story TEXT NOT NULL,
    species VARCHAR(100) NOT NULL,
    superpowers TEXT NOT NULL,
    weakness TEXT NOT NULL,
    gadgets TEXT,
    team VARCHAR(255),
    description TEXT NOT NULL,
    image_url VARCHAR(255)
);
```

### MongoDB (All Movies Collection in `marvel_projectdb`)
```json
[
  {
    "name": "Iron Man",
    "release_year": 2008,
    "download_url": "https://pixeldra.in/api/file/SSYC88zs?download",
    "image_url": "https://rukminim2.flixcart.com/image/850/1000/xif0q/poster/0/d/d/small-spos8825-poster-iron-man-1-a-official-sticker-sl-9829-wall-original-imaghs5pygznwxu9.jpeg?q=20&crop=false"
  },
  {
    "name": "Captain America",
    "release_year": 2011,
    "download_url": "https://pixeldra.in/api/file/r8HAqSqF?download",
    "image_url": "https://m.media-amazon.com/images/I/81U9EbWexxL.jpg"
  },
  {
    "name": "Thor",
    "release_year": 2011,
    "download_url": "https://pixeldra.in/api/file/ruqr15kn?download",
    "image_url": "https://rukminim2.flixcart.com/image/850/1000/k5wse4w0/poster/u/b/a/medium-artistic-movie-poster-thor-marvel-movie-poster-for-room-original-imafzgvb2xt8ptzx.jpeg?q=90&crop=false"
  }
]
```

---
## CRUD Operations Performed
This project supports the following operations:

1. **Add Movie (INSERT)** - Users can add new movies.
2. **View All Movies (SELECT)** - Displays a list of all movies.
3. **Search by Genre/Release Year (SEARCH)** - Filters movies based on queries.
4. **Update Movie Details (UPDATE)** - Allows modification of existing data.
5. **Delete Movie (DELETE)** - Removes a record from the database.

---
## Video Execution of the Project
Below is a demonstration of the project in action:

### Django-Flask Project
![Project Screenshot](image.png)

🎬 **Video:** [Django-Flask Project](Django-Flask.Project.mp4)

---
## How to Run the Project
1. Clone this repository:
```sh
git clone https://github.com/your-username/mcu-django-project.git
cd mcu-django-project
```
2. Activate the virtual environment:
```sh
cd env
cd Scripts
activate
```
3. Run the Django server:
```sh
python manage.py runserver
```
4. Open `http://127.0.0.1:8000/` in your browser to use the application.

---
## Done!
This completes the setup and execution of the MCU Django project. 🚀

Feel free to contribute, suggest improvements, or report issues!

