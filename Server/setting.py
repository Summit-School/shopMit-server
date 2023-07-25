# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'submit',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',  # Use 'localhost' if the database is on the same machine.
        'PORT': '8080',  # Default MySQL port is usually 3306.
    }
}
