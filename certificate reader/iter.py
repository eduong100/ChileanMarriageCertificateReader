#!/usr/bin/env python

import PyPDF2
import itertools

def extractTextList(self):
    text_list = []
    content = self["/Contents"].getObject()
    if not isinstance(content, ContentStream):
        content = ContentStream(content, self.pdf)

    for operands, operator in content.operations:
        if operator == b_("Tj"):
            _text = operands[0]
            if isinstance(_text, TextStringObject) and len(_text.strip()):
                text_list.append(_text.strip())
        elif operator == b_("T*"):
            pass
        elif operator == b_("'"):
            pass
            _text = operands[0]
            if isinstance(_text, TextStringObject) and len(operands[0]):
                text_list.append(operands[0])
        elif operator == b_('"'):
            _text = operands[2]
            if isinstance(_text, TextStringObject) and len(_text):
                text_list.append(_text)
        elif operator == b_("TJ"):
            for i in operands[0]:
                if isinstance(i, TextStringObject) and len(i):
                    text_list.append(i)
    return text_list

from PyPDF2.pdf import PageObject, u_, ContentStream, b_, TextStringObject
PageObject.extractTextList = extractTextList

def pdf_to_list(filename):
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    page0 = pdfReader.getPage(0)
    text_elements = page0.extractTextList()
    return text_elements
