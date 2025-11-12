import codecs
#
#<message>
#	<location line="+2"/>
#	<source>Allow</source>
#	<translation>允許</translation>
#</message>
#

def get_value_by_tag(element, tag_name):
	if element.find("<" + tag_name + ">")>=0 and element.find("</" + tag_name + ">")>=0:
		right_part = element.split("<" + tag_name + ">")[1]
		result = right_part.split("</" + tag_name + ">")[0]
		return result
	return ""
	
def get_source_map():
	f=codecs.open("mumble_zh_TW_from_zh_CN.txt","r", "utf-8")
	content = f.read()
	f.close()
	
	content_list = content.split("<message>")
	
	result_map = {}
	
	for one_element in content_list:
		source = get_value_by_tag(one_element, "source")
		translation = get_value_by_tag(one_element, "translation")
		
		if source and translation:
			result_map[source] = translation
	return result_map

def update_translation(element, translation):
	if element.find("<translation")>=0 and element.find('"unfinished"/>')>=0:
		result_list = element.split("<translation")
		
		return result_list[0] + "<translation>" + translation + "</translation>" + result_list[1].split('"unfinished"/>')[1]

	return element

def update_target(source_map):
	f = codecs.open("mumble_zh_TW.ts", "r", "utf-8")
	content  = f.read()
	f.close()

	content_list = content.split("<message>")
	for i in range(len(content_list)):
		one_element = content_list[i]
		source = get_value_by_tag(one_element, "source")

		if one_element.find('<translation type="unfinished"/>')>=0:
			updated_value = source_map[source]
			content_list[i]= update_translation(one_element, updated_value)

	result = "<message>".join(content_list)

	print("Will update mumble_zh_TW_update.ts")

	f=codecs.open("mumble_zh_TW_update.ts","w","utf-8")
	f.write(result)
	f.close()



def main():
	source_map = get_source_map()
	update_target(source_map)

main()