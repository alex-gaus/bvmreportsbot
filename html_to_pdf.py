import requests
import os
import pdfkit
from bs4 import BeautifulSoup
from bs4.element import Tag
import logging
logging.basicConfig(level=logging.INFO)

def html_to_pdf (link, name, picture_value):
    logging.info("html_to_pdf started")
    exists = os.path.isfile('pdfs/%s'%(name))
    if exists:
        logging.info("pdf exists already")
        return False
    else:
        r = requests.get(link).text
        soup = BeautifulSoup(r,"html.parser")

        soup.find('footer',class_='site-footer').decompose()
        # soup.find("div", id="icon_wrapper").decompose()
        soup.find("div", id="cookie-banner").decompose()
        soup.find("header", class_="site-header").decompose()
        
        if picture_value == False:
            def remove_img():
                soup.find("img").decompose()
                remove_img()
            try:
                remove_img()
            except AttributeError:
                print(AttributeError)

        if picture_value == True:
            try:
                soup.find("img", class_="attachment-full size-full").decompose()
            except AttributeError:
                print(AttributeError)

        
        options = {
        'page-size': 'A4',
        'margin-top': '0.5in',
        'margin-right': '0.75in',
        'margin-bottom': '1.5in',
        'margin-left': '0.75in',
    }
        with open("temp.html","w") as f:
            f.write(soup.prettify())
            try:
                pdfkit.from_file("temp.html","pdfs/%s"%(name),options)
                logging.info("Report saved in pdfs/%s"%(name))
            except OSError:
                logging.error(OSError)
        return r;