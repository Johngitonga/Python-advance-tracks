import os, shutil

def move_files():
	src = "/home/ipovi/Python-advance-tracks/file-categories/files/"
	csvDest = "/home/ipovi/Python-advance-tracks/file-categories/files/csvFiles"
	files = os.listdir(src)
	for file in files:
		if file.endswith('.csv'):
			filePath =  src + file
			shutil.move(filePath, csvDest)

move_files()