import openpyxl as xl
wb = xl.load_workbook("pythonxlsx.xlsx")
sheet = wb["Sheet"]

def bubblesort(A):
    for i in range(len(A)-1, 0, -1):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

for row in range(1, sheet.max_row + 1)
    cell = sheet.cell(row, 1)
    cell.bubblesort(cell)

wb.save()

