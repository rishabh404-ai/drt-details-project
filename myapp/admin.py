from django.contrib import admin
from .models import *

# Register your models here.
class Case_Proceeding_Details_Admin(admin.ModelAdmin):
    list_display = ('id','user_id','court_name','causelist_date','purpose')

class Case_Listing_Details_Admin(admin.ModelAdmin):
    list_display = ('id','user_id','case_listing_details')

class DRT_Case_Status_Report_Admin(admin.ModelAdmin):
    list_display = ('id','user_id','diary_no','case_type','case_no','date_of_filling','applicant','respondent','applicant_advocate','respondent_advocate')

class SearchedDataAdmin(admin.ModelAdmin):
    list_display = ('id','drt_or_drat','party_name','no_of_applicants')

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

