from pathlib import Path

folder = Path(".")

file_count = 0

folder_count = 0

print("Directory Scanner\n")

for item in folder.iterdir():

    if item.is_file():
        file_count += 1
        print(f"File:{item.name} | Extension: {item.suffix}")

    elif item.is_dir():
        folder_count += 1
        print(f"FOLDER:{item.name}")

print("\nSummary")

print(f"Files: {file_count}")
print(f"Folders: {folder_count}")



