from fpdf import FPDF
import json
from html_to_pdf import html_to_pdf
import os
from PyPDF2 import PdfFileMerger
from merge_pdf import merge_pdf
from add_footer import add_footer
from operator import itemgetter  

with open("db3.json", encoding='utf-8') as f:
    json_data = f.read()
    json_data = json.loads(json_data)
    json_data_s=sorted(json_data,key=itemgetter("date"))
# Set picture value False = No pictures included:
picture_value = True
for report in json_data:
    date= int(report["date"].replace("-","")[:8])
    if date > 20190228 and date < 20190401:
        link=report["report_link"]
        name=report["date"]
        print("hallo")
        html_to_pdf(link,"%s.pdf"%(name),picture_value)

merge_pdf("pdfs","summary")

add_footer("summary","summary_2019-03_pics")

 
# pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
# pdf.add_page()
# pdf.add_font('Roboto', '', 'Roboto-Regular.ttf', uni=True)
# pdf.add_font('RobotoB', '', 'Roboto-Black.ttf', uni=True)
  
# with open("db.json", encoding='utf-8') as f:
#     json_data = f.read()
#     json_data = json.loads(json_data)

# #title    
# pdf.set_font('RobotoB', size=20)
# pdf.cell(200, 5, txt="All Reports", ln=1, align="C")

# for report in json_data:
#     string=report["report_title"]
#     string= string.encode('utf-8')
#     string=string.decode("utf-8","ignore")
#     pdf.set_font_size(12)
#     pdf.cell(200, 10, txt=string, ln=1, align="L")

# pdf.output("simple_demo.pdf")