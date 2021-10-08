import os
from os.path import join, exists

reload = False      # change it back to false before deploying

default_proc_name = 'gunicorn_public_server'

bind = 'ip:port'

workers = 4

worker_class = 'gevent'

#logging

if not exists('logs'):
   os.mkdir('logs')

accesslog = join('logs', 'guni_access.log')
errorlog = join('logs', 'errors_log.log')


# cmd to start (ONLY FOR THIS CASE!!!) : gunicorn app:app -c gunicorn.settings.py
