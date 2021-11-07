from django.contrib import admin
from .models import *

# Register your models here.
class Case_Proceeding_Details_Admin(admin.ModelAdmin):
    list_display = ('id','court_name','causelist_date','purpose','user_id')

class Case_Listing_Details_Admin(admin.ModelAdmin):
    list_display = ('id','case_listing_details')

class DRT_Case_Status_Report_Admin(admin.ModelAdmin):
    list_display = ('id','diary_no')

class SearchedDataAdmin(admin.ModelAdmin):
    list_display = ('id','drt_or_drat')

class Property_Details_Admin(admin.ModelAdmin):
    list_display = ('id','user_id','property_type','detail_of_property')

class Petitioner_Detail_Admin(admin.ModelAdmin):
    list_display = ('id','user_id','petitioner_details')

class Respondents_Details_Admin(admin.ModelAdmin):
    list_display = ('id','user_id','respondents_details')


admin.site.register(Case_Proceeding_Details_Model,Case_Proceeding_Details_Admin)
admin.site.register(Case_Listing_Details_Model,Case_Listing_Details_Admin)
admin.site.register(SearchedDataModel,SearchedDataAdmin)
admin.site.register(DRT_Case_Status_Report_Model,DRT_Case_Status_Report_Admin)
admin.site.register(Property_Details_Model,Property_Details_Admin)
admin.site.register(Petitioner_Detail_Model,Petitioner_Detail_Admin)
admin.site.register(Respondents_Details_Model,Respondents_Details_Admin)

