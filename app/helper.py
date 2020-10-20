from app import data

ERROR_SKU = 'Invalid sku parameter'
ERROR_ACCURACY = 'Invalid accuracy parameter'


def check_sku(sku):
    if not sku or sku not in data.RECOMENDATIONS.keys():
        return ERROR_SKU
    return None


def check_accuracy(accuracy):
    if accuracy:
        try:
            float(accuracy)
        except ValueError:
            return ERROR_ACCURACY
    return None
