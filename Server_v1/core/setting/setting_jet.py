# coding:utf-8

JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },{
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },{
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },{
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },{
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },{
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]
JET_DEFAULT_THEME = 'light-blue'
JET_CHANGE_FORM_SIBLING_LINKS = False

JET_SIDE_MENU_COMPACT = False
# from django.utils.translation import ugettext as _
# JET_SIDE_MENU_ITEMS = [  # A list of application or custom item dicts
#     {'label': ('General'), 'app_label': 'core', 'items': [
#         {'name': 'help.question'},
#         {'name': 'pages.page', 'label': ('Static page')},
#         {'name': 'city'},
#         {'name': 'validationcode'},
#         {'label': ('Analytics'), 'url': 'http://example.com', 'url_blank': True},
#     ]},
#     {'label': ('Users'), 'items': [
#         {'name': 'core.user'},
#         {'name': 'auth.group'},
#         {'name': 'core.userprofile', 'permissions': ['core.user']},
#     ]},
#     {'app_label': 'banners', 'items': [
#         {'name': 'banner'},
#         {'name': 'bannertype'},
#     ]},
# ]
JET_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultIndexDashboard'
JET_APP_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultAppIndexDashboard'
