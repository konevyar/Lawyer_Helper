from django.contrib import admin

# Register your models here.

from .models import Case, Court, Defendant, Plaintiff

admin.site.register(Case)
admin.site.register(Court)
admin.site.register(Defendant)
admin.site.register(Plaintiff)
