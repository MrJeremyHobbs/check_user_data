#!/usr/bin/python3
import requests

def retrieve_xml(url="", method="get", params="", xml=""):
    method = method.lower()
    
    if method == "get":
        r = requests.get(url, params)
        return r

    if method == "post":
        pass

    if method == "put":
        headers = {'Content-Type': 'application/xml', 'charset':'UTF-8'}
        r = requests.put(url, data=xml.encode('utf-8'), headers=headers).text
        return r

    if method == "delete":
        pass

    if method == "patch":
        pass
    
    else:
        return None