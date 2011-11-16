"""  	
InterfazNMF.

"""

__version__ = "$Revision: 1 $"

from InterfazNMF_Control import ControlTypeLatentTopic
from InterfazNMF_Control import ControlLatentTopic
from InterfazNMF_Control import LTRelation



"""
    Given the CNMF result matrix, create a Type Latent Topic and each of the latent topics, and return a control class
    that can be use for the user to work.    
""" 
def crateTypeLatentTopic(ids,name,abreviature,LD,H,F1,W1,F2,W2):
    cTLT=ControlTypeLatentTopic(ids,name,abreviature,LD,H,F1,W1,F2,W2)
    return cTLT



"""
    Given the CNMF result matrix without the matrix of the asymmetric Factorization, create a Type Latent Topic and each of the latent topics, and return a control class
    that can be use for the user to work.    
""" 
def crateTypeLatentTopic(ids,name,abreviature,LD,H,F1,W1):
    cTLT=ControlTypeLatentTopic(ids,name,abreviature,LD,H,F1,W1,None,None)
    return cTLT



"""
    Make an image with the M matrix and save it.  
""" 
def matrixImage(path, escale, M):
    LTRelation.imagePrint(path, M, escale)



"""
    Create and return a matrix M(ControlLatentTopic list(LT1) vs ControlLatentTopic list(LT2)) 
    where each i,j position is the number of documents where the ith latent topic was the most important
    in the LT1 list, and the jth latent topic was the most important in the LT2 list.
   	        
    If for a document the belonging degree is not define this does not count.
""" 
def relationMatrix(LD,LT1,LT2):
    return LTRelation.createMatrix(LD,LT1,LT2)



