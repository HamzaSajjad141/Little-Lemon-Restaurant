# Little Lemon Restaurant 🍋

Welcome to the Little Lemon Restaurant Django web project! This project is designed to showcase a simple restaurant website with features like booking, menu display, and more. 

![Screenshot 2024-03-01 204145](https://github.com/HamzaSajjad141/Little-Lemon-Restaurant/assets/125465047/5f6fcefc-9916-434c-90d8-cbb1bc225ad3)


## Project Structure 📂

- **Project Name**: Little Lemon
- **App Name**: Restaurant

### Code Files 🖥️
- **`settings.py`**: Django settings file with configurations for the project.
- **`urls.py`**: URL configuration for routing requests to views.
- **`wsgi.py`**: WSGI configuration for deployment.

### App Files 🍽️
- **`models.py`**: Defines two models - `Booking` and `Menu`.
- **`admin.py`**: Registers models with the Django admin panel.
- **`apps.py`**: Configuration for the restaurant app.
- **`forms.py`**: Defines a form for booking.
- **`urls.py`**: URL patterns for the restaurant app.
- **`views.py`**: Contains views for rendering different pages.

### Templates 📄
- **`templates` folder**: Contains HTML templates for various pages:
  - `about.html`
  - `base.html`
  - `book.html`
  - `index.html`
  - `menu.html`
  - `menu_item.html`
  - `_footer.html`
  - `_header.html`

### Static Files 🎨
- **`static` folder**: Contains static files like CSS, images, etc.
  - `css/style.css`: Stylesheet for the website.
  - `image/`: Folder for images used in the project.
 
## Configuration ⚙️

- **Database:** SQLite3 is used by default. You can configure this in the `DATABASES` section of `settings.py`.
- **Static Files:** The project is configured to serve static files from the `restaurant/static/` directory.
- **Media Files:** Media files (e.g., uploaded images) are served from the `/media/` URL.

## Features 🌟

- **Home**: Welcome page introducing the restaurant.
- **About**: Learn more about Little Lemon Restaurant.
- **Book**: Reserve a table by filling out a booking form.
- **Menu**: Explore the delicious offerings on the menu.
- **Menu Item**: Detailed view of a specific menu item.

## Getting Started 🚀

1. Clone the repository: `git clone https://github.com/HamzaSajjad141/Little-Lemon-Restaurant.git`
2. Virtual Environmenta and Setup : 👉 [Click Here](https://github.com/HamzaSajjad141/Django-VirtualEnvironment-Setup)
3. Apply database migrations: `python manage.py makemigrations` then `python manage.py migrate`
5. Run the development server: `python manage.py runserver`
6. Access the website at `http://localhost:8000/`

Feel free to customize and enhance the project according to your preferences! Enjoy creating and managing your Little Lemon Restaurant. 🍽️🍹
