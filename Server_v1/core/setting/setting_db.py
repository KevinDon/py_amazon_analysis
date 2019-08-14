# coding:utf-8

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'newaim_amazon_analysis_server_v1',
        'USER': 'amazon_analysis',
        'PASSWORD': 'amazon#123',
        'HOST': '192.168.2.102',
        'PORT': '5432',
    },
}
"""
# import sqlserver
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'newaim_amazon_analysis_server_v1',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

# # add session
# SESSION_ENGINE = 'mongoengine.newaim_dc_warehouse.sessions'

DATABASE_ROUTERS = ['core.database_router.DatabaseAppsRouter']


# 数据库分配
DATABASE_APPS_MAPPING = {
    'admin': 'default',
    'auth': 'default',
    'contenttypes': 'default',
    'sessions': 'default',
    'cronjob': 'default',
    'appfront': 'default',
    'jet': 'default',
    'dashboard': 'default',
    'corsheaders': 'default',
    'manager': 'default',
    'dictionary': 'default',
    'system': 'default',
    'task': 'default',
    'amazon': 'default',
    'rule':'default',
}
