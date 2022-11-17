This repository contains (or will contain) a collection of scripts for manipulating or editing PDF metadata. These script(s) have been tweaked to allow anyone to utilize them and adjust the file sources and variable names for their personal use.

"copy_metadata_to_specific_PDFs.py" (Packages Required: os, time, datetime, PyPDF2)

Issue: Up through the winter of 2021-22, I had used a .xmp file to apply metadata to PDFs produced by a separate script. There must have been some changes to Adobe Acrobat in the interim (prior to the winter of 2022-23), so I needed to find a way to avoid adding the metadata by manually copying/pasting the information to the Properties of each PDF document I produced. 

Solution:
1. 
This script defines the folder path of the folder with the new PDFs and the file paths of the separate PDFs which have the distinct metadata information which will be applied to specific PDFs. 

2. 
For small or large collections of PDFs, a list of the PDF files in the denoted folder is produced and appended in an iteration. 

3. 
A FOR loop iterates over the PDF list and copies metadata from the appropriate metadata-PDFs to add to their constituent PDFs which require the additions. 
