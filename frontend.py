from flask import Flask, render_template, request, send_from_directory
import tes as tes

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        return render_template('awal.html')
    else:
        return render_template('awal.html')

@app.route('/rekomendasi', methods = ['POST', 'GET'])
def rekomendasi():
    if request.method == 'POST':
        input = request.form

        favorit = tes.favorite_restaurant(input['name']).iloc[0]

        rek_resto = tes.restaurant_recommendation(input['name'])

        rek_cuisines = tes.cuisines_recommendation(input['name'])
        
        rek_features = tes.features_recommendation(input['name'])

        rek_type = tes.type_recommendation(input['name'])


        return render_template('output.html',
            input=input, favorit=favorit, 
            len_cui=len(rek_cuisines), rek_cuisines=rek_cuisines, 
            rek_features=rek_features, 
            rek_resto=rek_resto,
            rek_type=rek_type)

# @app.route('/images/<path:path>')
# def static_file(path):
#     return send_from_directory('images', path)

if __name__ == "__main__":
    app.run(debug=True)