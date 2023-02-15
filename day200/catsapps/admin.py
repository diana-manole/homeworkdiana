from django.contrib import admin
from .models import Color,Cat,Kind,Behavor

# Register your models here.

admin.site.register(Kind)
admin.site.register(Color)
admin.site.register(Cat)
admin.site.register(Behavor)
