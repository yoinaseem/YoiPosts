from django.contrib import admin
from .models import Mz_Post
# Register your models here.
class MzPostAdmin (admin.ModelAdmin):
	pass
admin.site.register(Mz_Post, MzPostAdmin)