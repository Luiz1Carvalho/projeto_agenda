from django.shortcuts import get_object_or_404, redirect, render

from contact.forms import ContactForm
from contact.models import Contact

def create (request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('contact:create')
        return render(request, 'contact/create.html',context, )


    context = {'form': ContactForm()}
    return render(request, 'contact/create.html', context)

def update(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact:contact', contact_id=contact.id)
    else:
        form = ContactForm(instance=contact)
    
    context = {'form': form, 'contact': contact, 'site_title': 'Editar Contato'}
    return render(request, 'contact/update.html', context)

def delete(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    
    if request.method == 'POST':
        contact.delete()
        return redirect('contact:index')