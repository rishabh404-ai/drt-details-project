from selenium import webdriver
import time
import urllib.request
import easyocr
import os
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import json
from myapp.models import SearchedDataModel, Case_Proceeding_Details_Model, Case_Listing_Details_Model,DRT_Case_Status_Report_Model, Property_Details_Model, Petitioner_Detail_Model,Respondents_Details_Model 

def fetch_unique_id(js_unique_id_string):
    search_string = str(js_unique_id_string)
    start = search_string.find("('") + len("('")
    end = search_string.find("')")
    unique_id = search_string[start:end]
    print('UNIQUE_ID ===>', unique_id)
    return unique_id


def fetch_property_details(unique_id,tablr_data_3_txt):
    with open("property_data.txt", "a") as o:
        o.write(tablr_data_3_txt)
    lst = []
    property_file = open("property_data.txt")
    for line in property_file:
        lst.append(line)

    lst_of_data = lst[2:]
    if lst_of_data:
        for line in lst_of_data:
            x = line.rstrip()
            y = x.split()
            merge_data = ' '.join([str(elem) for elem in y[2:]])
            data = {'Property Type': y[0], 'Detail Of Property': ' '.join([str(elem) for elem in y[1:]])}
            Property_Details_Model.objects.create(user_id=unique_id,property_type=data['Property Type'],detail_of_property=data['Detail Of Property']) 

    else:
        data = {'Property Type': '', 'Detail Of Property': ''}
        Property_Details_Model.objects.create(user_id=unique_id,property_type=data['Property Type'],detail_of_property=data['Detail Of Property']) 

    os.remove("property_data.txt")
    print('----------------------------------------------------------')


def fetch_case_proceeding_details(unique_ids_and_no_of_applicants):
    data = unique_ids_and_no_of_applicants
    UNIQUE_ID_LISTS = data['unique_ids']

    for unique_id in UNIQUE_ID_LISTS:
        web = webdriver.Chrome()
        web.get(f'https://drt.gov.in/drtlive/Misdetailreport.php?no={unique_id}')
        tablr_data_2 = web.find_element_by_xpath('/html/body/div/form/font/table[4]')
        x = tablr_data_2.text
        lst = []
        with open("data.txt", "a") as o:
            o.write(x)
        a_file = open("data.txt")

        for line in a_file:
            lst.append(line)

        lst_of_data = lst[2:]

        if lst_of_data:
            for line in lst_of_data:
                x = line.rstrip()
                y = x.split()
                merge_data = ' '.join([str(elem) for elem in y[2:]])
               
                data = {'Court Name': y[0], 'Causelist Date': y[1], 'Purpose': merge_data}
                Case_Proceeding_Details_Model.objects.create(user_id=unique_id,court_name=data['Court Name'],causelist_date=data['Causelist Date'],purpose=data['Purpose'])
               
        else:
            data = {'Court Name': '', 'Causelist Date': '', 'Purpose': ''}
            Case_Proceeding_Details_Model.objects.create(user_id=unique_id,court_name=data['Court Name'],causelist_date=data['Causelist Date'],purpose=data['Purpose'])
            
        os.remove("data.txt")
        print('----------------------------------------------------------')

        tablr_data_3 = web.find_element_by_xpath('/ html / body / div / form / font / table[3] / tbody')
        tablr_data_3_txt = tablr_data_3.text
        fetch_property_details(unique_id,tablr_data_3_txt)

        tablr_data_2 = web.find_element_by_xpath('/ html / body / div / form / font / table[2] / tbody / tr[2] / td')
        petitioner_details_data = tablr_data_2.text

        p_lst = []
        r_lst=[]
        c_lst = []

        with open("petitioner_details_data.txt", "a") as o:
            o.write(petitioner_details_data)
        p_file = open("petitioner_details_data.txt")
        for line in p_file:
            x = line.rstrip()
            p_lst.append(x)
        Petitioner_Detail_Model.objects.create(user_id=unique_id,petitioner_details=p_lst)
        os.remove('petitioner_details_data.txt')


        tablr_data_1 = web.find_element_by_xpath('/html/body/div/form/font/table[2]/tbody/tr[4]/td')
        respondents_details = tablr_data_1.text
        with open("respondents_details.txt", "a") as o:
            o.write(respondents_details)
        r_file = open("respondents_details.txt")
        for line in r_file:
            x = line.rstrip()
            r_lst.append(x)
        Respondents_Details_Model.objects.create(user_id=unique_id,respondents_details=r_lst)
        os.remove('respondents_details.txt')


        tablr_data_0 = web.find_element_by_xpath('/html/body/div/form/font/table[1]/tbody')
        case_listing_details = tablr_data_0.text       
        with open("case_listing_details.txt", "a") as o:
            o.write(case_listing_details)
        c_file = open("case_listing_details.txt")
        for line in c_file:
            x = line.rstrip()
            c_lst.append(x)
        case_listing_details = c_lst[6:]
        Case_Listing_Details_Model.objects.create(user_id=unique_id,case_listing_details=case_listing_details)
        os.remove('case_listing_details.txt')

        web.quit()


def create_searched_data(drt,party_name,number_of_applicants):     
    SearchedDataModel.objects.create(drt_or_drat=drt,party_name=party_name,no_of_applicants=number_of_applicants)


def run_scrapping_automation(drt_or_drat,party_name,number_of_applicants):
    
    web = webdriver.Chrome()
    web.get('https://drt.gov.in/front/page1_advocate.php')
    time.sleep(2)

    PARTY = party_name
    party_name = web.find_element_by_xpath('//*[@id="name"]')
    party_name.send_keys(PARTY)

    DRT = drt_or_drat
    drt_name = web.find_element_by_xpath('//*[@id="schemaname"]')
    drt_name.send_keys(DRT)

    given_captcha_name = web.find_element_by_xpath('//*[@id="captchatext"]/img')
    captcha_name = web.find_element_by_xpath('//*[@id="captchatext"]/input')
    src = given_captcha_name.get_attribute('src')
    with open('captcha.png', 'wb') as file:
        file.write(web.find_element_by_xpath('//*[@id="captchatext"]/img').screenshot_as_png)
    reader = easyocr.Reader(['ch_sim','en'])
    result = reader.readtext('captcha.png')
    fetch_captcha_text = reader.readtext('captcha.png', detail = 0)
    CAPCTHA = int(' '.join([str(elem) for elem in fetch_captcha_text]))
    captcha_name.send_keys(CAPCTHA)
    os.remove('captcha.png')

    SUBMIT = web.find_element_by_xpath('//*[@id="submit1"]')
    SUBMIT.click()

    table = web.find_element_by_xpath('/html/body/div[1]/div/form/div[5]/div/div[2]/table/thead/tr')
    header = table.find_elements_by_tag_name('th')
    body = table.find_element_by_xpath('/html/body/div[1]/div/form/div[5]/div/div[2]/table/tbody')
    cells = body.find_elements_by_tag_name('tr')

    if cells:
        unique_ids_lst = [] 
        for cell in cells:
            searched_data_lst = []
            data = cell.find_elements_by_tag_name('td')
            for item in data:
                print(item.text)
                searched_data_lst.append(item.text)           
                if item.text == 'MORE DETAIL':
                    href = item.find_element_by_tag_name('a')
                    print('UNIQUE_ID_STRING ===>',href.get_attribute('href'))
                    js_unique_id_string = str(href.get_attribute('href'))
                    number_of_applicants+=1
                    unique_id = fetch_unique_id(js_unique_id_string)      
                    drt_case_status_report = DRT_Case_Status_Report_Model.objects.create(user_id=unique_id)
                    drt_case_status_report.save()
                    drt_case_status_report_id = drt_case_status_report.id   
                    unique_ids_lst.append(unique_id)                    
                    

            # DJANGO TO ADD ==> Diary No.	Case Type	Case No.	Date of Filing	Applicant	Respondent	Applicant Advocate	Respondent Advocate
            diary_no = searched_data_lst[0]
            case_type =searched_data_lst[1]
            case_no =searched_data_lst[2]
            date_of_filling =searched_data_lst[3]
            applicant =searched_data_lst[4]
            respondent =searched_data_lst[5]
            applicant_advocate =searched_data_lst[6]
            respondent_advocate =searched_data_lst[7]
            DRT_Case_Status_Report_Model.objects.filter(pk=drt_case_status_report_id).update(
                                                diary_no = diary_no,
                                                case_type = case_type,
                                                case_no = case_no,
                                                date_of_filling = date_of_filling, 
                                                applicant = applicant,
                                                respondent = respondent,
                                                applicant_advocate = applicant_advocate,
                                                respondent_advocate = respondent_advocate
                                            )
            drt_case_status_report_id = drt_case_status_report.id                          
            print('-----------------------')           

        create_searched_data(DRT,PARTY,number_of_applicants)
        unique_ids_and_no_of_applicants = {'unique_ids':unique_ids_lst,'no_of_applicants':number_of_applicants}
        fetch_case_proceeding_details(unique_ids_and_no_of_applicants)

    else:
        unique_ids_lst = []
        
    web.quit()    
    return {'unique_ids_lst':unique_ids_lst, 'number_of_applicants':number_of_applicants}
