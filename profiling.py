#LINE PROFILER

from line_profiler import LineProfiler
import random

def do_stuff(numbers):
    s = sum(numbers)
    l = [numbers[i]/43 for i in range(len(numbers))]
    m = ['hello'+str(numbers[i]) for i in range(len(numbers))]

numbers = [random.randint(1,100) for i in range(1000)]
lp = LineProfiler()
lp_wrapper = lp(do_stuff)
lp_wrapper(numbers)
lp.print_stats()

#output
Timer unit: 1e-06 s

Total time: 0.000649 s
File: <ipython-input-2-2e060b054fea>
Function: do_stuff at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           def do_stuff(numbers):
     5         1           10     10.0      1.5      s = sum(numbers)
     6         1          186    186.0     28.7      l = [numbers[i]/43 for i in range(len(numbers))]
     7         1          453    453.0     69.8      m = ['hello'+str(numbers[i]) for i in range(len(numbers))]

#cProfile

import cProfile
import pstat
cProfile.run('foo(bar)','filename')
p = pstats.Stats('restats')
p.strip_dirs().sort_stats(-1).print_stats()

# Note: only checks function calls, Lineprofile preferable for diagnostics. 


