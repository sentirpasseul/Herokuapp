from pathlib import Path


class PathUtils:
    DATA_DIR = "/data/"

    @staticmethod
    def get_data_path(file_name: str):
        project_dir = Path.cwd()
        path = str(project_dir) + PathUtils.DATA_DIR + file_name
        return path
