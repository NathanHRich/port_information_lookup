import grequests  # NOTE: If using the 'requests' module, import it before 'grequests'
import json
import pandas


def port_lookup(port_list):
    base_url = 'https://www.speedguide.net/port.php?port='
    urls = [(base_url + str(port)) for port in port_list]
    request = (grequests.get(url) for url in urls)
    response = grequests.map(request)
    final_list = []
    for item in response:
        port_dict_list = []
        raw_html = item.text
        pandas_table = (pandas.read_html(raw_html, header=0, thousands=None))
        for table in pandas_table:
            if 'Port(s)' in table:
                ports_response_list = json.loads(table.to_json(orient="records"))
                for port_dict in ports_response_list:
                    port_dict_list.append(port_dict)
        final_list.append(dict(port=item.url.split('=')[-1], port_info=port_dict_list))
    return final_list
