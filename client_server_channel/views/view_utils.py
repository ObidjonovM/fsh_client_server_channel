from os.path import join
from datetime import datetime


def url_join(path_list):
    the_path = join(*path_list)
    return the_path.replace('\\','/')


def parse_time(str_time):
	return datetime.strptime(str_time, '%a, %d %b %Y %H:%M:%S %Z')