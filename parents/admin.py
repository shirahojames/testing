from django.contrib import admin
from .models import Parent, Child


class ParentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Parent, ParentAdmin)

admin.site.register(Child)
# Register your models here.
