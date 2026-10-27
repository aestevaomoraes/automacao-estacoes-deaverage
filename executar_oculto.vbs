Set WshShell = CreateObject("WScript.Shell")

WshShell.Run Chr(34) & _
"C:\Users\oi310541\Documents\Projetos\Automacao_Estacoes_DeAverage\iniciar_automacao.bat" & _
Chr(34), 0, False

Set WshShell = Nothing