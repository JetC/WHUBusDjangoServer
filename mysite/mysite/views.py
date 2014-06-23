from django.http import HttpResponse
def hello(request):
	file = open('jsonLocation.txt','r')
	try:
		text = file.read()
	finally:
		file.close()

	return HttpResponse(text)