## this requires fpdf library to be installed in Python!

import os, os.path, csv, time
from fpdf import FPDF

def Divide():
    print("")
    time.sleep(0.01)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(0.01)
    print("")

def CreatePDF():
    with open(csvpath, newline="") as f:
        print("Creating PDF file...\n")
        reader = csv.reader(f)

        pdf = FPDF()
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin

        pdf.set_font( "Times", "B", 14.0 )
        pdf.cell( page_width, 0.0, "Class Roster - " + classID, align="L" )
        pdf.ln( 10 )

        pdf.set_font( "Times", "B", 20 )
                
        col_width = page_width/4

        pdf.ln( 1 )

        th = pdf.font_size

        rows = list(reader)
                
        for i in range(0, len(rows)):
            if (i != 0):
                print("Adding " + rows[i][0].replace('"','') + " " + rows[i][1].replace('"','') + " - " + rows[i][2].replace('"',''))

            pdf.cell( col_width, th, str(rows[i][0]).replace('"',''), border=1 )
            pdf.cell( col_width, th, rows[i][1].replace('"',''), border=1 )
            pdf.cell( col_width, th, rows[i][2].replace('"',''), border=1 )
            pdf.ln( th )
                    
            if (i == 0):
                pdf.set_font( "Times", "", 12 )
                
            time.sleep(0.01)

        print("\nWriting to pdf...\n")
        time.sleep(0.01)
        pdf.output( pdfpath, "F" )
        time.sleep(0.01)
        print("Complete!\nCreated new PDF file at " + pdfpath)
        Divide()

filepath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

Divide()
print("\nWelcome to the Black Rocket Username Tool!\n\nAuthor: Courteney T\nContributor(s): Ethan H\n\nSearching for .csv files in directory:\n" + filepath)
Divide()
    
while True:
    classID = input( "Enter Class ID or 'exit': " ).upper()
    
    if (classID.upper() == "EXIT"):
        print("\nHave a great day!")
        Divide()
        os._exit(0)
        
    Divide()

    if (len(classID) != 6):
        print("Invalid class ID!\nPlease enter a 6-letter code")
        Divide()
    else:
        csvpath = os.path.join(filepath, classID) + ".csv"
        pdfpath = os.path.join(filepath, classID) + ".pdf"
        
        if (not os.path.isfile(csvpath)):
            print("No CSV file named " + classID + " at ""\n" + csvpath + "")
            Divide()
        elif (os.path.isfile(pdfpath)):
            print("PDF file named " + classID + " already exists!\n")

            overwrite = ""

            while overwrite != "YES" and overwrite != "NO":
                overwrite = input( "Overwrite?: " ).upper()
                
                if overwrite != "YES" and overwrite != "NO":
                    print("'" + overwrite + "' is an invalid response. Please answer 'yes' or 'no'!\n")

            if overwrite == "YES":
                CreatePDF()
            else:
                Divide()
        else:
            CreatePDF()
