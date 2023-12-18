import pickle
from flask import Flask, render_template, request, jsonify
import numpy as np


app = Flask(__name__ , static_url_path='/static')

def get_data(): 
       year = 2000,2001, 2002, 2003, 2004, 2005, 2006,2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,2015,
       status = 'Developed', 'Developing',
       adultmortality = 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
       alcohol = 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5,20,
       hepatitisB =1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
       measles = int(request.form['measles']) if 'measles' in request.form else 0, 
       bmi =1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
       underFiveDeaths =0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250,
       polio =1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
       totalExpenditure =0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20,
       diphtheria =1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
       hivAids =1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
       gdp = int(request.form['gdp']) if 'gdp' in request.form else 0,
       population = int(request.form['population']) if 'population' in request.form else 0, 
       thinness1to19Years = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
       incomeComposition =0,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1,
       schooling =1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
       return {
            'year': year,
            'status': status,
            'adultmortality': adultmortality,  
            'alcohol': alcohol,
            'hepatitisB': hepatitisB,  
            'measles': measles,
            'bmi': bmi,
            'underFiveDeaths': underFiveDeaths,  
            'polio': polio,
            'totalExpenditure': totalExpenditure,  
            'diphtheria': diphtheria,
            'hivAids': hivAids,  
            'gdp': gdp,
            'population': population,
            'thinness1to19Years': thinness1to19Years,  
            'incomeComposition': incomeComposition,  
            'schooling': schooling
       }

@app.route('/', methods=['GET', 'POST'])
def home():
       data = get_data()
       if request.method == 'POST':
               return render_template("index.html", **data )
       else:
              return render_template("index.html", **data)

@app.route('/predict/', methods=['POST'])
def predict():
       if request.method == 'POST':
              year_val = int(request.form['year'])
              status_val = str(request.form['status'])
              adultmortalityVal = float(request.form['adultmortality'])
              alcoholVal = float(request.form['alcohol'])
              hepatitisBVal = float(request.form['hepatitisB'])
              measlesVal = float(request.form['measles'])
              bmiVal = float(request.form['bmi'])
              underFiveDeathsVal = float(request.form['underFiveDeaths'])
              polioVal = float(request.form['polio'])
              totalExpenditureVal = float(request.form['totalExpenditure'])
              diphtheriaVal = float(request.form['diphtheria'])
              hivAidsVal = float(request.form['hivAids'])
              gdpVal = float(request.form['gdp'])
              populationVal = float(request.form['population'])
              thinness1to19YearsVal = float(request.form['thinness1to19Years'])
              incomeCompositionVal = float(request.form['incomeComposition'])
              schoolingVal = float(request.form['schooling'])

              yearVal = int(year_val) - 2000
              statusVal = 0 if status_val.lower() == 'developed' else 1
              data = [[yearVal, statusVal, adultmortalityVal, alcoholVal,
                            hepatitisBVal, measlesVal, bmiVal, underFiveDeathsVal, polioVal, totalExpenditureVal,
                            diphtheriaVal, hivAidsVal, gdpVal, populationVal, thinness1to19YearsVal,
                            incomeCompositionVal, schoolingVal]]
              model = pickle.load(open('model/RFRegressorTrained.pkl', "rb"))
              prediction = model.predict(data)[0]
              return render_template("predict.html", prediction=float(prediction))

if __name__ == '__main__':
    app.debug = True
    app.run(
        host='0.0.0.0',
        port=7860,
        debug=True)
