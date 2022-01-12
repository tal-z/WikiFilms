import requests


def get_entries(title):
    base_url = "http://en.wikipedia.org/w/api.php"
    entries = []
    print(f"fetching revisions to {title}")
    while not entries:
        parameters = {
            'action': 'query',
            'format': 'json',
            'continue': '',
            'titles': title,
            'prop': 'revisions',
            'rvprop': 'ids|userid|user|timestamp',
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
            entries.append(entry)

        ## next series of passes, until you're done.
        else:
            while str(len(revisions)) == parameters['rvlimit']:
                #start_id = revision_list[-1]
                start_id = entries[-1]['revid']

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
                    entries.append(entry)

    return entries #revision_list, ts_list

def get_random_title():
    random_url = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=1'

    parameters = {
        'format': 'json',
    }

    response = requests.get(random_url, params=parameters)
    data = response.json()
    return data['query']['random'][0]['title']

if __name__ == '__main__':
    print(
        get_random_title()
    )