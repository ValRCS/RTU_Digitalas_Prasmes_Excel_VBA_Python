Option Explicit

Private Sub Worksheet_Change(ByVal Target As Range)

    Dim changedArea As Range
    Dim lastRow As Long
    Dim rngToSort As Range

    ' React only when something changes in columns C or D, starting from row 2
    Set changedArea = Intersect(Target, Me.Range("C2:D" & Me.Rows.Count))
    If changedArea Is Nothing Then Exit Sub

    On Error GoTo SafeExit
    Application.EnableEvents = False

    ' Find the last used row based on column A
    lastRow = Me.Cells(Me.Rows.Count, "A").End(xlUp).Row

    ' Stop if there is no data to sort
    If lastRow < 2 Then GoTo SafeExit

    ' Define the range to sort
    Set rngToSort = Me.Range("A1:E" & lastRow)

    ' Sort by column D descending, then by column C ascending
    rngToSort.Sort _
        Key1:=Me.Range("D1"), Order1:=xlDescending, _
        Key2:=Me.Range("C1"), Order2:=xlAscending, _
        Header:=xlYes

SafeExit:
    Application.EnableEvents = True

End Sub
