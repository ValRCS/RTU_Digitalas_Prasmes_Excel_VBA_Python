Private Sub Worksheet_Change(ByVal Target As Range)

    Dim ws As Worksheet
    Set ws = Me   ' refers to CleanData sheet

    ' Check if change happened in column D
    If Not Intersect(Target, ws.Range("D:D")) Is Nothing Then
        
        Application.EnableEvents = False
        
        ws.Range("A1:E10").Sort _
            Key1:=ws.Range("D1"), _
            Order1:=xlDescending, _
            Header:=xlYes
        
        Application.EnableEvents = True
        
    End If

End Sub
