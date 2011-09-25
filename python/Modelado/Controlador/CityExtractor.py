from os.path import join
from ChargeXML import chargeXML
class CityExtractor:
    def extract(self,idm,path):
        tree = chargeXML(join(path,'xml',str(idm)+'.xml'))
        return tree.find("photo").find("location").find("locality").text
