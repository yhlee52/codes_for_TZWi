import sys, os
from ROOT import *

chlist = ['ElElEl', 'MuElEl', 'ElMuMu', 'MuMuMu']
mclist = ['ttzct', 'dy', 'st', 'stv', 'tth', 'ttjet', 'ttv', 'ww', 'wz','zz'] # up to your mc categorizing
systlist = ['', 'jer', 'jes', 'PU', 'ElSF', 'MuID', 'MuISO', 'MuR', 'MuF', 'BtagJES', 'BtagLF', 'BtagHF', 'BtagHFStats1', 'BtagHFStats2', 'BtagLFStats1', 'BtagLFStats2', 'BtagCQErr1', 'BtagCQErr2']
up_down = ['Up', 'Down']

# output rule : For each channel_syst : [sig_up, bkg_up, sig_down, bkg_down]

result = {}

f = TFile.Open("shape_tZc.root")

for ch in chlist:
    tmp_list = []
    for syst in systlist:
        tmp_sig_up, tmp_sig_down = 0., 0.
        tmp_bkg_up, tmp_bkg_down = 0., 0.
        tmp_sig_cent, tmp_bkg_cent = 0., 0.
        for mc in mclist:
            for ud in up_down:
                if syst == '': # central
                    #print 'processing : {}_{}'.format(ch, mc)
                    htmp = f.Get("%s_%s"%(ch, mc))
                    cent_entry = htmp.Integral()
                    break
                #print 'processing : {}_{}_{}{}'.format(ch, mc, syst, ud)
                htmp = f.Get("%s_%s_%s%s"%(ch, mc, syst, ud))
                if ud == 'Up':
                    tmp_up = htmp.Integral()
                elif ud == 'Down':
                    tmp_down = htmp.Integral()
            if 'tz' in mc: # sig mc
                if syst == '':
                    tmp_sig_cent += cent_entry
                else:
                    tmp_sig_up += tmp_up
                    tmp_sig_down += tmp_down
            else:
                if syst == '':
                    tmp_bkg_cent += cent_entry
                else:
                    tmp_bkg_up += tmp_up
                    tmp_bkg_down += tmp_down
        if syst == '':
            tmp_list = [tmp_sig_cent, tmp_bkg_cent]
            result['%s_central'%(ch)] = tmp_list
        else:
            tmp_list = [tmp_sig_up, tmp_bkg_up, tmp_sig_down, tmp_bkg_down]
            result['%s_%s'%(ch, syst)] = tmp_list
#print result

### Interpretation
for ch in chlist:
    for key in result.keys():
        if ch in key and 'central' in key:
            sig_cent, bkg_cent = result[key][0], result[key][1]
    for key in result.keys():
        if ch in key and 'central' not in key:
            print '{}{}|  {}  |  {}  |  {}  |  {}'.format(key, ' '*(20-len(key)), round(100*(result[key][0]-sig_cent)/sig_cent,2), round(100*(result[key][2]-sig_cent)/sig_cent,2), round(100*(result[key][1]-bkg_cent)/bkg_cent,2), round(100*(result[key][3]-bkg_cent)/bkg_cent),2)
