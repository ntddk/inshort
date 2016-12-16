#!/usr/bin/env python
#coding: utf-8
import sys
import re
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter
from summpy.lexrank import summarize

def pdf_to_txt(path):
    rsrcmgr = PDFResourceManager(caching=True)
    laparams = LAParams()
    laparams.detect_vertical=True

    fp = open(path, 'rb')
    outfp = open(path + '.txt', 'w')
    device = TextConverter(rsrcmgr, outfp, codec='utf-8', laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)

    fp.close()
    outfp.close()
    device.close()

def txt_to_summary(path):
    fp = open(path, 'rb')
    txt = fp.read().decode('utf-8')
    sentences,debug_info = summarize(txt, sent_limit=5, continuous=True, debug=True)
    for sent in sentences:
        print sent.strip().encode('utf-8')

def main(argv):
    if len(argv) != 2:
        sys.exit('Input PDF file path.')

    pdf_to_txt(argv[1])
    txt_to_summary(argv[1] + '.txt')

if __name__ == "__main__":
    main(sys.argv)

