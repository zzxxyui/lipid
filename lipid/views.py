from django.shortcuts import render, get_object_or_404


def home(request):
	data = {
		'request': request,
		'title': 'Home'
	}
	return render(request, 'lipid/home.html', data)


def about(request):
	data = {
		'request': request,
		'title': 'About'
	}
	print('dsg')
	print(request.path)
	return render(request, 'lipid/about.html', data)


def tutorials(request):
	data = {
		'request': request,
		'title': 'Tutorials'
	}
	return render(request, 'lipid/tutorials.html', data)


def analysis(request):
	data = {
		'request': request,
		'title': 'Analysis'
	}
	return render(request, 'lipid/analysis.html', data)