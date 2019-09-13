from flask import Flask, render_template, jsonify
SahersPortfolio = Flask(__name__)

@SahersPortfolio.route('/SahersHome')
def SahersHome():
    return render_template('home.html', name='Saher')

@SahersPortfolio.route('/NameData')
def NameData():
    names = {'Name':'Bob',
    'Occupation':'Chicken'}
    print(names{'Occupation'})

    return jsonify(names)



if __name__ == '__main__':
    SahersPortfolio.run()

    Lists = ['Mary', 'Kim', 'John']
    print (Lists[0]) 





    

