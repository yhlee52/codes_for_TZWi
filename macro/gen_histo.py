import sys, os

###############################################
###   This code do not contain DATA shape.  ###
### Shapes for Data should be run manually. ###
###############################################

sigchannel = "ttzut"
SYS = ["central", "jesUp", "jesDown", "jerUp", "jerDown"]
#SYS = ["central", "jesUp"]
CH = ["ElElEl", "ElMuMu", "MuElEl", "MuMuMu"]
#CH = ["ElElEl", "ElMuMu"]
# MC : Depends on the signal and others, DEFAULT : OTHERS = st, ww, tth
MC = [sigchannel, "dy", "wz", "zz", "stv", "ttv", "ttjet", "others"]
#MC = [sigchannel, "dy"]
# TMVA Variables : fix manually.
originVARS = ["Z_mass", "MVAinput_bJ_DeepJetB", "MVAinput_qJ_DeepJetB", "W_MT", "MVAinput_ZL1ZL2_dPhi", "MVAinput_bJqJ_dR", "MVAinput_WLbJ_dPhi", "MVAinput_WLbJ_dR", "MVAinput_ZL1bJ_dR", "MVAinput_ZL1qJ_dR", "MVAinput_ZL1ZL2_dR", "KinTopZq_mass"]
#originVARS = ["Z_mass", "MVAinput_bJ_DeepJetB", "MVAinput_ZL1ZL2_dPhi", "W_MT", "TriLepton_WleptonZdPhi", "TriLepton_WleptonZdR", "MVAinput_WLbJ_dPhi", "MVAinput_WLbJ_dR", "MVAinput_Wlepchaeta", "MVAinput_ZL1bJ_dR", "MVAinput_ZL1ZL2_dR", "KinTopWb_phi"]

for i, channel in enumerate(CH):
    for j, syst in enumerate(SYS):
        for k, mc in enumerate(MC):
            DEFAULT_mc = mc
            print "========================================"
            print "Process for : %s_%s_%s"%(channel, syst, DEFAULT_mc)
            print "========================================"

            if "tt" in sigchannel:
                DEFAULT_cut = "!((CutStep>=2)&&(W_MT<=300)&&(TMath::Abs(Z_mass-91.2)<7.5)&&(nGoodJet>=2)&&(nGoodJet<=3)&&(nBjet>=1)&&(LeadingLepton_pt>25)&&(Z_charge==0)&&(HLT==1))"
                DEFAULT_ch = channel
            else:
                DEFAULT_cut = "!((CutStep>=2)&&(W_MT<=300)&&(TMath::Abs(Z_mass-91.2)<7.5)&&(nGoodJet==1)&&(nBjet==1)&&(LeadingLepton_pt>25)&&(Z_charge==0)&&(HLT==1))"
                DEFAULT_ch = "ST"+channel

            ## Central
            if (syst == "central"):
                fileName = "TMVAClassificationApplication_%s_%s.C"%(DEFAULT_ch, DEFAULT_mc)
                os.system("cp Default_central.C %s"%fileName)
                DEFAULT_sys = ""
            else:
                DEFAULT_sys = syst
                fileName = "TMVAClassificationApplication_%s_%s_%s.C"%(DEFAULT_ch, DEFAULT_sys, DEFAULT_mc)
                os.system("cp Default_syst.C %s"%fileName)
                os.system("sed -i 's/_DEF_SYS_/%s/g' %s"%(DEFAULT_sys, fileName))

            
            # The name of .txt file which is listing the .root files
            DEFAULT_txt = "filelist_"+syst+"_"+channel+"_"+mc+".txt"

            # Change appropriate strings in the copied TMVAClassApp file.
            for l, originvar in enumerate(originVARS):
                os.system("sed -i 's/_DEF_VAR%i_/%s/g' %s"%(l, originvar, fileName))
            os.system("sed -i 's/_DEF_CH_/%s/g' %s"%(DEFAULT_ch, fileName))
            os.system("sed -i 's/_DEF_MC_/%s/g' %s"%(DEFAULT_mc, fileName))
            os.system("sed -i 's/_DEF_TEXT_/%s/g' %s"%(DEFAULT_txt, fileName))
            os.system("sed -i 's/_DEF_CUT_/%s/g' %s"%(DEFAULT_cut, fileName))
            ## For fix bug
            os.system("sed -i 's/_DEF_CUT_/\&/g' TMVAClassificationApplication*")

            # Run the code
            os.system("root -l -q %s"%fileName)

            # Delete the code
            os.system("rm %s"%fileName)

            # Marker
            print "========================================"
            print "            Finished(%i/%i)             "%(i*len(SYS)*len(MC)+j*len(MC)+k+1,len(CH)*len(SYS)*len(MC))
            print "========================================"

    # Data
    print "========================================"
    print " Process for channel : %s data "%(DEFAULT_ch)
    print "========================================"
    DEFAULT_txt = "filelist_central_"+channel+"_data.txt"
    fileName = "TMVAClassificationApplication_%s_data.C"%DEFAULT_ch
    os.system("cp Default_data.C %s"%fileName)
    for l, originvar in enumerate(originVARS):
        os.system("sed -i 's/_DEF_VAR%i_/%s/g' %s"%(l, originvar, fileName))
    os.system("sed -i 's/_DEF_CH_/%s/g' %s"%(DEFAULT_ch, fileName))
    os.system("sed -i 's/_DEF_TEXT_/%s/g' %s"%(DEFAULT_txt, fileName))
    if "tt" in sigchannel:
        DEFAULT_cut = "!((CutStep>=2)&&(W_MT<=300)&&(TMath::Abs(Z_mass-91.2)<7.5)&&(nGoodJet>=2)&&(nGoodJet<=3)&&(nBjet>=1)&&(LeadingLepton_pt>25)&&(Z_charge==0))"
    else:
        DEFAULT_cut = "!((CutStep>=2)&&(W_MT<=300)&&(TMath::Abs(Z_mass-91.2)<7.5)&&(nGoodJet==1)&&(nBjet==1)&&(LeadingLepton_pt>25)&&(Z_charge==0))"
 
    os.system("sed -i 's/_DEF_CUT_/%s/g' %s"%(DEFAULT_cut, fileName))
    ## For fix bug
    os.system("sed -i 's/_DEF_CUT_/\&/g' TMVAClassificationApplication*")

    # Run the code
    os.system("root -l -q %s"%fileName)

    # Delete the code
    os.system("rm %s"%fileName)

    # Marker
    print "========================================"
    print "             Finished(%i/%i)            "%(i+1,len(CH))
    print "========================================"

# Merge into 1 file
os.system("hadd shape_%s.root *.root"%sigchannel)
# Remove other root files
os.system("rm *El*.root *MuMuMu*.root")
## Remove sed*
