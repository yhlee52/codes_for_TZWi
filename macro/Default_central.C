/// \ingroup tutorial_tmva
/// \notebook -nodraw
/// This macro provides a simple example on how to use the trained classifiers
/// within an analysis module
/// - Project   : TMVA - a Root-integrated toolkit for multivariate data analysis
/// - Package   : TMVA
/// - Exectuable: TMVAClassificationApplication
///
/// \macro_output
/// \macro_code
/// \author Andreas Hoecker
#include <cstdlib>
#include <vector>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include "TTree.h"
#include "TString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TStopwatch.h"
#include "TMVA/Reader.h"
#include "TMVA/MethodCuts.h"
using namespace TMVA;
void TMVAClassificationApplication__DEF_CH___DEF_MC_( TString myMethodList = "" )
{
   // This loads the library
   TMVA::Tools::Instance();
   // Default MVA methods to be trained + tested
   std::map<std::string,int> Use;
   Use["Cuts"]            = 0;
   Use["CutsD"]           = 0;
   Use["CutsPCA"]         = 0;
   Use["CutsGA"]          = 0;
   Use["CutsSA"]          = 0;
   //
   // 1-dimensional likelihood ("naive Bayes estimator")
   Use["Likelihood"]      = 0;
   Use["LikelihoodD"]     = 0; // the "D" extension indicates decorrelated input variables (see option strings)
   Use["LikelihoodPCA"]   = 0; // the "PCA" extension indicates PCA-transformed input variables (see option strings)
   Use["LikelihoodKDE"]   = 0;
   Use["LikelihoodMIX"]   = 0;
   //
   // Mutidimensional likelihood and Nearest-Neighbour methods
   Use["PDERS"]           = 0;
   Use["PDERSD"]          = 0;
   Use["PDERSPCA"]        = 0;
   Use["PDEFoam"]         = 0;
   Use["PDEFoamBoost"]    = 0; // uses generalised MVA method boosting
   Use["KNN"]             = 0; // k-nearest neighbour method
   //
   // Linear Discriminant Analysis
   Use["LD"]              = 0; // Linear Discriminant identical to Fisher
   Use["Fisher"]          = 0;
   Use["FisherG"]         = 0;
   Use["BoostedFisher"]   = 0; // uses generalised MVA method boosting
   Use["HMatrix"]         = 0;
   //
   // Function Discriminant analysis
   Use["FDA_GA"]          = 0; // minimisation of user-defined function using Genetics Algorithm
   Use["FDA_SA"]          = 0;
   Use["FDA_MC"]          = 0;
   Use["FDA_MT"]          = 0;
   Use["FDA_GAMT"]        = 0;
   Use["FDA_MCMT"]        = 0;
   //
   // Neural Networks (all are feed-forward Multilayer Perceptrons)
   Use["MLP"]             = 0; // Recommended ANN
   Use["MLPBFGS"]         = 0; // Recommended ANN with optional training method
   Use["MLPBNN"]          = 0; // Recommended ANN with BFGS training method and bayesian regulator
   Use["CFMlpANN"]        = 0; // Depreciated ANN from ALEPH
   Use["TMlpANN"]         = 0; // ROOT's own ANN
   Use["DNN_GPU"] = 0;         // Multi-core accelerated DNN.
   Use["SVM"]             = 0;
   //
   // Boosted Decision Trees
   Use["BDT"]             = 1; // uses Adaptive Boost
   Use["BDTG"]            = 0; // uses Gradient Boost
   Use["BDTB"]            = 0; // uses Bagging
   Use["BDTD"]            = 0; // decorrelation + Adaptive Boost
   Use["BDTF"]            = 0; // allow usage of fisher discriminant for node splitting
   //
   // Friedman's RuleFit method, ie, an optimised series of cuts ("rules")
   Use["RuleFit"]         = 0;
   // ---------------------------------------------------------------
   Use["Plugin"]          = 0;
   Use["Category"]        = 0;
   Use["SVM_Gauss"]       = 0;
   Use["SVM_Poly"]        = 0;
   Use["SVM_Lin"]         = 0;

   std::cout << std::endl;
   std::cout << "==> Start TMVAClassificationApplication" << std::endl;

   // Select methods (don't look at this code - not of interest)
   if (myMethodList != "") {
      for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) it->second = 0;

      std::vector<TString> mlist = gTools().SplitString( myMethodList, ',' );
      for (UInt_t i=0; i<mlist.size(); i++) {
         std::string regMethod(mlist[i]);

         if (Use.find(regMethod) == Use.end()) {
            std::cout << "Method \"" << regMethod
                      << "\" not known in TMVA under this name. Choose among the following:" << std::endl;
            for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) {
               std::cout << it->first << " ";
            }
            std::cout << std::endl;
            return;
         }
         Use[regMethod] = 1;
      }
   }
   // Create the Reader object
   TMVA::Reader *reader = new TMVA::Reader( "!Color:!Silent" );
   // Create a set of variables and declare them to the reader
   // - the variable names MUST corresponds in name and type to those given in the weight file(s) used
   Float_t _DEF_VAR0_;
   Float_t _DEF_VAR1_;
   Float_t _DEF_VAR2_;
   Float_t _DEF_VAR3_;
   Float_t _DEF_VAR4_;
   Float_t _DEF_VAR5_;
   Float_t _DEF_VAR6_;
   Float_t _DEF_VAR7_;
   Float_t _DEF_VAR8_;
   Float_t _DEF_VAR9_;
   Float_t _DEF_VAR10_;
   Float_t _DEF_VAR11_;

   reader->AddVariable( "_DEF_VAR0_", &_DEF_VAR0_ );
   reader->AddVariable( "_DEF_VAR1_", &_DEF_VAR1_ );
   reader->AddVariable( "_DEF_VAR2_", &_DEF_VAR2_ );
   reader->AddVariable( "_DEF_VAR3_", &_DEF_VAR3_ );
   reader->AddVariable( "_DEF_VAR4_", &_DEF_VAR4_ );
   reader->AddVariable( "_DEF_VAR5_", &_DEF_VAR5_ );
   reader->AddVariable( "_DEF_VAR6_", &_DEF_VAR6_ );
   reader->AddVariable( "_DEF_VAR7_", &_DEF_VAR7_ );
   reader->AddVariable( "_DEF_VAR8_", &_DEF_VAR8_ );
   reader->AddVariable( "_DEF_VAR9_", &_DEF_VAR9_ );
   reader->AddVariable( "_DEF_VAR10_", &_DEF_VAR10_ );
   reader->AddVariable( "_DEF_VAR11_", &_DEF_VAR11_ );

   // Spectator variables declared in the training have to be added to the reader, too
   Float_t Category_cat1, Category_cat2, Category_cat3;
   if (Use["Category"]){
      // Add artificial spectators for distinguishing categories
      reader->AddSpectator( "Category_cat1 := var3<=0",             &Category_cat1 );
      reader->AddSpectator( "Category_cat2 := (var3>0)&&(var4<0)",  &Category_cat2 );
      reader->AddSpectator( "Category_cat3 := (var3>0)&&(var4>=0)", &Category_cat3 );
   }
   // Book the MVA methods
   TString dir    = "dataset/weights/";
   TString prefix = "TMVAClassification";
   // Book method(s)
   for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) {
      if (it->second) {
         TString methodName = TString(it->first) + TString(" method");
         TString weightfile = TString("../") + dir + prefix + TString("_") + TString(it->first) + TString(".weights.xml");
         reader->BookMVA( methodName, weightfile );
      }
   }
   UInt_t nbin = 20;
   //TH1F *_DEF_CH___DEF_MC__obs(0);   
   // For Data case, comment out from here
   TH1F *_DEF_CH___DEF_MC_(0);
   TH1F *_DEF_CH___DEF_MC__PUUp(0);
   TH1F *_DEF_CH___DEF_MC__PUDown(0);
   TH1F *_DEF_CH___DEF_MC__ElSFUp(0);
   TH1F *_DEF_CH___DEF_MC__ElSFDown(0);
   TH1F *_DEF_CH___DEF_MC__MuIDUp(0);
   TH1F *_DEF_CH___DEF_MC__MuIDDown(0);
   TH1F *_DEF_CH___DEF_MC__MuISOUp(0);
   TH1F *_DEF_CH___DEF_MC__MuISODown(0);
   TH1F *_DEF_CH___DEF_MC__MuRUp(0);
   TH1F *_DEF_CH___DEF_MC__MuRDown(0);
   TH1F *_DEF_CH___DEF_MC__MuFUp(0);
   TH1F *_DEF_CH___DEF_MC__MuFDown(0);
   TH1F *_DEF_CH___DEF_MC__BtagJESUp(0);
   TH1F *_DEF_CH___DEF_MC__BtagJESDown(0);
   TH1F *_DEF_CH___DEF_MC__BtagLFUp(0);
   TH1F *_DEF_CH___DEF_MC__BtagLFDown(0);
   TH1F *_DEF_CH___DEF_MC__BtagHFUp(0);
   TH1F *_DEF_CH___DEF_MC__BtagHFDown(0);
   TH1F *_DEF_CH___DEF_MC__BtagHFStats1Up(0);
   TH1F *_DEF_CH___DEF_MC__BtagHFStats1Down(0);
   TH1F *_DEF_CH___DEF_MC__BtagHFStats2Up(0);
   TH1F *_DEF_CH___DEF_MC__BtagHFStats2Down(0);
   TH1F *_DEF_CH___DEF_MC__BtagLFStats1Up(0);
   TH1F *_DEF_CH___DEF_MC__BtagLFStats1Down(0);
   TH1F *_DEF_CH___DEF_MC__BtagLFStats2Up(0);
   TH1F *_DEF_CH___DEF_MC__BtagLFStats2Down(0);
   TH1F *_DEF_CH___DEF_MC__BtagCQErr1Up(0);  
   TH1F *_DEF_CH___DEF_MC__BtagCQErr1Down(0);  
   TH1F *_DEF_CH___DEF_MC__BtagCQErr2Up(0);  
   TH1F *_DEF_CH___DEF_MC__BtagCQErr2Down(0);
   // to here

   //_DEF_CH___DEF_MC__obs = new TH1F("_DEF_CH___DEF_MC__obs", "_DEF_CH___DEF_MC__obs", nbin, -1.0, 1.0);
   // For Data, comment out here
   _DEF_CH___DEF_MC_ = new TH1F("_DEF_CH___DEF_MC_", "_DEF_CH___DEF_MC_", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__PUUp = new TH1F("_DEF_CH___DEF_MC__PUUp", "_DEF_CH___DEF_MC__PUUp", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__PUDown = new TH1F("_DEF_CH___DEF_MC__PUDown", "_DEF_CH___DEF_MC__PUDown", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__ElSFUp = new TH1F("_DEF_CH___DEF_MC__ElSFUp", "_DEF_CH___DEF_MC__ElSFUp", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__ElSFDown = new TH1F("_DEF_CH___DEF_MC__ElSFDown", "_DEF_CH___DEF_MC__ElSFDown", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__MuIDUp = new TH1F("_DEF_CH___DEF_MC__MuIDUp", "_DEF_CH___DEF_MC__MuIDUp", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__MuIDDown = new TH1F("_DEF_CH___DEF_MC__MuIDDown", "_DEF_CH___DEF_MC__MuIDDown", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__MuISOUp = new TH1F("_DEF_CH___DEF_MC__MuISOUp", "_DEF_CH___DEF_MC__MuISOUp", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__MuISODown = new TH1F("_DEF_CH___DEF_MC__MuISODown", "_DEF_CH___DEF_MC__MuISODown", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__MuRUp = new TH1F("_DEF_CH___DEF_MC__MuRUp", "_DEF_CH___DEF_MC__MuRUp", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__MuRDown = new TH1F("_DEF_CH___DEF_MC__MuRDown", "_DEF_CH___DEF_MC__MuRDown", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__MuFUp = new TH1F("_DEF_CH___DEF_MC__MuFUp", "_DEF_CH___DEF_MC__MuFUp", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__MuFDown = new TH1F("_DEF_CH___DEF_MC__MuFDown", "_DEF_CH___DEF_MC__MuFDown", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagJESUp = new TH1F("_DEF_CH___DEF_MC__BtagJESUp", "_DEF_CH___DEF_MC__BtagJESUp", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagJESDown = new TH1F("_DEF_CH___DEF_MC__BtagJESDown", "_DEF_CH___DEF_MC__BtagJESDown", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagLFUp = new TH1F("_DEF_CH___DEF_MC__BtagLFUp", "_DEF_CH___DEF_MC__BtagLFUp", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagLFDown = new TH1F("_DEF_CH___DEF_MC__BtagLFDown", "_DEF_CH___DEF_MC__BtagLFDown", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagHFUp = new TH1F("_DEF_CH___DEF_MC__BtagHFUp", "_DEF_CH___DEF_MC__BtagHFUp", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagHFDown = new TH1F("_DEF_CH___DEF_MC__BtagHFDown", "_DEF_CH___DEF_MC__BtagHFDown", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagHFStats1Up = new TH1F("_DEF_CH___DEF_MC__BtagHFStats1Up", "_DEF_CH___DEF_MC__BtagHFStats1Up", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagHFStats1Down = new TH1F("_DEF_CH___DEF_MC__BtagHFStats1Down", "_DEF_CH___DEF_MC__BtagHFStats1Down", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagHFStats2Up = new TH1F("_DEF_CH___DEF_MC__BtagHFStats2Up", "_DEF_CH___DEF_MC__BtagHFStats2Up", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagHFStats2Down = new TH1F("_DEF_CH___DEF_MC__BtagHFStats2Down", "_DEF_CH___DEF_MC__BtagHFStats2Down", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagLFStats1Up = new TH1F("_DEF_CH___DEF_MC__BtagLFStats1Up", "_DEF_CH___DEF_MC__BtagLFStats1Up", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagLFStats1Down = new TH1F("_DEF_CH___DEF_MC__BtagLFStats1Down", "_DEF_CH___DEF_MC__BtagLFStats1Down", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagLFStats2Up = new TH1F("_DEF_CH___DEF_MC__BtagLFStats2Up", "_DEF_CH___DEF_MC__BtagLFStats2Up", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagLFStats2Down = new TH1F("_DEF_CH___DEF_MC__BtagLFStats2Down", "_DEF_CH___DEF_MC__BtagLFStats2Down", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagCQErr1Up = new TH1F("_DEF_CH___DEF_MC__BtagCQErr1Up", "_DEF_CH___DEF_MC__BtagCQErr1Up", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagCQErr1Down = new TH1F("_DEF_CH___DEF_MC__BtagCQErr1Down", "_DEF_CH___DEF_MC__BtagCQErr1Down", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagCQErr2Up = new TH1F("_DEF_CH___DEF_MC__BtagCQErr2Up", "_DEF_CH___DEF_MC__BtagCQErr2Up", nbin, -1.0, 1.0);
   _DEF_CH___DEF_MC__BtagCQErr2Down = new TH1F("_DEF_CH___DEF_MC__BtagCQErr2Down", "_DEF_CH___DEF_MC__BtagCQErr2Down", nbin, -1.0, 1.0);

      // Prepare input tree (this must be replaced by your data source)
   // in this example, there is a toy tree with signal and one with background events
   // we'll later on use only the "signal" events for the test in this example.
   TChain *theTree = new TChain("Events");

   std::string file_in_line;
   ifstream file_in("_DEF_TEXT_");
   while (std::getline(file_in, file_in_line)){
      TString file_in_line_R = file_in_line;
      theTree->Add(file_in_line_R);
   }

   /*TFile *input(0);
   TString fname = "./tmva_class_example.root";
   if (!gSystem->AccessPathName( fname )) {
      input = TFile::Open( fname ); // check if file in local directory exists
   }
   else {
      TFile::SetCacheFileDir(".");
      input = TFile::Open("http://root.cern.ch/files/tmva_class_example.root", "CACHEREAD"); // if not: download from ROOT server
   }
   if (!input) {
      std::cout << "ERROR: could not open data file" << std::endl;
      exit(1);
   }
   std::cout << "--- TMVAClassificationApp    : Using input file: " << input->GetName() << std::endl;*/

   // Event loop

   // Prepare the event tree
   // - Here the variable names have to corresponds to your tree
   // - You can use the same variables as above which is slightly faster,
   //   but of course you can use different ones and copy the values inside the event loop
   //
   std::cout << "--- Select signal sample" << std::endl;
   //Float_t userVar1, userVar2;
   theTree->SetBranchAddress( "_DEF_VAR0_", &_DEF_VAR0_ );
   theTree->SetBranchAddress( "_DEF_VAR1_", &_DEF_VAR1_ );
   theTree->SetBranchAddress( "_DEF_VAR2_", &_DEF_VAR2_ );
   theTree->SetBranchAddress( "_DEF_VAR3_", &_DEF_VAR3_ );
   theTree->SetBranchAddress( "_DEF_VAR4_", &_DEF_VAR4_ );
   theTree->SetBranchAddress( "_DEF_VAR5_", &_DEF_VAR5_ );
   theTree->SetBranchAddress( "_DEF_VAR6_", &_DEF_VAR6_ );
   theTree->SetBranchAddress( "_DEF_VAR7_", &_DEF_VAR7_ );
   theTree->SetBranchAddress( "_DEF_VAR8_", &_DEF_VAR8_ );
   theTree->SetBranchAddress( "_DEF_VAR9_", &_DEF_VAR9_ );
   theTree->SetBranchAddress( "_DEF_VAR10_", &_DEF_VAR10_ );
   theTree->SetBranchAddress( "_DEF_VAR11_", &_DEF_VAR11_ );
 
   const Int_t LHEindex = 9;
   // For Data case, comment out from here...
   Float_t LHEScaleWeight[LHEindex];
   Float_t genWeight;
   Float_t puWeight;
   Double_t BtagWeight;
   Float_t Trigger_SF;
   Float_t Electron_SF;
   Float_t Electron_SFerr;
   Float_t MuonID_SF;
   Float_t MuonID_SFerr;
   Float_t MuonISO_SF;
   Float_t MuonISO_SFerr;
   Float_t xsecNorm;
   Float_t puWeightUp;
   Float_t puWeightDown;
   Double_t BtagWeight_btagSF_deepjet_shape_up_jes;
   Double_t BtagWeight_btagSF_deepjet_shape_down_jes;
   Double_t BtagWeight_btagSF_deepjet_shape_up_lf;
   Double_t BtagWeight_btagSF_deepjet_shape_down_lf;
   Double_t BtagWeight_btagSF_deepjet_shape_up_hf;
   Double_t BtagWeight_btagSF_deepjet_shape_down_hf;
   Double_t BtagWeight_btagSF_deepjet_shape_up_hfstats1;
   Double_t BtagWeight_btagSF_deepjet_shape_down_hfstats1;
   Double_t BtagWeight_btagSF_deepjet_shape_up_hfstats2;
   Double_t BtagWeight_btagSF_deepjet_shape_down_hfstats2;
   Double_t BtagWeight_btagSF_deepjet_shape_up_lfstats1;
   Double_t BtagWeight_btagSF_deepjet_shape_down_lfstats1;
   Double_t BtagWeight_btagSF_deepjet_shape_up_lfstats2;
   Double_t BtagWeight_btagSF_deepjet_shape_down_lfstats2;
   Double_t BtagWeight_btagSF_deepjet_shape_up_cferr1;
   Double_t BtagWeight_btagSF_deepjet_shape_down_cferr1;
   Double_t BtagWeight_btagSF_deepjet_shape_up_cferr2;
   Double_t BtagWeight_btagSF_deepjet_shape_down_cferr2;
   theTree->SetBranchAddress( "LHEScaleWeight", &LHEScaleWeight);
   theTree->SetBranchAddress( "genWeight", &genWeight);
   theTree->SetBranchAddress( "puWeight", &puWeight);
   theTree->SetBranchAddress( "BtagWeight", &BtagWeight);
   theTree->SetBranchAddress( "Trigger_SF", &Trigger_SF);
   theTree->SetBranchAddress( "Electron_SF", &Electron_SF);
   theTree->SetBranchAddress( "MuonID_SF", &MuonID_SF);
   theTree->SetBranchAddress( "MuonID_SFerr", &MuonID_SFerr);
   theTree->SetBranchAddress( "MuonISO_SF", &MuonISO_SF);
   theTree->SetBranchAddress( "MuonISO_SFerr", &MuonISO_SFerr);
   theTree->SetBranchAddress( "xsecNorm", &xsecNorm);
   theTree->SetBranchAddress( "puWeightUp", &puWeightUp);
   theTree->SetBranchAddress( "puWeightDown", &puWeightDown);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_up_jes", &BtagWeight_btagSF_deepjet_shape_up_jes);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_down_jes", &BtagWeight_btagSF_deepjet_shape_down_jes);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_up_lf", &BtagWeight_btagSF_deepjet_shape_up_lf);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_down_lf", &BtagWeight_btagSF_deepjet_shape_down_lf);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_up_hf", &BtagWeight_btagSF_deepjet_shape_up_hf);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_down_hf", &BtagWeight_btagSF_deepjet_shape_down_hf);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_up_hfstats1", &BtagWeight_btagSF_deepjet_shape_up_hfstats1);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_down_hfstats1", &BtagWeight_btagSF_deepjet_shape_down_hfstats1);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_up_hfstats2", &BtagWeight_btagSF_deepjet_shape_up_hfstats2);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_down_hfstats2", &BtagWeight_btagSF_deepjet_shape_down_hfstats2);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_up_lfstats1", &BtagWeight_btagSF_deepjet_shape_up_lfstats1);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_down_lfstats1", &BtagWeight_btagSF_deepjet_shape_down_lfstats1);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_up_lfstats2", &BtagWeight_btagSF_deepjet_shape_up_lfstats2);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_down_lfstats2", &BtagWeight_btagSF_deepjet_shape_down_lfstats2);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_up_cferr1", &BtagWeight_btagSF_deepjet_shape_up_cferr1);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_down_cferr1", &BtagWeight_btagSF_deepjet_shape_down_cferr1);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_up_cferr2", &BtagWeight_btagSF_deepjet_shape_up_cferr2);
   theTree->SetBranchAddress( "BtagWeight_btagSF_deepjet_shape_down_cferr2", &BtagWeight_btagSF_deepjet_shape_down_cferr2);
   // To here.

   // For TTSR cut selection. Compare with input variables!
   Int_t CutStep;
   //Float_t W_MT; // Already mentioned
   //Float_t Z_mass; //Already mentioned
   Int_t nGoodJet;
   Int_t nBjet;
   Float_t LeadingLepton_pt;
   Int_t Z_charge;
   Bool_t HLT;
   theTree->SetBranchAddress( "CutStep", &CutStep);
   //theTree->SetBranchAddress( "W_MT", &W_MT);
   //theTree->SetBranchAddress( "Z_mass", &Z_mass);
   theTree->SetBranchAddress( "nGoodJet", &nGoodJet);
   theTree->SetBranchAddress( "nBjet", &nBjet);
   theTree->SetBranchAddress( "LeadingLepton_pt", &LeadingLepton_pt);
   theTree->SetBranchAddress( "Z_charge", &Z_charge);
   theTree->SetBranchAddress( "HLT", &HLT);
   
  
   // Efficiency calculator for cut method
   Int_t    nSelCutsGA = 0;
   Double_t effS       = 0.7;

   std::vector<Float_t> vecVar(4); // vector for EvaluateMVA tests

   std::cout << "--- Processing: " << theTree->GetEntries() << " events" << std::endl;
   TStopwatch sw;
   sw.Start();
   for (Long64_t ievt=0; ievt<theTree->GetEntries();ievt++) {

      if (ievt%1000 == 0) std::cout << "--- ... Processing event: " << ievt << std::endl;

      theTree->GetEntry(ievt);
      //var1 = userVar1 + userVar2;
      //var2 = userVar1 - userVar2;

      // TTSR conditions
      if  ( _DEF_CUT_ ) continue;
 
      // Return the MVA outputs and save the values to save MVA output score
      Float_t MVAscore = reader->EvaluateMVA( "BDT method" );

      // LHEScaleWeight save(For Data, comment out)
      Float_t LHEScale;
      Float_t LHEScale_MuRUp;
      Float_t LHEScale_MuRDown;
      Float_t LHEScale_MuFUp;
      Float_t LHEScale_MuFDown;
      for ( Int_t n=0;n<LHEindex;n++) {
         if ( n==4 ) LHEScale = LHEScaleWeight[n];
         else if ( n==7 ) LHEScale_MuRUp = LHEScaleWeight[n];
         else if ( n==1 ) LHEScale_MuRDown = LHEScaleWeight[n];
         else if ( n==5 ) LHEScale_MuFUp = LHEScaleWeight[n];
         else if ( n==3 ) LHEScale_MuFDown = LHEScaleWeight[n];
      }
      // Lepton SF error calculation(For Data, comment out)
      Float_t ElSFUp;
      Float_t ElSFDown;
      Float_t MuIDUp;
      Float_t MuIDDown;
      Float_t MuISOUp;
      Float_t MuISODown;
      ElSFUp = Electron_SF + Electron_SFerr;
      ElSFDown = Electron_SF - Electron_SFerr;
      MuIDUp = MuonID_SF + MuonID_SFerr;
      MuIDDown = MuonID_SF - MuonID_SFerr;
      MuISOUp = MuonISO_SF + MuonISO_SFerr;
      MuISODown = MuonISO_SF - MuonISO_SFerr;

      // Fill histograms
      //_DEF_CH___DEF_MC__obs -> Fill( MVAscore );
      // For Data case, comment out here
      _DEF_CH___DEF_MC_ -> Fill( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight*xsecNorm );
      _DEF_CH___DEF_MC__PUUp -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeightUp*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight*xsecNorm  );
      _DEF_CH___DEF_MC__PUDown -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeightDown*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight*xsecNorm  );
      _DEF_CH___DEF_MC__ElSFUp -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*ElSFUp*MuonID_SF*MuonISO_SF*BtagWeight*xsecNorm );
      _DEF_CH___DEF_MC__ElSFDown -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*ElSFDown*MuonID_SF*MuonISO_SF*BtagWeight*xsecNorm );
      _DEF_CH___DEF_MC__MuIDUp -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuIDUp*MuonISO_SF*BtagWeight*xsecNorm );
      _DEF_CH___DEF_MC__MuIDDown -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuIDDown*MuonISO_SF*BtagWeight*xsecNorm );
      _DEF_CH___DEF_MC__MuISOUp -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuISOUp*BtagWeight*xsecNorm );
      _DEF_CH___DEF_MC__MuISODown -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuISODown*BtagWeight*xsecNorm );
      _DEF_CH___DEF_MC__MuRUp -> Fill( MVAscore, LHEScale_MuRUp*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight*xsecNorm );
      _DEF_CH___DEF_MC__MuRDown -> Fill( MVAscore, LHEScale_MuRDown*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight*xsecNorm );
      _DEF_CH___DEF_MC__MuFUp -> Fill( MVAscore, LHEScale_MuFUp*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight*xsecNorm );
      _DEF_CH___DEF_MC__MuFDown -> Fill( MVAscore, LHEScale_MuFDown*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight*xsecNorm );
      _DEF_CH___DEF_MC__BtagJESUp -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_up_jes*xsecNorm  );
      _DEF_CH___DEF_MC__BtagJESDown -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_down_jes*xsecNorm  );
      _DEF_CH___DEF_MC__BtagLFUp -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_up_lf*xsecNorm  );
      _DEF_CH___DEF_MC__BtagLFDown -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_down_lf*xsecNorm  );
      _DEF_CH___DEF_MC__BtagHFUp -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_up_hf*xsecNorm  );
      _DEF_CH___DEF_MC__BtagHFDown -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_down_hf*xsecNorm  );
      _DEF_CH___DEF_MC__BtagHFStats1Up -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_up_hfstats1*xsecNorm  );
      _DEF_CH___DEF_MC__BtagHFStats1Down -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_down_hfstats1*xsecNorm  );
      _DEF_CH___DEF_MC__BtagHFStats2Up -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_up_hfstats2*xsecNorm  );
      _DEF_CH___DEF_MC__BtagHFStats2Down -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_down_hfstats2*xsecNorm  );
      _DEF_CH___DEF_MC__BtagLFStats1Up -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_up_lfstats1*xsecNorm  );
      _DEF_CH___DEF_MC__BtagLFStats1Down -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_down_lfstats1*xsecNorm  );
      _DEF_CH___DEF_MC__BtagLFStats2Up -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_up_lfstats2*xsecNorm  );
      _DEF_CH___DEF_MC__BtagLFStats2Down -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_down_lfstats2*xsecNorm  );
      _DEF_CH___DEF_MC__BtagCQErr1Up -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_up_cferr1*xsecNorm  ); 
      _DEF_CH___DEF_MC__BtagCQErr1Down -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_down_cferr1*xsecNorm  );
      _DEF_CH___DEF_MC__BtagCQErr2Up -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_up_cferr2*xsecNorm  );
      _DEF_CH___DEF_MC__BtagCQErr2Down -> Fill ( MVAscore, LHEScale*(abs(genWeight)/genWeight)*puWeight*Trigger_SF*Electron_SF*MuonID_SF*MuonISO_SF*BtagWeight_btagSF_deepjet_shape_down_cferr2*xsecNorm  );
   }

   // Get elapsed time
   sw.Stop();
   std::cout << "--- End of event loop: "; sw.Print();

   // Get efficiency for cuts classifier
   if (Use["CutsGA"]) std::cout << "--- Efficiency for CutsGA method: " << double(nSelCutsGA)/theTree->GetEntries()
                                << " (for a required signal efficiency of " << effS << ")" << std::endl;

   if (Use["CutsGA"]) {

      // test: retrieve cuts for particular signal efficiency
      // CINT ignores dynamic_casts so we have to use a cuts-secific Reader function to acces the pointer
      TMVA::MethodCuts* mcuts = reader->FindCutsMVA( "CutsGA method" ) ;

      if (mcuts) {
         std::vector<Double_t> cutsMin;
         std::vector<Double_t> cutsMax;
         mcuts->GetCuts( 0.7, cutsMin, cutsMax );
         std::cout << "--- -------------------------------------------------------------" << std::endl;
         std::cout << "--- Retrieve cut values for signal efficiency of 0.7 from Reader" << std::endl;
         for (UInt_t ivar=0; ivar<cutsMin.size(); ivar++) {
            std::cout << "... Cut: "
                      << cutsMin[ivar]
                      << " < \""
                      << mcuts->GetInputVar(ivar)
                      << "\" <= "
                      << cutsMax[ivar] << std::endl;
         }
         std::cout << "--- -------------------------------------------------------------" << std::endl;
      }
   }


   // Write histograms

   TFile *target  = new TFile( "_DEF_CH___DEF_MC_.root","RECREATE" );
   //_DEF_CH___DEF_MC__obs -> Write();
   // For Data, commnet out here
   _DEF_CH___DEF_MC_ -> Write();
   _DEF_CH___DEF_MC__PUUp -> Write();
   _DEF_CH___DEF_MC__PUDown -> Write();
   _DEF_CH___DEF_MC__ElSFUp -> Write();
   _DEF_CH___DEF_MC__ElSFDown -> Write();
   _DEF_CH___DEF_MC__MuIDUp -> Write();
   _DEF_CH___DEF_MC__MuIDDown -> Write();
   _DEF_CH___DEF_MC__MuISOUp -> Write();
   _DEF_CH___DEF_MC__MuISODown -> Write();
   _DEF_CH___DEF_MC__MuRUp -> Write();
   _DEF_CH___DEF_MC__MuRDown -> Write();
   _DEF_CH___DEF_MC__MuFUp -> Write();
   _DEF_CH___DEF_MC__MuFDown -> Write();
   _DEF_CH___DEF_MC__BtagJESUp -> Write();
   _DEF_CH___DEF_MC__BtagJESDown -> Write();
   _DEF_CH___DEF_MC__BtagLFUp -> Write();
   _DEF_CH___DEF_MC__BtagLFDown -> Write();
   _DEF_CH___DEF_MC__BtagHFUp -> Write();
   _DEF_CH___DEF_MC__BtagHFDown -> Write();
   _DEF_CH___DEF_MC__BtagHFStats1Up -> Write();
   _DEF_CH___DEF_MC__BtagHFStats1Down -> Write();
   _DEF_CH___DEF_MC__BtagHFStats2Up -> Write();
   _DEF_CH___DEF_MC__BtagHFStats2Down -> Write();
   _DEF_CH___DEF_MC__BtagLFStats1Up -> Write();
   _DEF_CH___DEF_MC__BtagLFStats1Down -> Write();
   _DEF_CH___DEF_MC__BtagLFStats2Up -> Write();
   _DEF_CH___DEF_MC__BtagLFStats2Down -> Write();
   _DEF_CH___DEF_MC__BtagCQErr1Up -> Write();
   _DEF_CH___DEF_MC__BtagCQErr1Down -> Write();
   _DEF_CH___DEF_MC__BtagCQErr2Up -> Write();
   _DEF_CH___DEF_MC__BtagCQErr2Down -> Write();

   target->Close();

   std::cout << "--- Created root file: \"_DEF_CH___DEF_MC_.root\" containing the MVA output histograms" << std::endl;

   delete reader;

   std::cout << "==> TMVAClassificationApplication is done!" << std::endl << std::endl;
}

int main( int argc, char** argv )
{
   TString methodList;
   for (int i=1; i<argc; i++) {
      TString regMethod(argv[i]);
      if(regMethod=="-b" || regMethod=="--batch") continue;
      if (!methodList.IsNull()) methodList += TString(",");
      methodList += regMethod;
   }
   TMVAClassificationApplication__DEF_CH___DEF_MC_(methodList);
   return 0;
}
