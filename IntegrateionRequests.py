import requests
import sys
import json


class IntegrationRequests:
    TIMEOUT_SEC = 120

    @staticmethod
    def __get_api(handler, url_suffix):

        url = handler + url_suffix

        try:
            res = requests.get(url, timeout=IntegrationRequests.TIMEOUT_SEC)
        except requests.exceptions.Timeout:
            print(url, file=sys.stderr)
            print('Timeout in IntegrationRequests for URL: ' + url, file=sys.stderr)
            return None
        except BaseException as e:
            print(url, file=sys.stderr)
            print('%s received in IntegrationRequests for URL: %s' % (e, url), file=sys.stderr)
            return None
        status_code = res.status_code
        if status_code != 200:
            print(url, file=sys.stderr)
            print('Status code ' + str(status_code) + ' for url: ' + url, file=sys.stderr)
            return None
        return res.json()

    @staticmethod
    def __post_api(handler, url_suffix, payload):

        url = handler + url_suffix
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json; charset=UTF-8"
        }

        try:
            res = requests.post(url, data=json.dumps(payload), headers=headers, timeout=IntegrationRequests.TIMEOUT_SEC)
        except requests.exceptions.Timeout:
            print(url, file=sys.stderr)
            print('Timeout in IntegrationRequests for URL: ' + url, file=sys.stderr)
            return None
        except BaseException as e:
            print(url, file=sys.stderr)
            print('%s received in IntegrationRequests for URL: %s' % (e, url), file=sys.stderr)
            return None
        status_code = res.status_code
        if status_code != 200:
            print(url, file=sys.stderr)
            print('Status code ' + str(status_code) + ' for url: ' + url, file=sys.stderr)
            return None
        return res.json()

    @staticmethod
    def Query_Xray():

        #   get request
        url = "http://rtx.ncats.io/api/rtx/v1/"
        url_suffix = "result/2"
        response = IntegrationRequests.__get_api(url, url_suffix)
        print(response)

        #   post request
        url_suffix = "query"
        post_data = {
            "bypass_cache": "true",
            "known_query_type_id": "Q1",
            "max_results": 100,
            "message": "Your question was understood.",
            "original_question": "what genetic conditions offer protection against malaria",
            "page_number": 1,
            "page_size": 100,
            "restated_question": "Which genetic conditions may offer protection against malaria?",
            "terms": {
                "disease": "malaria"
            }
        }
        response = IntegrationRequests.__post_api(url, url_suffix, post_data)
        print(response)


if __name__ == '__main__':
    IntegrationRequests.Query_Xray()