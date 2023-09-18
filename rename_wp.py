import os
import shutil
import argparse

def rename_images(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The specified folder '{folder_path}' does not exist.")
        return

    # Create a new directory for renamed images
    renamed_folder = os.path.join(folder_path, "renamed_wps")
    os.makedirs(renamed_folder, exist_ok=True)

    # List all files in the folder
    files = os.listdir(folder_path)

    # Filter only image files based on common image file extensions
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
    image_files = [file for file in files if file.lower().endswith(image_extensions)]

    if not image_files:
        print(f"No image files found in '{folder_path}'.")
        return

    # Rename and move the image files
    for index, old_name in enumerate(image_files, start=1):
        # Extract the file extension
        file_extension = os.path.splitext(old_name)[1]

        # Generate the new name with a 'wp' prefix and incrementing index
        new_name = f"wp{index}{file_extension}"

        # Construct the full paths for renaming and moving
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(renamed_folder, new_name)

        # Rename and move the file
        shutil.copy2(old_path, new_path)

        print(f"Renamed and moved '{old_name}' to '{new_name}' in 'renamed_wps'")

def main():
    parser = argparse.ArgumentParser(description="Rename and move image files in a directory.")
    parser.add_argument("folder_path", metavar="FOLDER_PATH", help="Path to the directory containing image files.")
    
    args = parser.parse_args()

    if args.folder_path == "--help":
        parser.print_help()
    else:
        rename_images(args.folder_path)

if __name__ == "__main__":
    main()
