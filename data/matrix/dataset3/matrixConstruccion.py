import numpy as np
from synmf import *
import scipy.io as sio

TD = np.array(sio.loadmat("TD.mat")["TD"])
TVD = np.array(sio.loadmat("termvDocumentMatrix.mat")["TVD"])
textual = SyNMF(TD,TVD,num_bases=50,niter = 100)
textual.initialization()
textual.factorize()
sio.savemat('Ht',{'Ht':textual.H})
sio.savemat('Ft',{'Ft':textual.Wc})
sio.savemat('FVt',{'FVt':textual.Wm})
visual = SyNMF(TVD,TD,num_bases=50,niter = 100)
visual.initialization()
visual.factorize()
sio.savemat('Hv',{'Hv':visual.H})
sio.savemat('Fv',{'Fv':visual.Wc})
sio.savemat('FTv',{'FTv':visual.Wm})



