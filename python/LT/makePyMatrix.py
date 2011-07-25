import scipy.io as sio
from numpy import *

def getFTMatrix(filename = 'Ft.mat'):
    return array(sio.loadmat(filename)['Ft'])
def getWTMatrix(filename = 'Wt.mat'):
    return array(sio.loadmat(filename)['Wt'])
def getHMatrix(filename = 'H.mat'):
    return array(sio.loadmat(filename)['Hv'])
def getFVMatrix(filename = 'Fv.mat'):
    return array(sio.loadmat(filename)['Fv'])
def getWVMatrix(filename = 'Wv.mat'):   
    return array(sio.loadmat(filename)['Wv'])
#Array wherrre the id of images are sorted as in Xv and Xt
def getTtMatrix(filename = 'Tt.mat'):
    return array(sio.loadmat(filename)['Tt'])
def getSortedLTMatrix(filename = 'SortedLT.mat'):
    return array(sio.loadmat(filename)['indexSortedLT'])
def getImgIds(filename = 'imgIds.mat'):
    return array(sio.loadmat(filename)['imgIdsTraining'])
def getImgDictionary(filename = 'imgIds.mat'):
    imgIndex = getImgIds(filename)
    imgDictionary = {}
    for i in range (len(imgIndex)):
    	imgDictionary[str(imgIndex[i][0][0].split(".")[0])]=i
    return imgDictionary
    
