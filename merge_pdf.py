import os, PyPDF2
import logging
logging.basicConfig(level=logging.INFO)
def merge_pdf(mergeList,userpdflocation,userfilename):
        logging.info("merge_pdf started")
        #Sets the scripts working directory to the location of the PDFs
        logging.info(os.getcwd())
        os.chdir(userpdflocation)
        logging.info(os.getcwd())
        # pdf2merge = []
        # filelist_unsorted = os.listdir(".") 
        # filelist = sorted(filelist_unsorted)
        # for filename in filelist:
        #         if filename.endswith(".pdf"):
        #                 pdf2merge.append(filename)

        pdfWriter = PyPDF2.PdfFileWriter()

        for filename in mergeList:
                logging.info(os.getcwd())
                try:
                        pdfFileObj = open("%s"%(filename),"rb")
                        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                #Opening each page of the PDF
                        for pageNum in range(pdfReader.numPages):
                                pageObj = pdfReader.getPage(pageNum)
                                pdfWriter.addPage(pageObj)
                except:
                        logging.info("The pdf %s was not found."%(filename))
        os.chdir("..")
        #save PDF to file, wb for write binary
        pdfOutput = open("pdfs/"+userfilename+".pdf", "wb")
        #Outputting the PDF
        pdfWriter.write(pdfOutput)
        #Closing the PDF writer
        pdfOutput.close()
        logging.info("merged pdf saved as pdfs/%s.pdf"%(userfilename))
        return 1
