from flask import Flask, render_template
import xmltodict, json

app = Flask(__name__)

# GET is default
@app.route('/')
def test_jstree():
    return render_template('jstree.html')

@app.route('/json')
def test_json():
    with open('test_data/Practice.xml') as xml_file:
    #with open('test_data/mtrobin.tmpl.xml') as xml_file:
        my_dict=xmltodict.parse(xml_file.read())
        xml_file.close()
        json_data = json.dumps(my_dict)

        return json_data
