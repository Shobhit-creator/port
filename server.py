from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_html>')
def html_page(page_html):
    return render_template(page_html)

def write_to_file(data):
    with open("database.txt", mode='a') as database:
            email   = data['email']
            subject = data['subject']
            message = data['message']
            database.write(f"\n{email},{subject},{message}")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
      except:  
        return 'did not save to database'
    else:
        return 'something went wrong. Try again!'

def write_to_csv(data):
    with open("database.csv", newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        
@app.route('/blog')
def blog():
    return 'These are my thoughts on blog'

@app.route('/2020/dogs')
def dogs():
    return 'this is my blog'

