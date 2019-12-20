import requests

base_url = 'https://api.zoom.us/v2'


def get_webinars(user_id, token_type, token):
    url = base_url + '/users/{userId}/webinars'.format(userId=user_id)
    headers = {
        'Authorization': '{} {}'.format(token_type, token)
    }
    params = {
        'page_size': 30,
        'page_number': 1
    }
    res = requests.get(url, params=params, headers=headers)
    return res.status_code, res.json()


def get_recordings(meeting_id, token_type, token):
    url = base_url + '/meetings/{meetingId}/recordings'.format(meetingId=meeting_id)
    headers = {
        'Authorization': '{} {}'.format(token_type, token)
    }
    params = {
        'page_size': 30,
        'page_number': 1
    }
    res = requests.get(url, params=params, headers=headers)
    return res.status_code, res.json()
