from flask import Response, json


class BaseSkeleton(object):
    status_code = 0
    payload = {}
    headers = {'Server': 'Backyard API'}

    def __init__(self, status_code, payload, headers=None):
        self.status_code = status_code
        self.payload = payload
        if headers:
            self.headers.update(headers)

    def response(self):
        response_payload = json.dumps(self.payload) if self.payload else ''
        return Response(headers=self.headers,
                        mimetype='application/json',
                        status=int(self.status_code),
                        response=response_payload)
