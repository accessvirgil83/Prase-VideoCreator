Option Explicit


Dim distrPath
distrPath = "distr"

Dim installerName
Dim is64Bit


If InStr(1, CreateObject("WScript.Network").ComputerName, "64") Then
    is64Bit = True
Else
    is64Bit = False
End If


If is64Bit Then
    installerName = "python-3.11.7-amd64.exe"
Else
    installerName = "python-3.11.7.exe" ' 
End If


Dim fullPath
fullPath = distrPath & "\" & installerName


Dim shell, pythonCheck, fso
Set fso = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("WScript.Shell")


On Error Resume Next
pythonCheck = shell.Exec("python --version").StdOut.ReadAll()
On Error GoTo 0

If pythonCheck = "" Then
    
    If fso.FileExists(fullPath) Then
        shell.Run """" & fullPath & """ /quiet InstallAllUsers=1 PrependPath=1 Include_test=0", 1, True
        WScript.Echo "the installer has started"

        
        On Error Resume Next
        pythonCheck = shell.Exec("python --version").StdOut.ReadAll()
        On Error GoTo 0

        If pythonCheck = "" Then
            WScript.Echo "Found: Python version."
            WScript.Quit
        End If
    Else
        WScript.Echo "Error; file" & installerName & " not found" & distrPath
        WScript.Quit
    End If
Else
    WScript.Echo "Python is exist. Версия: " & pythonCheck
End If


WScript.Echo "Установка pip "

shell.Run "python -m pip install --upgrade pip", 1, True
shell.Run "python -m pip install virtualenv", 1, True


shell.Run "python -m venv rs", 1, True

shell.Run "rs\Scripts\activate.bat & pip install -r requirements.txt", 1, True

WScript.Echo "Program is installer"

Set fso = Nothing
Set shell = Nothing