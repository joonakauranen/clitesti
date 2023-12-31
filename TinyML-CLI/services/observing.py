import json
import time

from pandas import json_normalize
import openapi_client
from openapi_client.apis.tags import observing_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.observation import Observation
from pprint import pprint
from rich import print


def observe_device_on_bridge(configuration):
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = observing_api.ObservingApi(api_client)

        path_params = {
            'bridge_id': 3,
            'device_id': 5,
        }
        try:
            print("Image is target:             Image is not target:")
            for i in range(0,2):
                time.sleep(0.5)
                
                # Observe Device On Bridge
                api_response = api_instance.observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get(
                    path_params=path_params,
                )
                
                data = api_response.response.data
                data_json = json.loads(data)
                data_dataframe = json_normalize(data_json)
                #Print the whole dataframe:
                #print(data_dataframe)

                #Print predictions only:
                val = data_dataframe['observation_value.1'].values[0]
                val2 = data_dataframe['observation_value.0'].values[0]
                val_formatted = str(val)
                val2_formatted = str(val2)
                print(f'[green]{val_formatted}[/]                          [red]{val2_formatted}[/]')
        except openapi_client.ApiException as e:
            print("Exception when calling ObservingApi->observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get: %s\n" % e)