from django.urls import path
from contact import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'contact'

urlpatterns = [
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),

    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)