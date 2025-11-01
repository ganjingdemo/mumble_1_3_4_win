import os

FILE_LIST=r'''g15helper/g15helper.plist
g15helper/g15helper.rc
installer/Settings.wxi
macx/common.pri
macx/osax/osax.plist
overlay/mumble_ol.rc
overlay/overlay-shared.pro
overlay/overlay_exe/overlay_exe.rc
overlay_winx64/mumble_ol.rc
overlay_winx64/overlay_exe_winx64/overlay_exe.rc
src/mumble.pri
src/mumble/mumble.plist
src/mumble/mumble.rc
src/mumble/mumble_dll.rc
src/murmur/murmur.plist
src/murmur/murmur.rc'''

ORIGINAL_CONTENT_LIST=["1.3.4", "1,3,4,0"]

UPDATE_CONTENT_LIST=["1.3.8", "1,3,8,0"]

def update_file(file_name):
	f = open(file_name,"r")
	content = f.read()
	f.close()

	bNeedUpdate = False
	for one_content in ORIGINAL_CONTENT_LIST:
		if content.find(one_content)>=0:
			bNeedUpdate = True
			break

	if not bNeedUpdate:
		print("No need to update: " + file_name)
		return

	for i in range(len(ORIGINAL_CONTENT_LIST)):
		one_content = ORIGINAL_CONTENT_LIST[i]
		content = content.replace(one_content, UPDATE_CONTENT_LIST[i])

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