from flask import Flask, request, jsonify, make_response
from app import app, data, helper


@app.route('/api/v1/recommendation/', methods=['GET'])
def get_recommendation():
    get_sku = request.args.get('sku')
    get_accuracy = request.args.get('accuracy')

    err_sku = helper.check_sku(get_sku)
    if err_sku:
        return make_response(err_sku)

    err_accuracy = helper.check_accuracy(get_accuracy)
    if err_accuracy:
        return make_response(err_accuracy)

    result = []
    if get_accuracy:
        for accuracy, recom in data.RECOMENDATIONS[get_sku].items():
            if float(accuracy) >= float(get_accuracy):
                result.append(recom)
    else:
        for _, recom in data.RECOMENDATIONS[get_sku].items():
            result.append(recom)

    return jsonify(result)


@app.errorhandler(404)
def not_found(error):
    return make_response('Page not found', 404)


@app.errorhandler(500)
def internal_error(error):
    return make_response('Server error', 500)
