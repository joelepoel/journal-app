journal-app

This is a Django-based journal application that allows users to create, edit, and delete journal entries. Each entry includes a title, description, and optional/default image. Entries are automatically ordered by date of creation.


Features

- Add, edit, and delete journal entries
- Each entry includes:
  - Title
  - Description
  - Image (optional)
- Entries ordered by date
- Custom user model (overrides Django's default)
- Profile model automatically created after user registration via Django signals


Setup Instructions

1. Clone the repository

   git clone https://github.com/yourusername/journal-project.git
   cd journal-project

2. Install dependencies using Pipenv and running:

    pipenv install
    pipenv shell

3. Create and configure your MySQL database

    Manually create a MySQL database.

    Open settings.py and update the DATABASES section with your MySQL credentials.

4. Make migrations and apply migrations by running:

    python manage.py makemigrations

    python manage.py migrate

5. (Optional) Create a superuser for admin access by running:

    python manage.py createsuperuser

6. Ensure media folder is set up

    By default, the app uses a media folder for uploaded images.

    Create a media/ directory in your project root, or update MEDIA_ROOT and MEDIA_URL in settings.py as needed.

    The Entry and Profile models will take default images from 'media/defaults/' called 'entry.jpg' and 'avatar.jpg'.

7. Run the development server by running:

    python manage.py runserver

    Access the application

        Visit http://127.0.0.1:8000/ in your browser.

Notes

    This project uses Pipenv for dependency management. Python and Django versions are handled automatically through the Pipfile.

    Uploaded images will be saved in the media/ folder unless configured otherwise.