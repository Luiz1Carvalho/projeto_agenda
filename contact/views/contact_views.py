from django.shortcuts import render
from contact.models import Contact

def index(request):
    contact = Contact.objects.filter(show=True).order_by('-id')

    context = {
        'contact': contact,
    }

    return render(request, 'contact/index.html', context)