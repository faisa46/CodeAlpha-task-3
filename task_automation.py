from pathlib import Path
import shutil

def move_jpg_files(source_folder, destination_folder):
    source = Path(source_folder)
    destination = Path(destination_folder)

    if not source.exists() or not source.is_dir():
        print("Source folder does not exist.")
        return

    destination.mkdir(parents=True, exist_ok=True)
    moved_count = 0

    for file_path in source.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in [".jpg", ".jpeg"]:
            target = destination / file_path.name

            if target.exists():
                print(f"Skipped (already exists): {file_path.name}")
                continue

            shutil.move(str(file_path), str(target))
            print(f"Moved: {file_path.name}")
            moved_count += 1

    print(f"Finished. {moved_count} JPG file(s) moved.")

if __name__ == "__main__":
    print("JPG File Organizer")
    source = input("Enter source folder path: ").strip().strip('"')
    destination = input("Enter destination folder path: ").strip().strip('"')
    move_jpg_files(source, destination)
