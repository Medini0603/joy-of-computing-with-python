#%%
#from operator import le
import statistics
import matplotlib.pyplot as py
estimate=[12,34,56,8,90,45,7,4,567,98,65,3456,8,65,67,45]
#py.plot(estimate)
y=[]
# for i in range(len(estimate)):
#     y.append(5)
#py.plot(estimate,y,'r--')
estimate.sort()
trimvalue=int(0.1*len(estimate))
# typecat is necessary here  
estimate=estimate[trimvalue:]
estimate=estimate[:len(estimate)-trimvalue]
# append acc to new estimate leght 
for i in range(len(estimate)):
    y.append(5)
py.plot(estimate,y,'r--')
py.plot([100],[5],'g^')
py.plot([statistics.mean(estimate)],[5],'ro')
py.plot([statistics.median(estimate)],[5],'bs')

# %%
