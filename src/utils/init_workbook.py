from openpyxl import load_workbook

def init_workbook(file):
     workbook = load_workbook(filename=file)
     return workbook