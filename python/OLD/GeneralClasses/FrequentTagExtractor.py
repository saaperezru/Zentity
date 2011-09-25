from ChargeXML import chargeXML
from os.path import join
class FrequentTagExtractor:
    def __init__(self,frequentTags):
        self.frequentTags = frequentTags
    def extract(self,idm,path):
        tree = chargeXML(join(path,'xml',str(idm)+'.xml'))
        for u in tree.find("photo").find("tags").getiterator("tag"):
            if (u.text in self.frequentTags):
                return u.text
        return "None"

