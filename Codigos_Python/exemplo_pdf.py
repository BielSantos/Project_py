from reportlab.pdfgen import canvas


pdf = canvas.Canvas("TEST.pdf")
pdf.drawString(100, 200, "Exemplo de PDF")
pdf.save()
