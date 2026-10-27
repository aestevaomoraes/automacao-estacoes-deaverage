Set WshShell = CreateObject("WScript.Shell")

WshShell.Run Chr(34) & _
"C:\XXXXXXXXX\Documents\Projetos\Automacao_Estacoes_XXXXX\iniciar_automacao.bat" & _
Chr(34), 0, False

Set WshShell = Nothing
