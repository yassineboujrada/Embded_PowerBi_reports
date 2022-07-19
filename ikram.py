
import os
from powerbi.client import PowerBiClient
class Authentification_for_PowerBI:
    def __init__(self,client_id,user,passwd,tenant,client_secret,file):
        self.CLIENT_ID=client_id 
        self.username=user
        self.password=passwd
        self.TENANT_ID=tenant
        self.AUTHORITY_URL = 'https://login.microsoftonline.com/'+self.TENANT_ID
        self.SCOPE = ["https://analysis.windows.net/powerbi/api/.default"]
        self.URL_TO_GET_GROUPS = 'https://api.powerbi.com/v1.0/myorg/groups'
        self.file=file
        self.CLIENT_POWER_BI = PowerBiClient(
            client_id=self.CLIENT_ID,
            client_secret=client_secret,
            scope=['https://analysis.windows.net/powerbi/api/.default'],
            redirect_uri="https://localhost/redirect",
            credentials=os.getcwd()+"/dashbord/__pycache__/"+self.file
        )
        self.reports_service = self.CLIENT_POWER_BI.reports()
Authentification_for_PowerBI("ce8492a7-a1da-446f-9c4f-2ee088fcb8cb","ikram.elmbarki@datastory.ma","Netvistacape21.","d431bd02-0a6f-4274-a923-25ffdb02db40","HWg8Q~ODrBhdtIvU4lgy8O2PW~zALgmP2LgNHa4D","ikram.elmbarki.jsonc")
    