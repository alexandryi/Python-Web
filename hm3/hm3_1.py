import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def copy_file(file_path, dist_dir):
    ext = file_path.suffix[1:]  
    if not ext:
        ext = "no_extension"
    target_dir = dist_dir / ext
    target_dir.mkdir(parents=True, exist_ok=True)  
    shutil.copy2(file_path, target_dir / file_path.name)  


def process_directory(directory, dist_dir, executor):
    futures = []

    for entry in os.scandir(directory):
        path = Path(entry.path)
        if entry.is_dir():
            futures.append(executor.submit(process_directory, path, dist_dir, executor))
        elif entry.is_file():
            futures.append(executor.submit(copy_file, path, dist_dir))

    for future in futures:
        future.result()


def main(source_dir, dist_dir):
    source_path = Path(source_dir)
    dist_path = Path(dist_dir)

    if not source_path.exists() or not source_path.is_dir():
        print(f"Source directory '{source_path}' is invalid!")
        sys.exit(1)

    dist_path.mkdir(parents=True, exist_ok=True)

    with ThreadPoolExecutor() as executor:
        process_directory(source_path, dist_path, executor)

    print("Files sorted successfully!")


if __name__ == "__main__":
    source_dir = 'C:\\Users\\DonK\\Desktop\\pictures'  
    dist_dir = 'C:\\Users\\DonK\\Desktop\\dist'    

    main(source_dir, dist_dir)
