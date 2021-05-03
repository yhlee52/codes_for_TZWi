from ROOT import *
import sys, json, os, math
#from sysWeight_cfi import *
from array import array

gROOT.SetBatch(True)

def calcError(hist, binstart, binend):
    herr = 0.
    h = hist
    for i in range(binstart, binend):
        herr += (h.GetBinError(i))**2
        sqrterr = math.sqrt(herr)
    return sqrterr

baseDir = "./hist"

chlist = ["ElElEl", "MuElEl", "ElMuMu", "MuMuMu", "All"]
steplist = ["S1", "S2", "S3", "WZCR", "STCR", "STSR", "TTCR", "TTSR"]
samplelist = ["DYJets", "WW", "WZ", "ZZ", "ttJets", "ttV", "ttH", "SingleTop", "SingleTopV", 
"Data", "STZutX10", "STZctX10", "TTZutX10", "TTZctX10"]

for i, ch in enumerate(chlist):
    rootFile = "%s/%s.root" %(baseDir, ch)
    f = TFile.Open(rootFile)
    print ch, " channel & S1 & S2 & S3 & WZCR & STCR & STSR & TTCR & TTSR \\\ \hline\hline"
    allmcyield = []
    allmcerror = []
    for j, mc in enumerate(samplelist):
        yieldslist = []
        errorslist = []
        for k, step in enumerate(steplist):
            histname = "%s/hW_MT/%s" %(step, mc)
            h = f.Get("%s/hW_MT/%s" %(step, mc))
            yields = h.Integral()
            errors = calcError(h, h.FindBin(0), h.FindBin(300))
            if not ( mc == "Data" ):
                yields = yields*35900
                errors = errors*35900
            elif "TZ" in mc:
                yields = yields*3590
                errors = errors*3590
            yieldslist.append(yields)
            errorslist.append(errors)
        allmcyield.append(yieldslist)
        allmcerror.append(errorslist)
        for p, slot in enumerate(yieldslist):
            yieldslist[p] = round(yieldslist[p], 3)
            errorslist[p] = round(errorslist[p], 3)
        print mc, " & ", yieldslist[0], "~$\pm$~", errorslist[0], " & ", yieldslist[1], "~$\pm$~", errorslist[1], " & ", yieldslist[2], "~$\pm$~", errorslist[2], " & ", yieldslist[3], "~$\pm$~", errorslist[3], " & ", yieldslist[4], "~$\pm$~", errorslist[4], " & ", yieldslist[5], "~$\pm$~", errorslist[5], " & ", yieldslist[6], "~$\pm$~", errorslist[6], " & ", yieldslist[7], "~$\pm$~", errorslist[7], "\\\ \hline"
    for n in range(0, 8):
        sumyield = 0.
        sumerror = 0.
        for m in range(0, 9):
            sumyield += allmcyield[m][n]
            sumerror += (allmcerror[m][n])**2
        sumyield = round(sumyield, 3)
        print " & ", sumyield, "~$\pm$~", round(math.sqrt(sumerror), 3)
