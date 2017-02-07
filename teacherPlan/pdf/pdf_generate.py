# -*- coding: utf-8 -*-
import os

from django.http import Http404
from django.utils import dateformat
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT,TA_JUSTIFY,TA_RIGHT
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import TableStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, Image
from reportlab.platypus.flowables import PageBreak, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

from moevmCommon.models import TeacherPlan

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

def conclusion_to_pdf(responce=None, id=1, has_cover_page=False,with_finish_page=False):
  pdfmetrics.registerFont(TTFont('TimesNewRoman', os.path.join(FILE_DIR,'TimesNewRoman.ttf')))
  pdfmetrics.registerFont(TTFont('TimesBold', os.path.join(FILE_DIR,'TimesBold.ttf')))
  pdfmetrics.registerFont(TTFont('TimesItalic', os.path.join(FILE_DIR,'TimesItalic.ttf')))
  styles = getSampleStyleSheet()
  #Стили под шапку
  styles.add(
    ParagraphStyle(
      name='TNR_H_Center',
      fontName='TimesNewRoman',
      fontSize=12,
      alignment=TA_CENTER,
      #leftIndent=1.5*inch
    )
  )
  styles.add(
    ParagraphStyle(
      name='TNR_Bold_H_Center',
      fontName='TimesBold',
      fontSize=12,
      alignment=TA_CENTER,
      leftIndent=-0.7 * inch,
      leading=12,
    )
  )
  styles.add(
    ParagraphStyle(
      name='TNR_Big_Bold_H_Center16',
      fontName='TimesBold',
      fontSize=16,
      alignment=TA_CENTER,
      leading=20,
    )
  )


  styles.add(
    ParagraphStyle(
      name='TNR_H_Left',
      fontName='TimesNewRoman',
      leading = 30,
      fontSize=12,
      alignment=TA_LEFT,
      leftIndent=1.5*inch
    )
  )
  styles.add(
    ParagraphStyle(
      name='TNR_Left',
      fontName='TimesNewRoman',
      spaceBefore=0.3,
      leading=12,
      fontSize=12,
      alignment=TA_LEFT
    )
  )



  styles.add(
    ParagraphStyle(
      name='TNR_Big_Bold_H_Center14',
      fontName='TimesBold',
      leading = 20,
      fontSize=14,
      alignment=TA_CENTER)
  )
  styles.add(
    ParagraphStyle(
      name='TNR_Big_Bold_H_Center12',
      fontName='TimesBold',
      leading = 20,
      fontSize=12,
      alignment=TA_CENTER
    )
  )
  styles.add(
    ParagraphStyle(
      name='TNR_mini',
      fontName='TimesItalic',
      leading = 12,
      fontSize=9,
      alignment=TA_CENTER
    )
  )
  styles.add(
      ParagraphStyle(
          name='TNR_mini_left',
          fontName='TimesItalic',
          leading=12,
          fontSize=9,
          alignment=TA_LEFT,
          leftIndent=4 * mm,
      )
  )
  styles.add(
    ParagraphStyle(
      name='TNR_normal',
      fontName='TimesNewRoman',
      leading = 12,
      fontSize=12,
      alignment=TA_CENTER
    )
  )
  styles.add(
      ParagraphStyle(
          name='TNR_normal_left',
          fontName='TimesNewRoman',
          leading=12,
          fontSize=12,
          alignment=TA_LEFT,
      )
  )
  styles.add(
      ParagraphStyle(
          name='content_table',
          fontName='TimesNewRoman',
          leading=10,
          fontSize=10,
          alignment=TA_JUSTIFY
      )
  )
  styles.add(
    ParagraphStyle(
      name='TNR_bold_text',
      fontName='TimesBold',
      leading=12,
      fontSize=12,
      alignment=TA_LEFT
    )
  )

  normal_table_style = TableStyle([
          ('FONT', (0, 0), (-1, -1), 'TimesNewRoman', 9),
          ('FONT', (0, 0), (-1, -1), 'TimesNewRoman', 9),
          ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
          ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
          ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
          ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
      ]
  )

  TITLE_1_table_style1 = TableStyle([
      ('LINEABOVE', (1, 1), (1, 1),0.5, colors.black),
      ('LINEABOVE', (1, 2), (1, 3),0.5, colors.black),
      ('LINEABOVE', (1, 3), (1, 3),0.5, colors.black),
      ('FONT', (0, 0), (-1, -1), 'TimesNewRoman', 12),
      ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
  ])

  TITLE_2_table_style = TableStyle([
      ('LINEABOVE', (0, 1), (0, 1), 0.5, colors.black),
      ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
  ])
  TITLE_3_table_style = TableStyle([
      ('LINEABOVE', (0, 1), (1, 1), 0.5, colors.black),
      ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
  ])

  BLACK_LINES_table_style = TableStyle([
      ('LINEABOVE', (0, 1), (-1, -1), 0.5, colors.black),
      ('FONT', (0, 0), (-1, -1), 'TimesNewRoman', 9),
      ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
  ])


  head_table_style = TableStyle([
          ('FONT', (0, 0), (-1, -1), 'TimesNewRoman', 12),
          ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
          ('VALIGN', (0, 0), (-1, -1), 'TOP'),
      ]
  )

  header_table_paragraph_style =  ParagraphStyle(
    name="header_paragraph",
    fontName = 'TimesNewRoman',
    fontSize = 12,
    leading=12,
    alignment=TA_LEFT,
  )


  try:
    tplan = TeacherPlan.objects.get(id=id)
  except:
    raise Http404

  story = []
  if has_cover_page:
    story.append(Paragraph("МИНОБРНАУКИ РОССИИ",styles['TNR_H_Center']))
    LETI_NAME = Paragraph("""<br/><br/>САНКТ-ПЕТЕРБУРГСКИЙ
    <br/>ГОСУДАРСТВЕННЫЙ ЭЛЕКТРОТЕХНИЧЕСКИЙ УНИВЕРСИТЕТ
    <br/>«ЛЭТИ» им.В.И.Ульянова (Ленина)""",styles['TNR_Bold_H_Center'])

    Leti_image = Image(os.path.join(FILE_DIR,'im.png').__str__())
    Leti_image.drawHeight = 25*mm
    Leti_image.drawWidth = 20*mm
    header_table = Table([[Leti_image,LETI_NAME]], colWidths=(20*mm,155*mm))
    header_table.setStyle(head_table_style)
    story.append(header_table)

    story.append(Paragraph("<br/><br/><br/><br/>ИНДИВИДУАЛЬНЫЙ  ПЛАН <br/>"
                           "ПРЕПОДАВАТЕЛЯ<br/>",styles['TNR_Big_Bold_H_Center16']))
    story.append(Spacer(0, 0.5 *inch))

    position = ""
    if not tplan.person_profile.position == None:
      position = unicode( tplan.person_profile.position)

    birth_date = ""
    if not tplan.person_profile.birth_date == None:
      birth_date = tplan.person_profile.birth_date.year

    election_date = ""
    if not tplan.person_profile.election_date == None:
      election_date = dateformat.format(tplan.person_profile.election_date, 'd E Y')

    academic_degree = ""
    if not tplan.person_profile.academic_degree == None:
      academic_degree = tplan.person_profile.get_academic_degree_display()

    academic_degree_date = ""
    if not tplan.person_profile.year_of_academic_degree == None:
      academic_degree_date = tplan.person_profile.year_of_academic_degree.year

    academic_status = ""
    if not tplan.person_profile.academic_status == None:
      academic_status = tplan.person_profile.get_academic_status_display()

    academic_status_date = ""
    if not tplan.person_profile.year_of_academic_status == None:
      academic_status_date = tplan.person_profile.year_of_academic_degree.year

    contract_date=""
    if not tplan.person_profile.contract_date == None:
      contract_date = dateformat.format(tplan.person_profile.contract_date, 'd E Y')
    rate = u" (0.5 ставки)"
    if not tplan.person_profile.rate == None:
        rate = u" (%s)" % tplan.person_profile.rate

    personal_data = [
        ['Факультет', 'КТИ'],
        ['Кафедра', 'МО ЭВМ'],
        ['Должность', position + rate],
    ]
    p_d = Table(personal_data,colWidths=(40*mm, 85*mm))
    p_d.setStyle(TITLE_1_table_style1)
    story.append(p_d)
    story.append(Spacer(0, 0.3 *inch))

    data = [
        [Paragraph(tplan.person_profile.last_name,styles['TNR_normal'])],
        [Paragraph(u"Фамилия",styles['TNR_mini'])]
    ]
    p_d = Table(data,colWidths=(145*mm))
    p_d.setStyle(TITLE_2_table_style)
    story.append(p_d)

    data = [
        [
            Paragraph(tplan.person_profile.first_name, styles['TNR_normal_left']),
            Paragraph(tplan.person_profile.patronymic, styles['TNR_normal_left']),
        ],
        [
            Paragraph(u"Имя", styles['TNR_mini_left']),
            Paragraph(u"Отчество", styles['TNR_mini_left'])
        ]
    ]
    p_d = Table(data, colWidths=(100 * mm, 45 * mm))
    p_d.setStyle(TITLE_3_table_style)
    story.append(p_d)

    data = [
        [Paragraph(unicode(birth_date), styles['TNR_normal'])],
        [Paragraph(u"Год рождения", styles['TNR_mini'])]
    ]
    p_d = Table(data, colWidths=(30 * mm))
    p_d.setStyle(TITLE_2_table_style)
    story.append(p_d)
    story.append(Spacer(0, 0.3 * inch))

    data = [
        [Paragraph(election_date, styles['TNR_normal'])],
        [Paragraph(u"Дата текущего  избрания или зачисления на преподавательскую должность",
                   styles['TNR_mini'])]
    ]
    p_d = Table(data, colWidths=(145 * mm))
    p_d.setStyle(TITLE_2_table_style)
    story.append(p_d)
    story.append(Spacer(0, 0.3 * inch))

    data = [
        [Paragraph(u"%s %s" % (academic_degree,academic_degree_date), styles['TNR_normal'])],
        [Paragraph(u"Ученая степень и год присуждения",
                   styles['TNR_mini'])]
    ]
    p_d = Table(data, colWidths=(145 * mm))
    p_d.setStyle(TITLE_2_table_style)
    story.append(p_d)
    story.append(Spacer(0, 0.3 * inch))

    data = [
        [Paragraph(u"%s %s" % (academic_status, academic_status_date), styles['TNR_normal'])],
        [Paragraph(u"Ученое звание и год присвоения",
                   styles['TNR_mini'])]
    ]
    p_d = Table(data, colWidths=(145 * mm))
    p_d.setStyle(TITLE_2_table_style)
    story.append(p_d)
    story.append(Spacer(0, 0.3 * inch))

    data = [
        [Paragraph(contract_date, styles['TNR_normal'])],
        [Paragraph(u"Дата переизбрания (окончания трудового договора)",
                   styles['TNR_mini'])]
    ]
    p_d = Table(data, colWidths=(145 * mm))
    p_d.setStyle(TITLE_2_table_style)
    story.append(p_d)

    story.append(PageBreak())

  story.append(Paragraph("2. Методическая работа", styles['TNR_Big_Bold_H_Center14']))
  story.append(Paragraph("2.1. Подготовка учебников, учебных пособий и методических указаний,"
                         " включая электронные издания", styles['TNR_Big_Bold_H_Center12']))
  story.append(Spacer(0, 0.3 *inch))

  tplan.study_books
  data = [
             [
               Paragraph('Наименование',styles['TNR_mini']),
               Paragraph('Вид издания',styles['TNR_mini']),
               Paragraph('Объем',styles['TNR_mini']),
               Paragraph('Вид грифа',styles['TNR_mini']),
               Paragraph('Срок сдачи рукописи',styles['TNR_mini']),
               Paragraph('Отметка о выполнении',styles['TNR_mini']),
             ]
        ]
  for i in tplan.study_books:
    data.append(
      [
        Paragraph(i.name, styles['content_table']),
        Paragraph(i.type, styles['content_table']),
        Paragraph(str(i.volume), styles['TNR_normal']),
        Paragraph(i.vulture, styles['content_table']),
        Paragraph(i.finishDate, styles['TNR_normal']),
        Paragraph('', styles['content_table'])
      ]
    )

  all_table=Table(data, colWidths=(67*mm, 22*mm, 19*mm,16*mm, 25*mm, 25*mm))
  all_table.setStyle(normal_table_style)
  all_table.width = 20
  story.append(all_table)
  story.append(Spacer(0, 0.3 *inch))



  story.append(Paragraph("2.2. Постановка и модернизация дисциплин", styles['TNR_Big_Bold_H_Center12']))
  story.append(Spacer(0, 0.3 *inch))

  data = [
            [
              Paragraph('Наименование дисциплины', styles['TNR_mini']),
              Paragraph('Вид занятий', styles['TNR_mini']),
              Paragraph('Характер изменения', styles['TNR_mini']),
              Paragraph('Отметка о выполнении', styles['TNR_mini']),
            ],
      ]

  for i in tplan.disciplines:
    data.append(
      [
        Paragraph(i.name, styles['content_table']),
        Paragraph(i.type, styles['content_table']),
        Paragraph(i.characterUpdate, styles['content_table']),
        Paragraph('', styles['content_table'])
      ]
    )

  all_table=Table(data, colWidths=(47*mm, 30*mm, 73*mm,25*mm) )
  all_table.setStyle(normal_table_style)
  story.append(all_table)

  story.append(Paragraph("Принял к исполнению", styles['TNR_Left']))
  story.append(Paragraph("Преподаватель __________________(подпись)", styles['TNR_Left']))

  story.append(Spacer(0, 0.3 *inch))

  story.append(Paragraph("3. Научная работа", styles['TNR_Big_Bold_H_Center14']))
  story.append(Paragraph("Научно-исследовательская  работа в университете и вне университета", styles['TNR_Big_Bold_H_Center12']))
  story.append(Spacer(0, 0.3 *inch))

  data = [
          [
            Paragraph('Наименование работы', styles['TNR_mini']),
            Paragraph('Период', styles['TNR_mini']),
            Paragraph('В качестве кого участвовал', styles['TNR_mini']),
            Paragraph('Организация или предприятие', styles['TNR_mini']),
          ],
      ]
  for i in tplan.NIRS:
    data.append(
      [
        Paragraph(i.name, styles['content_table']),
        Paragraph(i.period, styles['TNR_normal']),
        Paragraph(i.role, styles['content_table']),
        Paragraph(i.organisation, styles['content_table']),
      ]
    )

  all_table=Table(data, colWidths=(80*mm, 25*mm, 45*mm,25*mm))
  all_table.setStyle(normal_table_style)
  story.append(all_table)
  story.append(Spacer(0, 0.3 *inch))

  story.append(Paragraph("4. Участие в конференциях и выставках", styles['TNR_Big_Bold_H_Center14']))
  story.append(Spacer(0, 0.3 *inch))
  data = [
          [
            Paragraph('Дата', styles['TNR_mini']),
            Paragraph('Наименование конференции или выставки', styles['TNR_mini']),
            Paragraph('Уровень конференции или выставки', styles['TNR_mini']),
            Paragraph('Наименование доклада или экспоната', styles['TNR_mini']),
          ],
      ]
  for i in tplan.participations:
    data.append(
      [
        Paragraph(i.name, styles['TNR_normal']),
        Paragraph(i.date, styles['content_table']),
        Paragraph(i.level, styles['content_table']),
        Paragraph(i.report, styles['content_table'])
      ]
    )

  all_table=Table(data, colWidths=(21*mm, 56*mm, 41*mm,57*mm))
  all_table.setStyle(normal_table_style)
  story.append(all_table)
  story.append(Spacer(0, 0.3 *inch))

  story.append(Paragraph("5. Список публикаций", styles['TNR_Big_Bold_H_Center14']))

  story.append(Spacer(0, 0.3 *inch))
  data = [
          [
            Paragraph('Наименование работ', styles['TNR_mini']),
            Paragraph('Вид публикации', styles['TNR_mini']),
            Paragraph('Объем в п.л.', styles['TNR_mini']),
            Paragraph('Наименование издательства, журнала или сборника', styles['TNR_mini']),
          ],
      ]
  for i in tplan.publications:
    data.append(
      [
        Paragraph(i.name_work, styles['content_table']),
        Paragraph(i.type, styles['content_table']),
        Paragraph(str(i.volume), styles['TNR_normal']),
        Paragraph(i.name_publisher, styles['content_table'])
      ]
    )


  all_table=Table(data, colWidths=(80*mm, 29*mm, 18*mm,48*mm))
  all_table.setStyle(normal_table_style)
  story.append(all_table)
  story.append(Spacer(0, 0.3 *inch))

  story.append(Paragraph("6. Повышение  квалификации", styles['TNR_Big_Bold_H_Center14']))
  story.append(Paragraph("Научно-исследовательская  работа в университете и вне университета", styles['TNR_Big_Bold_H_Center12']))
  story.append(Spacer(0, 0.3 *inch))
  data = [
          [
            Paragraph('Период', styles['TNR_mini']),
            Paragraph('Форма повышения квалификации', styles['TNR_mini']),
            Paragraph('Документ', styles['TNR_mini']),
          ],
      ]
  for i in tplan.qualifications:
    data.append(
      [
        Paragraph(i.period, styles['TNR_normal']),
        Paragraph(i.form_training, styles['content_table']),
        Paragraph(i.document, styles['content_table'])
      ]
    )

  all_table=Table(data, colWidths=(27*mm, 79*mm, 69*mm))
  all_table.setStyle(normal_table_style)
  story.append(all_table)
  story.append(Spacer(0, 0.3 *inch))

  story.append(Paragraph("7. Другие виды работ, выполняемых в интересах университета, факультета и кафедры", styles['TNR_Big_Bold_H_Center14']))
  story.append(Spacer(0, 0.3 *inch))
  data = [
          [
            Paragraph('Период', styles['TNR_mini']),
            Paragraph('Вид работы', styles['TNR_mini']),
          ],
      ]
  for i in tplan.anotherworks:
    data.append(
      [
        Paragraph(i.work_date, styles['TNR_normal']),
        Paragraph(i.type_work, styles['content_table'])
      ]
    )

  all_table=Table(data, colWidths=(27*mm, 148*mm))
  all_table.setStyle(normal_table_style)
  story.append(all_table)
  story.append(Spacer(0, 0.3 *inch))

  story.append(Paragraph("8. Замечания по работе преподавателя", styles['TNR_Big_Bold_H_Center14']))
  story.append(Spacer(0, 0.3 *inch))
  data = [
          [
            Paragraph('Дата', styles['TNR_mini']),
            Paragraph('Характер замечания', styles['TNR_mini']),
            Paragraph('Должность лица, вносящего замечания', styles['TNR_mini']),
            Paragraph('Подпись лица, вносящего замечания', styles['TNR_mini']),
            Paragraph('Подпись преподавателя', styles['TNR_mini']),
          ],
          [' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' '],
      ]

  all_table=Table(data, colWidths=(14*mm, 66*mm, 31*mm, 31*mm, 33*mm))
  all_table.setStyle(normal_table_style)
  story.append(all_table)
  story.append(Spacer(0, 0.3 *inch))
  story.append(PageBreak())

  story.append(Paragraph("9. Заключение кафедры", styles['TNR_Big_Bold_H_Center14']))

  data=[
      [""],
      [""],
      [""],
      [""],
      [""],
      [""],
      [""],
  ]

  all_table=Table(data,colWidths=(175*mm))
  all_table.setStyle(BLACK_LINES_table_style)
  story.append(all_table)


  story.append(Spacer(0, 0.3 * inch))
  table_data = [
    [Paragraph('Преподаватель', styles['TNR_bold_text']),'________________________________________','_________________'],
    [Paragraph('Зав. кафедрой', styles['TNR_bold_text']),'________________________________________','_________________'],
    [],
  ]
  table = Table(table_data,colWidths=(40*mm,90*mm,45*mm))
  story.append(table)

  story.append(PageBreak())
  if with_finish_page:
    story.append(Paragraph("Заключение за пятилетний период работы", styles['TNR_Big_Bold_H_Center14']))
    story.append(Paragraph("Особые достижения преподавателя за пятилетний период работы " +
                           "(Подготовка и защита диссертации, подготовка призеров конкурсов студенческих и аспиранских работ, " +
                           "победителей предметных олимпиад и т.д.).", header_table_paragraph_style))

    story.append(Spacer(0, 0.3 * inch))


    table_data = [
      ['Наименование работ','Период'],
      ['',''],
      ['',''],
      ['',''],
      ['',''],
      ['',''],
      ['',''],
      ['',''],
    ]
    story.append(Spacer(0,0.3*inch))

    table = Table(table_data, colWidths=(120 * mm, 55 * mm))
    table.setStyle(normal_table_style)
    story.append(table)

    story.append(Paragraph("Заключение кафедры за 5-летний период работы", styles['TNR_Big_Bold_H_Center14']))



    story.append(Paragraph("______________________________________________________________________", styles['TNR_bold_text']))
    story.append(Paragraph("______________________________________________________________________", styles['TNR_bold_text']))
    story.append(Paragraph("______________________________________________________________________", styles['TNR_bold_text']))
    story.append(Paragraph("______________________________________________________________________", styles['TNR_bold_text']))
    story.append(Paragraph("______________________________________________________________________", styles['TNR_bold_text']))
    story.append(Paragraph("______________________________________________________________________", styles['TNR_bold_text']))

    story.append(Spacer(0, 0.3 * inch))

    table_data = [
      [Paragraph('Преподаватель', styles['TNR_bold_text']), '________________________________________','_________________'],
      [Paragraph('Зав. кафедрой', styles['TNR_bold_text']), '________________________________________','_________________'],
      [Paragraph('Декан', styles['TNR_bold_text']), '________________________________________','_________________'],
      [],
    ]
    table = Table(table_data, colWidths=(40 * mm, 90 * mm, 45 * mm))
    story.append(table)

  if(responce==None):
    doc = SimpleDocTemplate('mydoc.pdf',pagesize = A4)
  else:
    doc = SimpleDocTemplate(responce, pagesize=A4)
  doc.build(story)

  return responce