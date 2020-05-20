import os

if 'TRAVIS' in os.environ:
    

    if os.environ.get('IS_HEROKU') == True:
        import django_heroku

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'xy4(+@z$0sea7g=i#%w+^u5c3dlk2m7!e3h0dm5nj!=y!tpsio'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []


    # Application definition

    INSTALLED_APPS = [
        "todo.apps.TodoConfig",
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'allauth', # new
        'allauth.account', # new
        'allauth.socialaccount', # new
        'allauth.socialaccount.providers.google',
        'django.contrib.sites',
        'pages',
        'users', 
        'main',
        'social_django', 
        'weather',
        'calendarApp.apps.CalendarappConfig',
        'gpa.apps.GpaConfig',
        'bootstrap4', # for gpa module
    ]

    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
        'social_core.backends.twitter.TwitterOAuth',
        'social_core.backends.facebook.FacebookOAuth2',
    )

    SITE_ID = 1

    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False

    AUTH_USER_MODEL = 'users.CustomUser'
    LOGIN_REDIRECT_URL = 'home'
    LOGOUT_REDIRECT_URL = 'home'

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'social_django.middleware.SocialAuthExceptionMiddleware',
    ]

    ROOT_URLCONF = 'dashboard.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS':[os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'social_django.context_processors.backends', 
                    'social_django.context_processors.login_redirect', 
                ],
            },
        },
        
    ]

    WSGI_APPLICATION = 'dashboard.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

    if os.environ.get('IS_HEROKU') == True:
        import dj_database_url
        DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }


    # Password validation
    # https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]


    # Internationalization
    # https://docs.djangoproject.com/en/3.0/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    #Facebook API LOGIN OATH
    SOCIAL_AUTH_FACEBOOK_KEY = '259905795014698'      # App ID
    SOCIAL_AUTH_FACEBOOK_SECRET = '2c511f8bf96aa396f45a16b3c0823467' # App Secret

    #Twitter API Login Oath
    SOCIAL_AUTH_TWITTER_KEY = 'URi9HvMcXFx5kyhUOHKZIaEaX'
    SOCIAL_AUTH_TWITTER_SECRET = 'v70G2LuSYT7092V4ZS9Uu6iaTZB9RXRLfSFsC9Hf2FS99VG2Y8'
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.0/howto/static-files/

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    # Activate Django-Heroku.
    if os.environ.get('IS_HEROKU') == True:
        django_heroku.settings(locals())

else:
    import django_heroku

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    # Moved to DB section

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []


    # Application definition

    INSTALLED_APPS = [
        "todo.apps.TodoConfig",
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'allauth', # new
        'allauth.account', # new
        'allauth.socialaccount', # new
        'allauth.socialaccount.providers.google',
        'django.contrib.sites',
        'pages',
        'users', 
        'main',
        'social_django', 
        'weather',
        'calendarApp.apps.CalendarappConfig',
        'gpa.apps.GpaConfig',
        'bootstrap4', # for gpa module
    ]

    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
        'social_core.backends.twitter.TwitterOAuth',
        'social_core.backends.facebook.FacebookOAuth2',
    )

    SITE_ID = 1

    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False

    AUTH_USER_MODEL = 'users.CustomUser'
    LOGIN_REDIRECT_URL = 'home'
    LOGOUT_REDIRECT_URL = 'home'

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'social_django.middleware.SocialAuthExceptionMiddleware',
    ]

    ROOT_URLCONF = 'dashboard.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS':[os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'social_django.context_processors.backends', 
                    'social_django.context_processors.login_redirect', 
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'dashboard.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

    if os.environ.get('IS_HEROKU') == True:
        SECRET_KEY = os.environ["SECRET_KEY"] 
        import dj_database_url
        DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    
    else:
        SECRET_KEY = 'xy4(+@z$0sea7g=i#%w+^u5c3dlk2m7!e3h0dm5nj!=y!tpsio'
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }


    # Password validation
    # https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]


    # Internationalization
    # https://docs.djangoproject.com/en/3.0/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

   
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.0/howto/static-files/

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    # Activate Django-Heroku.
    django_heroku.settings(locals())
