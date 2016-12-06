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

def conclusion_to_pdf():
#def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="ureport.pdf"'

    pdfmetrics.registerFont(TTFont('TimesNewRoman', 'TimesNewRoman.ttf'))
    pdfmetrics.registerFont(TTFont('TimesBold', 'TimesBold.ttf'))
    pdfmetrics.registerFont(TTFont('TimesItalic', 'TimesItalic.ttf'))

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    # p = canvas.Canvas(buffer)
    # p.drawString(40,49,"12314")
    doc = SimpleDocTemplate(buffer,pagesize = A4)
#     p.drawString(1,1,"34")

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='h_first', fontName='TimesNewRoman', fontSize=12, alignment=TA_CENTER, leftIndent=2.32*inch))
    styles.add(ParagraphStyle(name='h_first2', fontName='TimesBold', fontSize=12, alignment=TA_CENTER, leftIndent=2.32*inch))
    styles.add(ParagraphStyle(name='h_second',fontName='TimesBold', fontSize=16, alignment=TA_CENTER))
#
#     styles.add(ParagraphStyle(name='mini_data',fontName='TimesItalic', fontSize=9, alignment=TA_CENTER))
    style_1 = styles['h_first']
    style_12 = styles['h_first2']
#     #style_2 = styles['h_second']
#     #style_3 = styles['h_third']
#     style_4 = styles['mini_data']
#
#     # canvas.line(480,747,580,747)
#     # canvas.line(480,747,580,747)
#     # canvas.line(480,747,580,747)
#     # canvas.line(480,747,580,747)
#     # canvas.line(480,747,580,747)
#     # canvas.line(480,747,580,747)
#     I = Image('im.png')
#     I.drawHeight = 1.25*inch*I.drawHeight / I.drawWidth
#     I.drawWidth = 1.25*inch
#
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


#    personal_data = [
#     ['Факультет', '---'],
#     ['Кафедра', '---'],
#     ['Должность', '---'],
#
#     #  ['Дата текущего избрания', '---'],
#     # ['Ученая степень и год присуждения', '---'],
#     # ['Ученое звание и год присвоения', '---'],
#     # ['Дата окончания трудового договора', '---'],
# ]
# p_d = Table(personal_data)
# p_d.setStyle(normal_table_style)

#     story.append(Paragraph("Фамилия", style_4))
#     story.append(Paragraph("Имя                                                                                        Отчество", style_4))
#     story.append(Paragraph("Год рождения", style_4))
#     story.append(Paragraph("Дата текущего  избрания или зачисления на преподавательскую должность", style_4))
#     story.append(Paragraph("Ученая степень и год присуждения", style_4))
#     story.append(Paragraph("Ученое звание и год присвоения", style_4))
#     story.append(Paragraph("Дата переизбрания (окончания трудового договора)", style_4))
#
#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     #p.drawString(100, 100, "МИНОБРНАУКИ РОССИИ")
#     #p.drawString(100, 100, "САНКТ-ПЕТЕРБУРГСКИЙ ГОСУДАРСТВЕННЫЙ ЭЛЕКТРОТЕХНИЧЕСКИЙ УНИВЕРСИТЕТ «ЛЭТИ» им.В.И.Ульянова (Ленина)")
#
#
#     p.showPage()
#     p.save()
#
# #!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#     styles.add(ParagraphStyle(name='h_third',fontName='TimesNewRoman', fontSize=14, alignment=TA_CENTER,))
#     #styles.add(ParagraphStyle(name='h_first2', fontName='TimesBold', fontSize=12, alignment=TA_CENTER, ))
#
#     style_3 = styles['h_third']
#     style_12 = styles['h_first2']
#
#     normal_table_style = TableStyle([
#         ('FONT', (0, 0), (-1, -1), 'TimesNewRoman', 9),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
#         ('BACKGROUND', (0, 0), (15, -2), colors.lightgrey),
#     ])
#
#     story.append(Paragraph("2. Методическая работа", style_3))
#     story.append(Paragraph("2.1. Подготовка учебников, учебных пособий и методических указаний,/"
#                            " включая электронные издания", style_12))
#     methodical_work = [
#             ['Наименование', 'Вид издания','Объем','Вид грифа','Срок сдачи рукописи','Отметка о выполнении'],
#             ['---','---','---','---','---','---']
#
#         ]
#
#     m_w=Table(methodical_work)
#     m_w.setStyle(normal_table_style)
#
#
#
#
#     #story.append(Paragraph("2. Методическая работа", style_3))
#     story.append(Paragraph("2.2. Постановка и модернизация дисциплин", style_12))
#
#     modern_dis = [
#         ['Наименование дисциплины','Вид занятий','Характер изменения', 'Отметка о выполнении'],
#         ['---','---','---','---']
#
#     ]
#
#     m_dis=Table(modern_dis)
#     m_dis.setStyle(normal_table_style)
#
#
#     story.append(Paragraph("3. Научная работа", style_3))
#     story.append(Paragraph("Научно-исследовательская  работа в университете и вне университета", style_12))
#
#
#     study_w = [
#         ['Наименование работы','Период','В качестве кого участвовал','Организация или предприятие'],
#         ['---','---','---','---',]
#
#     ]
#
#     st_w=Table(study_w)
#     st_w.setStyle(normal_table_style)
#
#
#     story.append(Paragraph("4. Участие в конференциях и выставках", style_3))
#     #story.append(Paragraph("2.1. Подготовка учебников, учебных пособий и методических указаний,/"
#              #              " включая электронные издания", style_12))
#
#
#     st_conf = [
#         ['Наименование конференции или выставки','Дата', 'Уровень конференции или выставки','Наименование доклада или экспоната'],
#         ['---','---','---','---',]
#
#     ]
#
#     st_c=Table(st_conf)
#     st_c.setStyle(normal_table_style)
#
#
#     story.append(Paragraph("5. Список публикаций", style_3))
#     # story.append(Paragraph("2.1. Подготовка учебников, учебных пособий и методических указаний,/"
#     #                        " включая электронные издания", style_12))
#
#
#     publication_w = [
#         ['Наименование работ', 'Вид публикации','Объем в п.л.','Наименование издательства, журнала или сборника'],
#         ['---','---','---','---','---',]
#
#     ]
#
#     pub_w=Table(publication_w)
#     pub_w.setStyle(normal_table_style)
#
#     p.showPage()
#     p.save()
#
# #!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#     #styles.add(ParagraphStyle(name='h_third', fontName='TimesNewRoman', fontSize=14, alignment=TA_CENTER, ))
#     #styles.add(ParagraphStyle(name='h_first2', fontName='TimesBold', fontSize=12, alignment=TA_CENTER, ))
#
#     style_3 = styles['h_third']
#     style_12 = styles['h_first2']
#
#     normal_table_style = TableStyle([
#         ('FONT', (0, 0), (-1, -1), 'TimesNewRoman', 9),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
#         ('BACKGROUND', (0, 0), (15, -2), colors.lightgrey),
#     ])
#
#     story.append(Paragraph("6. Повышение  квалификации", style_3))
#     #story.append(Paragraph("Научно-исследовательская  работа в университете и вне университета", style_12))
#     qualification_w = [
#         ['Период','Форма повышения квалификации', 'Документ'],
#         ['---','---','---',]
#
#     ]
#
#     q_w=Table(qualification_w)
#     q_w.setStyle(normal_table_style)
#
#
#     story.append(Paragraph("7. Другие виды работ, выполняемых в интересах университета, факультета и кафедры", style_3))
#     #story.append(Paragraph("Научно-исследовательская  работа в университете и вне университета", style_12))
#     another_w = [
#         ['Период','Вид работы'],
#         ['---','---','---',]
#
#     ]
#
#     an_w=Table(another_w)
#     an_w.setStyle(normal_table_style)
#
#
#     story.append(Paragraph("8. Замечания по работе преподавателя", style_3))
#     #story.append(Paragraph("Научно-исследовательская  работа в университете и вне университета", style_12))
#
#     remark_w = [
#         ['Дата','Характер замечания','Должность лица, вносящего замечания','Подпись лица, вносящего замечания', 'Подпись преподавателя','---'],
#         ['---','---','---','---','---','---',]
#
#     ]
#
#     rem_w=Table(remark_w)
#     rem_w.setStyle(normal_table_style)
#
#
#     story.append(Paragraph("8. Замечания по работе преподавателя", style_3))
#
#
#
#
#
#
#
#
#
#
#     # Close the PDF object cleanly.
#     p.showPage()
    doc.build(story)
    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    with open('text.pdf', 'w') as file:
        file.write(pdf)
    buffer.close()



    # response.write(pdf)
    # return response

conclusion_to_pdf()
