# How to set up your environment

1. Clone the repository.
2. Make a file called .env in the "src" folder, using .env.debug as a template. Do not change anything except allowed hosts and secret key.
3. Install all the packages in src/requirements.txt using pip. Set up a virtual environment before this, if you like.
4. Change into the "src" folder using ```cd src/```.
5. Run ```python manage.py migrate```.
6. You can now use the command ```python manage.py runserver```, and your website will be accessible on http://localhost:8000