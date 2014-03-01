"""
Django settings for register project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*lkip1l2_sage3m$0py$-_ij2=t@(!g&42#j+a53tp71fcs5xk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

#Project specific apps
    'locations',
    'sports',
    'user_profiles',
    'teams',
    'bugger',
    'leaps',




#External apps
    'csvimport',
    'south',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'bootstrapform',
    'bootstrap3_datetime',


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'boundis.urls'

WSGI_APPLICATION = 'boundis.wsgi.application'

# -----Authentication and other allauth settings ----------
# http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend"
)
 
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)
 
# auth and allauth settings
LOGIN_REDIRECT_URL = '/profile/myprofile'
LOGIN_URL = '/accounts/login'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'SCOPE': ['email', 'publish_stream'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': False}}

SITE_ID=1

#ACCOUNT_AUTHENTICATION_METHOD ="username" or "email"
ACCOUNT_CONFIRM_EMAIL_ON_GET =False

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
'''The URL to redirect to after a successful e-mail confirmation, in case no
  user is logged in.'''

ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL=None
''' The URL to redirect to after a successful e-mail confirmation, in
  case of an authenticated user. Set to `None` to use
  `settings.LOGIN_REDIRECT_URL`.'''

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
  #Determines the expiration date of email confirmation mails (# of days).

ACCOUNT_EMAIL_REQUIRED =True
  #The user is required to hand over an e-mail address when signing up.

ACCOUNT_EMAIL_VERIFICATION ="mandatory"
'''Determines the e-mail verification method during signup -- choose
  one of `"mandatory"`, `"optional"`, or `"none"`. When set to
  "mandatory" the user is blocked from logging in until the email
  address is verified. Choose "optional" or "none" to allow logins
  with an unverified e-mail address. In case of "optional", the e-mail
  verification mail is still sent, whereas in case of "none" no e-mail
  verification mails are sent.'''

ACCOUNT_EMAIL_SUBJECT_PREFIX ="Boundis.com "
'''Subject-line prefix to use for email messages sent. By default, the
  name of the current `Site` (`django.contrib.sites`) is used.'''

ACCOUNT_LOGOUT_ON_GET =False
'''Determines whether or not the user is automatically logged out by a
  mere GET request. See documentation for the `LogoutView` for
  details.'''

ACCOUNT_LOGOUT_REDIRECT_URL ="/accounts/login"
'''The URL (or URL name) to return to after the user logs out. This is
  the counterpart to Django `LOGIN_REDIRECT_URL`.'''

#ACCOUNT_SIGNUP_FORM_CLASS ='user_profiles.forms.SignupForm'
'''A string pointing to a custom form class
  (e.g. 'myapp.forms.SignupForm') that is used during signup to ask
  the user for additional input (e.g. newsletter signup, birth
  date). This class should implement a `def save(self, request, user)`
  method, where user represents the newly signed up user.'''

ACCOUNT_SIGNUP_PASSWORD_VERIFICATION =True
  #When signing up, let the user type in his password twice to avoid typ-o's.

ACCOUNT_UNIQUE_EMAIL =True
  #Enforce uniqueness of e-mail addresses.

#ACCOUNT_USER_MODEL_USERNAME_FIELD ="username"
'''The name of the field containing the `username`, if any. See custom
  user models.'''

ACCOUNT_USER_MODEL_EMAIL_FIELD ="email"
'''The name of the field containing the `email`, if any. See custom
  user models.'''

#ACCOUNT_USER_DISPLAY ="user.username"
'''A callable (or string of the form `'some.module.callable_name'`)
  that takes a user as its only argument and returns the display name
  of the user. The default implementation returns `user.username`.'''

ACCOUNT_USERNAME_MIN_LENGTH =3
  #An integer specifying the minimum allowed length of a username.

ACCOUNT_USERNAME_BLACKLIST =['fuck', 'shit', 'cunt', 'penis','vagina',]
  # list of usernames that can't be used by user.

ACCOUNT_USERNAME_REQUIRED =True
'''The user is required to enter a username when signing up. Note that
  the user will be asked to do so even if
  `ACCOUNT_AUTHENTICATION_METHOD` is set to `email`. Set to `False`
  when you do not wish to prompt the user to enter a username.'''

ACCOUNT_PASSWORD_INPUT_RENDER_VALUE =False
  #`render_value` parameter as passed to `PasswordInput` fields.

ACCOUNT_PASSWORD_MIN_LENGTH =6
  #An integer specifying the minimum password length.

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION =True
'''The default behaviour is to automatically log the user in once he confirms
  his email address. By changing this setting to False he will not be logged
  in, but redirected to the ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL'''

SOCIALACCOUNT_ADAPTER ="allauth.socialaccount.adapter.DefaultSocialAccountAdapter"
'''Specifies the adapter class to use, allowing you to alter certain
  default behaviour.'''

SOCIALACCOUNT_QUERY_EMAIL =ACCOUNT_EMAIL_REQUIRED
'''Request e-mail address from 3rd party account provider? E.g. using
  OpenID AX, or the Facebook "email" permission.'''

SOCIALACCOUNT_AUTO_SIGNUP =True
'''Attempt to bypass the signup form by using fields (e.g. username,
  email) retrieved from the social account provider. If a conflict
  arises due to a duplicate e-mail address the signup form will still
  kick in.'''

SOCIALACCOUNT_EMAIL_REQUIRED =ACCOUNT_EMAIL_REQUIRED
'''The user is required to hand over an e-mail address when signing up
  using a social account.'''

SOCIALACCOUNT_EMAIL_VERIFICATION =ACCOUNT_EMAIL_VERIFICATION
'''As `ACCOUNT_EMAIL_VERIFICATION`, but for social accounts.'''


# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'boundis.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Sydney'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = 'http://localhost:8000/locations/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "assets")

STATIC_URL = '/assets/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),)


TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
