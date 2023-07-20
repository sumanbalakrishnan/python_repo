"""
Author : Suman Balakrishnan
Date : 20-07-2023

Intake process works to extract CVE data from nvd endpoint.
"""

import logging
import traceback
import requests
import urllib


logger = logging.getLogger('root')
nvd_endpoint = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def handler(event, context):
    logger.info("intake process starts")
    try:
        nvd_vulnerabilities = get_nvd_vulnerabilities()
        save_vulnerabilities(nvd_vulnerabilities)
    except Exception as e:
        logger.error(f"Error in intake nvd vulnerabilities : {traceback.format_exc()}")


def get_nvd_vulnerabilities():
    try:
        # Get all vulnerabilities
        nvd_vulnerabilities = get_paginated_restapi_results("https://services.nvd.nist.gov/rest/json/cvehistory/2.0",
                                                            "cveChanges", 5000)
    except Exception as e:
        raise Exception(f"Error in getting nvd data: {traceback.format_exc()}")

    return nvd_vulnerabilities


def get_response_data(rest_api_result, results_key):
    if rest_api_result.ok:
        response_data = rest_api_result.json()

        if response_data:
            return response_data[results_key], rest_api_result['totalResults']
    return [], 0


def get_paginated_restapi_results(endpoint, result_key, page_size):
    if not endpoint:
        logger.info("Paginated rest api call without a valid endpoint")
        return []

    results = []
    response = requests.get(prepare_url(endpoint, {'resultsPerPage': page_size,
                                                   'startIndex': 0}))
    if response.ok:
        vulnerabilities, total_results = get_response_data(response)
        results.extend(vulnerabilities)

        start_index = 1
        # Loop until all data extracted
        while total_results > len(vulnerabilities):
            response = requests.get(prepare_url(endpoint, {'resultsPerPage': page_size,
                                                           'startIndex': start_index}))
            vulnerabilities, total_results = get_response_data(response)
            results.extend(vulnerabilities)
            start_index += 1
    return results


def prepare_url(endpoint, **kwargs):
    return endpoint + urllib.parse.urlencode(kwargs)


def save_vulnerabilities(nvd_vulnerabilities):
    pass

