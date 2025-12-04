import os

FILE_LIST=r'''src\mumble\Makefile.Release
src\mumble_exe\Makefile.Release
src\mumble_proto\Makefile.Release
overlay\Makefile.Release
overlay_winx64\Makefile.Release
src\murmur\Makefile.Release
src\murmur\murmur_ice\Makefile.Release'''

CONTENT_MAP={}

CONTENT_MAP["\\cygdrive\\c\\MumbleBuild\\"] = "c:\\MumbleBuild\\"

CONTENT_MAP["/cygdrive/c/MumbleBuild/"] = "c:\\MumbleBuild\\"

#if need to debug, can uncomment the following line
CONTENT_MAP[" -Ox "] = " -Od -Zi "


def update_file(file_name):
	f = open(file_name,"r")
	content = f.read()
	f.close()

	bNeedUpdate = False
	for key, value in CONTENT_MAP.items():
		if content.find(key)>0:
			bNeedUpdate = True
			break

	if not bNeedUpdate:
		print("No need to update: " + file_name)
		return

	for key, value in CONTENT_MAP.items():
		content = content.replace(key, value)

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