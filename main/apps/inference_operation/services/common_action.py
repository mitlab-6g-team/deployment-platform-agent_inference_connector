from main.apps.inference_operation.services.central_operation import ModelFileGeter
from main.apps.inference_operation.services.central_operation import InferenceFileGeter

def download_file(model_uid_str):
    payload_dict = {'model_uid': model_uid_str}
    ModelFileGeter.download(payload_dict)

    payload_dict = {'model_uid': model_uid_str}
    InferenceFileGeter.download(payload_dict)
    