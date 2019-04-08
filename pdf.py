import json
from html_to_pdf import html_to_pdf
import os
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

