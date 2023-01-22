from django.shortcuts import render

# Create your views here.
from .models import Product

def index(request):
    return render(request, "api/index.html")


def upload(request):
    if request.method == "POST": 
        date = request.POST['date_listed']
        image =request.FILES['image']
        products = Product.objects.create(title=request.POST['title'], description=request.POST['description'], image=image, date=date)
        products.save()
        
        return render(request, "api/index.html", {
                "message": "Upload Successful."
            })
    else:
        return render(request, 'api/index.html')

def retrieve(request):
    if request.method == 'POST':
        product = Product.objects.get(title=request.POST['title'])
        return render(request, "api/retrieve.html",{"product": product })
    else:
        return render(request, 'api/retrieve.html')    