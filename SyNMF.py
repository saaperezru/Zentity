

import numpy as np
from pymf import NMF
from pymf import Kmeans


__all__ = ["CNMF"]

class SyNMF(NMF):
	
	def __init__(self, data, W, b, num_bases=4, niter=100):
		NMF.__init__(self, data, num_bases=num_bases, niter=niter, show_progress=False , compW=False)
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