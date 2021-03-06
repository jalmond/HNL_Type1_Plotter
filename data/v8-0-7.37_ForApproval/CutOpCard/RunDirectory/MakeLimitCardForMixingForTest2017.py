import os
from python.MakeLimitDatacardForTest2017 import MakeLimitDatacardForTest2017

channels = ["MuMu", "ElEl", "MuEl"]
Bins = ["Bin1", "Bin2"]

masses = [40, 50, 60, 70, 80, 90, 100, 125, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
massesVBF = [300, 600, 800, 1000, 1200]

resultdir = "Outputs_MixingLimit"
carddir = resultdir+"/DatacardsForTest2017/"

for ch in channels:

  for Bin in Bins:

    this_resultdir = resultdir+"/"+ch+"_"+Bin

    for mass in masses:

      this_resultfilename = this_resultdir+"/HN"+ch+"_"+str(mass)+".log"
      MakeLimitDatacardForTest2017(this_resultfilename, ch, mass, carddir+"/"+ch+"_"+Bin, 'HN'+ch+'_'+str(mass)+'.txt')

    for mass in massesVBF:

      this_resultfilename = this_resultdir+"/HN"+ch+"_"+str(mass)+"_VBF.log"
      MakeLimitDatacardForTest2017(this_resultfilename, ch, mass, carddir+"/"+ch+"_"+Bin, 'HN'+ch+'_'+str(mass)+'_VBF.txt')
