# -*- coding: utf-8 -*-
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate

pdfmetrics.registerFont(TTFont('TimesNewRoman', 'TimesNewRoman.ttf'))
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='h_first', fontName='TimesNewRoman', fontSize=12, alignment=TA_CENTER, leftIndent=2.32*inch))

styleN = styles['Normal']
styleH = styles['Heading1']
style_1 = styles['h_first']

story = []
story.append(Paragraph("МИНОБРНАУКИ РОССИИ",style_1))
story.append(Paragraph("This is a paragraph in <i>Normal</i> style.",
styleN))
doc = SimpleDocTemplate('mydoc.pdf',pagesize = letter)
doc.build(story)