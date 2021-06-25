from os.path import join


def url_join(path_list):
    the_path = join(*path_list)
    return the_path.replace('\\','/')
