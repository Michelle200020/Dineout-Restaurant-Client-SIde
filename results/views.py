from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        
        name = request.POST.get("name")
        api_url = f'http://127.0.0.1:8000/restaurant/{name}'  # Replace with your API endpoint URL
        response = requests.get(api_url)
        restaurant_data = response.json()
        if response.status_code == 200:
            restaurant_data = response.json()
            return render(request, 'results.html', {'restaurant_data': restaurant_data})
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch restaurant results. Check Again!'})
    
        
    return render(request, 'index.html')
