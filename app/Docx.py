from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
import pyodbc
import pandas as pd
import numpy as np
from chatcompletion import ChatCompletion  
# Create a new Document
doc = Document()


# Add a section with a header
section = doc.sections[0]
header = section.header

# Add a paragraph to the header
paragraph = header.paragraphs[0]

# Add a run to the paragraph and insert an image into it
run1 = paragraph.add_run()
image_path = "D:\AI Automation\AI-Automation\data\KTB-Logo.jpg"
run1.add_picture(image_path, width=Inches(1.5))  # You can adjust the width as needed

# Add a tab character to separate the image from the text
run1.add_text('\t')

# Add another run to the paragraph and insert the text into it
run2 = paragraph.add_run("บันทึก")

#Modified text
run2.font.bold=True
run2.font.size=Pt(24)
# Center the paragraph
paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
# Add another paragraph to the header
paragraph2 = header.add_paragraph("เรื่อง")
paragraph2.style.font.bold=True
paragraph2.style.font.size=Pt(20)

run_paragraph2 =  paragraph2.add_run("\t")
run_paragraph2.add_text("เสนอคณะกรรมการขอทำ Project 10X ให้ประเทศไทยไม่เหมือนเดิมอีกต่อไป")
run_paragraph2.font.bold=False
run_paragraph2.font.size=Pt(16)
# Center the second paragraph
paragraph2.alignment = WD_ALIGN_PARAGRAPH.LEFT 

# Add another paragraph to the header
paragraph3 = header.add_paragraph("ทีม")
paragraph3.style.font.bold=True
paragraph3.style.font.size=Pt(20)

run_paragraph3 =  paragraph3.add_run("\t")
run_paragraph3.add_text("AI Automation")
run_paragraph3.font.bold=False
run_paragraph3.font.size=Pt(16)

# add another paragraph to the header
paragraph4 = header.add_paragraph("______________________________________________________________")
paragraph4.style.font.bold=False

# add heading to the document
content1 = doc.add_paragraph("1.ตัวอย่างการจัดทำเอกสารลองดึงข้อมูลจากฐานข้อมูลและสร้างกราฟแสดงผล")
content1.style.font.bold=True
content1.style.font.size=Pt(16) 

connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:cbdctest.database.windows.net,1433;Database=Transactions;Uid=CloudSA4ab3329e;Pwd=$sremmaH123456;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()



# Create a DataFrame from the data

# Fetch data from the table
cursor.execute('SELECT TOP 5 * FROM Transactions.Events')
data = cursor.fetchall()

# Get column names from the cursor description
column_names = [column[0] for column in cursor.description]

# Create a DataFrame from the data
data = np.array(data)
df = pd.DataFrame(data, columns=column_names)

# Add a table to the document
table = doc.add_table(rows=1, cols=len(column_names))
table.style = 'Table Grid'

# Add the column names to the table
for i, column_name in enumerate(column_names):
    cell = table.cell(0, i)
    cell.text = column_name
    for paragraph in cell.paragraphs:
        for run in paragraph.runs:
            run.font.size = Pt(10)

# Add the data rows to the table
for row_data in data:
    cells = table.add_row().cells
    for i, value in enumerate(row_data):
        cell = cells[i]
        cell.text = str(value)
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(10)

content2 = doc.add_paragraph("2.ตัวอย่างข้อมูลที่ได้จาก OpenAI API")
content2.style.font.bold=True
content2.style.font.size=Pt(16)

   
response = ChatCompletion(f'guess what my data is about {column_names}')
content3 = doc.add_paragraph(f"{response}")
content3.style.font.bold=False
content3.style.font.size=Pt(12)

# Save the document with a .docx extension
doc.save('output1.docx')