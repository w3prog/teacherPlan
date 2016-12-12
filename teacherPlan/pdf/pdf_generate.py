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
from reportlab.platypus.flowables import PageBreak, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.graphics.shapes import *

pdfmetrics.registerFont(TTFont('TimesNewRoman', 'TimesNewRoman.ttf'))
pdfmetrics.registerFont(TTFont('TimesBold', 'TimesBold.ttf'))
pdfmetrics.registerFont(TTFont('TimesItalic', 'TimesItalic.ttf'))
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TNR_H_Center', fontName='TimesNewRoman', fontSize=12, alignment=TA_CENTER, leftIndent=1.5*inch))
styles.add(ParagraphStyle(name='TNR_H_Left', fontName='TimesNewRoman', leading = 30, fontSize=12, alignment=TA_LEFT, leftIndent=1.5*inch))
styles.add(ParagraphStyle(name='TNR_Bold_H_Center', fontName='TimesBold', fontSize=12, alignment=TA_CENTER, leftIndent=1.5*inch))
styles.add(ParagraphStyle(name='TNR_Big_Bold_H_Center16',fontName='TimesBold',leading = 20, fontSize=16, alignment=TA_CENTER))
styles.add(ParagraphStyle(name='TNR_Big_Bold_H_Center14',fontName='TimesBold',leading = 20, fontSize=14, alignment=TA_CENTER))
styles.add(ParagraphStyle(name='TNR_Big_Bold_H_Center12',fontName='TimesBold',leading = 20, fontSize=12, alignment=TA_CENTER))
styles.add(ParagraphStyle(name='TNR_mini',fontName='TimesItalic',leading = 12, fontSize=9, alignment=TA_CENTER))
normal_table_style = TableStyle([
        ('FONT', (0, 0), (-1, -1), 'TimesNewRoman', 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.25, colors.black),

    ])

normal_table_style1 = TableStyle([
        ('FONT', (0, 0), (-1, -1), 'TimesNewRoman', 12),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')

    ])


story = []
story.append(Paragraph("МИНОБРНАУКИ РОССИИ",styles['TNR_H_Center']))
story.append(Paragraph("""<br/><br/>САНКТ-ПЕТЕРБУРГСКИЙ
<br/>ГОСУДАРСТВЕННЫЙ ЭЛЕКТРОТЕХНИЧЕСКИЙ УНИВЕРСИТЕТ
<br/>«ЛЭТИ» им.В.И.Ульянова (Ленина)""",styles['TNR_Bold_H_Center']))

story.append(Paragraph("<br/><br/><br/><br/>ИНДИВИДУАЛЬНЫЙ  ПЛАН <br/>ПРЕПОДАВАТЕЛЯ<br/><br/>",styles['TNR_Big_Bold_H_Center16']))
story.append(Spacer(0, 0.5 *inch))
personal_data = [
    ['Факультет', '---'],
    ['Кафедра', '---'],
    ['Должность', '---']
  ]
p_d = Table(personal_data)
p_d.setStyle(normal_table_style1)
story.append(p_d)
story.append(Paragraph("<br/><br/><br/>Фамилия", styles['TNR_mini']))
story.append(Paragraph("<br/><br/><br/>&nbsp &nbsp &nbsp &nbsp &nbsp  &nbspИмя  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Отчество", styles['TNR_mini']))
story.append(Paragraph("<br/><br/><br/>Год рождения", styles['TNR_mini']))
story.append(Paragraph("<br/><br/><br/>Дата текущего  избрания или зачисления на преподавательскую должность", styles['TNR_mini']))
story.append(Paragraph("<br/><br/><br/>Ученая степень и год присуждения", styles['TNR_mini']))
story.append(Paragraph("<br/><br/><br/>Ученое звание и год присвоения", styles['TNR_mini']))
story.append(Paragraph("<br/><br/><br/>Дата переизбрания (окончания трудового договора)", styles['TNR_mini']))
story.append(PageBreak())

story.append(Paragraph("2. Методическая работа", styles['TNR_Big_Bold_H_Center14']))
story.append(Paragraph("2.1. Подготовка учебников, учебных пособий и методических указаний,/"
                       " включая электронные издания", styles['TNR_Big_Bold_H_Center12']))
story.append(Spacer(0, 0.3 *inch))
data = [
           ['Наименование', 'Вид издания','Объем','Вид грифа','Срок сдачи рукописи','Отметка о выполнении'],
          ['---','---','---','---','---','---']

      ]

all_table=Table(data)
all_table.setStyle(normal_table_style)
story.append(all_table)
story.append(Spacer(0, 0.3 *inch))



story.append(Paragraph("2.2. Постановка и модернизация дисциплин", styles['TNR_Big_Bold_H_Center12']))
story.append(Spacer(0, 0.3 *inch))

data = [
     ['Наименование дисциплины','Вид занятий','Характер изменения', 'Отметка о выполнении'],
     ['---','---','---','---']

    ]

all_table=Table(data)
all_table.setStyle(normal_table_style)
story.append(all_table)
story.append(Spacer(0, 0.3 *inch))

story.append(Paragraph("3. Научная работа", styles['TNR_Big_Bold_H_Center14']))
story.append(Paragraph("Научно-исследовательская  работа в университете и вне университета", styles['TNR_Big_Bold_H_Center12']))
story.append(Spacer(0, 0.3 *inch))

data = [
        ['Наименование работы','Период','В качестве кого участвовал','Организация или предприятие'],
        ['---','---','---','---',]

    ]

all_table=Table(data)
all_table.setStyle(normal_table_style)
story.append(all_table)
story.append(Spacer(0, 0.3 *inch))

story.append(Paragraph("4. Участие в конференциях и выставках", styles['TNR_Big_Bold_H_Center14']))
story.append(Spacer(0, 0.3 *inch))
data = [
        ['Наименование конференции или выставки','Дата', 'Уровень конференции или выставки','Наименование доклада или экспоната'],
        ['---','---','---','---',]

    ]

all_table=Table(data)
all_table.setStyle(normal_table_style)
story.append(all_table)
story.append(Spacer(0, 0.3 *inch))

story.append(Paragraph("5. Список публикаций", styles['TNR_Big_Bold_H_Center14']))

story.append(Spacer(0, 0.3 *inch))
data = [
        ['Наименование работ', 'Вид публикации','Объем в п.л.','Наименование издательства, журнала или сборника'],
        ['---','---','---','---','---',]

    ]

all_table=Table(data)
all_table.setStyle(normal_table_style)
story.append(all_table)
story.append(Spacer(0, 0.3 *inch))
story.append(PageBreak())


story.append(Paragraph("6. Повышение  квалификации", styles['TNR_Big_Bold_H_Center14']))
story.append(Paragraph("Научно-исследовательская  работа в университете и вне университета", styles['TNR_Big_Bold_H_Center12']))
story.append(Spacer(0, 0.3 *inch))
data = [
        ['Период','Форма повышения квалификации', 'Документ'],
        ['---','---','---',]

    ]

all_table=Table(data)
all_table.setStyle(normal_table_style)
story.append(all_table)
story.append(Spacer(0, 0.3 *inch))

story.append(Paragraph("7. Другие виды работ, выполняемых в интересах университета, факультета и кафедры", styles['TNR_Big_Bold_H_Center14']))
story.append(Spacer(0, 0.3 *inch))
data = [
        ['Период','Вид работы'],
        ['---','---',]

    ]

all_table=Table(data)
all_table.setStyle(normal_table_style)
story.append(all_table)
story.append(Spacer(0, 0.3 *inch))

story.append(Paragraph("8. Замечания по работе преподавателя", styles['TNR_Big_Bold_H_Center14']))
story.append(Spacer(0, 0.3 *inch))
data = [
        ['Дата','Характер замечания','Должность лица, вносящего замечания','Подпись лица, вносящего замечания', 'Подпись преподавателя'],
        ['---','---','---','---','---']

    ]

all_table=Table(data)
all_table.setStyle(normal_table_style)
story.append(all_table)
story.append(Spacer(0, 0.3 *inch))
story.append(PageBreak())

story.append(Paragraph("9. Заключение кафедры", styles['TNR_Big_Bold_H_Center14']))

# story.append(Line(0, 5, 100, 50))
#




doc = SimpleDocTemplate('mydoc.pdf',pagesize = A4)
doc.build(story)