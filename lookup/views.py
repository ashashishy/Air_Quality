from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=62025&distance=25&API_KEY=F7A8BCA4-4F2F-4E7F-BB9D-45EA548FD7E6")
    try:
        api=json.loads(api_request.content)


    except Exception as e:
        api="Error..."



    return render(request, 'home.html',{'api':api})


def about(request):
    return render(request, 'about.html',{})
