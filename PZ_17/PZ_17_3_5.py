import subprocess
import os

folder_path = "/home/student/Документы/Prudnikov_IS27/reports/"
pdf_files = [file for file in os.listdir(folder_path) if file.endswith(".pdf")]
if pdf_files:
    pdf_file = os.path.join(folder_path, pdf_files[0])
    subprocess.call(['xdg-open', pdf_file])