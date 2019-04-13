class Greens:
	def implicit(self,num, phi, theta):
		G=0
		if num==0:
			G=1
		else:
			try:
				G=-theta[num-1]
			except IndexError:
				G=0

			for i in range(num):
				try:
					t=phi[i]
				except IndexError:
					phi.append(0)
				G+=phi[i]*funcTypes.ImpFindGreens(num-i-1, phi, theta)

		return G

	def explicit(self, num, phi, theta):
		# Works only for arma(2,1)
		lam1=0.5*(phi[0]+(phi[0]**2+4*phi[1])**0.5)
		lam2=0.5*(phi[0]-(phi[0]**2+4*phi[1])**0.5)
		g1=(lam1-theta[0])/(lam1-lam2)
		g2=(lam2-theta[0])/(lam2-lam1)
		return (g1*lam1**num+g2*lam2**num).real
