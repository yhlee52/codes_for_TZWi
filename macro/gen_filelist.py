import sys, os

RUN = "2017"
mode = ["central", "jesUp", "jesDown", "jerUp", "jerDown"]
channel = ["ElElEl", "MuElEl", "ElMuMu", "MuMuMu"]

basedir = "%s/src/TZWi/TopAnalysis/test/fcncTriLepton"%os.getenv("CMSSW_BASE")

if not os.path.exists(RUN):
   os.system("mkdir %s"%RUN)

for i, js in enumerate(mode):
    if (js == "central"):
        nfolder = "ntuple"
        ## Filelist generation for TMVAClassification
        ## Erase FCNC files in the bkg list manually...
        os.system("ls %s/%s/reco/*/*NANOAODSIM/*.root > filelist_2017_bkg.txt"%(basedir,nfolder))
    else: nfolder = "ntuple_%s"%js

    for j, ch in enumerate(channel):
        ## Detail filelist for TMVAClassificationApplication
        os.system("ls %s/%s/reco/%s/*Double*/*.root > filelist_%s_%s_data.txt"%(basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*DYJets*/*.root > filelist_%s_%s_dy.txt"%(basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*ST_s*/*.root %s/%s/reco/%s/*ST_t*/*.root > filelist_%s_%s_st.txt"%(basedir,nfolder,ch,basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*WWTo*/*.root > filelist_%s_%s_ww.txt"%(basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*WZTo*/*.root > filelist_%s_%s_wz.txt"%(basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*ZZTo*/*.root > filelist_%s_%s_zz.txt"%(basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*TTZ*/*.root %s/%s/reco/%s/*TTW*/*.root > filelist_%s_%s_ttv.txt"%(basedir,nfolder,ch,basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*TTJets*/*.root > filelist_%s_%s_ttjet.txt"%(basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*tZq*/*.root > filelist_%s_%s_stv.txt"%(basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*ttH*/*.root > filelist_%s_%s_tth.txt"%(basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*ST_FCNC*zut*/*.root > filelist_%s_%s_stzut.txt"%(basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*ST_FCNC*zct*/*.root > filelist_%s_%s_stzct.txt"%(basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*TT_FCNC*zut*/*.root > filelist_%s_%s_ttzut.txt"%(basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*TT_FCNC*zct*/*.root > filelist_%s_%s_ttzct.txt"%(basedir,nfolder,ch,js,ch))
        os.system("ls %s/%s/reco/%s/*ST_s*/*.root %s/%s/reco/%s/*ST_t*/*.root %s/%s/reco/%s/*WWTo*/*.root %s/%s/reco/%s/*ttH*/*.root > filelist_%s_%s_others.txt"%(basedir,nfolder,ch,basedir,nfolder,ch,basedir,nfolder,ch,basedir,nfolder,ch,js,ch))
        print "File list generation for channel : %s is finished."%ch

# signal merged txt file for TMVA training
os.system("ls %s/ntuple/reco/*/*ST_FCNC*zut*/*.root > filelist_2017_sig_stzut.txt"%basedir)
os.system("ls %s/ntuple/reco/*/*ST_FCNC*zct*/*.root > filelist_2017_sig_stzct.txt"%basedir)
os.system("ls %s/ntuple/reco/*/*TT_FCNC*zut*/*.root > filelist_2017_sig_ttzut.txt"%basedir)
os.system("ls %s/ntuple/reco/*/*TT_FCNC*zct*/*.root > filelist_2017_sig_ttzct.txt"%basedir)
