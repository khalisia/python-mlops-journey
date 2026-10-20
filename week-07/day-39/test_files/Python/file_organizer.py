from pathlib import Path
import shutil

#To be changed to folder you should organize

SOURCE = Path("test_files")

# A Dictionary mapping each destination folder to a list of file extensions.

FILE_TYPES = {
  "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "PDFs": [".pdf"],
    "Documents": [".docx", ".doc", ".txt"],
    "Data": [".csv", ".xlsx", ".json"],
    "Python": [".py"],
    "Archives": [".zip", ".rar", ".7z"], 
}

def organize_files():
    if not SOURCE.exists() or not SOURCE.is_dir():
        print(f"Folder not found: {SOURCE.resolve()}")
        return

    moved_count = 0

    for file in SOURCE.iterdir():
        #Skip the folders and only organize files.
        if not file.is_file():
            continue

        #Find the folder for this type of file
        destination_folder = None

        #Getting the file extension, finding correct folder, joining paths.

        for folder_name, extensions in FILE_TYPES.Items():
            if file.suffix.lower() in extensions:
                destination_folder = SOURCE/ folder_name
                break

        #Keep unknown file types in their original folder.
        if destination_folder is None:
            continue

        destination_folder.mkdir(exist_ok = True)

        destination = destination_folder/ file.name

        # Avoid overwriting an existing file.
        if destination.exists():
            print(f"Skipped duplicate: {file.name}")
            continue
        #Moving files and avoiding duplicates.

        shutil.move(str(file)), str(destination)
        print(f"Moved: {file.name} -> {destination_folder.name}/")
        moved_count += 1

    print(f"\nOrganization complete. Files moved: {moved_count}")

if __name__ == "__main__"
    organize_files()

