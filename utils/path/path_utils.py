from pathlib import Path
from utils.logs.logger import Logger


class PathUtils:
    @staticmethod
    def get_path(file_name: str):
        try:
            project_dir = Path.cwd()
            path = str(project_dir / 'data' / file_name)
            Logger.info(f"Get path: {path}")
            return path
        except:
            Logger.error(f"Failed to get path: {path}")
            raise

