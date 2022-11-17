#-------------------------------------------------------------------------------
# Name:        Add Metadata to Different PDFs in a Predefined-Folder
# Purpose:      For applying specific metadata to PDF files with specific naming
#                   syntaxes. The metadata is copied from preproduced PDFs.  
#
# Author:      Daniel Raleigh
#
# Created:     16 November 2022
# Copyright:   (c) daraleig 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------




import os,time,datetime,PyPDF2
from datetime import date, timedelta
from PyPDF2 import PdfFileReader, PdfFileMerger

# Date Management
start_time = time.time()
today = date.today()
today_year = today.year
today_month = today.month
today_day = today.day
today_year_str = today.strftime("%Y")
today_month_str = today.strftime("%m")
today_day_str = today.strftime("%d")
today_full_str = today_year_str + today_month_str + today_day_str
print(today_full_str)


# Define Data Locations and Other Variables

PDF_Folder = r"folderpath"                                              # folder path for the PDFs to which metadata will be added
Metadata_A = r"path\A_Metadata.pdf"                                     # PDF with the proper metadata for the "A" PDFs
Metadata_B = r"path\B_Metadata.pdf"                                     # PDF with the proper metadata for the "B" PDFs
Metadata_C = r"path\C_Metadata.pdf"                                     # PDF with the proper metadata for the "C" PDFs

# Set folder, produce list of PDFs that will receive metadata
PDFs_List = []
os.chdir(PDF_Folder)
PDFs_List = os.listdir(PDF_Folder)
for i in range(len(PDFs_List)):
    print(PDFs_List[i])

# Apply metadata to constituent files:
for file in PDFs_List:                                                                  # iterate over the list of PDFs
    if file.endswith("_A.pdf"):                                                         # set up an IF statement to select files in the list that end with "_A.pdf")
        print('adding metadata to this *type of* PDF: {}'.format(file))                 # set up a print statement to denote which file name ('file') will have the correct metadata added to it                
        PDFReader = PyPDF2.PdfFileReader(open(file, 'rb'))                              # pass the PdfFileReader object the iterated file that's opened in read binary mode (skipping the step to store the opened file in a FileObject); store the PdfFileReader object in 'PDFReader' for this code block
        AMReader = PyPDF2.PdfFileReader(open(Metadata_A, 'rb'))                         # pass the PdfFileReader object the previously-defined PDF document with the appropriate metadata that is opened in read binary mode (skipping the step to store the opened file in a FileObject); store the PdfFileReader object in 'AMReader' for this code block
        A_Metadata = AMReader.getDocumentInfo()                                         # define a variable to hold metadata information from the metadata PDF
        ApdfWriter = PyPDF2.PdfFileWriter()                                             # create a new PdfFileWriter object
        ApdfWriter.addMetadata(A_Metadata)                                              # add metadata to the PdfFileWriter from the associated metadata variable
        for pageNum in range(PDFReader.numPages):                                       # set up a FOR loop to iterate over all pages in the PDFReader object
            APageObj = PDFReader.getPage(pageNum)                                       # get the Page object by calling getPage() on the PdfFileReader object
            ApdfWriter.addPage(APageObj)                                                # for each of those iterated page Objects, pass the Page object to the PdfFileWriter's addPage() method
        ApdfOutput = open(file[:-4]+"_"+today_full_str+".pdf", 'wb')                    # set up an output file to take the last 4 digits off the end of the file name and add a space with the string date and the file extension 
        ApdfWriter.write(ApdfOutput)                                                    # task the PdfFileWriter to pass the File object to the write() method
        ApdfOutput.close()                                                              # close the Output file

    elif file.endswith("_DPAs.pdf"):                                                    # set up an IF statement to select files in the list that end with "_DPAs.pdf")
        print('adding metadata to this *type of* PDF: {}'.format(file))                 # set up a print statement to denote which file name ('file') will have the correct metadata added to it                
        PDFReader = PyPDF2.PdfFileReader(open(file, 'rb'))                              # pass the PdfFileReader object the iterated file that's opened in read binary mode (skipping the step to store the opened file in a FileObject); store the PdfFileReader object in 'PDFReader' for this code block
        BMReader = PyPDF2.PdfFileReader(open(Metadata_B, 'rb'))                         # pass the PdfFileReader object the previously-defined PDF document with the appropriate metadata that is opened in read binary mode (skipping the step to store the opened file in a FileObject); store the PdfFileReader object in 'BMReader' for this code block
        B_Metadata = BMReader.getDocumentInfo()                                         # define a variable to hold metadata information from the metadata PDF
        BpdfWriter = PyPDF2.PdfFileWriter()                                             # set up a PdfFileWriter by name
        BpdfWriter.addMetadata(B_Metadata)                                              # add metadata to the PdfFileWriter from the associated metadata variable
        for pageNum in range(PDFReader.numPages):                                       # set up a FOR loop to iterate over all pages in the PDFReader object
            BPageObj = PDFReader.getPage(pageNum)                                       # get the Page object by calling getPage() on the PdfFileReader object
            BpdfWriter.addPage(BPageObj)                                                # for each of those iterated page Objects, pass the Page object to the PdfFileWriter's addPage() method
        BpdfOutput = open(file[:-4]+"_"+today_full_str+".pdf", 'wb')                    # set up an output file to take the last 4 digits off the end of the file name and add a space with the string date and the file extension 
        BpdfWriter.write(BpdfOutput)                                                    # task the PdfFileWriter to pass the File object to the write() method
        BpdfOutput.close()                                                              # close the Output file            

    elif file.endswith("_Winter22_23.pdf"):                                             # set up an IF statement to select files in the list that end with "_Winter22_23.pdf")
        print('adding metadata to this *type of* PDF: {}'.format(file))                 # set up a print statement to denote which file name ('file') will have the correct metadata added to it                
        PDFReader = PyPDF2.PdfFileReader(open(file, 'rb'))                              # pass the PdfFileReader object the iterated file that's opened in read binary mode (skipping the step to store the opened file in a FileObject); store the PdfFileReader object in 'PDFReader' for this code block
        CMReader = PyPDF2.PdfFileReader(open(Metadata_C, 'rb'))                         # pass the PdfFileReader object the previously-defined PDF document with the appropriate metadata that is opened in read binary mode (skipping the step to store the opened file in a FileObject); store the PdfFileReader object in 'WbDPAMReader' for this code block
        C_Metadata = CMReader.getDocumentInfo()                                         # define a variable to hold metadata information from the metadata PDF
        CpdfWriter = PyPDF2.PdfFileWriter()                                             # set up a PdfFileWriter by name
        CpdfWriter.addMetadata(C_Metadata)                                              # add metadata to the PdfFileWriter from the associated metadata variable
        for pageNum in range(PDFReader.numPages):                                       # set up a FOR loop to iterate over all pages in the PDFReader object
            CPageObj = PDFReader.getPage(pageNum)                                       # get the Page object by calling getPage() on the PdfFileReader object
            CpdfWriter.addPage(CPageObj)                                                # for each of those iterated page Objects, pass the Page object to the PdfFileWriter's addPage() method
        CpdfOutput = open(file[:-4]+"_"+today_full_str+".pdf", 'wb')                    # set up an output file to take the last 4 digits off the end of the file name and add a space with the string date and the file extension 
        CpdfWriter.write(CpdfOutput)                                                    # task the PdfFileWriter to pass the File object to the write() method
        CpdfOutput.close()                                                              # close the Output file                                                    


# Display time taken just for fun:
print('This script took %s seconds...' % (time.time() - start_time))