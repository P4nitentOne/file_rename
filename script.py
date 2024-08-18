import os
import shutil

# Define the source and destination directories
source_dir = r'C:\devprojects\justagrid\piano-mp3'
destination_dir = r'C:\devprojects\justagrid\renamed-piano'

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# List all MP3 files in the source directory
mp3_files = [f for f in os.listdir(source_dir) if f.endswith('.mp3')]

# Ensure we only process the first 89 files
for i, filename in enumerate(mp3_files[:89], start=1):
    # Define the new filename
    new_filename = f'piano{i}.mp3'
    
    # Define full file paths
    original_file_path = os.path.join(source_dir, filename)
    new_file_path = os.path.join(destination_dir, new_filename)
    
    # Copy the file to the new destination with the new name
    shutil.copy2(original_file_path, new_file_path)

print(f"Successfully renamed and moved {len(mp3_files[:89])} files to {destination_dir}.")
