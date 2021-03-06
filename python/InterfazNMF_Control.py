import numpy as np
#from pylab import *
from InterfazNMF_Model import LatentTopic
from InterfazNMF_Model import TypeLatentTopic

class ControlTypeLatentTopic:
    """Control entity whose function is to be a layer between the user and TypeLatentTopic model, 
    also it will be the only thing the user can see and use to access and work with the model.

    Asymmetric Factorization
    X  = F1*H = X*W1*H
        
    X' = F2*H = X'W2*H
	
    Parameters
    ----------
    id : int,
        ID of the TypeLatentTopic
    name: String 
        Name of the TypeLatentTopic. 
    abreviature: String
        Abreviature of the TypeLatentTopic.
    LD: List of String or Documents, optional
        List of Documents 
    H: array or matrix, 
        Representation Matrix.
    F1: array or matrix, 
        Basis Matrix.
    W1: array or matrix, 
        Basis Matrix in terms of the documents (Documents vs Latent Topics).
    F2: array or matrix, 
        Basis Matrix of the second matrix on the Asymmetric Factorization.
    W2: array or matrix, 
        Basis Matrix in terms of the documents (Documents vs Latent Topics) on the Asymmetric Factorization.
	
    Attributes
    ----------
        arrayControlLatentTopics : List of ControlLatentTopics who are correlated for the same list of documents.
        typeLatentTopic : TypeLatentTopic entity. 	
    """
    def __init__(self, id, name, abreviature, LD, H, F1, W1, F2, W2):
        
        #Review matrix type.
        
        if not self.correctClass(H):
            raise ClassError("H matrix is not a numpy array or a numpy matrix")
        if not self.correctClass(F1):
            raise ClassError("F matrix is not a numpy array or a numpy matrix")
        if not self.correctClass(LD):
            raise ClassError("The list of document is not a numpy array or a numpy matrix")
        if W1!=None:
            if not self.correctClass(W1):
                raise ClassError("W matrix is not a numpy array or a numpy matrix")
        if F2!=None:
            if not self.correctClass(F2):
                raise ClassError("Assymetric F matrix is not a numpy array or a numpy matrix")
        if W2!=None:
            if not self.correctClass(W2):
                raise ClassError("Assymetric W matrix is not a numpy array or a numpy matrix")
        
        if(LD.shape[0] < LD.shape[1]):
            LD = np.transpose(LD)
        if(LD.shape[1] != 1):
            raise SizeError("Document List is not a vector")
        
        #Review the dimensions of each matrix.
        if not self.correctDimensions(LD, H, F1, W1, F2, W2):
            raise SizeError("Document List is not a vector")

        #Attributes initialization.  
        self.__arrayControlLatentTopics=[]
        LLD =[]
        for i in  LD.tolist():
            LLD.append(i[0][0])
        self.__typeLatentTopic=TypeLatentTopic(id, name, abreviature, self.createDictionary(LLD))
        #ControlLatentTopics creation.
        for i in xrange(H.shape[0]):
            belongingVector = self.normalize(H[i]).tolist()
            sortedbelongingVector = self.sortVector(self.normalize(H[i])).tolist()
            sortedbelongingVector.reverse() 
            representativeWords = self.normalize(np.transpose(F1)[i]).tolist()
            sortedIndexRepresentativeWords = self.sortVector(np.array(np.transpose(F1)[i])).tolist()
            sortedIndexRepresentativeWords.reverse()
            if W1!= None:
                representativeDocuments = self.normalize(np.transpose(W1)[i]).tolist()
                sortedIndexRepresentativeDocuments = self.sortVector(np.transpose(W1)[i]).tolist()
                sortedIndexRepresentativeDocuments.reverse()
            else:
                representativeDocuments = None
                sortedIndexRepresentativeDocuments = None
            if F2!=None:
                resumeWords = self.normalize(np.transpose(F2)[i]).tolist()
                sortedIndexResumeWords = self.sortVector(np.transpose(F2)[i]).tolist()
                sortedIndexResumeWords.reverse()
            else:
                resumeWords = None
                sortedIndexResumeWords = None
            if W2!=None:
                resumeDocuments = self.normalize(np.transpose(W2)[i]).tolist()
                sortedIndexResumeDocuments = self.sortVector(np.transpose(W2)[i]).tolist()
                sortedIndexResumeDocuments.reverse()
            else:
                resumeDocuments = None
                sortedIndexResumeDocuments = None   
            CLT=ControlLatentTopic(i, belongingVector, sortedbelongingVector, representativeWords, sortedIndexRepresentativeWords, representativeDocuments, sortedIndexRepresentativeDocuments, resumeWords, sortedIndexResumeWords, resumeDocuments, sortedIndexResumeDocuments, self)
            self.__arrayControlLatentTopics.append(CLT)
                

    def correctDimensions(self, LD, H, F1, W1, F2, W2):
        """ Check if the matrix dimensions are related to each.
            return:
                True if the dimensions between matrix are ok, False otherwise. 
        """
        mi = min(H.shape[0],F1.shape[1])
        ma = max(H.shape[0],F1.shape[1])
        if(W1!=None):
            mi = min(mi,W1.shape[1])
            ma = max(ma,W1.shape[1])
        if(F2!=None):
            mi = min(mi,F2.shape[1])
            ma = max(ma,F2.shape[1])
        if(W2!=None):
            mi = min(mi,W2.shape[1])
            ma = max(ma,W2.shape[1])
        if(mi!=ma):
            return False
        mi = min(H.shape[1],LD.shape[0])
        ma = max(H.shape[1],LD.shape[0])
        if(W1!=None):
            mi = min(mi,W1.shape[0])
            ma = max(ma,W1.shape[0])
        if(W2!=None):
            mi = min(mi,W2.shape[0])
            ma = max(ma,W2.shape[0])
        if(mi!=ma):
            return False
        return True

        
    def correctClass(self, M):
        """ Check the type of the parameter.
            return:
                True if the parameter M is a matrix or an array, False otherwise. 
        """
        if type(M) == type(np.array([])) or type(M) == type(np.matrix([])):
            return True
        else:
            return False


    def normalize(self, M):
        """ Normalize M vector.
            return:
                M vector with |M|=1. 
        """ 
        if self.correctClass(M):
            s=sum(M)
	    Mt=M/s
	    return Mt
        else:
            raise ClassError("The given matrix is not a numpy matrx or a nupy array")

    def sortVector(self, M):
        """ Sort the index of a M vector depending on M.
            return:
                Vector with the sorted index. 
        """
        if self.correctClass(M):
            return np.argsort(M) 
        else:
            raise ClassError("The given matrix is not a numpy matrx or a nupy array")
        

    def createDictionary(self, LD):
        """ Create a dictionary mapping between the list of documents and his position.
            Where the key is LD[i] and the object is the number i, which is the id-column of the 
            ith document of the representation matrix.   
        """
        x=range(len(LD))
        return  dict(zip(LD, x))
    

    def getDictionary(self,imaged):
        """ Given a id of a document check on the dictionary his position. 
            return:
               i if the parameter imaged is a key of the dictionary, None otherwise.
        """
        return  self.__typeLatentTopic.getDictionary(imaged)
 

    def getLatentTopicsForImg(self,identificador):
        """ Return a sorted list of ControlLatenTopics. The other depends of the belong degree of the Latent Topic to the document.
        """
        return sorted(self.__arrayControlLatentTopics, key=lambda ControlLatentTopic: ControlLatentTopic.getBelongingDegree(identificador), reverse=True) 
    

    def getMostImportantLatentTopicForImg(self,identificador):
        """ Return a ControlLatenTopics with the highest belong degree of the Latent Topics to the document."""
        return max(self.__arrayControlLatentTopics, key=lambda ControlLatentTopic: ControlLatentTopic.getBelongingDegree(identificador))


    def getControlArrayLatentTopics(self):
        """ Return the list of ControlLatenTopics."""
        return self.__arrayControlLatentTopics


    def getSizeDictionary(self):
        """ Return the length of the dictionary."""
        return self.__typeLatentTopic.getSizeDictionary() 


    def setTypeLatantTopicId(selsf, ids):
        """ Change the TypeLatentTopic id."""
        self.__typeLatentTopic.setId(ids)
    

    def setTypeLatantTopicName(self, name):
        """ Change the TypeLatentTopic name."""
        self.__typeLatentTopic.setName(name)
    

    def setTypeLatantTopicAbreviature(self, Abreviature):
        """ Change the TypeLatentTopic abreviature."""
        self.__typeLatentTopic.setAbreviature(Abreviature)


    def getTypeLatantTopicId(self):
        """ Get the TypeLatentTopic id."""
        return self.__typeLatentTopic.getId()
    

    def getTypeLatantTopicName(self):
        """ Get the TypeLatentTopic name."""
        return self.__typeLatentTopic.getName()
    

    def getTypeLatantTopicAbreviature(self):
        """ Get the TypeLatentTopic abreviature."""
        return self.__typeLatentTopic.getAbreviature()



class ControlLatentTopic:
    """Control entity whose function is to be a layer between the user and LatentTopic model, 
    also it will be the only thing the user can see and use to access and work with the model.

	
    Parameters
    ----------
    id : int,
        ID of the LatentTopic
    name: String 
        Name of the LatentTopic.
    H: array or matrix, 
        Vector of belonging degrees of each Document to the Latent Topic.
    F1: array or matrix, 
        Basis of the Latent Topic.
    W1: array or matrix, 
        Basis of the Latent Topic in terms of the documents.
    F2: array or matrix, 
        Basis of the Latent Topic on the Asymmetric Factorization.
    W2: array or matrix, 
        Basis of the Latent Topic in terms of the documents on the Asymmetric Factorization.
	
    Attributes
    ----------
        controlTypeLatentTopic : ControlTypeLatentTopic control entity.
        latentTopic : LatentTopic entity. 	
	
    Example
    -------
    """   
    def __init__(self, id, H, HI, F1, IF1, W1, IW1, F2, IF2, W2, IW2, CTLT):
        self.__latentTopic=LatentTopic(id, "", H, HI, F1, IF1, W1, IW1, F2, IF2, W2, IW2)
        self.__controlTypeLatentTopic=CTLT

    

    def getBelongingDegree(self,identificador):
        """ Return the belong degree of the document, -1 if the document is not on the dictionary.
            That means the document was not on the initial list of documents.
        """
        id=self.__controlTypeLatentTopic.getDictionary(identificador)
        if id!=None:
            return self.__latentTopic.getBelongingVector(id)
        else:
            return -1



    def getModalResume(self, type=True):
        """Return a sorted index list of the array representativeWords or resumeWords."""
        if type:
            return self.__latentTopic.getSortedIndexRepresentativeWords()
        else:
            return self.__latentTopic.getSortedIndexResumeWords()

    

    def getDocumentResume(self, type=1):
        """Return a sorted index list of the array representativeDocuments or resumeDocuments."""
        if type == 1:
            return self.__latentTopic.getSortedIndexBelongingVector()
        if type == 2:
            return self.__latentTopic.getSortedIndexReoresentativeDocuments()
        return self.__latenTopic.getSortedIndexResumeDocuments()
        

    
    def setLatantTopicName(self, name):
        """ Change the LatentTopic name."""
        self.__latentTopic.setName(name)



    def getLatantTopicName(self):
        """ Change the LatentTopic name."""
        return self.__latentTopic.getName()



    def getLatantTopicId(self):
        """ Change the LatentTopic name."""
        return self.__latentTopic.getId()




class LTRelation:

    @staticmethod
    def createMatrix(LD,LT1,LT2):
        """Create and return a matrix M(ControlLatentTopic list(LT1) vs ControlLatentTopic list(LT2)) 
           where each i,j s is the number of documents where the ith latent topic was the most important
           in the LT1 list, and the jth latent topic was the most important in the LT2 list.
   	        
           If for a document the belonging degree is not define this does not count.
	"""    
	x=len(LT1)
        y=len(LT2)
        
	matirx = np.zeros((x,y))
        
	for data in LD:
            CLT=LTRelation.getMostImportantLatentTopic(data, LT1)
            if CLT!=None:
                i= LT1.index(CLT)
                CLT=LTRelation.getMostImportantLatentTopic(data, LT2)
                if CLT!=None:
                    j= LT2.index(CLT)
                    matirx[i,j]=matirx[i,j]+1
	return matirx
    
    
    @staticmethod
    def getMostImportantLatentTopic(id, LT):
        """Return the most important latent topic in the LT  list for a id document.
           If for a document the belonging degree is not define return None.  
        """ 
        CLT=min(LT, key=lambda ControlLatentTopic: ControlLatentTopic.getBelongingDegree(id))
        if CLT.getBelongingDegree(id)>=0:
            return max(LT, key=lambda ControlLatentTopic: ControlLatentTopic.getBelongingDegree(id))
        else:
            return None


    @staticmethod
    def imagePrint( path, M, escale):
        """Make an image with the M matrix."""  
        X=LTRelation.escalar(M, escale)
        figsize=(array(X.shape)/100.0)[::-1]
        rcParams.update({'figure.figsize':figsize})
        fig = figure(figsize=figsize)
        axes([0,0,1,1]) # Make the plot occupy the whole canvas
        axis('off')
        fig.set_size_inches(figsize)
        imshow(X,origin='lower', cmap=cm.gray)
        savefig(path, facecolor='black', edgecolor='black', dpi=100)
        close(fig)
        

    @staticmethod
    def escalar(M,scale):
        """Scale the size of the M matrix to a bigger one.""" 
        Mt = np.zeros((M.shape[0]*scale,M.shape[1]*scale))
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                    for k in range(scale):
                            for l in range(scale):
                                    Mt[(j*scale)+l,(i*scale)+k]  = M[i,j]
        return Mt

