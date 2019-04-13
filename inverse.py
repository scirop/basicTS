class Inverse:
	def Implicit(num, phi, theta):
		I = 0
		if num==0:
			I=-1
		else:
			try:
				I=phi[num-1]
			except IndexError:
				I=0

			for i in range(num):
				try:
					t=theta[i]
				except IndexError:
					theta.append(0)
				I+=theta[i]*funcTypes.ImpFindInverses(num-i-1, phi, theta)

		return I

	def Explicit(num, phi, theta):
		if num==0:
			return -1
		elif num==1:
			return phi[0]-theta[0]
		else:
			return (phi[1]-theta[0]*(theta[0]-phi[0]))*theta[0]**(num-2)
