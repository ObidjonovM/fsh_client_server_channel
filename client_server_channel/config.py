import os

# database connection information
DB_CONNECT = 'dbname=database user=login password=password'

#logging folder path
LOGS_PATH = '/your/log/path'

if not os.path.exists(LOGS_PATH):
    os.mkdir(LOGS_PATH)
