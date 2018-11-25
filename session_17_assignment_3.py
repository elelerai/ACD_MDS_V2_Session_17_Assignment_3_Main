# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:39:37 2018

@author: Eliud Lelerai
"""
import numpy as np
import pandas as pd

# R=reb balls , B=Black balls

# First determine the probabilities of the events.

  # events           Probability
   #RR          (4/10)(3/9) = 2/15
   #RB          (4/10)(6/9) = 4/15
   #BR          (6/10)(4/9) = 4/15 
   #BB          (6/10)(5/9) = 1/3

#The probability of 0 blue balls (RR)is 2/15
#The probability of 1 blue ball is (RB or BR) is 4/15+4/15 = 8/15
#The probability of 2 blue balls (BB) is 1/3

data={'x':list(range(3)),'p(x)':[2/15,8/15,1/3]}
probability_distribution=pd.DataFrame(data,columns=['x','p(x)'])                                