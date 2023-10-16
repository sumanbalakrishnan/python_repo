"""
Author : Suman Balakrishnan
Date : 20-07-2023

General lambda function invoker module
"""

import os

from lambda_functions import  intake_nvd_vulnerabilities

os.environ["env"] = "dev"

intake_nvd_vulnerabilities.handler(None,None)

