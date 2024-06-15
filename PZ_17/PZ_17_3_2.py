import os
import shutil

os.chdir("/home/student/Документы/Prudnikov_IS27/")

os.mkdir("test")

os.mkdir("test/test1")

shutil.copyfile("/home/student/Документы/Prudnikov_IS27/PZ_6/PZ_6_1.py", "test/PZ_6_1.py")
shutil.copyfile("/home/student/Документы/Prudnikov_IS27/PZ_6/PZ_6_2.py", "test/PZ_6_2.py")

shutil.copyfile("/home/student/Документы/Prudnikov_IS27/PZ_7/PZ_7_2.py", "test/test1/test.txt")

files = os.listdir("test")
for file in files:
    file_size = os.path.getsize(os.path.join("test", file))
    print(f"{file}: {file_size} bytes")