import numpy as np


a=np.random.rand(3,4)


CLT=CTLT.getControlArrayLatentTopics()

LS=CTLT.getLatentTopicsForImg("perro")
print LS[0].getBelongingDegree("perro")
print LS[1].getBelongingDegree("perro")

lss=CTLT.getMostImportantLatentTopicForImg("perro")
print lss.getBelongingDegree("perro")


CCLT=CTLT.copyControlArrayLatentTopics()



