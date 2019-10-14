from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter,process_pdf
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from docx import Document
document = Document()
import warnings
warnings.filterwarnings("ignore")
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
import codecs
from urllib.request import urlopen
# import pandas as pd

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content
def save_to_file(file_name, contents):
    # fh = open(file_name, 'w',",encoding='utf-8'")
    fh = codecs.open(file_name, 'a', 'utf-8')
    # with open(r'test2.doc', 'a', encoding='utf-8') as f:
    fh.write(contents)
    fh.close()

# save_to_file('mobiles.txt', 'your contents str')


def main():
    # pdfFile = urlopen("D:/file/pdf/111.pdf")
    pdfFile = open('D:/file/pdf/111.pdf', 'rb')
    # pdfFile = codecs.open('D:/file/pdf/111.pdf', 'r', 'utf-8')
    outputString = readPDF(pdfFile)
    #c.word
    save_to_file('D:/file/pdf/tst.doc',outputString)
if __name__ == '__main__':
    main()