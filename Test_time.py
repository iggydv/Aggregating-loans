import pandas as pd
import gc
import numpy as np
import timeit as t
import LoanAggregateCalculator

from numpy.ma.extras import average

a = np.arange(100)
aa = np.arange(100, 200)

test_object = LoanAggregateCalculator.LoanAggregateCalculator()

s = pd.Series(a)
ss = pd.Series(aa)
i = np.random.choice(a, size=10)

#timer1 = t.repeat("ss[i]", "from __main__ import ss,i \ gc.enable()", number=1000)
# convert to micro seconds
#print(str(average(timer1)*10)+' us')

'text = "sample string"; char = "g"'
gc.enable()
timer2 = t.repeat("test_object.calculate_aggregate()", setup='gc.enable();'+'from __main__ import test_object', number=1)
# convert to micro seconds
print(str(average(timer2)*10)+' us')
