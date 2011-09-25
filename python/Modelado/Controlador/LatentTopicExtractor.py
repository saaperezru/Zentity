class LatentTopicExtractor:
    def __init__(self,LatentTopic):
        self.LT = LatentTopic

    def extract(self,idm,path):
        return self.LT.getBelongingDegree(idm)
