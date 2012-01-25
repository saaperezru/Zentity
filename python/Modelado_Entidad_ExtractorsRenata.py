from ChargeXML import chargeXML
from os.path import join
from Modelado_Exception import *
class DescriptionExtractor:
    def __init__(self,path):
        self.path = path
    def extract(self,idm):
        try:
            tree = chargeXML(join(self.path,'xml',str(idm)+'.txt'))
            for f in tree.findall("field"):
                if (f.get("name")=="comentario"):
                    return f.text
        except:
            print "[ERROR] Error extracting " + str(idm) + " description"
        return "No description"

class ImageIdExtractor:
    def extract(self,idm):
        return idm
class LatentTopicExtractor:
    def __init__(self,LatentTopic):
        self.LT = LatentTopic

    def extract(self,idm):
        return self.LT.getBelongingDegree(idm)

class MostImportantLatentTopicExtractor:
    def __init__(self,TypeLatentTopic):
        self.TLT = TypeLatentTopic
        
    def extract(self,idm):
        return  self.TLT.getMostImportantLatentTopic(idm).name.replace("/","___").replace("-","__")

class TagExtractor:
    def __init__(self,tagValue,Xt):
        self.tagValue = tagValue
        self.Xt=Xt
    def extract(self,idm):
        if self.Xt.getFC(idm,self.tagValue):
            return "True"
        return "False"

class TitleExtractor:
    def __init__(self,path):
        self.path = path
    
    def extract(self,idm):
        try:
            tree = chargeXML(join(self.path,str(idm)+'.txt'))
            for f in tree.findall("field"):
                if (f.get("name")=="nombre"):
                    return f.text.split('.')[0]
        except:
            raise(ErrorModelado("[ERROR] Extraction of " + str(idm) + " title failed."))
        return "No title"
