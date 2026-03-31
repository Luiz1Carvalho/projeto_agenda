from django.contrib import admin

from .models import Category, Contact, Asd
"""LUIZ - 123"""
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'created_date')
    ordering = ('-created_date',)
    list_filter = ('created_date',)
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    list_per_page = 10
    list_max_show_all = 100
    #list_editable = ('first_name', 'last_name', 'phone', 'email')
    list_display_links = ('id', 'first_name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id',)

@admin.register(Asd)
class AsdAdmin(admin.ModelAdmin):
    list_display = ('only_name',)