"""
Django settings for data_center1 project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from core.constants import *

# 载入所有配置
from core.setting import *

# BASE_LOG_DIR = os.path.join(BASE_DIR, "var/logs")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/


# Application definition
INSTALLED_APPS = [
    # 'suit',
    'jet.dashboard',
    'jet',
    # 'appfront.admin.MyAdminSite',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'mongoengine',
    'rest_framework',
   #'rest_framework.authtoken',
    'rest_framework_swagger',
    'corsheaders',
    'dictionary',
    'cronjob',
    'appfront',
    'system',
    'manager',
    'task',
    'amazon',
    'rule',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS
CORS_ORIGIN_WHITELIST = (
    '192.168.2.212', # live
    '192.168.2.212:80', # live
    '127.0.0.1',
    '127.0.0.1:80',
    'localhost',
    'localhost:80',
    'localhost:8080',
    'localhost:8081',
)
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

ROOT_URLCONF = 'core.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.contrib.messages.context_processors.messages',
        ],
        'builtins': [
        ],
    },
},]


WSGI_APPLICATION = 'core.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# menu set
# SUIT_CONFIG = { # suit页面配置
#   'ADMIN_NAME': 'Data Center', # 登录界面提示
#   'LIST_PER_PAGE': 100, # 表中显示行数
# }

# BOOTSTRAP_ADMIN_SIDEBAR_MENU = True
#
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    # 'guardian.backends.ObjectPermissionBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'api.view.authentication.PubAuthentication',
        #'rest_framework.authentication.TokenAuthentication',
        #"rest_framework_jwt.authentication.JSONWebTokenAuthentication",
     ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'EXCEPTION_HANDLER': 'api.views.api_exception_handler',
    'PAGE_SIZE': 50,
    'DEFAULT_VERSION': 'v1',            # 默认版本
    'ALLOWED_VERSIONS': ['v1', 'v2'],   # 允许的版本
    'VERSION_PARAM': 'version'          # URL中获取值的key
}

SWAGGER_SETTINGS = {
    # 基础样式
    # 'SECURITY_DEFINITIONS': {
    #     "basic":{
    #         'type': 'basic'
    #     }
    # },
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'USE_SESSION_AUTH': True,
    'DOC_EXPANSION': 'list',
    # 接口文档中方法列表以首字母升序排列
    'APIS_SORTER': 'alpha',
    'SECURITY_DEFINITIONS': None,
    # 'SHOW_REQUEST_HEADERS':True,
    # 'USE_SESSION_AUTH': True,
    # 'DOC_EXPANSION': 'list',
    # 如果支持json提交, 则接口文档中包含json输入框
    # 'JSON_EDITOR': True,
    # 方法列表字母排序
    # 'OPERATIONS_SORTER': 'alpha',
    # 'VALIDATOR_URL': True,
    'CUSTOM_HEADERS': True,
    # 'SUPPORTED_SUBMIT_METHODS': True,
}