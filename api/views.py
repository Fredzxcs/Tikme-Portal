from django.shortcuts import render

# Authentication
def portal(request):
    return render(request, 'portal.html')
