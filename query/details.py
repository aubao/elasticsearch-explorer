from flask import request,Blueprint
import json
from db import *

details_module = Blueprint('details_module', __name__)

@details_module.route('/details', methods=['POST'])
def details():
	if request.method == 'POST':
		db_index = request.form['db_index']
		db_doctype = request.form['db_doctype']
		word = request.form['max_docs']
                print word
       		q = {
    "query": {
        "match": {
            "author": word
        }
    }
}		
		res = es_search(q,False)
                return json.dumps(res["hits"])
