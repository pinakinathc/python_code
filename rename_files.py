import os
def rename_files():
	# (1) get file names from a folder
	file_list=os.listdir("/home/morphine/Pictures/prank")
	print(file_list)
	saved_path=os.getcwd()
	os.chdir("/home/morphine/Pictures/prank")
	#(2) for each file, rename filename
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,"0123456789"))
	print(file_list)
	os.chdir(saved_path)

rename_files()
