#!/usr/bin/env python

import PyPDF2
import itertools
from iter import extractTextList

from PyPDF2.pdf import PageObject, u_, ContentStream, b_, TextStringObject
PageObject.extractTextList = extractTextList

def between(text_elements, drop_while, take_while):
    return list(itertools.takewhile(take_while, itertools.dropwhile(drop_while, text_elements)))[1:]

def verification(text_elements):
    label_v1 = u'C\xf3digo Verificaci\xf3n:'
    if label_v1 in text_elements:
        place = text_elements.index(label_v1)
        label_v2 = text_elements[place + 2]
        return between(text_elements, lambda x: x != label_v1, lambda x: label_v2 not in x)[0]
    else:
        return "N/A"

def district(text_elements):
    label_d1 = u'Circunscripci\xf3n   :'
    label_d2 = u'Nro. inscripci\xf3n  :'
    if label_d1 and label_d2 in text_elements:
        return between(text_elements, lambda x: x != label_d1, lambda x: label_d2 not in x)[0]
    else:
        return "N/A"

def inscrip_no(text_elements):
    label_n1 = u'Nro. inscripci\xf3n  :'
    if label_n1 in text_elements:
        label_n2 = u'Registro :'
        return between(text_elements, lambda x: x != label_n1, lambda x: label_n2 not in x)[0]
    else:
        return "N/A"

def name(text_elements):
    label_t1 = u'Nombre inscrito   :'
    label_t2 = u'R.U.N.            :'
    if label_t1 and label_t2 in text_elements:
        return between(text_elements, lambda x: x != label_t1, lambda x: label_t2 not in x)[0]
    else:
        return "N/A"

def run(text_elements):
    label_r1 = u'R.U.N.            :'
    label_r2 = u'Fecha nacimiento  :'
    if label_r1 and label_r2 in text_elements:
        return between(text_elements, lambda x: x != label_r1, lambda x: label_r2 not in x)[0]
    else:
        return "N/A"

def date(text_elements):
    label_d1 = u'Fecha nacimiento  :'
    label_d2 = u'Sexo              :'
    if label_d1 and label_d2 in text_elements:
        return between(text_elements, lambda x: x != label_d1, lambda x: label_d2 not in x)[0]
    else:
        return "N/A"

def sex(text_elements):
    label_s1 = u'Sexo              :'
    if label_s1 in text_elements:
        place = text_elements.index(label_s1)
        label_s2 = text_elements[place + 2]
        return between(text_elements, lambda x: x != label_s1, lambda x: label_s2 not in x)[0]
    else:
        return "N/A"

def father_name(text_elements):
    label_f1 = u'Nombre del padre  :'
    if label_f1 in text_elements:
        place = text_elements.index(label_f1)
        label_f2 = text_elements[place + 2]
        return between(text_elements, lambda x: x != label_f1, lambda x: label_f2 not in x)[0]
    else:
        return "N/A"

def father_run(text_elements):
    label_f1 = u'R.U.N. del padre  :'
    if label_f1 in text_elements:
        place = text_elements.index(label_f1)
        label_f2 = text_elements[place + 2]
        return between(text_elements, lambda x: x != label_f1, lambda x: label_f2 not in x)[0]
    else:
        return "N/A"

def mother_name(text_elements):
    label_m1 = u'Nombre de la madre:'
    if label_m1 in text_elements:
        place = text_elements.index(label_m1)
        label_m2 = text_elements[place + 2]
        return between(text_elements, lambda x: x != label_m1, lambda x: label_m2 not in x)[0]
    else:
        return "N/A"

def mother_run(text_elements):
    label_m1 = u'R.U.N. de la madre:'
    if label_m1 in text_elements:
        place = text_elements.index(label_m1)
        label_m2 = text_elements[place + 2]
        return between(text_elements, lambda x: x != label_m1, lambda x: label_m2 not in x)[0]
    else:
        return "N/A"

def combined(text_elements):
    return [name(text_elements), run(text_elements), date(text_elements), sex(text_elements), father_name(text_elements), father_run(text_elements), mother_name(text_elements), mother_run(text_elements)]
