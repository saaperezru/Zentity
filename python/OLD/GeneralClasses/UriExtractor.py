from os.path import join
from ChargeXML import chargeXML
class UriExtractor:
    def extract(self,idm,path):
        tree = chargeXML(join(path,'xml',str(idm)+'.xml'))
        for u in tree.find("photo").find("urls").getiterator("url"):
            if u.attrib["type"]=="photopage":
                return u.text
