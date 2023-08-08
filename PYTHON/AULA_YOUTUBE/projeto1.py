frase_do_dia = 'Tudo é facil com um bom direcionamento'
frase_do_dia = 'tudo é fácil com um bom direcionamento'

from fpdf import FPDF

teste = FPDF()
teste.add_page()
teste.set_font("Arial")
teste.text(10,10,frase_do_dia)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")