from pathlib import Path
import shutil
from datetime import datetime

SOURCE = Path(".")
BACKUP_DIR = Path("backup")

def create_backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_path = BACKUP_DIR / f"backup_{timestamp}"

    backup_path.mkdir(parents=True, exist_ok=True)

    files_copied = 0

    for file in SOURCE.iterdir():

        if file.is_file() and file.name != "day38_backup.py":
            destination = backup_path/ file.name

            shutil.copy2(file, destination)

            files_copied += 1

        print(f"Backup created: {backup_path}")
        print(f"Files copied: {files_copied}")


if __name__ == "__main__":
    create_backup()