import zipfile

with zipfile.ZipFile("output_file", "r") as zip_ref:
    zip_ref.extractall("extracted_files")