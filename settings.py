import logging
import tornado
import tornado.template
import os
from tornado.options import define, options

import environment
import logconfig

from view.modules.components import UIAppHeader, UIContextHeader, UINavHeader
from view.modules.components import UIGamesList, UIRankingsList
from view.modules.components import UICreateGameDialog

# Application constants
# FIXME - build this based on user
LEAGUE = 693

# Make filepaths relative to settings.
path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=8000, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=True, help="debug mode")
tornado.options.parse_command_line()

MEDIA_ROOT = path(ROOT, 'media')
TEMPLATE_ROOT = path(ROOT, 'view/templates')

# Deployment Configuration

class DeploymentType:
    PRODUCTION = "PRODUCTION"
    DEV = "DEV"
    SOLO = "SOLO"
    STAGING = "STAGING"
    dict = {
        SOLO: 1,
        PRODUCTION: 2,
        DEV: 3,
        STAGING: 4
    }

if 'DEPLOYMENT_TYPE' in os.environ:
    DEPLOYMENT = os.environ['DEPLOYMENT_TYPE'].upper()
else:
    DEPLOYMENT = DeploymentType.SOLO

settings = {}
settings['debug'] = DEPLOYMENT != DeploymentType.PRODUCTION or options.debug
settings['static_path'] = MEDIA_ROOT

settings['cookie_secret'] = "\xee\x0ec\x9bl\x02\xeb/.\xd4\xeb\xc2(\xb0\xb1\x8a\x0b\xb5[^Tq\xecy"
settings['xsrf_cookies'] = True
settings['login_url'] = "/"
settings['facebook_api_key'] = "184725354981659"
settings['facebook_secret'] = "06a89856418cad1d4ce484c159cbdafc"

settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)
settings['ui_modules'] = {
        'UIAppHeader' : UIAppHeader,
        'UIContextHeader' : UIContextHeader,
        'UINavHeader' : UINavHeader,
        'UIRankingsList' : UIRankingsList,
        'UIGamesList' : UIGamesList,
        'UICreateGameDialog' : UICreateGameDialog
        }

settings['league_id'] = LEAGUE

SYSLOG_TAG = "boilerplate"
SYSLOG_FACILITY = logging.handlers.SysLogHandler.LOG_LOCAL2

# See PEP 391 and logconfig for formatting help.  Each section of LOGGERS
# will get merged into the corresponding section of log_settings.py.
# Handlers and log levels are set up automatically based on LOG_LEVEL and DEBUG
# unless you set them here.  Messages will not propagate through a logger
# unless propagate: True is set.
LOGGERS = {
   'loggers': {
        'boilerplate': {},
    },
}

if settings['debug']:
    LOG_LEVEL = logging.DEBUG
else:
    LOG_LEVEL = logging.INFO
USE_SYSLOG = DEPLOYMENT != DeploymentType.SOLO

logconfig.initialize_logging(SYSLOG_TAG, SYSLOG_FACILITY, LOGGERS,
        LOG_LEVEL, USE_SYSLOG)

if options.config:
    tornado.options.parse_config_file(options.config)
