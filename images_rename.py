# import os

# # Set your folder path
# folder_path = 'images/'  # Change this to your folder

# # Get all image files
# files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

# # Sort files by their current number
# files.sort()

# # Rename files sequentially
# for index, filename in enumerate(files, start=1):
#     old_path = os.path.join(folder_path, filename)
#     extension = os.path.splitext(filename)[1]  # Get file extension
#     new_filename = f"Image_{index}{extension}"
#     new_path = os.path.join(folder_path, new_filename)
    
#     os.rename(old_path, new_path)
#     print(f"Renamed: {filename} → {new_filename}")

# print(f"\n✅ Renamed {len(files)} images successfully!")

import os

# Set your folder path
folder_path = 'dataset images/wildfire aerial view'  # Change this to your folder

# Get all image files
files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

# Sort files
files.sort()

print("Step 1: Renaming to temporary names...")
# First pass: Rename to temporary names (avoid conflicts)
for index, filename in enumerate(files, start=1):
    old_path = os.path.join(folder_path, filename)
    extension = os.path.splitext(filename)[1]
    temp_filename = f"TEMP_{index}{extension}"
    temp_path = os.path.join(folder_path, temp_filename)
    
    os.rename(old_path, temp_path)

print("Step 2: Renaming to final names...")
# Second pass: Rename from temporary to final names
temp_files = [f for f in os.listdir(folder_path) if f.startswith('TEMP_')]
temp_files.sort()

for index, filename in enumerate(temp_files, start=81):
    old_path = os.path.join(folder_path, filename)
    extension = os.path.splitext(filename)[1]
    new_filename = f"Image_{index}{extension}"
    new_path = os.path.join(folder_path, new_filename)
    
    os.rename(old_path, new_path)
    print(f"Renamed: {filename} → {new_filename}")

print(f"\n✅ Renamed {len(temp_files)} images successfully!")