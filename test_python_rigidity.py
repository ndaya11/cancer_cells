import numpy as np
import pandas as pd
import matplotlib . pyplot as plt
import FDApy as fda

# il me faudra un fichier comme cd4 avec tout les rigidités une ligne represente la rigidités en fonction du gap
# je ne sais pas ou stoker mon argval si j 'ai bien compris cela est mon gap


rigidity = pd.read_csv(’toto.csv’, index col=0)

all_argvals = rigidity.columns.astype(np.int64)
argvals = {idx: np.array(all_argvals[ ̃np.isnan(row)])
            for idx, row in enumerate(rigidity.values)}
values = {idx: row[ ̃np.isnan(row)]
            for idx, row in enumerate(rigidity.values)}
rigiditycounts = IrregularFunctionalData({’input dim 0’: argvals}


_= plot(cd4counts[5:15])
plt.xlabel(’Month since seroconversion’)
plt.ylabel(’CD4 cell counts (log−scale)’)
plt.title(’CD4 counts for individual 5−14’)
plt.show()
