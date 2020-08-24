import os
import settings

def full_path(file_path):
    return os.path.join(settings.BASE_DIR, file_path)