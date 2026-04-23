from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact

@login_required(login_url='contact:login')
def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contact:create')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact/create.html', context)

@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, show=True, owner=request.user)
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact:contact', contact_id=contact.id)
    else:
        form = ContactForm(instance=contact)
    
    context = {'form': form, 'contact': contact, 'site_title': 'Editar Contato'}
    return render(request, 'contact/update.html', context)

@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, show=True, owner=request.user)
    
    if request.method == 'POST':
        contact.delete()
        return redirect('contact:index')