import os
import yaml


# Not great code, relies on knowing the code layout, but need to move on.
def load_app_settings():

    settings_file_name = 'app_settings.yaml'
    try:
        settings_file_path = get_file_path(settings_file_name)
        with open(settings_file_path, 'r') as settings_file:
            settings = yaml.load(settings_file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        raise FileNotFoundError('File Not Found: ' + settings_file_name)

    return settings


def get_file_path(file_name):
    folder_depth = 30
    file_found = False
    path_to_file = ''
    current_folder = os.path.dirname(os.path.abspath(__file__))
    file_folder = os.path.split(current_folder)
    current_folder = file_folder[0]
    while file_found is False and folder_depth > 0:
        folder_depth = folder_depth - 1
        path_to_check = os.path.join(current_folder + '/' + file_name)
        if os.path.exists(path_to_check):
            path_to_file = path_to_check
            file_found = True
        else:
            new_current_folder = os.path.split(current_folder)
            current_folder = new_current_folder[0]

    if len(path_to_file) > 0:
        return path_to_file
    else:
        raise FileNotFoundError('File Not Found: ' + file_name)
