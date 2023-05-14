from matplotlib import pyplot as plp
import matplotlib as mlp
from nugridpy import utils as ut
import numpy as np
import pickle

global jb_dict,jb_elems
data_dir = '/data/nugrid/data/iprocess-impact-MC/one-zone-run_default/'
pickle_in = open(data_dir+'../data_utils/Jinabasedict.pickle',"rb")
jb_dict,jb_elems = pickle.load(pickle_in)


def get_jb_o(elem,select='CR',jb_dict=jb_dict,jb_elems=jb_elems):
    '''Get elemental abundance in JinaBase pickle for elem name and selection
    '''
    elem_abu = {}
    elem_abu['obs'] = np.array([jb_dict[select][i][1][np.where(jb_elems == elem)].astype('float')[0] for i in range(len(jb_dict[select]))])
    elem_abu_ul = np.array([jb_dict[select][i][2][np.where(jb_elems == elem)].astype('float')[0] for i in range(len(jb_dict[select]))])
    elem_abu['ul'] = ( elem_abu_ul == 0 )   # boolean True for "is not upper limit"
    return (elem_abu)

def is_upper_limit(upper_limit):
    return not upper_limit

def plot_elemratios(els, selections = ['S', 'I', 'R1', 'R2'], uls = False):
    for i,s in enumerate(selections):
        # check if the minimum number of nans is > 0 for all elements for this selection, only
        # in that case print (and create)
        if np.array([np.count_nonzero(~np.isnan(get_jb_o(el,s)['obs'])) for el in els]).min() > 0:
            mask = np.ones(len(get_jb_o(els[0],s)['ul']), dtype=bool)
            for el in els: mask = mask*get_jb_o(el,s)['ul']
            if uls:
                plp.plot(get_jb_o(els[0],s)['obs']-get_jb_o(els[1],s)['obs'],\
                     get_jb_o(els[2],s)['obs']-get_jb_o(els[3],s)['obs'],ut.linestylecb(i)[1],color=ut.linestylecb(i)[2],fillstyle="none")
            plp.plot((get_jb_o(els[0],s)['obs']-get_jb_o(els[1],s)['obs'])[mask],\
                 (get_jb_o(els[2],s)['obs']-get_jb_o(els[3],s)['obs'])[mask],ut.linestylecb(i)[1],label=s,color=ut.linestylecb(i)[2])
    
    
