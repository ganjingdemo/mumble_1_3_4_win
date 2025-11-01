import os

FILE_LIST=r'''src\mumble\Makefile.Release
src\mumble_exe\Makefile.Release
src\mumble_proto\Makefile.Release
overlay\Makefile.Release
overlay_winx64\Makefile.Release
src\murmur\Makefile.Release
src\murmur\murmur_ice\Makefile.Release'''

ORIGINAL_PATH_LIST=["\\cygdrive\\c\\MumbleBuild\\","/cygdrive/c/MumbleBuild/"]

UPDATE_PATH="c:\\MumbleBuild\\"

def update_file(file_name):
	f = open(file_name,"r")
	content = f.read()
	f.close()

	bNeedUpdate = False
	for one_path in ORIGINAL_PATH_LIST:
		if content.find(one_path)>0:
			bNeedUpdate = True
			break

	if not bNeedUpdate:
		print("No need to update: " + file_name)
		return

	for one_path in ORIGINAL_PATH_LIST:
		content = content.replace(one_path, UPDATE_PATH)

	print("Will update file: " + file_name)
	f = open(file_name,"w")
	f.write(content)
	f.close()


def main():
	update_file_list = FILE_LIST.split("\n")
	for one_file in update_file_list:
		one_file = one_file.strip()
		full_path = os.path.realpath(one_file)
		if os.path.isfile(full_path):
			print("\nprocessing: " + full_path)
			update_file(full_path)
		else:
			print("\nCannot find file: " + full_path)

main()