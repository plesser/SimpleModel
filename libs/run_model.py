import json
import logging
from lxml import etree
from . import calculate_model


def parse(data):
    mapa = {}
    res = "1975"
    type_out = ''

    model = ''
    client_data = {}

    try:
        #print('json')
        mapa = json.loads(data)

        model = mapa['model']
        client_data = mapa['data']

        type_out = 'json'
    except ValueError as e:
        logging.error('json ' + str(e))
        # значит у нас не json а xml
        model, client_data = parse_xml(data)
        type_out = 'xml'


    logging.debug(type_out)
    logging.debug(model)
    logging.debug(client_data)

    #print('running', model, client_data)

    #print(client_data)
    if model == 'auto_base':
        predict = calculate_model.run_dict(client_data)
        #print(predict)

    return res

def parse_xml(data):
    mapa = {}
    model = ""

    #root = ET.fromstring(str(data))
    parser = etree.XMLParser(recover=True)
    root = etree.fromstring(data, parser=parser)

    for child in root:
        #print(child.tag, child.text)
        if child.tag == 'model':
            model = child.text
        elif child.tag == 'data':
            for dchild in child:
                mapa[dchild.tag] = dchild.text

    return model, mapa

def process_score(request):
    logging.basicConfig(filename='ws.log', filemode='w+', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

    if request.method == 'POST':
        #print('POST')
        data = request.get_data()
        parse(data)
    else:
        return 'error', 400
    return '1975\n'


