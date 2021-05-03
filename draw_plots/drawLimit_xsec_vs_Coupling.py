from ROOT import *
import CMS_lumi, tdrstyle

# CMS Style
CMS_lumi.cmsText = "CMS"
CMS_lumi.extraText = "Preliminary"
CMS_lumi.cmsTextSize = 0.65
CMS_lumi.outOfFrame = True
tdrstyle.setTDRStyle()

#scanrange = [0., 0.00005, 0.00010, 0.00015, 0.00020, 0.00025, 0.00030, 0.00035, 0.00040, 0.00045, 0.00050] # range1 : for tZc
scanrange = [0., 0.000005, 0.000010, 0.000015, 0.000020, 0.000025, 0.000030, 0.000035, 0.000040, 0.000045, 0.000050] # range1 : for tZu
N = 50
scanmax = 0.00030
scanstep = scanmax/(N-1)
scanpoint = 0.

# Plot upper limits
yellow = TGraph(2*N) # Yellow band
green = TGraph(2*N) # Green band
expected = TGraph(N) # Expected limit line
observed = TGraph(N) # Observed limit line
theoretical = TGraph(N) # Theoretical line

climit = [2.0444, 0.5911, 0.8060, 1.1641, 1.7069, 2.4014] # obs, -2sig, -1sig, exp, +1sig, +2sig # tZc
ulimit = [0.4899, 0.2293, 0.3140, 0.4551, 0.6709, 0.9522] # obs, -2sig, -1sig, exp, +1sig, +2sig # tZu
ttzctlimit = [2.2701, 0.6141, 0.8409, 1.2188, 1.7969, 2.5501]
stzctlimit = [4.0957, 2.1582, 2.9426, 4.2500, 6.2151, 8.7570]
ttzutlimit = [0.6536, 0.2441, 0.3338, 0.4883, 0.7277, 1.0441]
#stzutlimit = [0.8971, 0.6850, 0.9379, 1.3594, 1.9988, 2.8410]
stzutlimit = [0.5714, 0.4286, 0.5918, 0.8571, 1.2653, 1.7959]

calcfactor = (674.1*2*3*3.36*3*10.8)/10000
topwidth = 1.32158
cpwidthdivcoupsquare = 1.636554*10000
upwidthdivcoupsquare = 1.637005*10000*(0.049/0.022)

cTTxsec = 2*0.00484 # tZc
cSTxsec = 0.00406 #tZc
uTTxsec = 2*0.0108 #tZu
uSTxsec = 0.0136 #tZu 

# Merged xsec
tZcxsec = 0.00748
tZuxsec = 0.0188

# Calculation values for plotting
result = []
for i in range(6):
    result.append(uTTxsec*ulimit[i])

up2s = []
for i in range(N):
    up2s.append(result[5])
    yellow.SetPoint(i, scanpoint, result[5])
    green.SetPoint(i, scanpoint, result[4])
    expected.SetPoint(i, scanpoint, result[3])
    green.SetPoint(2*N-1-i, scanpoint, result[2])
    yellow.SetPoint(2*N-1-i, scanpoint, result[1])
    observed.SetPoint(i, scanpoint, result[0])
    theoretical.SetPoint(i, scanpoint, (1/topwidth)*calcfactor*upwidthdivcoupsquare*scanpoint*scanpoint)


    scanpoint += scanstep

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
    frame.GetYaxis().SetTitle("#sigma (pb)")
#    frame.GetYaxis().SetTitle("95% upper limit on #sigma #times BR / (#sigma #times BR)_{SM}")
    frame.GetXaxis().SetTitle("#kappa_{tZu}/#Lambda (GeV^{-1})")
    frame.SetMinimum(0)
    frame.SetMaximum(max(up2s)*2.5)
    frame.GetXaxis().SetLimits(0, scanmax)
 
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

    theoretical.SetLineColor(kRed)
    theoretical.SetLineWidth(2)
    theoretical.SetLineStyle(1)
    theoretical.Draw('Lsame')

    CMS_lumi.CMS_lumi(c,14,11)
    gPad.SetTicks(1,1)
    frame.Draw('sameaxis')
 
    x1 = 0.85
    x2 = x1 + 0.1
    y2 = 0.95
    y1 = 0.75
    #legend = TLegend(x1,y1,x2,y2)
    legend = TLegend(0.50, 0.72, 0.90, 0.85)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.SetTextSize(0.030)
    legend.SetTextFont(42)
    legend.AddEntry(expected, "Expected",'L')
    legend.AddEntry(observed, "Observed",'L')
    legend.AddEntry(theoretical, "Theory",'L')
    legend.AddEntry(green, "#pm 1 std. deviation",'f')
#    legend.AddEntry(green, "Asymptotic CL_{s} #pm 1 std. deviation",'f')
    legend.AddEntry(yellow,"#pm 2 std. deviation",'f')
#    legend.AddEntry(green, "Asymptotic CL_{s} #pm 2 std. deviation",'f')
    legend.Draw()
 
    print " "
    c.SaveAs("upperlimit_tZu_xsec_vs_Coupling.png")
    c.Close()
