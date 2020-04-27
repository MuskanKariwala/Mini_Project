from flask import Flask, request, render_template
import pandas as pd
import os
UPLOAD_FOLDER = 'C:/Users/Muskan/Desktop/uploads'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():

	#if request.method=='POST':

      file = request.files['file']
      df = pd.read_csv(file)
      print(type(df))
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
      #file.open(os.path.join(app.config['UPLOAD_FOLDER'], "hello"))

      #return render_template("index.html", message="File uploaded successfully")
      return render_template('index.html', data = df.head(15).to_html(), title= 'The Mammogram Dataset', shape = ' Number of rows and columns available in the dataset: {}'.format(df.shape))
      
    #return render_template("index.html", message="Upload")


@app.route('/fill', methods=['GET','POST'])
def fill():
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)