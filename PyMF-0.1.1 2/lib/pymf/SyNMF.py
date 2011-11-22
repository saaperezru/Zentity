

__version__ = "$Revision: 8 $"

import numpy as np

from nmf import NMF
from kmeans import Kmeans


__all__ = ["CNMF"]

class SyNMF(NMF):
	"""  	
	SyNMF(data, num_bases=4, niter=100, show_progress=True, compW=True)
	
	
	Symmetric NMF. Factorize a data matrix into two matrices s.t.
	F = | data - H'*H |  is minimal.	
	
	Parameters
	----------
	data : array_like
		the input data
	num_bases: int, optional 
		Number of bases to compute (column rank of W and row rank of H). 
		4 (default)
	niter: int, optional
		Number of iterations of the alternating optimization.
		100 (default)
	show_progress: bool, optional
		Print some extra information
		False (default)
	
	Attributes
	---------
		H : "num bases x num_samples" matrix of coefficients
		ferr : frobenius norm (after calling .factorize())
	
		"""

	_VINFO = 'pymf-synmf v0.1'
	
	def __init__(self, data, num_bases=4, niter=100, show_progress=False, b):
		NMF.__init__(self, data, num_bases=num_bases, niter=niter, show_progress=show_progress, compW=False)
                self.b=b
	
	
	def initialization(self):		
		# init basic matrices	
		self.H = np.zeros((self._data_dimension, self._num_bases))
		#####
		
		# initialize using k-means
		km = Kmeans(self.data[:,:], num_bases=self._num_bases, show_progress=self._show_progress)
		km.initialization()
		km.factorize()
		assign = km.assigned

		num_i = np.zeros(self._num_bases)
		for i in range(self._num_bases):
			num_i[i] = len(np.where(assign == i)[0])

		self.H[range(len(assign)), assign] = 1.0 
		self.H += 0.01						
		self.H /= np.tile(np.reshape(num_i[assign],(-1,1)), self.H.shape[1])
	
		
		
			
	
	# see .factorize() for the update of W and H
	def updateW(self):
		pass		
		
	def updateH(self):
		pass
	
	def factorize(self):
		""" Perform factorization s.t. data = H'H using the standard multiplicative 
		update rule for Non-negative matrix factorization.
		"""	
							
		# iterate over H
		for i in xrange(self._niter):
			# update H

                        H = H * (1 - self.b + self.b * (np.dot(self.data[:,:], H)) / ( np.dot(H,np.dot(self.H.T,H))))

								
			self.ferr[i] = self.frobenius_norm()

			self._print_cur_status('iteration ' + str(i+1) + '/' + str(self._niter) + ' Fro:' + str(self.ferr[i]))

			if i > 1:
				if self.converged(i):					
					self.ferr = self.ferr[:i]					
					break

if __name__ == "__main__":
	import doctest  
	doctest.testmod()	