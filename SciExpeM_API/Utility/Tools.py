import SciExpeM_API.settings as settings
import SciExpeM_API.Utility.RequestAPI as rAPI
from SciExpeM_API.Models import *
import json


def getProperty(model_name, element_id, property_name):
    params = {'model': model_name, 'id': element_id, 'property': property_name}

    address = 'ExperimentManager/API/requestProperty'

    request = rAPI.RequestAPI(ip=settings.IP,
                              port=settings.PORT,
                              address=address,
                              token=settings.TOKEN,
                              mode=rAPI.HTTP_TYPE.POST,
                              secure=settings.SECURE,
                              params=params)
    return json.loads(request.requests.text) if json.loads(request.requests.text) != '' else None


def optimize(database, model_name, text):
    # print(model_name, text)
    model = eval(model_name)
    tmp = [model.from_dict(element) for element in json.loads(text)]
    result = []

    for element in tmp:
        attribute = getattr(database, model_name)
        if element.id in attribute:
            result.append(attribute[element.id])
        else:
            attribute[element.id] = element
            result.append(element)
    return result


# def create
