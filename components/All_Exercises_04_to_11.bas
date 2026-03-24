Attribute VB_Name = "All_Exercises_04_to_11"
Option Explicit

Sub WriteHello()
    Worksheets("Playground").Range("A1").Value = "Hello, VBA"
End Sub

Sub WriteToSheet()
    Worksheets("CleanData").Range("A1").Value = "Processed"
End Sub

Sub CopyData()
    Worksheets("CleanData").Cells.Clear
    Worksheets("RawData").Range("A1:D10").Copy Destination:=Worksheets("CleanData").Range("A1")
End Sub

Sub CleanData()

    Dim ws As Worksheet
    Set ws = Worksheets("CleanData")

    ws.Columns("B").Delete
    ws.Range("E1").Value = "Processed"
    ws.Range("E2:E10").Value = "Yes"

End Sub

Sub SortData()

    Dim ws As Worksheet
    Set ws = Worksheets("CleanData")

    ws.Range("A1:E10").Sort Key1:=ws.Range("C1"), Order1:=xlAscending, Header:=xlYes

End Sub

Sub GenerateReport()

    Dim src As Worksheet, dst As Worksheet

    Set src = Worksheets("CleanData")
    Set dst = Worksheets("Report")

    dst.Cells.Clear

    dst.Range("A1").Value = "Sales Report"
    dst.Range("A2").Value = "Generated: " & Now

    src.Range("A1:E10").Copy Destination:=dst.Range("A4")
    dst.Columns("A:E").AutoFit

End Sub

Sub ReportWithInput()

    Dim title As String
    title = InputBox("Enter report title")

    If title = "" Then
        title = "Sales Report"
    End If

    Worksheets("Report").Range("A1").Value = title

End Sub

Sub FullWorkflow()

    Call CopyData
    Call CleanData
    Call SortData
    Call GenerateReport
    Call ReportWithInput

    MsgBox "Report completed!", vbInformation

End Sub
