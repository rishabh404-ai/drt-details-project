from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response 
from .models import *
from .serializers import *
from .services.web_scrape_and_automation import *

# Create your views here.
class ViewDRTDataViewSet(viewsets.ViewSet):
    queryset = SearchedDataModel.objects.none()
    serializer_class = Searched_Data_Serializer    

    def list(self,request,*args,**kwargs):
       drt_or_drat = str(self.request.query_params.get('drt_or_drat'))
       party_name = str(self.request.query_params.get('party_name'))

       unique_ids = run_scrapping_automation(drt_or_drat,party_name,0)  
       number_of_applicants = unique_ids['number_of_applicants']

       if (unique_ids['unique_ids_lst']) and (number_of_applicants != 0):     
            drt_case_status_data_details = []
            drt_case_proceeding_details = []
            drt_case_property_details = []
            drt_case_petitioner_details = []
            drt_case_respondents_details = []
            drt_case_listing_details = []
            
            unique_ids_lst = unique_ids['unique_ids_lst']       

            for unique_id in unique_ids_lst:
                check = DRT_Case_Status_Report_Model.objects.filter(user_id=unique_id)
                if check:
                    queryset_1 = DRT_Case_Status_Report_Model.objects.filter(user_id=unique_id)
                    serializer_1 = DRT_Case_Status_Report_Serializer(queryset_1, many=True)
                    data_1 = serializer_1.data
                    drt_case_status_data_details.append(data_1)  

                    queryset_2 = Case_Proceeding_Details_Model.objects.filter(user_id=unique_id)
                    serializer_2 = Case_Proceeding_Details_Serializer(queryset_2, many=True)
                    data_2 = serializer_2.data
                    drt_case_proceeding_details.append(data_2)  

                    queryset_3 = Property_Details_Model.objects.filter(user_id=unique_id)
                    serializer_3 = Property_Details_Serializer(queryset_3, many=True)
                    data_3 = serializer_3.data
                    drt_case_property_details.append(data_3)  

                    queryset_4 = Petitioner_Detail_Model.objects.filter(user_id=unique_id)
                    serializer_4 = Petitioner_Details_Serializer(queryset_4, many=True)
                    data_4 = serializer_4.data
                    drt_case_petitioner_details.append(data_4)  

                    queryset_5 = Respondents_Details_Model.objects.filter(user_id=unique_id)
                    serializer_5 = Respondents_Details_Serializer(queryset_5, many=True)
                    data_5 = serializer_5.data
                    drt_case_respondents_details.append(data_5)

                    queryset_6 = Case_Listing_Details_Model.objects.filter(user_id=unique_id)
                    serializer_6 = Case_Listing_Details_Serializer(queryset_6, many=True)
                    data_6 = serializer_6.data
                    drt_case_listing_details.append(data_6)

            return Response({
                            'status' : 'success',
                            'message': 'Data fetched successfully',
                            'drt_or_drat':drt_or_drat,
                            'party_name':party_name,
                            'number_of_applicants_found':number_of_applicants,
                            'data':({'drt_case_status_details_data':drt_case_status_data_details},
                                    {'drt_case_property_details_data':drt_case_property_details},
                                    {'drt_case_petitioner_details_data':drt_case_petitioner_details},                              
                                    {'drt_case_respondents_details_data':drt_case_respondents_details},
                                    {'drt_case_listing_details_data':drt_case_listing_details},
                                    {'drt_case_proceeding_details_data':drt_case_proceeding_details})
                            },status=status.HTTP_201_CREATED) 
     
       else:
           return Response({
                            'status' : 'success',
                            'message': 'No Data Found',
                            'drt_or_drat':drt_or_drat,
                            'party_name':party_name,
                            'number_of_applicants_found':number_of_applicants,
                            'data':[]
                        },status=status.HTTP_201_CREATED) 
