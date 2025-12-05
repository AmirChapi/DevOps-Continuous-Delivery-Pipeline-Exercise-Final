import os
import zipfile
import sys

base_names = ['a', 'b', 'c', 'd']

version = os.environ.get('VERSION', '1.0.0')

created_txt_files = []
created_zip_files = []

try:
    for name in base_names:
        txt_file = f"{name}.txt"
        with open(txt_file, 'w') as f:
            f.write(f"This is the content for {name} with version {version}.")
        created_txt_files.append(txt_file)

    print("SUCCESS: All .txt files created.")
except Exception as e:
    print(f"FAILURE: Could not create text files: {e}")
    sys.exit(1)

try:
    for name in base_names:
        txt_file = f"{name}.txt"
        zip_file = f"{name}_{version}.zip"

        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(txt_file)

        created_zip_files.append(zip_file)

    print(f"SUCCESS: All {len(created_zip_files)} zip files created: {', '.join(created_zip_files)}")
except Exception as e:
    print(f"FAILURE: Could not create zip files: {e}")
    sys.exit(1)
finally:
    for f in created_txt_files:
        if os.path.exists(f):
            os.remove(f)

#תקלה יזומה
#bad_file = f"c_{version}.zip"
#if os.path.exists(bad_file):
#   os.remove(bad_file)
#   print(f"Simulated error: Deleted {bad_file}")

expected_zip_files = [f"{name}_{version}.zip" for name in base_names]
missing_files = [f for f in expected_zip_files if not os.path.exists(f)]

if missing_files:
    print("ERROR: Missing expected zip files:", ", ".join(missing_files))
    sys.exit(1)

print("VALIDATION PASSED: All expected zip files exist.")
