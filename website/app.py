import pandas as pd
from flask import Flask, render_template,request

__all__ = ["create_app"]

app = Flask(__name__)

df = pd.read_excel('PARALEL-2023.xlsx', sheet_name="ÖZET") # This is the file and sheet path on your own.
df = df.fillna(0) # Replace Null value => 0

# We updated the columns to 2 digits after the comma with the following 2 codes.
df['PUAN'] = df['PUAN'].map('{:.2f}'.format)
df['Ok Ort.'] = df['Ok Ort.'].map('{:.2f}'.format) 

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/')

    def html_table(): 
        df.index = [i+1 for i in range(len(df))]
        return render_template('index.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
        """The function converts a DataFrame into an ordered HTML table and 
        displays that table in an HTML page using the render_template function.
        """
    return app
