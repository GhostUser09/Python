import xlsxwriter

workbook = xlsxwriter.Workbook("Excel_schreiben_Ares_Reisinger.xlsx")
worksheet = workbook.add_worksheet()

bold = workbook.add_format({"bold": True})

worksheet.write('A1', 'Ares', bold)
worksheet.write('A2', 'Reisinger', bold)
worksheet.write('A3', 'Wachtelgasse 8', bold)
worksheet.write('A4', 'Kalsdorf', bold)
worksheet.write('A5', '0660 1789997', bold)
worksheet.insert_image('D2', 'logo.png')

row = 1
col = 0

workbook.close()
