# coding:utf-8
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True
# TEMPLATE_DEBUG = False
# TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8w7hd7#^e(ebsp1@_8v#5ef5z$tr)r1e(w-d#y98=s+btw1jr5'


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGES = (
    ('en-au', ('English')),
    ('zh-hans', ('中文简体')),
    ('zh-hant', ('中文繁體')),
)
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'en-au'
# LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'Asia/Shanghai'
TIME_ZONE = 'Australia/Melbourne'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# DATETIME_FORMAT = 'Y-m-d H:m:s'
# TIME_FORMAT = 'H:m:s'

# 翻译文件所在目录，需要手工创建
LOCALE_PATHS = ( os.path.join(BASE_DIR, 'locale'),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'

#媒体文件目录
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# 与STATIC_ROOT不能共存
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), os.path.join(BASE_DIR, "media")]
# 以下用于发布前的静态文件更新位置，与STATICFILES_DIRS不能共存
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

