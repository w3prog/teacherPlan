# -*- coding: utf-8 -*-
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.platypus import TableStyle
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4


pdfmetrics.registerFont(TTFont('TimesNewRoman', 'TimesNewRoman.ttf'))
pdfmetrics.registerFont(TTFont('TimesBold', 'TimesBold.ttf'))
pdfmetrics.registerFont(TTFont('TimesItalic', 'TimesItalic.ttf'))
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TNR_H_Center', fontName='TimesNewRoman', fontSize=12, alignment=TA_CENTER, leftIndent=1.5*inch))
styles.add(ParagraphStyle(name='TNR_H_Left', fontName='TimesNewRoman', leading = 30, fontSize=12, alignment=TA_LEFT, leftIndent=1.5*inch))
styles.add(ParagraphStyle(name='TNR_Bold_H_Center', fontName='TimesBold', fontSize=12, alignment=TA_CENTER, leftIndent=1.5*inch))
styles.add(ParagraphStyle(name='TNR_Big_Bold_H_Center',fontName='TimesBold',leading = 20, fontSize=16, alignment=TA_CENTER))
styles.add(ParagraphStyle(name='TNR_mini',fontName='TimesItalic',leading = 12, fontSize=9, alignment=TA_CENTER))

story = []
story.append(Paragraph("МИНОБРНАУКИ РОССИИ",styles['TNR_H_Center']))
story.append(Paragraph("""<br/><br/>САНКТ-ПЕТЕРБУРГСКИЙ
<br/>ГОСУДАРСТВЕННЫЙ ЭЛЕКТРОТЕХНИЧЕСКИЙ УНИВЕРСИТЕТ
<br/>«ЛЭТИ» им.В.И.Ульянова (Ленина)""",styles['TNR_Bold_H_Center']))
story.append(Paragraph("<br/><br/><br/><br/>ИНДИВИДУАЛЬНЫЙ  ПЛАН <br/>ПРЕПОДАВАТЕЛЯ",styles['TNR_Big_Bold_H_Center']))

story.append(Paragraph("<br/>Факультет", styles['TNR_H_Left']))
story.append(Paragraph("Кафедра", styles['TNR_H_Left']))
story.append(Paragraph("Должность", styles['TNR_H_Left']))
story.append(Paragraph("<br/><br/><br/>Фамилия", styles['TNR_mini']))
story.append(Paragraph("<br/><br/><br/>&nbsp &nbsp &nbsp &nbsp &nbsp  &nbspИмя  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Отчество", styles['TNR_mini']))
story.append(Paragraph("<br/><br/><br/>Год рождения", styles['TNR_mini']))
story.append(Paragraph("<br/><br/><br/>Дата текущего  избрания или зачисления на преподавательскую должность", styles['TNR_mini']))
story.append(Paragraph("<br/><br/><br/>Ученая степень и год присуждения", styles['TNR_mini']))
story.append(Paragraph("<br/><br/><br/>Ученое звание и год присвоения", styles['TNR_mini']))
story.append(Paragraph("<br/><br/><br/>Дата переизбрания (окончания трудового договора)", styles['TNR_mini']))





doc = SimpleDocTemplate('mydoc.pdf',pagesize = A4)
doc.build(story)