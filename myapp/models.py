from django.db import models

# Create your models here.

class SearchedDataModel(models.Model):
    drt_or_drat = models.CharField(max_length=200,null=True,blank=True)
    party_name = models.CharField(max_length=200,null=True,blank=True)
    no_of_applicants = models.IntegerField(null=True,blank=True)

class DRT_Case_Status_Report_Model(models.Model):
    user_id = models.CharField(max_length=200,null=True,blank=True)
    diary_no = models.CharField(max_length=200,null=True,blank=True)
    case_type = models.CharField(max_length=200,null=True,blank=True)
    case_no = models.CharField(max_length=200,null=True,blank=True)
    date_of_filling = models.CharField(max_length=200,null=True,blank=True)
    applicant = models.CharField(max_length=200,null=True,blank=True)
    respondent = models.CharField(max_length=200,null=True,blank=True)
    applicant_advocate = models.CharField(max_length=200,null=True,blank=True)
    respondent_advocate = models.CharField(max_length=200,null=True,blank=True)

class Property_Details_Model(models.Model):
    user_id = models.CharField(max_length=200,null=True,blank=True)
    property_type = models.CharField(max_length=200,null=True,blank=True)
    detail_of_property = models.CharField(max_length=200,null=True,blank=True)

class Case_Proceeding_Details_Model(models.Model):
    user_id = models.CharField(max_length=200,null=True,blank=True)
    court_name = models.CharField(max_length=200,null=True,blank=True)
    causelist_date = models.CharField(max_length=200,null=True,blank=True)
    purpose = models.CharField(max_length=200,null=True,blank=True)

class Petitioner_Detail_Model(models.Model):
    user_id = models.CharField(max_length=200,null=True,blank=True)
    petitioner_details = models.TextField(null=True,blank=True)

class Respondents_Details_Model(models.Model):
    user_id = models.CharField(max_length=200,null=True,blank=True)
    respondents_details = models.TextField(null=True,blank=True)

class Case_Listing_Details_Model(models.Model):
    user_id = models.CharField(max_length=200,null=True,blank=True)
    case_listing_details = models.TextField(null=True,blank=True)


