from flask import Flask, render_template, url_for, request

app = Flask(__name__)



    

players_dict = {}


    


@app.route("/home", methods=['GET','POST','PUT'])
def home():

    return render_template('home.html')

@app.route("/new-game", methods=['GET','POST'])
def new_game():

    players = int(request.args['nplayers'])

    return render_template('new-game.html', players=players)

@app.route("/game-play", methods=['GET', 'POST'])
def game_play():

    round = int(request.args['round_num'])
    
    if round == 0:
        print('TRUE')
        players = [x.title() for x in list(dict(request.args).values()) if x != str(round)]

        for p in players:
            players_dict[p] = {
                "starting_score":0,
                "current_score":0,
                "previous_score":0
            }
        

    else:
        players = list(players_dict.keys())
        scores = dict(request.args)
        print(players_dict)
        print(request.args)
        
        for p in players:
            players_dict[p]['previous_score'] = players_dict[p]['current_score']
            print(p)
            print(f"{int(scores[f'{p}-blitz-pile'])*-2} + {scores[f'{p}-dutch-pile']} + {players_dict[p]['previous_score']}")
            players_dict[p]['current_score'] = (int(scores[f'{p}-blitz-pile'])*-2) + int(scores[f'{p}-dutch-pile']) + int(players_dict[p]['previous_score'])

        print(players_dict)
    return render_template("score_card.html", players_dict = players_dict, players = players, round = round)


app.run(debug = True)