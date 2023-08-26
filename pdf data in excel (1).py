#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install PyPDF2


# In[ ]:


pip install tabula


# In[ ]:


pip install pdfplumber


# # (Table Extraction) universal

# In[ ]:


import pdfplumber
import pandas as pd

pdf_path = 'www.pdf'  # Replace with the actual path to your PDF file

# Create an empty DataFrame to hold all extracted tables
master_df = pd.DataFrame()

# Loop through pages, extract data, and append to the master DataFrame
with pdfplumber.open(pdf_path) as pdf:
    num_pages = len(pdf.pages)
    for page_number in range(num_pages ):
        page = pdf.pages[page_number]
        table = page.extract_table()
        
        if table:
            # Convert the extracted table into a pandas DataFrame
            df = pd.DataFrame(table)
            
            # Append the DataFrame to the master DataFrame
            master_df = master_df.append(df, ignore_index=True)
            
        
        else:
            print(f"No table found on page {page_number + 1}")

# Save the master DataFrame to an Excel file
excel_filename = 'a_Tables.xlsx'
master_df.to_excel(excel_filename, index=False)

print(f"All tables saved to {excel_filename}")


# # (Table Extraction) single file page

# In[ ]:


import pdfplumber
import pandas as pd

pdf_path = 'www.pdf'  # Replace with the actual path to your PDF file

# Create an empty DataFrame to hold all extracted tables
master_df = pd.DataFrame()

# Loop through pages, extract data, and append to the master DataFrame
with pdfplumber.open(pdf_path) as pdf:
    num_pages = int(input())
    for page_number in range(num_pages , num_pages+1):
        page = pdf.pages[page_number]
        table = page.extract_table()
        
        if table:
            # Convert the extracted table into a pandas DataFrame
            df = pd.DataFrame(table)
            
            # Append the DataFrame to the master DataFrame
            master_df = master_df.append(df, ignore_index=True)
            
        
        else:
            print(f"No table found on page {page_number + 1}")

# Save the master DataFrame to an Excel file
excel_filename = 'Tables.xlsx'
master_df.to_excel(excel_filename, index=False)

print(f"All tables saved to {excel_filename}")


# # pdfplumber
pdfplumber is a Python library used for extracting data from PDF documents.
It provides a way to access and extract text, tables, and images from PDF files.


                               (Text Extraction)
    
You can use pdfplumber to extract plain text content from PDFs, 
allowing you to access and work with the textual information present in the document.

                               (Table Extraction)
    
pdfplumber is particularly useful for extracting tabular data from PDFs.
It can detect tables in PDF documents and provide methods to convert 
them into structured data that you can work with using tools like pandas.

                               (Image Extraction)
    
While its primary focus is on text and table extraction,
pdfplumber can also help extract images or figures embedded within PDF documents.

                               (Page Information)
    
You can obtain metadata about each page, such as its dimensions, rotation, and other properties.

                               (Page-to-Image Conversion)
    
It can convert individual pages of a PDF into images for further analysis or display.



pdfplumber is useful for a variety of tasks such as data extraction for analysis, data transformation for reporting, 
and data migration from PDFs to other formats like CSV, Excel, or databases.

# # (Text Extraction)

# In[ ]:


import pdfplumber

pdf_path = 'newdata.pdf'  # Replace with the actual path to your PDF file

# Create a text file to hold the extracted text
text_filename = 'extracted_text.txt'

# Loop through pages, extract text, and append to the text file
with pdfplumber.open(pdf_path) as pdf:
    num_pages = len(pdf.pages)
    
    with open(text_filename, 'w', encoding='utf-8') as text_file:
        for page_number in range(num_pages):
            page = pdf.pages[page_number]
            text = page.extract_text()
            
            text_file.write(f"Page {page_number + 1}:\n")
            text_file.write(text)
            text_file.write("\n\n")

print(f"Extracted text saved to {text_filename}")


# # (Image Extraction)

# In[ ]:


pip install PyMuPDF


# In[ ]:


import fitz
import os

pdf_path = 'data.pdf'  # Replace with the actual path to your PDF file

# Create a folder to save the extracted images
image_folder = 'extracted_images'
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Loop through pages, extract images, and save them
for page_number in range(pdf_document.page_count):
    page = pdf_document[page_number]
    image_list = page.get_images(full=True)
    
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        
        # Save the image
        image_filename = f"{image_folder}/page_{page_number + 1}_img_{img_index + 1}.png"
        with open(image_filename, "wb") as image_file:
            image_file.write(image_bytes)

pdf_document.close()

print("Images extracted and saved successfully.")


# #                           (Page Information)

# In[ ]:


import fitz
import os

pdf_path = 'data.pdf'  # Replace with the actual path to your PDF file

# Create a folder to save the extracted images
image_folder = 'extracted_images'
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Loop through pages, extract images, display page info, and save images
for page_number in range(pdf_document.page_count):
    page = pdf_document[page_number]
    image_list = page.get_images(full=True)
    
    # Display page information
    print(f"Page {page_number + 1} Info:")
    print(f"Dimensions: {page.rect.width:.2f} x {page.rect.height:.2f} points")
    print(f"Rotation: {page.rotation}")
    
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        
        # Save the image
        image_filename = f"{image_folder}/page_{page_number + 1}_img_{img_index + 1}.png"
        with open(image_filename, "wb") as image_file:
            image_file.write(image_bytes)

pdf_document.close()

print("Images extracted and saved successfully.")


# #  (Page-to-Image Conversion)

# In[ ]:


import fitz
import os

pdf_path = 'newdata.pdf'  # Replace with the actual path to your PDF file

# Create a folder to save the extracted images
image_folder = 'extracted_images'
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Loop through pages, convert pages to images, and save images
for page_number in range(pdf_document.page_count):
    page = pdf_document[page_number]
    
    # Convert the page to a pixmap
    pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # You can adjust the matrix scale as needed
    
    # Save the pixmap as an image
    image_filename = f"{image_folder}/page_{page_number + 1}.png"
    pixmap.save(image_filename, "png")

pdf_document.close()

print("Pages converted to images and saved successfully.")


# In[ ]:




