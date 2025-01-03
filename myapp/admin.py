from django.contrib import admin
from .models import About, Portfolio, Blog

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    
admin.site.register(Portfolio)
admin.site.register(Blog)
