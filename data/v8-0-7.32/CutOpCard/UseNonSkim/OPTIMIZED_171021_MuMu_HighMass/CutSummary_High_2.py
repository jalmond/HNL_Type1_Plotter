import os

masses = [250, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]

varorder = [
"leadingLepton_Pt >",
"secondLepton_Pt >",

"m_jj_jjWclosest >",
"m_jj_jjWclosest <",

"m_lljj_jjWclosest >",

"m_SubLeadljj_jjWclosest >",
"m_SubLeadljj_jjWclosest <",

"MET2ST <",
]
names = [
"pt1 >\t",
"pt2 >\t",

"m(jj)\t",
"",

"m(lljj) >\t",

"m(l2jj)\t",
"",

"MET2/ST <\t",
]

varsinboth = [
"m_jj_jjWclosest >",
"m_SubLeadljj_jjWclosest >"
]

print 'm(N) [GeV]\t',
for name in names:
  print name,
print ""

for mass in masses:
  lines = open('HNMuMu_'+str(mass)+'.txt').readlines()

  print str(mass)+'\t',
  counter = 0
  for var in varorder:
    for line in lines:
      words = line.split()
      this_var = words[0]+" "+words[1]
      if not (this_var == var):
        continue

      value = str(int(float(words[2])))

      if var in varsinboth:
        print value+" -",
      else:
        print value+'\t',

    counter = counter+1
  print ""