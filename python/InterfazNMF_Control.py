import numpy as np
from pylab import *
from scipy import mgrid
from InterfazNMF_Model import LatentTopic
from InterfazNMF_Model import TypeLatentTopic

class ControlTypeLatentTopic:
    """  	
    ControlTypeLatentTopic(id, name, abreviature, LD, H, F1, W1, F2, W2)
    
    RESUME

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
	
    Example
    -------
    """
    def __init__(self, id, name, abreviature, LD, H, F1, W1, F2, W2):
        
        #Review matrix type.
        if not ControlTypeLatentTopic.correctClass(H):
            print "Error-class H"
            return None
        if not ControlTypeLatentTopic.correctClass(F1):
            print "Error-class F"
            return None
        if not ControlTypeLatentTopic.correctClass(W1):
            print "Error-class W"
            return None
        if F2!=None:
            if not ControlTypeLatentTopic.correctClass(F2):
                print "Error-class"
                return None
        if W2!=None:
            if not ControlTypeLatentTopic.correctClass(W2):
                print "Error-class"
                return None

        #Review the dimensions of each matrix.
        if ControlTypeLatentTopic.correctDimensions(LD, H, F1, W1, F2, W2):
            print "Error-shape"
            return None

        #Attributes initialization.  
        self.__arrayControlLatentTopics=[]
        self.__typeLatentTopic=TypeLatentTopic(id, name, abreviature, self.createDictionary(LD))

	#ControlLatentTopics creation.
        if F2!=None and W2!=None:
            for i in xrange(H.shape[0]):
		HT=ControlTypeLatentTopic.normalize(H[i])
                CLT=ControlLatentTopic(i,HT,F1[:,i],W1[:,i],F2[:,i],W2[:,i],self)
                self.__arrayControlLatentTopics.append(CLT)
        else:
            for i in xrange(H.shape[0]):
                HT=ControlTypeLatentTopic.normalize(H[i])
                CLT=ControlLatentTopic(i,HT,F1[:,i],W1[:,i],None,None,self)
                self.__arrayControlLatentTopics.append(CLT)
                

  
    @staticmethod  
    def correctDimensions(LD, H, F1, W1, F2, W2):
        """ Check if the matrix dimensions are related to each.
            return:
                True if the dimensions between matrix are ok, False otherwise. 
        """
        if(F2!=None and W2!=None):
            if min(H.shape[0],F1.shape[1],W1.shape[1],F2.shape[1],W2.shape[1])!=max(H.shape[0],F1.shape[1],W1.shape[1],F2.shape[1],W2.shape[1]):
                return False
            if min(H.shape[1],W1.shape[0],W2.shape[0],len(LD))!=max(H.shape[1],W1.shape[0],W2.shape[0],len(LD)):
                return False    
        else:
            if min(H.shape[0],F1.shape[1],W1.shape[1])!=max(H.shape[0],F1.shape[1],W1.shape[1]):
                return False
            if min(H.shape[1],W1.shape[0],len(LD))!=max(H.shape[1],W1.shape[0],len(LD)):
                return False
        return True

    
    
    @staticmethod
    def correctClass(M):
        """ Check the type of the parameter.
            return:
                True if the parameter M is a matrix or an array, False otherwise. 
        """
        if type(M) == type(np.array([])) or type(M) == type(np.matrix([])):
            return True
        else:
            return False



    @staticmethod
    def normalize(M):
        """ Normalize M vector.
            return:
                M vector with |M|=1. 
        """
        s=sum(M)
	M=M/s
	return M    



    @staticmethod
    def createDictionary(LD):
        """ Create a dictionary mapping between the list of documents and his position.
            Where the key is LD[i] and the object is the number i, which is the id-column of the 
            ith document of the representation matrix.   
        """
        x=xrange(len(LD))
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
        """ Return a ControlLatenTopics with the highest belong degree of the Latent Topics to the document.
        """
        return max(self.__arrayControlLatentTopics, key=lambda ControlLatentTopic: ControlLatentTopic.getBelongingDegree(identificador))

    

    def getLatentTopicsForWord(self,identificador):
        """ Return a sorted list of ControlLatenTopics. The other depends of the belong degree of the Latent Topic to the word.
        """
        return sorted(self.__arrayControlLatentTopics, key=lambda ControlLatentTopic:  ControlLatentTopic.getWordValue(identificador), reverse=True)
    
    

    def getMostImportantLatentTopicForWord(self,identificador):
        """ Return a ControlLatenTopics with the highest belong degree of the Latent Topics to the word.
        """
	return max(self.__arrayControlLatentTopics, key=lambda ControlLatentTopic: ControlLatentTopic.getWordValue(identificador))

    

    def copyControlArrayLatentTopics(selfs):
        """ Return a copy of the list of ControlLatenTopics.
        """
        copy=__arrayControlLatentTopics[:]
        return copy

    

    def getControlArrayLatentTopics(selfs):
        """ Return the list of ControlLatenTopics.
        """
        return __arrayControlLatentTopics

    

    def getSizeDictionary(self):
        """ Return the length of the dictionary.
        """
        return self.__typeLatentTopic.getSizeDictionary() 

    

    def setTypeLatantTopicId(self, ids):
        """ Change the TypeLatentTopic id.
        """
        self.__typeLatentTopic.setId(ids)
    
    

    def setTypeLatantTopicName(self, name):
        """ Change the TypeLatentTopic name.
        """
        self.__typeLatentTopic.setName(name)
    
    

    def setTypeLatantTopicAbreviature(self, Abreviature):
        """ Change the TypeLatentTopic abreviature.
        """
        self.__typeLatentTopic.setAbreviature(Abreviature)



class ControlLatentTopic:
    """  	
    ControlLatentTopic(id, H, F1, W1, F2, W2, CTLT)
    
    RESUME

	
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
        Basis of the Latent Topic in terms of the documnets.
    F2: array or matrix, 
        Basis of the Latent Topic on the Asymmetric Factorization.
    W2: array or matrix, 
        Basis of the Latent Topic in terms of the documnets on the Asymmetric Factorization.
	
    Attributes
    ----------
        controlTypeLatentTopic : ControlTypeLatentTopic control entity.
        latentTopic : LatentTopic entity. 	
	
    Example
    -------
    """   
    def __init__(self, id, H, F1, W1, F2, W2, CTLT):
        self.__latentTopic=LatentTopic(id, "", H, F1, W1, F2, W2)
        self.__controlTypeLatentTopic=CTLT

    

    def getBelongingDegree(self,Img):
        """ Return the belong degree of the document, -1 if the document is not on the dictionary.
            That means the document was not on the inicial list of documents.
        """
        id=self.__controlTypeLatentTopic.self.getDictionary(identificador)
        if id!=None:
            return str(round(self.__latentTopic.getBelongingVector(id),6))
        else:
            return -1
    
    

    def getWordValue(self,Id):
        """ Return the belong degree of the word, it depends of the position represented by the id.
            That means the document was not on the inicial list of documents.
        """
        if id>=0 and id<self.__controlTypeLatentTopic.getSizeDictionary():
            return str(round(self.__latentTopic.getRepresentativewords(id),6))
        else:
            return -1

    

    def setLatantTopicName(self, name):
        """ Change the LatentTopic name.
        """
        self.__latentTopic.setName(name)



class LTRelation:
    """  	
    LTRelation()
    
    Interface class with methods to do a correlation matrix between Latent Topics and make an image with this matrix.
	
	
    Example
    -------
    """     
    


    @staticmethod
    def createMatrix(LD,LT1,LT2):
        """
		Create and return a matrix M(ControlLatentTopic list(LT1) vs ControlLatentTopic list(LT2)) 
                where each i,j position is the number of documents where the ith latent topic was the most important
                in the LT1 list, and the jth latent topic was the most important in the LT2 list.
   	        
                If for a document the belonging degree is not define this does not count.
        """    
	x=len(LT1)
        y=len(LT2)
        
	matirx = np.zeros((x,y))
        
	for data in LD:
            CLT=LTRelation.getMostImportantLatentTopic(data.getId(), LT1)
            if CLT!=None:
                i= LT1.index(CLT)
                CLT=LTRelation.getMostImportantLatentTopic(data.getId(), LT2)
                if CLT!=None:
                    j= LT2.index(CLT)
                    matirx[i,j]=matirx[i,j]+1
	return matirx
    
    
    
    @staticmethod
    def getMostImportantLatentTopic(id, LT):
        """
	    Return the most important latent topic in the LT  list for a id document.
            If for a document the belonging degree is not define return None.  
        """ 
        CLT=min(LT1, key=lambda ControlLatentTopic: ControlLatentTopic.getBelongingDegree(id))
        if CLT.getBelongingDegree(id)>=0:
            return max(LT1, key=lambda ControlLatentTopic: ControlLatentTopic.getBelongingDegree(id))
        else:
            return None

    

    @staticmethod
    def imagePrint( path, M, escale):
        """
	    Make an image with the M matrix  
        """ 
        if not ControlTypeLatentTopic.correctClass(M):
            print "Error-class M"
        else: 
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
        """
	    scale the size of the M matrix to a bigger one.  
        """ 
        Mt = np.zeros((M.shape[0]*scale,M.shape[1]*scale))
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                    for k in range(scale):
                            for l in range(scale):
                                    Mt[(j*scale)+l,(i*scale)+k]  = M[i,j]
        return Mt

