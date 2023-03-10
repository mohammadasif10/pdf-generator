from fpdf import FPDF #importing a class called FPDF so you can create instances of FPDF objects. Each class has methods associated with its instances. That's why we create an instance mypdf. After that, all those methods are accesible to mypdf 
import pandas as pd


mypdf = FPDF(orientation="P", unit="mm", format="A4")#orientation can be eitehr L or P, unit is definfing what unit we may pass other paramaters in with like if I jsut made the margins and passed it an argument of 1, it will know that i mean 1 mm. can change units. format is just a predefined format, many exist just search them.
csvreader = pd.read_csv("topics.csv")
for index, row in csvreader.iterrows():
  mypdf.add_page()
  mypdf.set_font(family="Times", style="B", size=24)#everything after this line will have this font. sometimes a default font is selected automatically, sometimes, before addigntext you MUST set a font otherwise lots of errors. takes three arguments. NOTE: size in this is not in mm as defined before. that's for everything else besides size
  mypdf.set_text_color(100,100,100)#(RGB) for grey
  mypdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1) #border=1)
#w and h are the size of the field we are creating. when it = 0, it goes to the end of the page. these sizes are in mm. txt is just the text. align is just text alignment left, right, or center.
  #ln is the line break. if ln is set to 0, the next field starts exactly where the last one ended so if ln was 0 and w of the forst one was not till the end if the line, it would create the second field on the same line as the first one and they'd be touching. setting ln to 1 will make everything clean on its own line. border outlines the field and shows exactly how big it is. 1 for on, just don't list it for off
  mypdf.line(10,22,200,22)#draws a line, values are in mm bc that's predefiend (x1, y1, x2, y2)(distance from left of page to where line starts, distance from top of page where line starts, distance from LEFT of page(starts from beginning of left, usually way bigger, best to think of it as where it ends, maybe can use negative numbers, and the distance from top where line ends))
  #print(row)prints values of csv file but also prints Name which is just the index iterrows gives it and dtype which iis just data type, just object in this instance bc its an object of pandas

  for i in range(row["pages"] - 1):#inside top loop so it can access each row as it loops through it, minus 1 bc we already create an initial page each time the first loop runs in forst line, this will create whatever the each row says for pages but since we alr have 1, we just subtract it here 
    mypdf.addpage()
#for i in range(5):
  #print("hello") #this is a for loop that iterates over a range starting from 0 anf containing the number of elements passed as a parameter. range(5) is like 0,1,2,3,4. 5 total numbers but i will only ever equal 4, not 5 in this loop due to range starting at 0 as well.


mypdf.output("myoutput.pdf")