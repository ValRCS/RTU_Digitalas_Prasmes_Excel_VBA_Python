Sub WriteHello()
    ' Mans pirmais makro
    Worksheets("Playground").Range("A1:A3").Value = "Alus"
End Sub

Sub WriteToSheet()
    Worksheets("CleanData").Range("A1").Value = "Processed"
End Sub

Sub CopyData()
    Worksheets("CleanData").Cells.Clear
    Worksheets("RawData").Range("A4:E19").Copy _
        Destination:=Worksheets("CleanData").Range("A1")
End Sub

Sub CleanData()

    Dim ws As Worksheet
    Set ws = Worksheets("CleanData")

    ws.Columns("B").Delete
    ws.Rows("13").Delete
    ws.Range("E1").Value = "Processed"
    ws.Range("E2:E10").Value = "Yes"

End Sub

Sub SortData()

    Dim ws As Worksheet
    Set ws = Worksheets("CleanData")

    ws.Range("A1:E10").Sort _
        Key1:=ws.Range("D1"), Order1:=xlDescending, _
        Key2:=ws.Range("C1"), Order2:=xlAscending, _
        Header:=xlYes

End Sub

Sub GenerateReport()

    Dim src As Worksheet
    Dim dst As Worksheet
    Dim chartObj As ChartObject
    Dim lastRow As Long
    Dim reportLastRow As Long
    Dim maxRow As Long

    Set src = Worksheets("CleanData")
    Set dst = Worksheets("Report")

    ' Find last row
    lastRow = src.Cells(src.Rows.Count, "A").End(xlUp).Row

    ' Clear report and charts
    dst.Cells.Clear
    For Each chartObj In dst.ChartObjects
        chartObj.Delete
    Next chartObj

    ' Header
    dst.Range("A1").Value = "Sales Report"
    dst.Range("A2").Value = "Generated: " & Now

    ' Copy data
    src.Range("A1:E" & lastRow).Copy Destination:=dst.Range("A4")
    dst.Columns("A:E").AutoFit

    ' Calculate last row in report
    reportLastRow = lastRow + 3

    ' Limit to first 10 data rows (rows 5–14)
    maxRow = Application.WorksheetFunction.Min(reportLastRow, 14)

    ' Create chart
    Set chartObj = dst.ChartObjects.Add( _
        Left:=dst.Range("H4").Left, _
        Top:=dst.Range("H4").Top, _
        Width:=400, _
        Height:=250)

    With chartObj.Chart
        .ChartType = xlPie
        .HasTitle = True
        .ChartTitle.Text = "Sales Distribution (Top 10 Rows)"

        With .SeriesCollection.NewSeries
            .XValues = dst.Range("A5:A" & maxRow)   ' Names
            .Values = dst.Range("D5:D" & maxRow)    ' Sales
            .Name = "Sales"
        End With

        .ApplyDataLabels
        With .SeriesCollection(1)
            .HasDataLabels = True
            .DataLabels.ShowCategoryName = True
            .DataLabels.ShowPercentage = True
            .DataLabels.ShowValue = False
        End With
    End With

End Sub

Sub GenerateReportWithPieBar()

    Dim src As Worksheet
    Dim dst As Worksheet
    Dim chartObj As ChartObject
    Dim pieChartObj As ChartObject
    Dim barChartObj As ChartObject
    Dim lastRow As Long
    Dim reportLastRow As Long
    Dim maxPieRow As Long

    Set src = Worksheets("CleanData")
    Set dst = Worksheets("Report")

    ' Find last used row in source sheet based on column A
    lastRow = src.Cells(src.Rows.Count, "A").End(xlUp).Row

    ' Clear report sheet
    dst.Cells.Clear

    ' Remove old charts
    For Each chartObj In dst.ChartObjects
        chartObj.Delete
    Next chartObj

    ' Add report heading
    dst.Range("A1").Value = "Sales Report"
    dst.Range("A2").Value = "Generated: " & Now

    ' Copy source data to report
    src.Range("A1:E" & lastRow).Copy Destination:=dst.Range("A4")
    dst.Columns("A:E").AutoFit

    ' Calculate last row in report sheet
    reportLastRow = lastRow + 3

    ' Limit pie chart to first 10 data rows only
    maxPieRow = Application.WorksheetFunction.Min(reportLastRow, 14)

    ' -----------------------------
    ' Create pie chart at H4
    ' -----------------------------
    Set pieChartObj = dst.ChartObjects.Add( _
        Left:=dst.Range("H4").Left, _
        Top:=dst.Range("H4").Top, _
        Width:=400, _
        Height:=250)

    With pieChartObj.Chart
        .ChartType = xlPie
        .HasTitle = True
        .ChartTitle.Text = "Sales Distribution (First 10 Rows)"

        With .SeriesCollection.NewSeries
            .XValues = dst.Range("A5:A" & maxPieRow)
            .Values = dst.Range("D5:D" & maxPieRow)
            .Name = "Sales"
        End With

        .ApplyDataLabels
        With .SeriesCollection(1)
            .HasDataLabels = True
            .DataLabels.ShowCategoryName = True
            .DataLabels.ShowPercentage = True
            .DataLabels.ShowValue = False
        End With
    End With

    ' -----------------------------
    ' Create bar chart at H22
    ' -----------------------------
    Set barChartObj = dst.ChartObjects.Add( _
        Left:=dst.Range("H22").Left, _
        Top:=dst.Range("H22").Top, _
        Width:=500, _
        Height:=300)

    With barChartObj.Chart
        .ChartType = xlColumnClustered
        .HasTitle = True
        .ChartTitle.Text = "All Sales by Name"

        With .SeriesCollection.NewSeries
            .XValues = dst.Range("A5:A" & reportLastRow)
            .Values = dst.Range("D5:D" & reportLastRow)
            .Name = "Sales"
        End With

        .Axes(xlCategory).HasTitle = True
        .Axes(xlCategory).AxisTitle.Text = "Names"

        .Axes(xlValue).HasTitle = True
        .Axes(xlValue).AxisTitle.Text = "Sales"
    End With

End Sub

Sub GenerateReportWithAggregation()

    Dim src As Worksheet
    Dim dst As Worksheet
    Dim chartObj As ChartObject
    Dim pieChartObj As ChartObject
    Dim barChartObj As ChartObject
    Dim regionPieChartObj As ChartObject

    Dim lastRow As Long
    Dim reportLastRow As Long
    Dim maxPieRow As Long

    Dim i As Long
    Dim outputRow As Long

    Dim regionName As String
    Dim salesValue As Double

    Dim regionDict As Object
    Dim key As Variant

    Set src = Worksheets("CleanData")
    Set dst = Worksheets("Report")

    lastRow = src.Cells(src.Rows.Count, "A").End(xlUp).Row

    ' Stop if there is no data beyond header row
    If lastRow < 2 Then
        MsgBox "No data found in CleanData.", vbExclamation
        Exit Sub
    End If

    dst.Cells.Clear

    ' Remove old charts
    For Each chartObj In dst.ChartObjects
        chartObj.Delete
    Next chartObj

    ' Header
    dst.Range("A1").Value = "Sales Report"
    dst.Range("A2").Value = "Generated: " & Now

    ' Copy data
    src.Range("A1:E" & lastRow).Copy Destination:=dst.Range("A4")
    dst.Columns("A:E").AutoFit

    reportLastRow = lastRow + 3
    maxPieRow = Application.WorksheetFunction.Min(reportLastRow, 14)

    ' -----------------------------
    ' Pie chart (first 10 rows) at H4
    ' -----------------------------
    If maxPieRow >= 5 Then
        Set pieChartObj = dst.ChartObjects.Add( _
            Left:=dst.Range("H4").Left, _
            Top:=dst.Range("H4").Top, _
            Width:=400, _
            Height:=250)

        With pieChartObj.Chart
            .ChartType = xlPie
            .HasTitle = True
            .ChartTitle.Text = "Sales Distribution (First 10 Rows)"

            Do While .SeriesCollection.Count > 0
                .SeriesCollection(1).Delete
            Loop

            With .SeriesCollection.NewSeries
                .Name = "Sales"
                .XValues = dst.Range("A5:A" & maxPieRow)
                .Values = dst.Range("D5:D" & maxPieRow)
            End With

            .ApplyDataLabels
            With .SeriesCollection(1)
                .HasDataLabels = True
                .DataLabels.ShowCategoryName = True
                .DataLabels.ShowPercentage = True
                .DataLabels.ShowValue = False
            End With
        End With
    End If

    ' -----------------------------
    ' Column chart (all data) at H22
    ' -----------------------------
    Set barChartObj = dst.ChartObjects.Add( _
        Left:=dst.Range("H22").Left, _
        Top:=dst.Range("H22").Top, _
        Width:=500, _
        Height:=300)

    With barChartObj.Chart
        .ChartType = xlColumnClustered
        .HasTitle = True
        .ChartTitle.Text = "All Sales by Name"

        Do While .SeriesCollection.Count > 0
            .SeriesCollection(1).Delete
        Loop

        With .SeriesCollection.NewSeries
            .Name = "Sales"
            .XValues = dst.Range("A5:A" & reportLastRow)
            .Values = dst.Range("D5:D" & reportLastRow)
        End With

        .Axes(xlCategory).HasTitle = True
        .Axes(xlCategory).AxisTitle.Text = "Names"

        .Axes(xlValue).HasTitle = True
        .Axes(xlValue).AxisTitle.Text = "Sales"
    End With

    ' -----------------------------
    ' Aggregate sales by region
    ' -----------------------------
    Set regionDict = CreateObject("Scripting.Dictionary")

    For i = 5 To reportLastRow
        regionName = Trim(CStr(dst.Cells(i, "C").Value))

        If IsNumeric(dst.Cells(i, "D").Value) Then
            salesValue = CDbl(dst.Cells(i, "D").Value)
        Else
            salesValue = 0
        End If

        If regionName <> "" Then
            If regionDict.Exists(regionName) Then
                regionDict(regionName) = regionDict(regionName) + salesValue
            Else
                regionDict.Add regionName, salesValue
            End If
        End If
    Next i

    ' -----------------------------
    ' Write helper data to B and C
    ' -----------------------------
    dst.Range("B38").Value = "Region"
    dst.Range("C38").Value = "Total Sales"

    outputRow = 39
    For Each key In regionDict.Keys
        dst.Cells(outputRow, "B").Value = key
        dst.Cells(outputRow, "C").Value = regionDict(key)
        outputRow = outputRow + 1
    Next key

    ' dst.Columns("M:O").AutoFit

    ' -----------------------------
    ' Region pie chart at H38
    ' -----------------------------
    If outputRow > 2 Then
        Set regionPieChartObj = dst.ChartObjects.Add( _
            Left:=dst.Range("H38").Left, _
            Top:=dst.Range("H38").Top, _
            Width:=400, _
            Height:=250)

        With regionPieChartObj.Chart
            .ChartType = xlPie
            .HasTitle = True
            .ChartTitle.Text = "Sales by Region"

            Do While .SeriesCollection.Count > 0
                .SeriesCollection(1).Delete
            Loop

            With .SeriesCollection.NewSeries
                .Name = "Regional Sales"
                .XValues = dst.Range("B39:B" & (outputRow - 1))
                .Values = dst.Range("C39:C" & (outputRow - 1))
            End With

            .ApplyDataLabels
            With .SeriesCollection(1)
                .HasDataLabels = True
                .DataLabels.ShowCategoryName = True
                .DataLabels.ShowPercentage = True
                .DataLabels.ShowValue = False
            End With
        End With
    End If

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
    ' Call CleanData
    Call SortData
    Call GenerateReportWithAggregation
    Call ReportWithInput

    MsgBox "Report completed!", vbInformation

End Sub

Option Explicit

Sub ExportTop5SalesToWord()

    Dim ws As Worksheet
    Dim wdApp As Object
    Dim wdDoc As Object
    Dim savePath As String

    Dim lastRow As Long
    Dim i As Long
    Dim endRow As Long

    Dim personName As String
    Dim salesValue As Variant

    On Error GoTo ErrorHandler

    Set ws = Worksheets("Report")

    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row

    If lastRow < 5 Then
        MsgBox "No report data found in sheet 'Report'.", vbExclamation
        Exit Sub
    End If

    endRow = Application.WorksheetFunction.Min(lastRow, 9)

    If ThisWorkbook.Path = "" Then
        MsgBox "Please save the Excel workbook first, so the Word file can be saved next to it.", vbExclamation
        Exit Sub
    End If

    savePath = ThisWorkbook.Path & Application.PathSeparator & "report.docx"

    Set wdApp = CreateObject("Word.Application")
    Set wdDoc = wdApp.Documents.Add

    With wdDoc.Content
        .InsertAfter "Top 5 Sales Report" & vbCrLf
        .InsertAfter "Generated: " & Format(Now, "yyyy-mm-dd hh:nn:ss") & vbCrLf & vbCrLf
        .InsertAfter "Top 5 sales names:" & vbCrLf & vbCrLf
    End With

    For i = 5 To endRow
        personName = CStr(ws.Cells(i, "A").Value)
        salesValue = ws.Cells(i, "D").Value

        wdDoc.Content.InsertAfter CStr(i - 4) & ". " & personName & " - Sales: " & salesValue & vbCrLf
    Next i

    wdDoc.SaveAs2 Filename:=savePath, FileFormat:=16
    wdDoc.Close SaveChanges:=False
    wdApp.Quit

    Set wdDoc = Nothing
    Set wdApp = Nothing

    MsgBox "Word document created: " & savePath, vbInformation
    Exit Sub

ErrorHandler:
    On Error Resume Next

    If Not wdDoc Is Nothing Then
        wdDoc.Close SaveChanges:=False
    End If

    If Not wdApp Is Nothing Then
        wdApp.Quit
    End If

    Set wdDoc = Nothing
    Set wdApp = Nothing

    MsgBox "An error occurred while creating the Word report.", vbExclamation

End Sub
