# -*- coding: utf-8 -*-
from io import BytesIO

from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import (
    black,
    purple,
    white,
    yellow
)

from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfgen import *
#from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts
from reportlab.platypus import TableStyle
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet

PAGE_SIZE = A4
#MyFontObject = ttfonts.TTFont('Arial', ‘arial.ttf’)
#pdfmetrics.registerFont(MyFontObject)

def conclusion_to_pdf(response,id=1):

    pdfmetrics.registerFont(TTFont('TimesNewRoman', 'TimesNewRoman.ttf'))
    pdfmetrics.registerFont(TTFont('TimesBold', 'TimesBold.ttf'))
    pdfmetrics.registerFont(TTFont('TimesItalic', 'TimesItalic.ttf'))

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='h_first', fontName='TimesNewRoman', fontSize=12, alignment=TA_CENTER, leftIndent=2.32*inch))
    styles.add(ParagraphStyle(name='h_first2', fontName='TimesBold', fontSize=12, alignment=TA_CENTER, leftIndent=2.32*inch))
    styles.add(ParagraphStyle(name='h_second',fontName='TimesBold', fontSize=16, alignment=TA_CENTER))
    style_1 = styles['h_first']
    style_12 = styles['h_first2']
    normal_table_style = TableStyle([
        ('FONT', (0, 0), (-1, -1), 'TimesNewRoman', 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BACKGROUND', (0, 0), (15, -2), colors.lightgrey),
    ])
    story = []
    story.append(Paragraph("МИНОБРНАУКИ РОССИИ", style_1))
    story.append(Paragraph("""САНКТ-ПЕТЕРБУРГСКИЙ
                           "ГОСУДАРСТВЕННЫЙ ЭЛЕКТРОТЕХНИЧЕСКИЙ УНИВЕРСИТЕТ/ "
                           "«ЛЭТИ» им.В.И.Ульянова (Ленина)""", style_12))

    story.append(Paragraph("/"
                           "/"
                           "/"
                           "ИНДИВИДУАЛЬНЫЙ  ПЛАН ПРЕПОДАВАТЕЛЯ/"
                           "", style_1))

    doc = SimpleDocTemplate(response, pagesize=A4)

    doc.build(story)
    return response

if __name__ == '__main__':
    conclusion_to_pdf('mydoc.pdf')
