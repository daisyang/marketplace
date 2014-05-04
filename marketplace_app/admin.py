from django.contrib import admin
from marketplace_app.models import Provider,School
# Register your models here.

class Provider_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Provider information',             {'fields': ['name','address','non_profit','rating']}),
        ('Advanced options', {'fields': ['website','contract','perception'], 'classes': ['collapse']}),
        ('School funded',               {'fields': ['target_schools','time_start','time_end','school_level','funding_amount']}),
        ]
    list_display =('name','address','non_profit','rating')

admin.site.register(Provider,Provider_Admin)

class School_Admin(admin.ModelAdmin):
    list_display= ('name','address','rating')
admin.site.register(School,School_Admin)

