# filebin

Steps to get started

1 git clone\
2 cd filebin\
3 pip install -r requirements.txt ( make sure pip is installed )\
4 python filebin_main.py ( make sure python3+ is installed )\
5 Visit http://127.0.0.1:5000/ and see application running\


# Assumptions
Instead of one time clickablity feature expiration time of sharable link is used whose setting can be changed from the main script. After 5 mins the link stops working.\
File type taken into consideration are PDF CSV JPEG PNG XLSX DOCX. 
A simple app to upload the file and share link with link expiration time set to 5 minutes.\
According to stripe we can configure the value of purpose argument while creating stripe\
files which controls the supported file types and size of files like parameters. 
<pre># purpose attribute values                      file format supported                     Max file size</pre>
<pre>purpose  = dispute_evidence                    PDF JPEG PNG                                8MB</pre>
<pre>purpose = tax_document_user_upload            PDF CSV JPEG PNG XLSX DOCX                  16 MB</pre>

(more can be referred from scripe docs )



