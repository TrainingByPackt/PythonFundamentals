import requests

def validate_url(url):
	"""Validates the given url passed as string.
	
	Arguments:
    url -- String, A valid url should be of form <Protocol>://<hostmain>/<fileinfo>
	
	Protocol = [http, https, ftp]
	Hostname = string
	Fileinfo = [.html, .csv, .docx]
	"""
	# your code starts here.
	

	
	return # return True if url is valid else False


if __name__ == '__main__':
	url = input("Enter an Url: ")
	print(validate_url(url))
	



