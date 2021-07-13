# check_user_data.py

check_user_data.py is a simple script to lookup patron data in Alma.


# Use

This script does not include an interface, but can be modified to run as a command line script on a local machine, or else hosted as a Rundeck process or AWS lambda.

The script performs 2 operations, based on "search_type".
1 - Search all Alma users by last name (or other custom query).
2 - Search for a specific user by perm ID.

## Requirements

An Alma API key with USERS read permissions is needed.
Store the APIKEY in a local environmental variable called 'ALMA_PRODUCTION_API_KEY'.

## API Documentation
Retrieve Users API https://developers.exlibrisgroup.com/alma/apis/docs/users/R0VUIC9hbG1hd3MvdjEvdXNlcnM=/

Get Users Details API
https://developers.exlibrisgroup.com/alma/apis/docs/users/R0VUIC9hbG1hd3MvdjEvdXNlcnMve3VzZXJfaWR9/