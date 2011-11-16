import numpy as np
import pymf
import InterfazNMF as IN


a=np.random.rand(3,4)
b=np.random.rand(5,4)
nmf_mdl = pymf.CNMF(a, num_bases=2, niter=10)
nmf_mdl.initialization()
nmf_mdl.factorize()

nmf_mdl2 = pymf.CNMF(b, num_bases=2, niter=10)
nmf_mdl2.initialization()
nmf_mdl2.factorize()

LD=range(4)
H=np.matrix(nmf_mdl.H)
W=np.matrix(nmf_mdl.W)
F=np.matrix(nmf_mdl.G)

H2=np.matrix(nmf_mdl2.H)
W2=np.matrix(nmf_mdl2.W)
F2=np.matrix(nmf_mdl2.G)



cTLT,cTLT2=IN.crateTypeLatentTopic(1,"name1","abreviature1",LD,H,F,W,None,None,2,"name2","abreviature2",H2,F2,W2,None,None)

ARRAY=cTLT.copyControlArrayLatentTopics()
