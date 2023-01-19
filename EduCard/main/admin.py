from django.contrib import admin
from .models import *

#class cacoca(admin.ModelAdmin):
    #prepopulated_fields = {"slug":("name",)}

admin.site.register(Themes)
admin.site.register(Classes)
admin.site.register(Subjects)
admin.site.register(Items)
admin.site.register(Tags,)#cacoca)



