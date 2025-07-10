import os
from reportlab.lib.pagesizes import latter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from docx import Document
from PIL import Image

def converter_doc_para_pdf (caminhi_doc, caminho_pdf):
    '''
    converte um arquivo .doc ou(.docx) para PDF
    Extrai o texto do documento e escreve em um PDF
    '''

try:
    documento = Document(caminho_doc) #Abre o documento.docx ou doc usnado python-docx.
    c =  canvas.Canvas(caminio_pdf, pagesize = latter) #Cria um novo objeto Canvas (o PDF) com o caminho de saída e tamanho da página.
    largura,altura = latter # Obtém as dimenções da página definida

    y_pos = altura - 50

    for paragrafo in documento.paragraphs:
        texto = paragrafo.text # extrai o texto pudo do parágrafo atual

        linhas = [] #inicializa uma lista para armazenar as linhas de texto
        linha_atual = "" #inicializa uma string para construir a linha atual antes de adicionar à lista 'linhas'.
        for palavra in texto.plit():

            if c.stringWidth(linha_atual + "" + palavra, 'Helvetica', 12) < (largura - 100):
                linha_atual += '' + palavra 
            else:
                linhas.append(linha_atual.strip())
                linha_atual = palavra
        
     