from ChargeXML import chargeXML
from os.path import join
class TagExtractor:
    def __init__(self,tagValue):
        self.tagValue = tagValue
    def extract(self,idm,path):
        tree = chargeXML(join(path,'xml',str(idm)+'.xml'))
        for u in tree.find("photo").find("tags").getiterator("tag"):
            if u.text==self.tagValue:
                return "True"
        return "False"
