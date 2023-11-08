from flask import Flask, request, jsonify
import index
app = Flask(__name__)


@app.route('/whatsapp_business', methods=["POST"])
def whatsapp_business():
     input_json = request.get_json(force=True) 
     business_name = index.get_whatsapp_business_name(input_json['number'])
     dictToReturn = {'result': business_name}
     return jsonify(dictToReturn)