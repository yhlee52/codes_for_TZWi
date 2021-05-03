from ROOT import *
import CMS_lumi, tdrstyle

# CMS Style
CMS_lumi.cmsText = "CMS"
CMS_lumi.extraText = "Preliminary"
CMS_lumi.cmsTextSize = 0.65
CMS_lumi.outOfFrame = True
tdrstyle.setTDRStyle()

#scanrange = [0., 0.00005, 0.00010, 0.00015, 0.00020, 0.00025, 0.00030, 0.00035, 0.00040, 0.00045, 0.00050] # range1 : for tZc
#scanrange = [0., 0.00003, 0.00006, 0.00009, 0.00012, 0.00015, 0.00018, 0.00021, 0.00024, 0.00027, 0.00030] # range1 : for tZu
#N = len(scanrange)

N = 2

# Plot upper limits
yellow = TGraph(2*N) # Yellow band
green = TGraph(2*N) # Green band
expected = TGraph(N) # Expected limit line
observed = TGraph(N) # Observed limit line
eightTeVexp = TGraph(N)
eightTeVobs = TGraph(N)

climit = [2.0444, 0.5911, 0.8060, 1.1641, 1.7069, 2.4014] # obs, -2sig, -1sig, exp, +1sig, +2sig # tZc
ulimit = [0.4899, 0.2293, 0.3140, 0.4551, 0.6709, 0.9522] # obs, -2sig, -1sig, exp, +1sig, +2sig # tZu
ttzctlimit = [2.2701, 0.6141, 0.8409, 1.2188, 1.7969, 2.5501]
stzctlimit = [4.0957, 2.1582, 2.9426, 4.2500, 6.2151, 8.7570]
ttzutlimit = [0.6536, 0.2441, 0.3338, 0.4883, 0.7277, 1.0441]
stzutlimit = [0.8971, 0.6850, 0.9379, 1.3594, 1.9988, 2.8410]

calcfactor = (674.1*2*3*3.36*3*10.8)/10000
cTTxsec = 2*0.00484 # tZc
cSTxsec = 0.00406 #tZc
uTTxsec = 2*0.0108 #tZu
uSTxsec = 0.0136 #tZu

# Merged xsec
tZcxsec = 0.00748
tZuxsec = 0.0188

# 8TeV limit
c8TeVobs = 0.00049
c8TeVexp = 0.00118
u8TeVobs = 0.00022
u8TeVexp = 0.00027

## Use this value!
inputtZuBr = (100*100*0.0216)/(674.1*2*32.4*10.08)
inputtZcBr = (100*100*0.00968)/(674.1*2*32.4*10.08)
inputtZuxsec = 0.0216
inputtZcxsec = 0.00968

# Calculation values for plotting
cresult = []
uresult = []
for i in range(6):
    cresult.append(inputtZcBr*climit[i])
    uresult.append(inputtZuBr*ulimit[i])


up2s = []
for i in range(N):
    up2s.append(cresult[5]) 
    if (i == 0):
        yellow.SetPoint(i, 0., cresult[5])
        green.SetPoint(i, 0., cresult[4])
        expected.SetPoint(i, 0., cresult[3])
        green.SetPoint(2*N-1-i, 0., cresult[2])
        yellow.SetPoint(2*N-1-i, 0., cresult[1])
        observed.SetPoint(i, 0., cresult[0])
        eightTeVexp.SetPoint(i, 0., c8TeVexp)
        eightTeVobs.SetPoint(i, 0., c8TeVobs)
    if ( i == 1 ):
        yellow.SetPoint(i, uresult[5], 0.)
        green.SetPoint(i, uresult[4], 0.)
        expected.SetPoint(i, uresult[3], 0.)
        green.SetPoint(2*N-1-i, uresult[2], 0.)
        yellow.SetPoint(2*N-1-i, uresult[1], 0.)
        observed.SetPoint(i, uresult[0], 0.)
        eightTeVexp.SetPoint(i, u8TeVexp, 0.)
        eightTeVobs.SetPoint(i, u8TeVobs, 0.)


    W = 800
    H  = 600
    T = 0.08*H
    B = 0.12*H
    L = 0.12*W
    R = 0.12*W
    c = TCanvas("c","c",100,100,W,H)
    c.SetFillColor(0)
    c.SetBorderMode(0)
    c.SetFrameFillStyle(0)
    c.SetFrameBorderMode(0)
    c.SetLeftMargin( L/W )
    c.SetRightMargin( R/W )
    c.SetTopMargin( T/H )
    c.SetBottomMargin( B/H )
    c.SetTickx(0)
    c.SetTicky(0)
    c.SetGrid()
    c.cd()
    frame = c.DrawFrame(1.4,0.001, 4.1, 10)
    frame.GetYaxis().CenterTitle()
    frame.GetYaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetTitleOffset(0.9)
    frame.GetXaxis().SetNdivisions(508)
    frame.GetYaxis().CenterTitle(True)
    frame.GetYaxis().SetTitle("BR_{tZc}")
#    frame.GetYaxis().SetTitle("95% upper limit on #sigma #times BR / (#sigma #times BR)_{SM}")
    frame.GetXaxis().SetTitle("BR_{tZu}")
    frame.SetMinimum(0)
    frame.SetMaximum(0.00150)
    frame.GetXaxis().SetLimits(0,1.25*(uresult[5]))
 
    yellow.SetFillColor(kOrange)
    yellow.SetLineColor(kOrange)
    yellow.SetFillStyle(1001)
    yellow.Draw('F')
 
    green.SetFillColor(kGreen+1)
    green.SetLineColor(kGreen+1)
    green.SetFillStyle(1001)
    green.Draw('Fsame')
 
    expected.SetLineColor(1)
    expected.SetLineWidth(2)
    expected.SetLineStyle(2)
    expected.Draw('Lsame')
 
    observed.SetLineColor(1)
    observed.SetLineWidth(2)
    observed.SetLineStyle(1)
    observed.Draw('Lsame')

    eightTeVexp.SetLineColor(kBlue)
    eightTeVexp.SetLineWidth(2)
    eightTeVexp.SetLineStyle(2)
    eightTeVexp.Draw('Lsame')

    eightTeVobs.SetLineColor(kBlue)
    eightTeVobs.SetLineWidth(2)
    eightTeVobs.SetLineStyle(1)
    eightTeVobs.Draw('Lsame')

    CMS_lumi.CMS_lumi(c,14,11)
    gPad.SetTicks(1,1)
    frame.Draw('sameaxis')
 
    x1 = 0.85
    x2 = x1 + 0.1
    y2 = 0.95
    y1 = 0.75
    #legend = TLegend(x1,y1,x2,y2)
    legend = TLegend(0.50, 0.62, 0.90, 0.85)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.SetTextSize(0.030)
    legend.SetTextFont(42)
    legend.AddEntry(expected, "Expected",'L')
    legend.AddEntry(observed, "Observed",'L')
    legend.AddEntry(green, "#pm 1 std. deviation",'f')
#    legend.AddEntry(green, "Asymptotic CL_{s} #pm 1 std. deviation",'f')
    legend.AddEntry(yellow,"#pm 2 std. deviation",'f')
#    legend.AddEntry(green, "Asymptotic CL_{s} #pm 2 std. deviation",'f')
    legend.AddEntry(eightTeVexp, "CMS 8TeV best limit(exp)", 'L')
    legend.AddEntry(eightTeVobs, "CMS 8TeV best limit(obs)", 'L')
    legend.Draw()
 
    print " "
    c.SaveAs("upperlimit_Br_bothcoupling.png")
    c.Close()
