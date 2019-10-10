from flask import Flask, render_template, jsonify
SahersPortfolio = Flask(__name__)

@SahersPortfolio.route('/SahersHome')
def SahersHome():
    return render_template('home.html', name='Saher')

@SahersPortfolio.route('/BookData')
def BookData():
    book = {
        "Pages": 344,
        "Title": "The Great",
        "Author": "JK Rowling",
        "Genre": "Drama"     
    }

    print(book["Author"])

    return jsonify(book)

@SahersPortfolio.route('/AboutMe')
def AboutMe():
    return render_template('aboutme.html', name='Saher', address='123 Chicken')





if __name__ == '__main__':
    SahersPortfolio.run()





    

