import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.special as sp
from pycoda import extra
import scipy.optimize as optimization
import pandas as pd
import pycoda as coda
import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
#Import libraries needed
import pandas as pd
import pycoda as coda
import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

## MUSIC GENRE DATA SET CREATION
#Open file from folder
data = pd.read_csv('spotify_19-04-22.csv', sep=';', index_col=0)
#Transpose data because we are going to study what music is listened in each europe country
data = pd.DataFrame.transpose(data)
data['Song titles'] = data.index
#Join music genre to data table
data['Genre'] = ['Pop', 'Rap', 'R&B', 'Pop', 'Rock', 'Disco', 'Reggaeton', 'Pop', 'Pop', 'Latin Urban', 'Rock', 'Rock', 'Pop', 'Latin Urban', 'Reggaeton', 'Pop', 'Pop', 'Reggaeton', 'Pop', 'Rock']
#Set music genre as index before ammalgamation
data.set_index('Genre')
#Amalgamated data set by musical genre
st_data = data.groupby('Genre').sum('Country')
st_data = pd.DataFrame.transpose(st_data)


# do zero-replacement with eq4.1 using a delta = 0.5, since our data has rounded zero
print('zero replacement')

all_list = list()
for sample in st_data.index:
    eq4d1 = [0.5 if i == 0. else i *
             (1-1./20 * 0.5*np.count_nonzero(st_data.loc[sample] == 0)) for i in st_data.loc[sample]]
    all_list.append(eq4d1)

##get replaced df
replaced_data = pd.DataFrame(all_list, columns = st_data.columns, index = st_data.index)

# descriptive statistics, sample center, variation matrix and total matrix
print("calculate sample center")

# Geometric center
gm = ss.mstats.gmean(replaced_data)
gm = 100/np.sum(gm) * gm
print(gm)

# Variation matrix
npdata = np.array(replaced_data)
var_matrix = np.var(np.log(npdata[:, :, None] * 1./npdata[:, None]), axis=0)
print(var_matrix)

# Total variation
totvar = 1./(2 * 3) * np.sum(var_matrix)
print(totvar)

