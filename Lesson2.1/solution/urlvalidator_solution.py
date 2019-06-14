import requests

def validate_url(url):
	"""Validates the given url passed as string.
	
	Arguments:
    url -- String, A valid url should be of form <Protocol>://<hostmain>/<fileinfo>
	
	Protocol = [http, https, ftp]
	Hostname = string
	Fileinfo = [.html, .csv, .docx]
	"""
	protocol_valid = True
	valid_protocols = ['http', 'https', 'ftp']
	valid_fileinfo = ['.html', '.csv', '.docx']
	#first split the url to get protocol
	protocol = url.split("://")[0]
	if protocol not in valid_protocols:
		protocol_valid = False

	fileinfo_valid = False
	for finfo in valid_fileinfo:
		if url.endswith(finfo):
			fileinfo_valid = True
	# both protocol and fileinfo should be valid to return true.	
	if protocol_valid and fileinfo_valid:
		return True
	else:
		return False

#take home solution
def get_url_response(url):
	r = requests.get(url)
	if r.status_code == 200:
		return r.text
	else:
		return r.status_code

if __name__ == '__main__':
	url = input("Enter an Url: ")
	print(validate_url(url))
	



