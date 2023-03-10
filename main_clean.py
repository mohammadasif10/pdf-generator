from fpdf import FPDF 
import pandas as pd


mypdf = FPDF(orientation="P", unit="mm", format="A4")
mypdf.set_auto_page_break(auto=False, margin=0)
csvreader = pd.read_csv("topics.csv")

#add parent pages
for index, row in csvreader.iterrows():
  mypdf.add_page()
  mypdf.set_font(family="Times", style="B", size=24)
  mypdf.set_text_color(100,100,100)
  mypdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
  
  #draw lines
  for i in range(20, 298, 10):
    mypdf.line(10, i, 200, i)
    
  #set footer
  mypdf.ln(265)
  mypdf.set_font(family="Times", style="B", size=8)
  mypdf.set_text_color(180,180,180)#grey
  mypdf.cell(w=0, h=10, txt=row["Topic"], align="R")
  
  #add child pages
  for i in range(row["Pages"] - 1):
    mypdf.add_page()
    
    #add lines
    for i in range(10, 298, 10):
      mypdf.line(10,i,200,i)
      
    #add footer  
    mypdf.ln(275)
    mypdf.set_font(family="Times", style="B", size=8)
    mypdf.set_text_color(180,180,180)#grey
    mypdf.cell(w=0, h=10, txt=row["Topic"], align="R")

mypdf.output("myoutput.pdf")