from xlwt import Workbook
import makePyMatrix

def buildBook():
    book = Workbook()
    sheet1 = book.add_sheet('FFF')
    LT = getLatentTopics()
    imgIds = makePyMatrix.getImgIds()
    r = 1
    for L in LT:
        print "[DEBUG] Writing LT " + L.name
        i = 0
        for img in L.belongingVector:
            sheet1.write(r,0,L.name)
            sheet1.write(r,1,str(imgIds[i][0][0]))
            sheet1.write(r,2,img)
            i = i + 1
            r = r + 1
    book.save('tmp.xls')

class LatentTopic:
    imgDictionary = makePyMatrix.getImgDictionary()
    def __init__(self,name,belongingVector):
        self.name = name
        self.belongingVector = belongingVector
    def getBelongingDegree(self,imgId):
        return belongingVector[self.imgDictionary[str(imgId)]]
    
def getLatentTopics(numberOfTermsByLT = 5):
    Tt = makePyMatrix.getTtMatrix()
    H = makePyMatrix.getHMatrix()
    LT = []
    for i in range(len(Tt[0])):
        LTName = ""
        for j in range(numberOfTermsByLT):
            LTName += str(Tt[i][j][0]) + " - "
        LT.append(LatentTopic(LTName,H[i]))
    return LT

