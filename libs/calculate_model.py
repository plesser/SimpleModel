import sys
import dill as pickle
import pandas as pd
import os

def run_dict(client_data):
    try:
        del client_data['runId']
        #print(client_data)
        #print(os.getcwd())
        sys.path.append(os.getcwd() + '/libs')

        with open('./libs/models/model_base_card.pickle', 'rb') as model_p:
            model = pickle.load(model_p)

        df = model.transform(pd.DataFrame(data=client_data))

        return df
    except:
        print(sys.exc_info()[0])
        return None

