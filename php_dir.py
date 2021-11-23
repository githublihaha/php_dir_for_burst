# 读取某个文件夹下的所有文件,然后去除其中的重复行
# php+dir

import os
filePath = 'D:\\work\\2021\\python\\php_dir\\php'
files = os.listdir(filePath)
print(files)
print(len(files))

urls = []

for i in files:
    file_path = filePath + '\\' + i
    print(file_path)

    with open(file_path, 'rb') as file:
        for line in file:
            line_raw = line.rstrip() + b"\n"
            if line_raw not in urls:
                urls.append(line_raw)

print(len(urls))

with open('php_dir.txt', 'wb') as file:
    file.writelines(urls)

