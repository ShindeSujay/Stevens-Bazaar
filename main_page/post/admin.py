from django.contrib import admin

# Register your models here.
from .models import PostTable

class AdPostAdmin(admin.ModelAdmin):
    class Meta:
        model = PostTable
        
        
admin.site.register(PostTable, AdPostAdmin)
