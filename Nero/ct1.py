from problem import prob
import numpy as np

a_solution = { 'parameters': {}, 'method': None, 'conclusive' : False}
a_solution['parameters']['temp'] = None
a_solution['parameters']['knob'] = None
a_solution['method'] = '_twist_knob' 
np.save('solist',[a_solution])

x1=prob()
x1.label='water_too_hot'
x1.parameters['temp'] = 'too_hot'
x1.parameters['knob'] = None
print(x1.solve())



 