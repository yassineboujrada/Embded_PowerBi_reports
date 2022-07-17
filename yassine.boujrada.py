
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
            credentials=self.file
        )
        self.reports_service = self.CLIENT_POWER_BI.reports()
Authentification_for_PowerBI("x,xkkdkd","yassine.boujrada@gmail.com","nnb","ccdc","fjjf","yassine.boujrada)
    