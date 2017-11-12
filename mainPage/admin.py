from django.contrib import admin
from .models import *

class CustomPersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('fullName',)}

admin.site.register(CustomPerson, CustomPersonAdmin)
admin.site.register(TwitterAccount)
admin.site.register(Tweet)
