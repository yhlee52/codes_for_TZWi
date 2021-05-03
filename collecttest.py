from ROOT import *
import sys, os
import glob
import pandas as pd

#flist = glob.glob("./ntuple/reco/*/TT_FCNC*zut*/*.root") ## For TT_Zut
#flist = glob.glob("./ntuple/reco/*/TT_FCNC*zct*/*.root") ## For TT_Zct
#flist = glob.glob("./ntuple/reco/*/ST_FCNC*zut*/*.root") ## For ST_Zut
#flist = glob.glob("./ntuple/reco/*/ST_FCNC*zct*/*.root") ## For ST_Zct
flist = glob.glob("./ntuple/reco/*/*/*.root") ## General

numofbkg = 0
numofsig = 0

accudata = []
#datalabel = ["label","Z_mass","MVAinput_bJ_DeepJetB","MVAinput_qJ_DeepJetB","W_MT","MVAinput_ZL1ZL2_dPhi","MVAinput_bJqJ_dR","MVAinput_WLbJ_dPhi","MVAinput_WLbJ_dR","MVAinput_ZL1bJ_dR","MVAinput_ZL1qJ_dR","MVAinput_ZL1ZL2_dR","KinTopZq_mass"] # TMVA Variables
datalabel = ["label","Z_mass","MVAinput_bJ_DeepJetB","MVAinput_qJ_DeepJetB","W_MT","MVAinput_WLZL1_dPhi","MVAinput_WLZL1_dR","MVAinput_WLZL2_dPhi","MVAinput_WLZL2_dR","MVAinput_ZL1ZL2_dPhi","MVAinput_ZL1ZL2_dR","MVAinput_Wlepchapt","MVAinput_Wlepchaeta","MVAinput_bJ_pt","MVAinput_qJ_pt","MVAinput_bJqJ_dPhi","MVAinput_bJqJ_dR","MVAinput_WLbJ_dPhi","MVAinput_WLbJ_dR","MVAinput_WLqJ_dPhi","MVAinput_WLqJ_dR","MVAinput_ZL1bJ_dPhi","MVAinput_ZL1bJ_dR","MVAinput_ZL1qJ_dPhi","MVAinput_ZL1qJ_dR","MVAinput_ZL2bJ_dPhi","MVAinput_ZL2bJ_dR","MVAinput_ZL2qJ_dPhi","MVAinput_ZL2qJ_dR","KinTopZq_mass","TriLepton_mass","TriLepton_WleptonZdPhi","TriLepton_WleptonZdR","KinTopWb_pt","KinTopWb_eta","KinTopWb_phi","KinTopWb_mass","KinTopZq_pt","KinTopZq_eta","KinTopZq_phi","KinTop_deta","KinTop_dphi","scaling"] ## TTSR variables(1+41+1)
#datalabel = ["label","Z_mass","MVAinput_bJ_DeepJetB","W_MT","MVAinput_WLZL1_dPhi","MVAinput_WLZL1_dR","MVAinput_WLZL2_dPhi","MVAinput_WLZL2_dR","MVAinput_ZL1ZL2_dPhi","MVAinput_ZL1ZL2_dR","MVAinput_Wlepchapt","MVAinput_Wlepchaeta","MVAinput_bJ_pt","MVAinput_WLbJ_dPhi","MVAinput_WLbJ_dR","MVAinput_ZL1bJ_dPhi","MVAinput_ZL1bJ_dR","MVAinput_ZL2bJ_dPhi","MVAinput_ZL2bJ_dR","TriLepton_mass","TriLepton_WleptonZdPhi","TriLepton_WleptonZdR","KinTopWb_pt","KinTopWb_eta","KinTopWb_phi","KinTopWb_mass","scaling"] ## STSR variables(1+25+1)


for i, fl in enumerate(flist):   
    if 'Double' in fl: continue
    elif 'ST_FCNC' in fl: continue ## ST pass
    elif 'TT_FCNC' in fl: continue ## TT pass
    print "Read file : ", fl
    accudata = []
    label = 0
    xsecnorm = 0.
    f = TFile.Open(fl)
    t = f.Get("Events")

    ### xsecnorm reading
    if 'TT_FCNC-T2ZJ_aTleptonic_ZToll_kappa_zut' in fl: xsecnorm = (0.0108/1042395)*35900
    elif 'TT_FCNC-T2ZJ_aTleptonic_ZToll_kappa_zct' in fl: xsecnorm = (0.00484/988009)*35900
    elif 'TT_FCNC-aT2ZJ_Tleptonic_ZToll_kappa_zut' in fl: xsecnorm = (0.0108/1046339)*35900
    elif 'TT_FCNC-aT2ZJ_Tleptonic_ZToll_kappa_zct' in fl: xsecnorm = (0.00484/1055193)*35900
    elif 'ST_FCNC-TLL_Tleptonic_kappa_zut' in fl: xsecnorm = (0.0136/1999031)*35900
    elif 'ST_FCNC-TLL_Tleptonic_kappa_zct' in fl: xsecnorm = (0.00406/2000000)*35900
    elif 'M-50' in fl: xsecnorm = (6077.22/80929255)*35900
    elif 'M-10to50' in fl: xsecnorm = (18610/78443820)*35900
    elif 'ST_s' in fl: xsecnorm = (3.36/622990)*35900
    elif 'ST_t-channel_top' in fl: xsecnorm = (136.02/67105876)*35900
    elif 'ST_tW_top' in fl: xsecnorm = (35.85/6952830)*35900
    elif 'ST_t-channel_antitop' in fl: xsecnorm = (80.95/38811017)*35900
    elif 'ST_tW_antitop' in fl: xsecnorm = (35.85/6933094)*35900
    elif 'WWTo' in fl: xsecnorm = (12.178/1999000)*35900
    elif 'WZTo2L2Q' in fl: xsecnorm = (5.595/15879472)*35900
    elif 'WZTo3LNu' in fl: xsecnorm = (4.679/7387013)*35900
    elif 'ZZTo2L2Nu' in fl: xsecnorm = (0.564/57586850)*35900
    elif 'ZZTo2L2Q' in fl: xsecnorm = (3.22/496436)*35900
    elif 'ZZTo4L' in fl: xsecnorm = (1.212/103121112)*35900
    elif 'TTWJetsToLNu' in fl: xsecnorm = (0.2043/2716249)*35900
    elif 'TTWJetsToQQ' in fl: xsecnorm = (0.4062/430310)*35900
    elif 'TTZToLLNuNu' in fl: xsecnorm = (0.2529/6420825)*35900
    elif 'TTZToQQ' in fl: xsecnorm = (0.5297/351164)*35900
    elif 'TT_Tune' in fl: xsecnorm = (831.76/76915549)*35900
    elif 'tZq_ll' in fl: xsecnorm = (0.0758/3618998)*35900
    elif 'ttHTobb' in fl: xsecnorm = (0.2934/3799066)*35900
    elif 'ttHToNonbb' in fl: xsecnorm = (0.2151/3905798)*35900

    for evt in t:
        scaling = 0.
        CutStep = evt.CutStep
        W_MT = evt.W_MT
        Z_mass = evt.Z_mass
        LeadingLepton_pt = evt.LeadingLepton_pt
        Z_charge = evt.Z_charge
        nGoodJet = evt.nGoodJet
        nBjet = evt.nBjet
        HLT = evt.HLT
        if not (CutStep >= 2 and W_MT <= 300 and abs(Z_mass-91.2)<7.5 and LeadingLepton_pt>25 and Z_charge == 0 and 2<=nGoodJet and 3>=nGoodJet and nBjet>=1 and HLT==1): continue # TTSR condition
        #if not (CutStep >= 2 and W_MT <= 300 and abs(Z_mass-91.2)<7.5 and LeadingLepton_pt>25 and Z_charge == 0 and nGoodJet==1 and nBjet==1 and HLT==1): continue # STSR condition
        else:
        
            datalist = []

            #if "ST_FCNC" in fl:
            if "TT_FCNC" in fl:
                label = 1
                numofsig += 1
            else:
                label = 0
                numofbkg += 1
            MVAinput_bJ_DeepJetB = evt.MVAinput_bJ_DeepJetB
            MVAinput_qJ_DeepJetB = evt.MVAinput_qJ_DeepJetB
            MVAinput_ZL1ZL2_dPhi = evt.MVAinput_ZL1ZL2_dPhi
            MVAinput_bJqJ_dR = evt.MVAinput_bJqJ_dR
            MVAinput_WLbJ_dPhi = evt.MVAinput_WLbJ_dPhi
            MVAinput_WLbJ_dR = evt.MVAinput_WLbJ_dR
            MVAinput_ZL1bJ_dR = evt.MVAinput_ZL1bJ_dR
            MVAinput_ZL1qJ_dR = evt.MVAinput_ZL1qJ_dR
            MVAinput_ZL1ZL2_dR = evt.MVAinput_ZL1ZL2_dR
            KinTopZq_mass = evt.KinTopZq_mass

            scalecheck = len(evt.LHEScaleWeight)
            if (scalecheck <= 4): 
                print("LHEScale[4] is not exist. Set to 1") 
                LHEScaleweight = 1.
            else: LHEScaleweight = evt.LHEScaleWeight[4]
            if not evt.genWeight:
                print("genWeight is not exist. Set to 1")
                genWeight = 1.
            else: genWeight = evt.genWeight
            puWeight = evt.puWeight
            BtagWeight = evt.BtagWeight
            Lepton_SF = evt.Lepton_SF
            Trigger_SF = evt.Trigger_SF
            scaling = xsecnorm*LHEScaleweight*(genWeight/abs(genWeight))*puWeight*BtagWeight*Lepton_SF*Trigger_SF

            datalist.append(label)
            datalist.append(evt.Z_mass)
            datalist.append(evt.MVAinput_bJ_DeepJetB)
            datalist.append(evt.MVAinput_qJ_DeepJetB)
            datalist.append(evt.W_MT)
            datalist.append(evt.MVAinput_WLZL1_dPhi)
            datalist.append(evt.MVAinput_WLZL1_dR)
            datalist.append(evt.MVAinput_WLZL2_dPhi)
            datalist.append(evt.MVAinput_WLZL2_dR)
            datalist.append(evt.MVAinput_ZL1ZL2_dPhi)
            datalist.append(evt.MVAinput_ZL1ZL2_dR)
            datalist.append(evt.MVAinput_Wlepchapt)
            datalist.append(evt.MVAinput_Wlepchaeta)
            datalist.append(evt.MVAinput_bJ_pt)
            datalist.append(evt.MVAinput_qJ_pt)
            datalist.append(evt.MVAinput_bJqJ_dPhi)
            datalist.append(evt.MVAinput_bJqJ_dR)
            datalist.append(evt.MVAinput_WLbJ_dPhi)
            datalist.append(evt.MVAinput_WLbJ_dR)
            datalist.append(evt.MVAinput_WLqJ_dPhi)
            datalist.append(evt.MVAinput_WLqJ_dR)
            datalist.append(evt.MVAinput_ZL1bJ_dPhi)
            datalist.append(evt.MVAinput_ZL1bJ_dR)
            datalist.append(evt.MVAinput_ZL1qJ_dPhi)
            datalist.append(evt.MVAinput_ZL1qJ_dR)
            datalist.append(evt.MVAinput_ZL2bJ_dPhi)
            datalist.append(evt.MVAinput_ZL2bJ_dR)
            datalist.append(evt.MVAinput_ZL2qJ_dPhi)
            datalist.append(evt.MVAinput_ZL2qJ_dR)
            datalist.append(evt.KinTopZq_mass)
            datalist.append(evt.TriLepton_mass)
            datalist.append(evt.TriLepton_WleptonZdPhi)
            datalist.append(evt.TriLepton_WleptonZdR)
            datalist.append(evt.KinTopWb_pt)
            datalist.append(evt.KinTopWb_eta)
            datalist.append(evt.KinTopWb_phi)
            datalist.append(evt.KinTopWb_mass)
            datalist.append(evt.KinTopZq_pt)
            datalist.append(evt.KinTopZq_eta)
            datalist.append(evt.KinTopZq_phi)
            datalist.append(evt.KinTop_deta)
            datalist.append(evt.KinTop_dphi)
            datalist.append(abs(scaling))

            accudata.append(datalist)
    df = pd.DataFrame(accudata, columns=datalabel)
    
    if not os.path.exists('eventcollect_TTZct.csv'):
        df.to_csv('eventcollect_TTZct.csv', index=False, mode='w', encoding='cp949')
    else:
        df.to_csv('eventcollect_TTZct.csv', index=False, mode='a', encoding='cp949', header=False)

    f.Close()
