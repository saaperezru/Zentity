from extractMatlabMatrix import MatlabExtract
from os.path import join
class MostImportantLatentTopicExtractor:
    def __init__(self,LatentTopicsArray,path):
        self.LTs =  LatentTopicsArray
        MLExtract = MatlabExtract(join(path,'data'))
        self.sortedLT = MLExtract.getSortedLTMatrix()
        self.imgD = MLExtract.getImgDictionary()
        
    def extract(self,idm,path):
        imgMatrixID = self.imgD[str(idm)]
        latentTopicID = self.sortedLT[0][imgMatrixID]
        return self.LTs[latentTopicID-1].name
        
