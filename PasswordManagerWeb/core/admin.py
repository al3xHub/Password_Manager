from django.contrib import admin
from .models import Site

admin.site.site_header = "ADMIN DASHBOARD: Password Manager"


class AdminConfig(admin.ModelAdmin):
    list_display = ('website_name', 'created')
    exclude = ('website_password', 'master_password',)


# Register your models here.
admin.site.register(Site, AdminConfig)
