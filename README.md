# Dgango Blog App

## Description
This Django-based blog app allows users to create, edit, and view blog posts. It features user authentication, post management, and a clean, responsive UI.

## Features
- User Authentication (Sign up, Log in, Log out)
- Create, Edit, and Delete Posts
- Rich Text Editor for Post Creation
- Commenting System
- User Profile Management

## Installation

### Prerequisites
- Python 3.x
- Django 3.x

### Setup
1. **Clone the Repository**
    ```bash
    git clone [https://github.com/sweetscripts/Django-Blog]
    cd blog-app
    ```

2. **Create a Virtual Environment (Optional)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Initialize Database**
    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser (Optional)**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Server**
    ```bash
    python manage.py runserver
    ```

## Usage
After running the server, access the application at `http://127.0.0.1:8000/`. Use the admin panel at `http://127.0.0.1:8000/admin/` to manage the blog.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
Thank you Corey Schafer!

