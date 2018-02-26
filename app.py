from flask import Flask
 
app = Flask(__name__)
 
 
@app.route('/') 
def anasayfa():
 return 'Merhaba Dünya';
 
@app.route('/hakkimizda')
def hakkimizda():
 return 'Hakkımızda Sayfası';
 
 
 
if __name__ == '__main__':
 app.run(debug=True)
