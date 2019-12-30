from flask import Flask, Response, request, redirect, url_for, jsonify
from flask import render_template
import json, csv
import helpers
import io
from flask import make_response

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return app.send_static_file('index.html')

    elif request.method == 'POST':
        year = request.form['year']
        month = request.form['month']
        day = request.form['day']

        date = str(year) + '-' + str(month) + '-' + str(day)

        result = request.form['shop_sale_details']
        processedData = helpers.processData(result, date)

        filename = processedData['filename']
        row_list = processedData['data']

        contentDisposition = "attachment; filename="+filename

        si = io.StringIO()
        writer =  csv.writer(si, dialect='excel')
        writer.writerows(row_list)

        output = make_response(si.getvalue())
        output.headers["Content-Disposition"] = contentDisposition
        output.headers["Content-type"] = "text/csv"
        return output


@app.route('/ice', methods=['GET', 'POST'])
def ice():
    if request.method=="GET":
        return redirect(url_for('static', filename='ice.html'))

@app.route('/ice-new', methods=['GET', 'POST'])
def ice2():
    if request.method=="GET":
        return app.send_static_file('ice.html')


def createCSV(file_name, row_list):

    fileName = '/output/'+file_name

    with open(file_name, 'w', newline='') as csvfile:
        writer =  csv.writer(csvfile)
        writer.writerows(row_list)

def generateCSV(file_name, row_list):
        si = io.StringIO()
        writer =  csv.writer(si, dialect='excel')
        writer.writerows(row_list)

        output = make_response(si.getvalue())
        output.headers["Content-Disposition"] = "attachment; filename="+file_name
        output.headers["Content-type"] = "text/csv"
        return output
