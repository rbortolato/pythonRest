from flask import Blueprint, jsonify
from myApp.controller.premiacao import getPremiacao

premiosEndpoint = Blueprint('premio', __name__)

@premiosEndpoint.route('/premio')
def getPremio():
    return jsonify(getPremiacao())