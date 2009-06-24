from fixmystreet.mainapp.models import Ward,ReportCategory, ReportCategoryClass, FaqEntry, Councillor
from django.contrib import admin
from transmeta import canonical_fieldname

class ReportCategoryClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(ReportCategoryClass,ReportCategoryClassAdmin)

class ReportCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'hint')

admin.site.register(ReportCategory, ReportCategoryAdmin)

class FaqEntryAdmin(admin.ModelAdmin):
    list_display = ('q', 'order')
#    prepopulated_fields = {'slug': ('q') }

admin.site.register(FaqEntry, FaqEntryAdmin)

class CouncillorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
    
admin.site.register(Councillor,CouncillorAdmin)


class WardAdmin(admin.ModelAdmin):
    list_display = ('id','city','number','name')
    ordering       = ['city', 'number']

    
admin.site.register(Ward,WardAdmin)
