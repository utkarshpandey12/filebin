from flask import *
import stripe
import os
from datetime import datetime
from datetime import timedelta
#test stripe api key
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
# creating flask app object
app = Flask(__name__)

# Upload page Decorator 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  

# Getting URL of uploaded file page decorator 
@app.route('/success', methods = ['POST'])  
def success():
    # Checking if the request type matches as submitted in the form
    if request.method == 'POST':
        # Getting the request files from the home page as files
        f = request.files['file']
        # Saving the file to the folder containing this script
        f.save(f.filename)
        # Opening the file saved 
        with open(f.filename, "rb") as fp:
            # Create file_id from stripe python client 
            resp = stripe.File.create(purpose="dispute_evidence",file=fp)
        # deleting the current file from the directory to avoid name collisions
        #if os.path.exists(f.filename):
        os.remove(f.filename)
        # getting the sharable file url from the file_id to share it with
        # non-stripe users. Expiry time of link can be modified using minutes argument of timedelta
        resp1 = stripe.FileLink.create(file=resp['id'],expires_at=int((datetime.now()+timedelta(minutes=5)).timestamp()))
        # returning the response 
        return {'File_sharable_url':resp1['url'],'file_sharable_link_expiry_time':'5 mins'}  
if __name__ == '__main__':
    # Running the application
    app.run(debug = True)  
