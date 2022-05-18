# import msal
# import requests
# import json
# from pprint import pprint

# # --------------------------------------------------
# # Set local variables
# # --------------------------------------------------
# client_id='5ddb532c-2735-4570-adc2-32eacfd30068'
# username="yassineboujrada@datastory453.onmicrosoft.com"
# password="yassine@2002"

# authority_url = 'https://login.microsoftonline.com/a23b80fb-03cf-48e7-b7ea-4a9094cff16c'
# scope = ["https://analysis.windows.net/powerbi/api/.default"]
# url_groups = 'https://api.powerbi.com/v1.0/myorg/groups'

# # --------------------------------------------------
# # Use MSAL to grab a token
# # --------------------------------------------------
# app = msal.PublicClientApplication(client_id, authority=authority_url)
# result = app.acquire_token_by_username_password(username=username,password=password,scopes=scope)

# # --------------------------------------------------
# # Check if a token was obtained, grab it and call the
# # Power BI REST API, otherwise throw up the error message
# # --------------------------------------------------
# if 'access_token' in result:
#     access_token = result['access_token']
#     header = {'Content-Type':'application/json','Authorization': f'Bearer {access_token}'}
#     api_out = requests.get(url=url_groups, headers=header)
#     pprint(api_out.json())
# else:
#     print(result.get("error"))
#     print(result.get("error_description"))
 
