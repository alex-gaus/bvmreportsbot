from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

def add_footer(input_file,output_file):
    # Get pages
    reader = PdfReader("%s.pdf"%(input_file))
    pages = [pagexobj(p) for p in reader.pages]


    # Compose new pdf
    canvas = Canvas("%s.pdf"%(output_file))
    pdfmetrics.registerFont(TTFont('SourceSansPro', 'SourceSansPro-Regular.ttf'))

    for page_num, page in enumerate(pages, start=2):

        # Add page
        canvas.setPageSize((page.BBox[2], page.BBox[3]))
        canvas.doForm(makerl(canvas, page))

        # Draw footer
        footer_text = "www.borderviolence.eu"
        x = 80
        canvas.saveState()
        canvas.setStrokeColorRGB(0.19, 0.19, 0.19)
        canvas.setLineWidth(0.3)
        canvas.line(75, 78, page.BBox[2] - 66, 78)
        canvas.setFont('SourceSansPro', 10)
        canvas.setFillColor(HexColor(0x333333))
        canvas.drawString(page.BBox[2]-x, 85, str(page_num))
        canvas.drawString(page.BBox[2]-x-436, 85, footer_text)
        canvas.restoreState()

        canvas.showPage()

    canvas.save()
    return 1