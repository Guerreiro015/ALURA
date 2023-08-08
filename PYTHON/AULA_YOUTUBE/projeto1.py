frase_do_dia = 'Tudo é facil com um bom direcionamento'
frase_do_dia = 'tudo é fácil com um bom direcionamento'.upper()

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
pdf.image("template.png", x=0, y=0 )
pdf.text(10,10,frase_do_dia)
pdf.text(115, 145, "projeto")
pdf.text(115, 160, 'horas_estimadas')
pdf.text(115, 175, 'valor_hora')
pdf.text(115, 190, 'prazo_estimado')
pdf.text(115, 205, str('valor_total_estimado'))

pdf.output("orçamento.pdf")
print("Orçamento gerado com sucesso!")