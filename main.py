from fpdf import FPDF #importing a class called FPDF so you can create instances of FPDF objects. Each class has methods associated with its instances. That's why we create an instance mypdf. After that, all those methods are accesible to mypdf 
import pandas as pd


mypdf = FPDF(orientation="P", unit="mm", format="A4")#orientation can be eitehr L or P, unit is definfing what unit we may pass other paramaters in with like if I jsut made the margins and passed it an argument of 1, it will know that i mean 1 mm. can change units. format is just a predefined format, many exist just search them. dimensions of a4 are 210x297mm
mypdf.set_auto_page_break(auto=False, margin=0)#pakes sure page breaks arent automatic(not sure)
csvreader = pd.read_csv("topics.csv")
for index, row in csvreader.iterrows():
  mypdf.add_page()
  mypdf.set_font(family="Times", style="B", size=24)#everything after this line will have this font. sometimes a default font is selected automatically, sometimes, before addigntext you MUST set a font otherwise lots of errors. takes three arguments. NOTE: size in this is not in mm as defined before. that's for everything else besides size
  mypdf.set_text_color(100,100,100)#(RGB) for grey
  mypdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1) #border=1)
#w and h are the size of the field we are creating. when it = 0, it goes to the end of the page. width and height sizes are in mm. 12 is it being 12mm down from the top. txt is just the text. align is just text alignment left, right, or center.
  #ln is the line break. if ln is set to 0, the next field starts exactly where the last one ended so if ln was 0 and w of the forst one was not till the end if the line, it would create the second field on the same line as the first one and they'd be touching. setting ln to 1 will make everything clean on its own line. border outlines the field and shows exactly how big it is. 1 for on, just don't list it for off
  for i in range(20, 298, 10):#this is saying for in range beteween 20 and 298, third number is how much to increment by and in this case is 10 so it'll count by 10 each time. so to recap, i will initailize as 20, not 0 as is the case in saying range(4)(0,1,2,3). Then, it'll count up by 10 each time.
    mypdf.line(10, i, 200, i)#line will start 10mm from left page, and i will be the number of millimeters from the top it is and will increment by 10, 200 is how many mm from the left of page line stop, i is the same thing. basically each lines starts 10 mm from the left and goes to the left till it hits 200mm on the page(jumps 190mm). i stays the same bc its a stright line and stays the same distance from the top.
  mypdf.line(10,22,200,22)#draws a line, values are in mm bc that's predefiend (x1, y1, x2, y2)(distance from left of page to where line starts, distance from top of page where line starts, distance from LEFT of page(starts from beginning of left, usually way bigger, best to think of it as where it ends, maybe can use negative numbers, and the distance from top where line ends))
  #print(row)prints values of csv file but also prints Name which is just the index iterrows gives it and dtype which iis just data type, just object in this instance bc its an object of pandas
#set footer
  mypdf.ln(265)#pdf basically has a cursor where it "writes" things. since the last thing we "wrote" is making that line underneath title, the cursor is there rn. This makes it jump 265mm from that spot by making line breaks(blank lines) and now it will "write" there
  mypdf.set_font(family="Times", style="B", size=8)
  mypdf.set_text_color(180,180,180)#grey
  mypdf.cell(w=0, h=10, txt=row["Topic"], align="R")

  for i in range(row["Pages"] - 1):#inside top loop so it can access each row as it loops through it, minus 1 bc we already create an initial page each time the first loop runs in forst line, this will create whatever the each row says for pages but since we alr have 1, we just subtract it here.
    #this is called a nested for loop, a for loop inside of another for loop. A for loop usually executes all the code inside it each iteration. since this for loop is part of the code of the outer for loop, this will loop all the times it needs to before a single iteratrion of the outer loop is considered complete
    mypdf.add_page()
    #set lines in new pages
    for i in range(10, 298, 10):#starts at 10 this time bc no title to account for
      mypdf.line(10,i,200,i)
    #set footer in new pages  
    mypdf.ln(275)#since new pages don't have titles written to them, the cursor isn't at the end of the title but at thte top of the page so has to jump more mm here
    mypdf.set_font(family="Times", style="B", size=8)
    mypdf.set_text_color(180,180,180)#grey
    mypdf.cell(w=0, h=10, txt=row["Topic"], align="R")
#for i in range(5):
  #print("hello") #this is a for loop that iterates over a range starting from 0 anf containing the number of elements passed as a parameter. range(5) is like 0,1,2,3,4. 5 total numbers but i will only ever equal 4, not 5 in this loop due to range starting at 0 as well.


mypdf.output("myoutput.pdf")