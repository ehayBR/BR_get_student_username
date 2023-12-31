## this requires fpdf library to be installed in Python!

import os.path, csv
from fpdf import FPDF

while True:
    classID = input( "Enter class ID: " ).upper()
    print("")
    
    if (len(classID) != 6):
        print("Invalid class ID!\nPlease enter a 6-letter code")
    else:
        path = os.path.join(os.path.dirname(__file__), classID) + ".csv"
    
        if (not os.path.isfile(path)):
            print("No CSV file named " + classID + " at " + os.path.dirname(__file__) + "\n" + path + "\n")
        else:
            with open( f"{classID}.csv", newline="" ) as f:
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

                print("\nWriting to pdf...\n")
                pdf.output( f"{classID}_students.pdf", "F" )
                print("Complete!\nCreated new PDF file at " + os.path.join(os.path.dirname(__file__), classID + ".csv\n"))
