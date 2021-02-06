from flask import Flask, render_template, redirect, url_for, request, session
import game
import random

app = Flask(__name__)
global categories
global letters
global roundNum
roundNum = 0
global listLength
listLength = 0

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/mode")
def mode():
    return render_template("mode.html")

@app.route("/playOne", methods=["GET", "POST"])
def playOne():
    global categories
    global letters
    global roundNum
    global listLength
    global roundCategories
    global roundLetter

    if request.method == "POST":
        print("does it do this again?")
        family = request.form['fam']
        categories = game.getGameList(family)
        print(game.getGameList("true"))
        allLet = request.form['all']
        letters = game.getLetterGroup(allLet)

    return categories

@app.route("/play")
def play():
    global roundNum

    roundNum += 1
    roundColor = game.getRoundColor()
    roundCategories = getTen()
    roundLetter = random.choice(letters).upper()
    data = {'listLength':len(categories),'roundColor': roundColor, 'round': roundNum, 'categories' : roundCategories, 'letter' : roundLetter}
    return render_template("play.html", data=data)

@app.route("/done")
def done():
    print(len(categories))
    return render_template("done.html")

def getTen():
    roundList = []
    global listLength
    global categories
    listLength = len(categories)
    if listLength < 10:
        return []
    for i in range(10):
        print("LIST LENGTH: " + str((len(categories))))
        index = random.randint(0,listLength-1)
        cat = categories[index]
        while cat in roundList:
            index = random.randint(0,listLength-1)
            cat = categories[index] 
        roundList.append(cat)
        categories.remove(cat)
        listLength = listLength - 1
    return roundList






if __name__ == "__main__":
  app.run(debug=True)
