import urequests
import secrets

class ThingSpeakApi:
    def __init__(self):
        self.server = secrets.server
        self.apikey = secrets.write_api
        
    def WriteData(self, field, fieldvalue):
        url = f"{self.server}/update?api_key={self.apikey}&field{field}={fieldvalue}"
        request = urequests.post(url)
        request.close()
        
    def WriteMultipleFields(self, field_data):
        url = f"{self.server}/update?api_key={self.apikey}"
        i = 1
        for field_val in field_data:
            url = url + f"&field{i}={field_val}"
            i = i + 1
        request = urequests.post(url)
        request.close()