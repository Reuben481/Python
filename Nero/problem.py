import numpy as np

class prob:

	def __init__(self):
		"""
		prob() class instance containing info as formatted for nero solution

		Parameters:
		--------------
		label : 	timestamp, type: str, default None
		
		parameters: dict_of any

		solved: type Bool

		solutions: returns sols if previously attempted 
				   type: dict (so far)
				   None otherwise
			
			defn:
			-----------
			solution = { 'parameters': {}, 'method': None, 'conclusivity' : 0}

			NOTE: method -> should be a functional, atm just a string. (pseudo code).



				   


		"""
		self.label = None
		self.parameters = {}
		self.solved = False
		self.attempts = False
		self.solutions = [{ 'parameters': {}, 'method': None, 'conclusivity' : 0}]
	
	def solve(self):
		# load sols already has saved, idealy in order of satisfaction, solutions. 
		solist = np.load('solist.npy')

		for sol in solist:
			if sol['parameters'].keys() == self.parameters.keys():
				# MORE CRITERIA 
				return sol['method']

				#NOTE: measurement of conclusivity
					
				# sol['conclusivity']=method.test
				# for i in self.solutions:
					# if sol['conclusivity']>i['conclusivity']:
						# insertval()
						# self.save


class method:
	def __init__(self):
		self.lib = None #np.load('method_lib')
		# test(equal_pars=True)

		#should contain table with methods on x, response variate on y.
		 
		#example: method.test(_twist_knob, water_too_hot) 
		#		    --> conclusivity = 0.5 , parameters: _knob=_twist, temp = None 
		#		  method.test(_twist_knob, water_too_hot.parameters['_temp']=_change)
		# 			--> conclusivity = 1.0 _twist_knob_change_temp
		# 		  method.test(_twist_knob, water_too_hot_and_strong.parameters['_pressure']=change)
	    #			--> conclusivity = 1.5 parameters: _knob = _twist, _temp = _change, _pressure = _change 
	    # 		  method.test(_twist_knob, water_too_strong.parameters['_pressure','knob']= None, None)
	    #			--> conclusivity = 1.0 _twist_knob_change_pressure 




"""
Stuff we still need:

(1) Functional for method (params-> bool, num ) !!!
(2) link from problems to solutions, more sofisticated map than solist. 
(3) quantification of conclusivity -> scale measure. (i.e how conclusive was this method on a scale from 1-10 for a given problem)
(4) more criteria in solve for attempting a method.
(5) point at which nero saves solutions.  
"""


















