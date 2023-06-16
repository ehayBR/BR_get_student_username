## this requires fpdf library to be installed in Python!

import csv
from fpdf import FPDF

classID = input( "Enter class ID: " )

with open( f"{classID}.csv", newline="" ) as f:
    reader = csv.reader(f)

    pdf = FPDF()
    pdf.add_page()
    page_width = pdf.w - 2 * pdf.l_margin

    pdf.set_font( "Times", "B", 14.0 )
    pdf.cell( page_width, 0.0, "Students", align="L" )
    pdf.ln( 10 )

    pdf.set_font( "Times", "", 12 )
    
    col_width = page_width/4

    pdf.ln( 1 )

    th = pdf.font_size

    for row in reader:
        pdf.cell( col_width, th, str(row[0]), border=1 )
        pdf.cell( col_width, th, row[1], border=1 )
        pdf.cell( col_width, th, row[2], border=1 )
        pdf.ln( th )

pdf.output( f"{classID}_students.pdf", "F" )