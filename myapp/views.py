from django.shortcuts import render
import requests

# def index(request):
#     url = "https://swapi.dev/api/people/1/"

#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise HTTPError for bad responses
#         data = response.json()
#         return render(request, 'myapp/index.html', {'data': data})
#     except requests.RequestException as e:
#         print(f"Request failed: {e}")
#         return render(request, 'myapp/error.html', {'error_message': "Failed to fetch data"})
    
def index(request):
    return render(request, 'myapp/index.html')