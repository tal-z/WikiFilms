import requests


def get_revision_ids(title):
    base_url = "http://en.wikipedia.org/w/api.php"
    revision_list = []
    ts_list = []
    ## first API call
    while not revision_list:
        parameters = {
            'action': 'query',
            'format': 'json',
            'continue': '',
            'titles': title,
            'prop': 'revisions',
            'rvprop': 'ids|userid|timestamp',
            'rvlimit': '500',
        }

        wp_call = requests.get(base_url, params=parameters)
        response = wp_call.json()

        query = response['query']
        pages = query['pages']
        page_id_list = list(pages.keys())
        page_id = page_id_list[0]
        page_info = pages[str(page_id)]
        revisions = page_info['revisions']

        for entry in revisions:
            revision_list.append(entry['revid'])
            ts_list.append(entry['timestamp'])

        ## next series of passes, until you're done.
        else:
            while str(len(revisions)) == parameters['rvlimit']:
                start_id = revision_list[-1]

                parameters = {
                    'action': 'query',
                    'format': 'json',
                    'continue': '',
                    'titles': title,
                    'prop': 'revisions',
                    'rvprop': 'ids|userid|user|timestamp',
                    'rvlimit': '500',
                    'rvstartid': start_id,
                }

                wp_call = requests.get(base_url, params=parameters)
                response = wp_call.json()

                query = response['query']
                pages = query['pages']
                page_id_list = list(pages.keys())
                page_id = page_id_list[0]
                page_info = pages[str(page_id)]
                revisions = page_info['revisions']

                for entry in revisions[1:]:
                    print(entry)
                    revision_list.append(entry['revid'])
                    ts_list.append(entry['timestamp'])

    return revision_list, ts_list
