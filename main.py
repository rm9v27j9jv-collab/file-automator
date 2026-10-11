from pathlib import Path
import shutil
import logging
import argparse
logging.basicConfig(level=logging.INFO, format="%(asctime)s -  %(levelname)s - %(message)s")
DIRECTORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"},
    "Videos": {".mp4", ".mov", ".mkv", ".avi"},
    "Archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
    "Code": {".py", ".js", ".html", ".css", ".json", ".cpp"}
}
def organize_directory(target_dir: Path):
    if not target_dir.exists() or not target_dir.is_dir():
        logging.error(f"Target directory does not exist or is invalid: {target_dir}")
        return
    logging.info(f"Starting organization for: {target_dir}")
    for item in target_dir.iterdir():
        if item.is_dir() or item.name.startswith('.'):
            continue
        file_ext = item.suffix.lower()
        moved = False
        for category, extensions in DIRECTORIES.items():
            if file_ext in extensions:
                dest_folder = target_dir / category
                dest_folder.mkdir(exist_ok=True)
                dest_path = dest_folder / item.name
                if dest_path.exists(): 
                    dest_path = dest_folder / f"{item.stem}_copy{item.suffix}"

                shutil.move(str(item), str(dest_path))
                logging.info(F"Moved: {item.name} -> {category}")
                moved = True
                break
        if not moved:
            other_folder = target_dir / "Others"
            other_folder.mkdir(exist_ok=True)
            dest_path = other_folder / item.name
            if dest_path.exists():
                dest_path = other_folder / f"{item.stem}_copy{item.suffix}"
            shutil.move(str(item), str(dest_path))
            logging.info(f"Moved: {item.name} -> Others/")
    logging.info("File organization completed succesfully")
def main():
    parser = argparse.ArgumentParser(description="Automate organizing files in a directory")
    parser.add_argument("--path", type=str, default=str(Path.home() / "Downloads"), help="Path to the directory you want to organize (defaults to Downloads)" )
    args = parser.parse_args()
    organize_directory(Path(args.path))
if __name__ == '__main__':
    main()