from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

def homepage(request):
    #return HttpResponse('homepage')
    return render(request, 'homepage.html')

def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')

def request_error(request):
    return render(request, '404.html')

def handle404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handle500(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response
