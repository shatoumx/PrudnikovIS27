import os

folder_path = "/home/student/Документы/Prudnikov_IS27/"
files = os.listdir(folder_path)

shortest_filename = min(files, key=len)
print(os.path.basename(shortest_filename))
