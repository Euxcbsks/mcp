from re import sub

__all__ = [
    "format_source_data",
	"format_name"
]

def format_source_data(data):
	data = sub(r', *//.*', ',', data) #Remove comment
	data = sub(r': *\.', ': 0.', data) #Remove float-like(.1, .2, ...)
	data = data.strip() #Remove space at start and end
	list_data = data.split('\n') #Prepare for get first line and last line
	while '"' not in list_data[1]:
		data = data[len(list_data[0]):-len(list_data[-1])].strip() #Remove first line and last line
		list_data = data.split('\n') #Overwrite list_data with new data
	
	data = data.replace(list_data[0], '{') #Let first line turn into "{"
	data = data.replace(list_data[-1], '}') #Let last line turn into "}"
	
	return data

def format_name(name):
	name = sub(r"[\s']", '-', name)
	return name
