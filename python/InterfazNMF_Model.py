class LatentTopic:
    """  	
        LatentTopic(self, ids, name, belongingVector, representativeWords, sortedIndexRepresentativeWords, representativeDocuments, sortedIndexRepresentativeDocuments, resumeWords, sortedIndexResumeWords, resumeDocuments, sortedIndexResumeDocuments)
    
        Entity that keep the structure and attributes of each of the latent topics, 
        includes: belonging degree of each document, 
        vector representation of this and the resulting vectors by the asymmetric factorization.

	
        Parameters
        ----------
        id : int,
            ID of the LatentTopic
        name: String 
            Name of the LatentTopic.
        belongingVector: array or matrix, 
            Vector of belonging degrees of each Document to the Latent Topic.
        representativeWords: array or matrix, 
            Basis of the Latent Topic.
        sortedIndexRepresentativeWords: array or matrix, 
            Vector of position index of the representativeWords in decreasing order.
        representativeDocuments: array or matrix, 
            Basis of the Latent Topic in terms of the documents.
        sortedIndexRepresentativeDocuments: array or matrix, 
            Vector of position index of the representativeDocuments in decreasing order.
        resumeWords: array or matrix, 
            Basis of the Latent Topic on the Asymmetric Factorization.
        sortedIndexResumeWords: array or matrix, 
            Vector of position index of the resumeWords in decreasing order.
        resumeDocuments: array or matrix, 
            Basis of the Latent Topic in terms of the documents on the Asymmetric Factorization.
        sortedIndexResumeDocuments: array or matrix, 
            Vector of position index of the resumeDocuments in decreasing order.
	
        Attributes
        ----------
        id : int,
            ID of the LatentTopic
        name: String 
            Name of the LatentTopic.
        belongingVector: array or matrix, 
            Vector of belonging degrees of each Document to the Latent Topic.
        representativeWords: array or matrix, 
            Basis of the Latent Topic.
        sortedIndexRepresentativeWords: array or matrix, 
            Vector of position index of the representativeWords in decreasing order.
        representativeDocuments: array or matrix, 
            Basis of the Latent Topic in terms of the documents.
        sortedIndexRepresentativeDocuments: array or matrix, 
            Vector of position index of the representativeDocuments in decreasing order.
        resumeWords: array or matrix, 
            Basis of the Latent Topic on the Asymmetric Factorization.
        sortedIndexResumeWords: array or matrix, 
            Vector of position index of the resumeWords in decreasing order.
        resumeDocuments: array or matrix, 
            Basis of the Latent Topic in terms of the documents on the Asymmetric Factorization.
        sortedIndexResumeDocuments: array or matrix, 
            Vector of position index of the resumeDocuments in decreasing order.	
    """   
    def __init__(self, ids, name, belongingVector, representativeWords, sortedIndexRepresentativeWords, representativeDocuments, sortedIndexRepresentativeDocuments, resumeWords, sortedIndexResumeWords, resumeDocuments, sortedIndexResumeDocuments):
        self.__id = ids
        self.__name = name
        self.__belongingVector = belongingVector
        self.__representativeWords = representativeWords
        self.__sortedIndexRepresentativeWords = sortedIndexRepresentativeWords
        self.__representativeDocuments = representativeDocuments
        self.__sortedIndexRepresentativeDocuments = sortedIndexRepresentativeDocuments
	    self.__resumeWords = resumeWords
        self.__sortedIndexResumeWords = sortedIndexResumeWords
	    self.__resumeDocuments = resumeDocuments
        self.__sortedIndexResumeDocuments = sortedIndexResumeDocuments
        
    
    
    #Getters for each attributes
    def getId(self):
        """ Returns the LatentTopic Id.
        """
        return self.__id
    def getName(self):
        """ Returns the LatentTopic Name.
        """
        return self.__name
    def getBelongingVector(self, id):
        """ Returns the belonging degree of a document in the LatentTopic.
        """
        return self.__belongingVector[id]
    def getRepresentativeWords(self, id):
        """ Returns the belonging degree of a word to the LatentTopic.
        """
        return self.__representativeWords[id]
    def getSortedIndexRepresentativeWords(self):
        """ Returns a sort vector of indices in decrease order depending on the values of the representativeWords vector.
        """
        return self.__sortedIndexRepresentativeWords
    def getRepresentativeDocuments(self, id):
        """ Returns the belonging degree of a document to the LatentTopic depending on the W matrix.
        """
        return self.__representativeDocuments[id]
    def getSortedIndexRepresentativeDocuments(self):
        """ Returns a sort vector of indices in decrease order depending on the values of the representativeDocuments vector.
        """
        return self.__sortedIndexRepresentativeDocuments
    def getResumeWords(self, id):
        """ Returns the belonging degree of a word to the LatentTopic depending on the F matrix in the asymmetric factorization.
        """
        return self.__resumeWords[id]
    def getSortedIndexResumeWords(self):
        """ Returns a sort vector of indices in decrease order depending on the values of the resumeWords vector.
        """
        return self.__sortedIndexResumeWords
    def getResumeDocuments(self,id):
        """ Returns the belonging degree of a document to the LatentTopic depending on the W matrix in the asymmetric factorization.
        """
        return self.__resumeDocuments[id]
    def getSortedIndexResumeDocuments(self):
        """ Returns a sort vector of indices in decrease order depending on the values of the resumeDocuments vector.
        """
        return self.__sortedIndexResumeDocuments

    
   
    #set method for the only attribute that can change.
    def setName(self,name):
        """ Safe the LatentTopic Id.
        """
        self.__name=name
   


class TypeLatentTopic:
    """
        TypeLatentTopic(self,ids,name,abreviature,Dictionary)
    
        This will save the dictionary class of documents for a modality
        and link all resulting Latent Topics for this modality, 
        as well as save information needed to work with it.
	
        Parameters
        ----------
        id : int,
            ID of the TypeLatentTopic
        name: String 
            Name of the TypeLatentTopic. 
        abreviature: String
            Abreviature of the TypeLatentTopic.
        Dictionary: dict 
            Dictionay of Documents where the key is the id of the document and the object is the position of the document on the matrixes.
        

        Attributes
        ----------
        id : int,
            ID of the TypeLatentTopic
        name: String 
            Name of the TypeLatentTopic. 
        abreviature: String
            Abreviature of the TypeLatentTopic.
        Dictionary: dict
            Dictionary of Documents where the key is the id of the document and the object is the position of the document on the matrixes.   
    """
    def __init__(self,ids,name,abreviature,Dictionary):
        self.__id = ids
        self.__name = name
        self.__abreviature=abreviature
        self.__dictionary =Dictionary



    #Getters for each attributes
    def getId(self):
        """ Returns the TypeLatentTopic Id.
        """
        return self.__id
    def getName(self):
        """ Returns the TypeLatentTopic name.
        """
        return self.__name
    def getAbreviature(self):
        """ Returns the TypeLatentTopic Abreviature.
        """
        return self.__abreviature
    def getDictionary(self,id):
        """ Given the id key returns the object on the dictionary.
        """
        return self.__dictionary.get(id)
    


    def getSizeDictionary(self):
        """ Return the size of the dictionary. 
        """
        return len(self.__dictionary)
    
    

    #Setters
    def setId(self,ids):
        """ Safe the TypeLatentTopic Id.
        """
        self.__id=ids
    def setName(self,name):
        """ Safe the TypeLatentTopic name.
        """
        self.__name=name
    def setAbreviature(self,Abreviature):
        """ Safe the TypeLatentTopic Abreviature.
        """
        self.__abreviature=Abreviature





