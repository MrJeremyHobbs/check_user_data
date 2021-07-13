#!/usr/bin/python3
from alma_helper import http
from alma_helper import errors
from lxml import objectify
import xmltodict

# Documentation
# https://developers.exlibrisgroup.com/alma/apis/users/

class RetrieveUsers():
    def __init__(self, limit="100", offset="0", q="", order_by="last_name,first_name,primary_id", 
                 source_institution_code= "", source_user_id="", apikey=""):
            self.RetrieveUsers = RetrieveUsers

            self.base_url = f'https://api-na.hosted.exlibrisgroup.com/almaws/v1/users'
            self.url = f'{self.base_url}?limit={limit}&offset={offset}&q={q}&order_by={order_by}&apikey={apikey}'

            self.r = http.retrieve_xml(url=self.url, method="get")
            self.xml = self.r.text

            # Check for errors in Response object.
            self.errors = errors.Errors(self.r)

            # Parse return
            if self.errors.exist is False:
                self.xml = self.r.text
                self.dict = xmltodict.parse(self.xml, dict_constructor=dict)
                self.total_record_count = int(self.dict['users']['@total_record_count'])
                self.xml_bytes = bytes(self.xml, encoding="utf-8")
                self.object = objectify.fromstring(self.xml_bytes)
                
                self.found = True

                # human readable result set
                if self.total_record_count == 1:
                    self.results = []
                    result = {
                        'first_name': self.dict['users']['user']['first_name'],
                        'last_name': self.dict['users']['user']['last_name'],
                        'primary_id': self.dict['users']['user']['primary_id'],
                    }
                    self.results.append(result)

                if self.total_record_count > 1:
                    self.results = []
                    for user in self.dict['users']['user']:
                        result = {
                            'first_name': user['first_name'],
                            'last_name': user['last_name'],
                            'primary_id': user['primary_id'],
                        }
                        self.results.append(result)


            else:
                self.found = False


class GetUserDetails():
    def __init__(self, user_id, user_id_type="all_unique", view="full", expand="none", 
                 source_institution_code= "", apikey=""):
            self.GetUserDetails = GetUserDetails

            self.base_url = f'https://api-na.hosted.exlibrisgroup.com/almaws/v1/users/{user_id}'
            self.url = f'{self.base_url}?user_id_type={user_id_type}&view={view}&expand={expand}&apikey={apikey}'

            self.r = http.retrieve_xml(url=self.url, method="get")
            self.xml = self.r.text

            # Check for errors in Response object.
            self.errors = errors.Errors(self.r)

            # Parse return
            if self.errors.exist is False:
                self.xml = self.r.text
                self.dict = xmltodict.parse(self.xml, dict_constructor=dict)
                self.xml_bytes = bytes(self.xml, encoding="utf-8")
                self.object = objectify.fromstring(self.xml_bytes)
                
                self.found = True
            else:
                self.found = False

class UpdateUserDetails():
    def __init__(self, user_id, user_id_type="all_unique", send_pin_number_letter="false", 
                 recalculate_roles="false", source_institution_code= "", user_xml="", apikey=""):
            self.UpdateUserDetails = UpdateUserDetails
            self.base_url = f'https://api-na.hosted.exlibrisgroup.com/almaws/v1/users/{user_id}'
            self.url = f'{self.base_url}?user_id_type={user_id_type}&send_pin_number_letter={send_pin_number_letter}&recalculate_roles={recalculate_roles}&apikey={apikey}'

            self.r = http.retrieve_xml(url=self.url, method="put", xml=user_xml)
            #print(self.r)
            self.xml = self.r

            # Check for errors in Response object.
            self.errors = errors.Errors(self.r)

            # Parse return
            if self.errors.exist is False:
                self.xml = self.r
                self.dict = xmltodict.parse(self.xml, dict_constructor=dict)
                self.xml_bytes = bytes(self.xml, encoding="utf-8")
                self.object = objectify.fromstring(self.xml_bytes)