'''
arif.darmawan@riflab.com

20200211 first version
20200322 update workdir and save directory
'''

import os
import shutil
from glob import glob as list_image

workdir = '../data/'+'kurma'
dirpath1 = workdir+'/saved/'+'ig*.png'
images = list_image(dirpath1)

k=0
for i in range (1,8):
	dirpath2 = workdir + '/kurma_u_'+str(i).zfill(2)
	if not os.path.exists(dirpath2):
		os.makedirs(dirpath2)
	for j in range(0,5):
		shutil.copy(images[k], dirpath2)
		k+=1