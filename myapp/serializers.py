from rest_framework import serializers
from .models import *

class Case_Proceeding_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Case_Proceeding_Details_Model
        fields = '__all__'

class DRT_Case_Status_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DRT_Case_Status_Report_Model
        fields = '__all__'

class Searched_Data_Serializer(serializers.ModelSerializer):
    no_of_applicants = serializers.ReadOnlyField()
    class Meta:
        model = SearchedDataModel
        fields = ['drt_or_drat','party_name','no_of_applicants']

class Property_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Property_Details_Model
        fields = '__all__'

class Petitioner_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Petitioner_Detail_Model
        fields = '__all__'

class Respondents_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Respondents_Details_Model
        fields = '__all__'

class Case_Listing_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Case_Listing_Details_Model
        fields = '__all__'