import json
import logging
import sys

def load_data_from_json(path_file):
    try:
        with open(path_file, encoding='utf-8') as json_file:
            data = json.load(json_file)
    except:
        logging.error('Ops ' + str(sys.exc_info()[0]) + ' occured!')
        raise

    return data
