from flask import Flask, render_template, request
from graph import legend2M, legend1M, legend0M, ABlabels, Avalues2M, Avalues1M, Avalues0M, Bvalues2M, Bvalues1M, Bvalues0M, Plabels, Pvalues,svc_data_html, min_data_html
from indicator import basic_function,pivot_function, hazard_function, ppm_function, ffr_function
import pandas as pd 

def html_table(input_table):
    input_table_html=input_table.to_html()
    input_table_html=input_table_html.replace('border="1" class="dataframe"','id="datatablesSimple"' )
    input_table_html=input_table_html.replace('<tr style="text-align: right;">','<tr>')
    input_table_html=input_table_html.replace('<th></th>','<th>No</th>')
    return input_table_html

app = Flask(__name__)

@app.route("/")
def index():
    print(ABlabels)
    return render_template('index.html', ABlabels=ABlabels,
    Avalues2M=Avalues2M, Avalues1M=Avalues1M, Avalues0M=Avalues0M,
    Bvalues2M=Bvalues2M,Bvalues1M=Bvalues1M,Bvalues0M=Bvalues0M,
    legend2M=legend2M, legend1M=legend1M, legend0M=legend0M, min_data_html=min_data_html)

@app.route("/charts")
def charts():
    return render_template('charts.html', ABlabels=ABlabels,
    Avalues2M=Avalues2M, Avalues1M=Avalues1M, Avalues0M=Avalues0M,
    Bvalues2M=Bvalues2M,Bvalues1M=Bvalues1M,Bvalues0M=Bvalues0M,
    Plabels=Plabels,Pvalues=Pvalues,
    legend2M=legend2M, legend1M=legend1M, legend0M=legend0M)

@app.route("/tables")
def tables():
    return render_template('tables.html',svc_data_html=svc_data_html)

@app.route("/layout_static")
def layout_static():
    return render_template('layout-static.html')

@app.route("/layout_sidenav")
def layout_sidenav():
    return render_template('layout-sidenav-light.html')

@app.route("/quality",methods=["POST","GET"])
def quality():
    if request.method=='POST':
        #pivot chart
        input_data=request.form.getlist('symptom')
        sort_pivot=pivot_function(input_data)
        sort_pivot_html=html_table(sort_pivot)

        # value=hazard_function(['PCB','EXTERIOR']) 
        # print(value)

    # original total symptoms
    input_data=["DRAIN","EXPLANATION","EXTERIOR","FILLING","LEAK","LID","MISASSEMBLY","MOTOR","NOISE/VIBRATION","OTHER","PCB","RETURN"]
    
    # pivot chart_original
    sort_pivot=pivot_function(input_data)
    sort_pivot_html=html_table(sort_pivot)

    # hazard graph_original
    hazard_table=hazard_function(input_data).style.hide_index()
    print(hazard_table[3])

    return render_template('quality.html',sort_pivot_html=sort_pivot_html,hazard_table=hazard_table)

if __name__ == "__main__":
    app.run(debug=True)