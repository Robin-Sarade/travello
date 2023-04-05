from django.shortcuts import render
from . models import Destination, Contact
from datetime import datetime



# Create your views here.
def index(request):
    dests = Destination.objects.all()

    return render(request, 'index.html',{"dests":dests})

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        sub=request.POST.get('sub')
        msg=request.POST.get('msg')

        contact = Contact(name=name, email=email, sub=sub,msg=msg, date=datetime.today())
        contact.save()

    return render(request,'contact.html')