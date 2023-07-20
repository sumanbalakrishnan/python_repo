"""
Author : Suman Balakrishnan
Date : 20-07-2023

General application configuration parameters
"""


import os

application_parameters = {
    "dev": {

    },
    "prod": {

    },
    "qa": {

    }
}


def get_application_parameter(parameter_name, default):
    app_environment = os.getenv("env")
    return application_parameters.get(app_environment, {}).get(parameter_name, default)
