from os.path import join
from ChargeXML import chargeXML
class DateModifiedExtractor:
    def extract(self,idm,path):
        tree = chargeXML(join(path,'xml',str(idm)+'.xml'))
        return tree.find("photo").find("dates").attrib["lastupdate"]
