import os
import zipfile
import sys

# שמות הקבצים הבסיסיים
base_names = ['a', 'b', 'c', 'd']

# גרסה מגיעה מה-ENV (כמו ב-Jenkins)
version = os.environ.get('VERSION', '1.0.0')

created_txt_files = []
created_zip_files = []

# שלב 1 - יצירת קבצי TXT
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

# שלב 2 - יצירת קבצי ZIP
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
    # מוחקים את קבצי ה-TXT, כי כבר ארזנו אותם
    for f in created_txt_files:
        if os.path.exists(f):
            os.remove(f)

# --- תקלה יזומה: מוחקים בכוונה ZIP אחד ---
bad_file = f"c_{version}.zip"
if os.path.exists(bad_file):
    os.remove(bad_file)
    print(f"Simulated error: Deleted {bad_file}")

# שלב 3 - ולידציה: בודקים שכל קבצי ה-ZIP קיימים
expected_zip_files = [f"{name}_{version}.zip" for name in base_names]
missing_files = [f for f in expected_zip_files if not os.path.exists(f)]

if missing_files:
    print("ERROR: Missing expected zip files:", ", ".join(missing_files))
    sys.exit(1)

print("VALIDATION PASSED: All expected zip files exist.")
