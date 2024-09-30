import os
from dotenv import load_dotenv
from dataclasses import dataclass

# Initialization
load_dotenv(".env.common")
load_dotenv('.env', override=True)


@dataclass
class ServerConfig:
    """
       Server config
    """
    HOST_IP: str
    PORT: str
    NAME: str
    VERSION: str


@dataclass
class Config:
    """
        Config sets
    """
    LOGS_FOLDER_PATH: str
    DJANGO_SETTINGS_MODULE: str
    DEBUG: str
    ALLOWED_HOSTS: str

    MODEL_DEPLOYMENT_MGT:ServerConfig
    SYSTEM_STATUS_MGT:ServerConfig
    ABSTRACT_METADATA:ServerConfig
    FILE_METADATA:ServerConfig
    CENTRAL_OPERATION:ServerConfig
    INFERENCE_OPERATION:ServerConfig


config = Config(
    #Default 
    LOGS_FOLDER_PATH=os.getenv("LOGS_FOLDER_PATH"),
    DJANGO_SETTINGS_MODULE=os.getenv("DJANGO_SETTINGS_MODULE"),
    DEBUG=os.getenv("DEBUG"),
    ALLOWED_HOSTS=os.getenv("ALLOWED_HOSTS"),

    # inference-layer.system_rt_mgt.system_task_mgt.model_deployment_mgt
    MODEL_DEPLOYMENT_MGT=ServerConfig(
        HOST_IP=os.getenv("HTTP_MODEL_DEPLOYMENT_MGT_HOST_IP"),
        PORT=os.getenv("HTTP_MODEL_DEPLOYMENT_MGT_PORT"),
        NAME=os.getenv("HTTP_MODEL_DEPLOYMENT_MGT_NAME"),
        VERSION=os.getenv("HTTP_MODEL_DEPLOYMENT_MGT_VERSION"),
    ),
    # inference-layer.system_rt_mgt.system_task_mgt.system_status_mgt
    SYSTEM_STATUS_MGT=ServerConfig(
        HOST_IP=os.getenv("HTTP_SYSTEM_STATUS_MGT_HOST_IP"),
        PORT=os.getenv("HTTP_SYSTEM_STATUS_MGT_PORT"),
        NAME=os.getenv("HTTP_SYSTEM_STATUS_MGT_NAME"),
        VERSION=os.getenv("HTTP_SYSTEM_STATUS_MGT_VERSION"),
    ),

    #agent-layer.agent_mgt.metadata_mgt.abstract_metadata
    ABSTRACT_METADATA=ServerConfig(
        HOST_IP=os.getenv("HTTP_ABSTRACT_METADATA_HOST_IP"),
        PORT=os.getenv("HTTP_ABSTRACT_METADATA_PORT"),
        NAME=os.getenv("HTTP_ABSTRACT_METADATA_NAME"),
        VERSION=os.getenv("HTTP_ABSTRACT_METADATA_VERSION"),
    ),
    FILE_METADATA=ServerConfig(
        HOST_IP=os.getenv("HTTP_FILE_METADATA_HOST_IP"),
        PORT=os.getenv("HTTP_FILE_METADATA_PORT"),
        NAME=os.getenv("HTTP_FILE_METADATA_NAME"),
        VERSION=os.getenv("HTTP_FILE_METADATA_VERSION"),
    ),
    #agent-layer.agent_mgt.central_connector.central_operation
    CENTRAL_OPERATION=ServerConfig(
        HOST_IP=os.getenv("HTTP_CENTRAL_OPERATION_HOST_IP"),
        PORT=os.getenv("HTTP_CENTRAL_OPERATION_PORT"),
        NAME=os.getenv("HTTP_CENTRAL_OPERATION_NAME"),
        VERSION=os.getenv("HTTP_CENTRAL_OPERATION_VERSION"),
    ),
    #agent-layer.agent_mgt.inference_connector.inference_operation
    INFERENCE_OPERATION=ServerConfig(
        HOST_IP=os.getenv("HTTP_INFERENCE_OPERATION_HOST_IP"),
        PORT=os.getenv("HTTP_INFERENCE_OPERATION_PORT"),
        NAME=os.getenv("HTTP_INFERENCE_OPERATION_NAME"),
        VERSION=os.getenv("HTTP_INFERENCE_OPERATION_VERSION"),
    )
)
