Option Explicit

' Укажите путь к файлу Excel и желаемый путь для CSV-файла
Dim excelPath, csvPath
excelPath = "./2.xlsx"
csvPath = "./3.csv"

' Создаём объекты для работы с Excel
Dim excelApp, workbook, worksheet
Set excelApp = CreateObject("Excel.Application")
excelApp.Visible = False

' Открытие файла Excel
Set workbook = excelApp.Workbooks.Open(excelPath)
Set worksheet = workbook.Sheets(1)

' Проверка наличия текста "Обязательное поле" во второй строке
Dim cellValue
cellValue = worksheet.Cells(2, 1).Value

If InStr(1, cellValue, "Обязательное поле", vbTextCompare) > 0 Then
    ' Удаление второй строки
    worksheet.Rows(2).Delete
End If

' Сохранение в формате CSV
workbook.SaveAs csvPath, 6 ' 6 означает формат CSV

' Закрытие книги и завершение работы с Excel
workbook.Close False
excelApp.Quit

' Освобождение ресурсов
Set worksheet = Nothing
Set workbook = Nothing
Set excelApp = Nothing

WScript.Echo "Конвертация завершена. Файл сохранён как: " & csvPath