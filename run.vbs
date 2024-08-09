Option Explicit

' Укажите путь к вашему виртуальному окружению и скрипту parser.py
Dim venvPath, scriptPath, shell
venvPath = "rs"
scriptPath = "parse.py"

' Создание объекта Shell
Set shell = CreateObject("WScript.Shell")

' Проверка существования скрипта parser.py
Dim fso
Set fso = CreateObject("Scripting.FileSystemObject")
If Not fso.FileExists(scriptPath) Then
    WScript.Echo "Ошибка: файл parser.py не найден по указанному пути: " & scriptPath
    WScript.Quit
End If

' Формирование команды для активации виртуального окружения и вызова parser.py
Dim command
command = venvPath & "\Scripts\activate.bat & python " & scriptPath

' Запуск команды
shell.Run command, 1, True

' Освобождение ресурсов
Set fso = Nothing
Set shell = Nothing