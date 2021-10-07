from flask import Flask
from flask.templating import render_template
from datetime import datetime
from source_csv.pm25 import get_pm25
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', **locals())


@app.route('/sum/x=<int:x>&y=<int:y>')
def get_sum(x,y):
    return f'total:{eval(x)+eval(y)}'

@app.route('/test')
def test():
    name = 'jerry'
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # return render_template('index.html', **locals())

    return render_template('index.html', data = {'name':name, 'time':time})

@app.route('/today/<string:name>')
def getToday(name):
    
    print(datetime.now())
    return name + " "+ datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@app.route('/stock')
def stock():
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    stocks=[
        {'分類': '日經指數', '指數': '22,920.30'},
        {'分類': '韓國綜合', '指數': '2,304.59'},
        {'分類': '香港恆生', '指數': '25,083.71'},
        {'分類': '上海綜合', '指數': '3,380.68'}
    ]
    return render_template('stock.html',stocks=stocks, time=time)



@app.route('/pm25')
def pm25():
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    columns, datas = get_pm25(sort=True)
    return render_template('pm25.html', **locals())

@app.route('/echarts')
def echarts():
    return render_template('echarts.html')

@app.route('/pm25-echarts')
def pm25_echarts():
    return render_template('pm25-echarts.html')

@app.route('/pm25-data', methods=['GET','POST'])
def pm25_data():
    columns, datas=get_pm25()
    sites, values=[],[]
    for data in datas:
        sites.append(data[0])
        values.append(data[-1])
    data = {'sites':sites, 'values':values}
    
    return json.dumps(data, ensure_ascii=False)



if __name__=='__main__':
    app.run(debug=True)