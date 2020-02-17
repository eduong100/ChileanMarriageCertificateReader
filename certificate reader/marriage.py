#!/usr/bin/env python

import PyPDF2
import itertools
from iter import extractTextList

from PyPDF2.pdf import PageObject, u_, ContentStream, b_, TextStringObject
PageObject.extractTextList = extractTextList

from birth import between, verification, district, inscrip_no

def husband_name(text_elements):
    label_m1 = u'Nombre del Marido :'
    if label_m1 in text_elements:
        label_m2 = u'R.U.N.            :'
        a = between(text_elements, lambda x: x != label_m1, lambda x: label_m2 not in x)
        name_h = ' '
        for x in a:
            name_h = name_h + x + ' '
        return name_h
    else:
        return "N/A"

def husband_run(text_elements):
    label_m1 = u'R.U.N.            :'
    if label_m1 in text_elements:
        place = text_elements.index(label_m1)
        label_m2 = text_elements[place + 2]
        return between(text_elements, lambda x: x != label_m1, lambda x: label_m2 not in x)[0]
    else:
        return "N/A"

def husband_birth(text_elements):
    label_m1 = u'Fecha nacimiento  :'
    if label_m1 in text_elements:
        place = text_elements.index(label_m1)
        label_m2 = text_elements[place + 2]
        return between(text_elements, lambda x: x != label_m1, lambda x: label_m2 not in x)[0]
    else:
        return "N/A"

def wife_name(text_elements):
    label_m1 = u'Nombre de la Mujer:'
    if label_m1 in text_elements:
        label_m2 = u'R.U.N.            :'
        a = between(text_elements, lambda x: x != label_m1, lambda x: label_m2 not in x)
        name_w = ' '
        for x in a:
            name_w = name_w + x + ' '
        return name_w
    else:
        return "N/A"

list2 = []
def wife_run(text_elements):
    global list2
    for i, j in enumerate(text_elements):
        if j == u'R.U.N.            :':
            list2.append(i)
    return text_elements[list2[1] + 1]


list1 = []
def wife_birth(text_elements):
    global list1
    for i, j in enumerate(text_elements):
        if j == u'Fecha nacimiento  :':
            list1.append(i)
    return text_elements[list1[1] + 1]

def wed_date(text_elements):
    label_m1 = u'FECHA CELEBRACI\xd3N :'
    if label_m1 in text_elements:
        place = text_elements.index(label_m1)
        label_m2 = text_elements[place + 2]
        return between(text_elements, lambda x: x != label_m1, lambda x: label_m2 not in x)[0]
    else:
        return "N/A"

def combined_m(text_elements):
    return [husband_name(text_elements), husband_run(text_elements), husband_birth(text_elements), wife_name(text_elements), wife_run(text_elements), wife_birth(text_elements), wed_date(text_elements)]




#change placement of if statement
