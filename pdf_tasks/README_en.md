# Student Practical Task List
## Topic: PDF Document Analysis with Python

### 1. task: Opening a PDF file and exploring its structure
Objective: become familiar with loading a PDF document in Python.

Tasks:
- load a PDF file with `PyPDF2`;
- determine the number of pages in the document;
- print the number of each page;
- check whether text can be extracted from the page.

Expected result:
- the student can open a PDF file and read its basic information.

### 2. task: Text extraction from PDF
Objective: extract text from a digitally generated PDF document.

Tasks:
- extract text from a single page;
- extract text from the whole document;
- save the result to a `.txt` file;
- identify the most common words or keywords.

Expected result:
- the student can extract and save PDF text content for further analysis.

### 3. task: Table extraction with `pdfplumber`
Objective: learn how to extract tabular data from a PDF file.

Tasks:
- open a PDF document with `pdfplumber`;
- locate a table in the document;
- convert the table into a list or a `pandas DataFrame`;
- export the result to a `.csv` file.

Expected result:
- the student can extract a table from a PDF and prepare it for analysis.

### 4. task: Checking text and table quality
Objective: evaluate the quality of extracted data.

Tasks:
- compare the PDF content with the extracted result;
- identify paragraph, symbol, or column errors;
- clean extra spaces and blank lines;
- normalize column names.

Expected result:
- the student understands that PDF extraction often requires post-processing.

### 5. task: Applying OCR to a scanned PDF
Objective: become familiar with the use of OCR for processing scanned documents.

Tasks:
- compare a digital PDF and a scanned PDF;
- perform OCR text recognition on a scanned document;
- evaluate the quality of the recognized text;
- identify the most common OCR errors.

Expected result:
- the student understands when OCR is needed and what its limitations are.

### 6. task: Batch processing of multiple PDF files
Objective: automate the processing of multiple PDF documents.

Tasks:
- process all PDF files in a folder;
- for each file, obtain the page count and text or table output;
- save the results in a structured format;
- create a summary table for all files.

Expected result:
- the student can automate PDF file processing in Python.

### 7. task: Mini project
Objective: apply the acquired skills in a complete workflow.

Tasks:
- choose one or more PDF documents;
- determine the most suitable processing approach;
- extract text, tables, or OCR results;
- prepare a short summary of the obtained data.

Expected result:
- the student demonstrates the ability to process PDF documents independently and interpret the results.

## Assessment suggestions
- correct use of Python code;
- ability to choose an appropriate library for a specific PDF type;
- result quality and data cleaning;
- ability to explain the processing workflow and the issues encountered.
