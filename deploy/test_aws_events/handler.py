import requests
from osbot_utils.context_managers.capture_duration import capture_duration


def run(event,context):
    with capture_duration() as duration:
        data = {'event': event}
        url = "https://serverless-flows.dev.aws.cyber-boardroom.com/dev/flow-testing-tasks"
        response = requests.post(url, json=data)

    return {'status_code': response.status_code,
            'text'       : response.text       ,
            'duration'   : duration.seconds    }