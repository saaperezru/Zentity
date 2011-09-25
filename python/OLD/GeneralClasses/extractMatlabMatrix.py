import scipy.io as sio
from numpy import *
from os.path import join

class MatlabExtract:
    def __init__(self,path):
        self.path = path
    def getFTMatrix(self,filename = 'Ft.mat'):
        return array(sio.loadmat(join(self.path,filename))['Ft'])
    def getWTMatrix(self,filename = 'Wt.mat'):
        return array(sio.loadmat(join(self.path,filename))['Wt'])
    def getHMatrix(self,filename = 'H.mat'):
        return array(sio.loadmat(join(self.path,filename))['H_norm'])
    def getFVMatrix(self,filename = 'Fv.mat'):
        return array(sio.loadmat(join(self.path,filename))['Fv'])
    def getWVMatrix(self,filename = 'Wv.mat'):
        return array(sio.loadmat(join(self.path,filename))['Wv'])
    def getBsMatrix(self, filename = 'Bs.mat'):
        return array(sio.loadmat(join(self.path,filename))['Bs'])        

    #Array wherrre the id of images are sorted as in Xv and Xt
    def getTtMatrix(self,filename = 'Tt.mat'):
        return array(sio.loadmat(join(self.path,filename))['Tt'])
    def getSortedLTMatrix(self,filename = 'SortedLT.mat'):
        return array(sio.loadmat(join(self.path,filename))['indexSortedLT'])
    def getImgIds(self,filename = 'imgIds.mat'):
        return array(sio.loadmat(join(self.path,filename))['imgIdsTraining'])
    def getImgDictionary(self,filename = 'imgIds.mat'):
        imgIndex = self.getImgIds(filename)
        imgDictionary = {}
        for i in range (len(imgIndex)):
            imgDictionary[str(imgIndex[i][0][0].split(".")[0])]=i
        return imgDictionary
    
