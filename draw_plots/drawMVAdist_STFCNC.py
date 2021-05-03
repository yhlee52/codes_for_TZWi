import sys, os
from ROOT import *

chlist = ["STElElEl", "STMuElEl", "STElMuMu", "STMuMuMu"]
mclist = ["dy", "st", "stv", "zz", "wz", "ww", "tth", "ttv", "ttjet"]
colorlist = ["kOrange+1", "kMagenta+1", "kMagenta+2", "kCyan-1", "kAzure+6", "kBlue-6", "kRed+3", "kRed+4", "kRed"]

f = TFile.Open("stzct/shape_stzct_10bin_1.root")
#f = TFile.Open("stzct/shape_stzct_BDT.root")

def createCanvasPads():
    c = TCanvas("c", "canvas", 800, 800)
    pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0.1)
    pad1.SetGridx()
    pad1.Draw()

    c.cd()
    pad2 = TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
    pad2.SetTopMargin(0)
    pad2.SetBottomMargin(0.2)
    pad2.SetGridx()
    pad2.Draw()

    return c, pad1, pad2

def createRatio(hdata, hbkg):
    hratio = hdata.Clone("hratio")
    hratio.SetLineColor(kBlack)
    hratio.SetMaximum(1.5)
    hratio.SetMinimum(0.5)
    hratio.Sumw2()
    hratio.SetStats(0)
    hratio.Divide(hbkg)
    hratio.SetMarkerStyle(21)
    
    return hratio

def drawplot(hdata, hbkg, hsig, hratio, legend, channel):
#def drawplot (hdata, hbkg, hsig, channel):

    c, pad1, pad2 = createCanvasPads()

    pad1.cd()
    hdata.SetTitle("%s_MVAscore"%channel)
    hdata.SetMarkerStyle(8)
    hdata.SetMarkerSize(1)
    hdata.SetLineColor(kBlack)
    hdata.SetStats(0)
    hdata.Draw("ep")
    hbkg.Draw("hist, same") # THStack
    hdata.Draw("ep, same")
    hsig.SetLineColor(eval("kGreen+1"))
    hsig.SetLineWidth(2)
    hsig.SetStats(0)
    #hsig.Scale(10) ## Signal MC scaling
    hsig.Draw("same, hist")
    leg.SetNColumns(3)
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    leg.Draw()

    c.cd()

    pad2.cd()
    hratio.Draw("ep")
    hratio.SetTitle("")
    hratio.GetYaxis().SetTitle("ratio Data/MC")
    hratio.GetYaxis().SetNdivisions(505)
    hratio.GetYaxis().SetTitleSize(20)
    hratio.GetYaxis().SetTitleFont(40)
    hratio.GetYaxis().SetTitleOffset(1.55)
    hratio.GetYaxis().SetLabelFont(43)
    hratio.GetYaxis().SetLabelSize(15)

    hratio.GetXaxis().SetTitleSize(20)
    hratio.GetXaxis().SetTitleFont(40)
    hratio.GetXaxis().SetTitleOffset(4.)
    hratio.GetXaxis().SetLabelFont(43)
    hratio.GetXaxis().SetLabelSize(15)

    c.SaveAs("MVAdist_%s_stzct.png"%channel)


for i, channel in enumerate(chlist):
    hs = THStack("hs", "")
    hs0 = TH1F("hs0","hs0", 20, -1.0, 1.0)
    leg = TLegend(0.50, 0.72, 0.90, 0.85)
    for j, mc in enumerate(mclist):
        htemp = f.Get("%s_%s"%(channel, mc))
        hs0.Add(htemp)
        htemp.SetLineColor(kBlack)
        htemp.SetFillColor(eval(colorlist[j]))
        hs.Add(htemp)
        leg.AddEntry(htemp, mc, "F")
    hdata = f.Get("%s_data_obs"%channel)
    hsig = f.Get("%s_stzct"%channel)
    leg.AddEntry(hsig, "stzct", "l")
    leg.AddEntry(hdata, "Data", "lp")
    hratio = createRatio(hdata, hs0) # hsig for test
    hs0.Delete()
    drawplot(hdata, hs, hsig, hratio, leg, channel)
