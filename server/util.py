import json
import numpy as np
import pickle

__data_columns = None
__locations = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        location_index = __data_columns.index(location.lower())
    except:
        location_index = -1

    X = np.zeros(len(__data_columns))
    X[0] = sqft
    X[1] = bhk
    X[2] = bath
    if location_index >= 0:
        X[location_index] = 1

    estimated_price = __model.predict([X])[0]
    print(round(estimated_price, 2))
    return round(estimated_price, 2)


def get_location_names():
    return __locations


def load_saved_artifacts():
    print('Loading saved artifacts ...')
    global __data_columns
    global __locations
    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
    __locations = __data_columns[3:]
    print('Locations loaded successfully')

    global __model
    with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as fm:
        __model = pickle.load(fm)
    print("Model loaded successfully")

    return __model


if __name__ == "__main__":
    load_saved_artifacts()
    # print(get_location_names())
    get_estimated_price('1st block jayanagar', 200.0, 3, 3)
