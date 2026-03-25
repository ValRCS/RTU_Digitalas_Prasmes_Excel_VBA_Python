Sub WriteHello()
    Worksheets("Playground").Range("A1").Value = "Hello, VBA no RTU! "
End Sub

Sub InsertLatvianText()

    Worksheets("Playground").Range("C9").Value = "Mans vārds ir Valdis no Rīgas "

End Sub

Sub WriteToCleanDataSheet()
    Worksheets("CleanData").Range("A1").Value = "Processed"
End Sub

Sub CopyData()
    Worksheets("CleanData").Cells.Clear
    Worksheets("RawData").Range("A4:E19").Copy _
        Destination:=Worksheets("CleanData").Range("A1")
End Sub

Sub CopySingleCell()

    Worksheets("CleanData").Range("D22").Value = _
        Worksheets("Playground").Range("C9").Value

End Sub

Sub CleanData()

    Dim ws As Worksheet
    Set ws = Worksheets("CleanData")

    ws.Columns("B").Delete
    ws.Range("H1").Value = "Processed"
    ws.Range("H2:H10").Value = "Yes"

End Sub

Sub SortData()

    Dim ws As Worksheet
    Set ws = Worksheets("CleanData")

    ws.Range("A1:D10").Sort Key1:=ws.Range("C1"), Order1:=xlDescending, Header:=xlYes

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

Sub GenerateReportWithPie()

    Dim src As Worksheet, dst As Worksheet
    Dim chartObj As ChartObject
    Dim dataRange As Range, labelRange As Range

    Set src = Worksheets("CleanData")
    Set dst = Worksheets("Report")

    ' Clear report sheet
    dst.Cells.Clear

    ' Header
    dst.Range("A1").Value = "Sales Report"
    dst.Range("A2").Value = "Generated: " & Now

    ' Copy table
    src.Range("A1:E10").Copy Destination:=dst.Range("A4")
    dst.Columns("A:E").AutoFit

    ' Define data for chart
    Set labelRange = src.Range("A2:A11") ' categories (names)
    Set dataRange = src.Range("C2:C11")  ' values

    ' Create chart
    Set chartObj = dst.ChartObjects.Add(Left:=dst.Range("H4").Left, _
                                        Top:=dst.Range("H4").Top, _
                                        Width:=300, Height:=250)

    With chartObj.Chart
        .ChartType = xlPie
        
        ' Set data
        .SetSourceData Source:=dataRange
        
        ' Add labels
        .SeriesCollection(1).XValues = labelRange
        
        ' Title
        .HasTitle = True
        .ChartTitle.Text = "Distribution by Category"
        
        ' Optional: show percentages
        .SeriesCollection(1).HasDataLabels = True
        .SeriesCollection(1).DataLabels.ShowPercentage = True
    End With
    
    ' -----------------------
    ' BAR CHART (H16)
    ' -----------------------
    Set barChart = dst.ChartObjects.Add( _
        Left:=dst.Range("H16").Left, _
        Top:=dst.Range("H16").Top, _
        Width:=300, Height:=250)

    With barChart.Chart
        .ChartType = xlColumnClustered   ' vertical bar chart
        .SetSourceData Source:=dataRange
        .SeriesCollection(1).XValues = labelRange
        .HasTitle = True
        .ChartTitle.Text = "Values by Category"
        
        ' Optional: show values on bars
        .SeriesCollection(1).HasDataLabels = True
    End With


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
    Call GenerateReportWithPie
    Call ReportWithInput

    MsgBox "Report completed!", vbInformation

End Sub

