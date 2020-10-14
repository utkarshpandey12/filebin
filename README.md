# filebin

Steps to get started

1 git clone\
2 cd filebin\
3 pip install -r requirements.txt ( make sure pip is installed )\
4 python filebin_main.py\
5 Visit http://127.0.0.1:5000/ and see application running\


# Assumptions
Instead of one time clickablity feature expiration time of sharable link is used whose setting can be changed from the main script.\
File type consideration are performed only for images type files of type JPG/PNG format but can be extended to other file formats as well by changing purpose of stripe file create\ 
function inside the python script as per below needs.
<pre># purpose attribute values                      file format supported                     Max file size</pre>\
<<<<<<< HEAD
<pre>purpose  = dispute_evidence                    PDF JPEG PNG                                8MB</pre>\
<pre>purpose = tax_document_user_upload            PDF CSV JPEG PNG XLSX DOCX                  16 MB</pre>\

(more can be referred from scripe docs )

Thanks 
=======
purpose  = dispute_evidence                    PDF JPEG PNG                                8MB\
purpose = tax_document_user_upload            PDF CSV JPEG PNG XLSX DOCX                  16 MB\

(more can be referred from scripe docs )

Thanks 


>>>>>>> 16080e841dfdbe3bf0f0cfbb355fed0b30e43d00
