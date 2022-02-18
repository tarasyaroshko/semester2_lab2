from flask import Flask, request, render_template
import map
import locations
app = Flask(__name__, template_folder="templates")


@app.route('/', methods=["GET", "POST"])
def index():
   return render_template('index.html')

app.run(debug=True)

@app.route('/map')
def map_generation():
    # print(request.args.get('name'))
    map.create_map(locations.get_friends_locations(request.args.get('name'), request.args.get('number')))
    return render_template('Map.html')
