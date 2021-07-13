#!/usr/bin/python3
import os
import requests
import pprint
from alma_helper.users import users

# vars
# store key as local environmental variable
api_key = os.environ.get('ALMA_PRODUCTION_API_KEY')

# search type
# uncomment the type of search you want to run
search_type = "find_users"
#search_type = "get_user_details"

# retrieve users ##############################################################
if search_type == "find_users":
    query = "last_name~hobbs"

    retrieved_users = users.RetrieveUsers(q=query, apikey=api_key)

    # check for errors
    if retrieved_users.errors.exist == True:
        print(retrieved_users.errors.message)
        exit()

    # display results
    for result in retrieved_users.results:
        print(result['last_name'])
        print(result['first_name'])
        print(result['primary_id'])
        print("--------------------------------------")

# get user details ############################################################
if search_type == "get_user_details":
    user_id = ""
    user = users.GetUserDetails(user_id=user_id, apikey=api_key)

    # check for errors
    if user.errors.exist == True:
        print(user.errors.message)
        exit()
    
    # display user details
    pprint.pprint(user.xml)