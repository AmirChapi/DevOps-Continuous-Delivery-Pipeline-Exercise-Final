import os
import zipfile
import sys

base_names = ['a', 'b', 'c', 'd']
version = os.environ.get('VERSION', '1.0.0')

created_files = []

try:
    for name in base_names:
        txt_file = f"{name}.txt"
        with open(txt_file, 'w') as f:
            f.write(f"This is the content for {name} with version {version}.")
        created_files.append(txt_file)
    print("SUCCESS: All .txt files created.")
except Exception as e:
    print(f"FAILURE: Could not create text files: {e}")
    sys.exit(1)

zip_files_created = []
try:
    for name in base_names:
        txt_file = f"{name}.txt"
        zip_file = f"{name}_{version}.zip"

        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(txt_file)

        zip_files_created.append(zip_file)

    print(f"SUCCESS: All {len(zip_files_created)} zip files created: {', '.join(zip_files_created)}")

except Exception as e:
    print(f"FAILURE: Could not create zip files: {e}")
    sys.exit(1)

finally:
    for f in created_files:
        if os.path.exists(f):
            os.remove(f)