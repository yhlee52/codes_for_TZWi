import sys, os
from ROOT import *

chlist = ["ElElEl", "MuElEl", "ElMuMu", "MuMuMu"]
mclist = ["dy", "stv", "zz", "wz", "ttv", "ttjet", "others"]
#mclist = ["dy", "st", "stv", "zz", "wz", "ww", "tth", "ttv", "ttjet"]
colorlist = ["kOrange+1", "kMagenta+1", "kMagenta+2", "kCyan-1", "kAzure+6", "kBlue-6", "kRed+3", "kRed+4", "kRed"]
syslist = ["jer", "jes", "PU", "ElSF", "MuID", "MuISO", "MuR", "MuF", "BtagJES", "BtagLF", "BtagHF", "BtagHFStats1", "BtagHFStats2", "BtagLFStats1", "BtagLFStats2", "BtagCQErr1", "BtagCQErr2"]

f = TFile.Open("ttzut/shape_ttzut_fix.root")

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

def createRatio(hcent, hsys, color):
    hratio = hcent.Clone("hratio")
    hratio.SetLineColor(eval(color))
    hratio.SetMaximum(1.5)
    hratio.SetMinimum(0.5)
    hratio.Sumw2()
    hratio.SetStats(0)
    hratio.Divide(hsys)
    hratio.SetMarkerStyle(21)
    hratio.SetMarkerColor(eval(color))
    
    return hratio

def drawplot(hcent, hup, hdown, hratioup, hratiodown, legend, channel, syst, flag):
#def drawplot (hdata, hbkg, hsig, channel):

    c, pad1, pad2 = createCanvasPads()

    pad1.cd()
    hdown.SetTitle("%s_MVAscore"%syst)
    hdown.SetLineColor(kRed)
    hdown.SetStats(0)
    hdown.Draw("hist")
    hup.SetLineColor(kBlue)
    hup.Draw("same, hist")
    hcent.SetLineColor(kBlack)
    hcent.Draw("same, hist")
    leg.SetNColumns(3)
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    leg.Draw()

    c.cd()

    pad2.cd()
    hratioup.Draw("ep")
    hratioup.SetTitle("")
    hratioup.GetYaxis().SetTitle("ratio cent/syst")
    hratioup.GetYaxis().SetNdivisions(505)
    hratioup.GetYaxis().SetTitleSize(20)
    hratioup.GetYaxis().SetTitleFont(40)
    hratioup.GetYaxis().SetTitleOffset(1.55)
    hratioup.GetYaxis().SetLabelFont(43)
    hratioup.GetYaxis().SetLabelSize(15)

    hratioup.GetXaxis().SetTitleSize(20)
    hratioup.GetXaxis().SetTitleFont(40)
    hratioup.GetXaxis().SetTitleOffset(4.)
    hratioup.GetXaxis().SetLabelFont(43)
    hratioup.GetXaxis().SetLabelSize(15)

    hratiodown.Draw("ep, same")

    c.SaveAs("MVAdist_%s_%s.png"%(syst,flag))


hscent = TH1F("hscent","hscent", 10, -1.0, 1.0)
hscentsig = TH1F("hscentsig","hscentsig", 10, -1.0, 1.0)

for i, channel in enumerate(chlist):
    htcentsig = f.Get("%s_ttzut"%(channel))
    hscentsig.Add(htcentsig)
    for j, mc in enumerate(mclist):
        htcent = f.Get("%s_%s"%(channel, mc))
        hscent.Add(htcent)

for syst in syslist:
    leg = TLegend(0.60, 0.72, 0.80, 0.85)
    hsup = TH1F("hsup","hsup", 10, -1.0, 1.0)
    hsdown = TH1F("hsdown","hsdown", 10, -1.0, 1.0)
    hsupsig = TH1F("hsupsig","hsupsig", 10, -1.0, 1.0)
    hsdownsig = TH1F("hsdownsig","hsdownsig", 10, -1.0, 1.0)
    for ch1 in chlist:
        htupsig = f.Get("%s_ttzut_%sUp"%(ch1, syst))
        htdownsig = f.Get("%s_ttzut_%sDown"%(ch1, syst))
        hsupsig.Add(htupsig)
        hsdownsig.Add(htdownsig)
        for mc1 in mclist:
            htup = f.Get("%s_%s_%sUp"%(ch1, mc1, syst))
            htdown = f.Get("%s_%s_%sDown"%(ch1, mc1, syst))
            hsup.Add(htup)
            hsdown.Add(htdown)

    leg.AddEntry(hscent, "central", "l")
    leg.AddEntry(hsup, "Up", "l")
    leg.AddEntry(hsdown, "Down", "l")
    hratioup = createRatio(hscent, hsup, "kRed") # hsig for test
    hratiodown = createRatio(hscent, hsdown, "kBlue") # hsig for test
    drawplot(hscent, hsup, hsdown, hratioup, hratiodown, leg, channel, syst, "background")
    hratioupsig = createRatio(hscentsig, hsupsig, "kRed") # hsig for test
    hratiodownsig = createRatio(hscentsig, hsdownsig, "kBlue") # hsig for test
    drawplot(hscentsig, hsupsig, hsdownsig, hratioupsig, hratiodownsig, leg, channel, syst, "signal")
    leg.Delete()
    hsup.Delete()
    hsdown.Delete()
    hsupsig.Delete()
    hsdownsig.Delete()
