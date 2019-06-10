from django.utils.translation import ugettext_lazy as _
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import mm 
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

from mysite.settings import STATIC_ROOT # import file rootpath


# pdfmetrics.registerFont(TTFont('FreeSans', STATIC_ROOT + 'fonts/FreeSans.ttf'))
# pdfmetrics.registerFont(TTFont('FreeSansBold', STATIC_ROOT + 'fonts/FreeSansBold.ttf'))

class PdfPrint:
	# initialize class
	def __init__(self, buffer, pageSize):
		self.buffer = buffer
		# default format is A4
		if pageSize == 'A4':
			self.pageSize = A4
		elif pageSize == 'Letter':
			self.pageSize = letter
		self.width, self.height = self.pageSize

	# add page numbers to pdf document
	def pageNumber(self, canvas, doc):
		number = canvas.getPageNumber()
		canvas.drawCentredString(100*mm, 15*mm, str(number))

	# create pdf document, organize its components and layout
	def report(self, pdfdownload, title):
		# set some characteristics for pdf documents
		doc = SimpleDocTemplate(
			self.buffer,
			rightMargin=72,
			leftMargin=72,
			topmargin=30,
			bottomMargin=72,
			pagesize=self.pageSize)

		# a collection of styles offered by the library
		styles=getSampleStyleSheet()
		# add custom paragraph style
		styles.add(ParagraphStyle(
			name="TableHeader", fontSize=11, alignment=TA_CENTER))
		styles.add(ParagraphStyle(
			name="ParagraphTitle", fontSize=11, alignment=TA_JUSTIFY))
		styles.add(ParagraphStyle(
			name="Justify", alignment=TA_JUSTIFY))
		# list used for elements addded into document
		data = []
		data.append(Paragraph(title, styles['Title']))
		# insert a blank space
		data.append(Spacer(1, 12))
		table_data = []
		# table header
		table_data.append([
			Paragraph('Contribution Date', styles['TableHeader']),
			Paragraph('Name', styles['TableHeader']),
			Paragraph('Amount', styles['TableHeader'])]),
		for pd in pdfdownload:
			# data.append(Spacer(1, 24))
			# add a row to table
			table_data.append(
				[pd.Contribution_date,
				 Paragraph(pd.member.username, styles['Justify']),
				 u"Ksh.{0}".format(pd.amount)])
		
		# create table
		pd_table = Table(table_data, colWidths=[doc.width/3.0]*7)
		pd_table.hAlign = 'LEFT'
		pd_table.setStyle(TableStyle(
			[('INNERGRID', (0, 0),(-1, -1), 0.25, colors.black),
			 ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
             ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
             ('BACKGROUND', (0, 0), (-1, 0), colors.gray)]))
		data.append(pd_table)
		data.append(Spacer(1, 48))

		# create document
		doc.build(data, onFirstPage=self.pageNumber, onLaterPages=self.pageNumber)
		pdf = self.buffer.getvalue()
		self.buffer.close()
		return pdf




