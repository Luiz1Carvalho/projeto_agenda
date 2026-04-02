from django.shortcuts import redirect, render
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    contact = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contact, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Agenda de Contatos',
    }

    return render(request, 'contact/index.html', context)

def contact(request, contact_id):
    single_contact = Contact.objects.get(id=contact_id)
    context = {
        'contact': single_contact,
        'site_title': "Contato - " + single_contact.first_name,
    }

    return render(request, 'contact/contact.html', context)

def search(request):
    query = request.GET.get('q')
    contact = Contact.objects.filter(show=True).filter(
                                     Q(first_name__icontains=query) |
                                     Q(last_name__icontains=query) |
                                     Q(email__icontains=query) |
                                     Q(phone__icontains=query)
                                     ).order_by('-id')

    if query is None or query.strip() == '':
        return redirect('contact:index')
    
    paginator = Paginator(contact, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Procurando por: ' + query,
        'valor_pesquisa': query,
    }

    return render(request, 'contact/index.html', context)