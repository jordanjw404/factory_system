from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'quantity', 'status', 'location', 'updated_at')
    list_filter = ('status', 'location')
    search_fields = ('code', 'name', 'barcode')
