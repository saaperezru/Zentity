import numpy as npimport pymfimport InterfazNMF as IN


a=np.random.rand(3,4)nmf_mdl = pymf.CNMF(a, num_bases=2, niter=10)nmf_mdl.initialization()nmf_mdl.factorize()LD=["perro","gato","arana","sapo"]H=np.matrix(nmf_mdl.H)F=np.matrix(nmf_mdl.W)W=np.matrix(nmf_mdl.G)
CTLT=IN.crateTypeLatentTopic(1,"","",LD,H,F,W)

CLT=CTLT.getControlArrayLatentTopics()

LS=CTLT.getLatentTopicsForImg("perro")
print LS[0].getBelongingDegree("perro")
print LS[1].getBelongingDegree("perro")

lss=CTLT.getMostImportantLatentTopicForImg("perro")
print lss.getBelongingDegree("perro")


CCLT=CTLT.copyControlArrayLatentTopics()




