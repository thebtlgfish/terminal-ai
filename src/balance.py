import requests

def usage(api_key):
    url = 'https://ollama.com/api/balance'
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if 'included' in data:
            inc = data['included']
            balance_usd = inc.get('balance_usd')
            allowance_usd = inc.get('allowance_usd')

            if balance_usd is not None and allowance_usd and allowance_usd > 0:
                percent_left = (balance_usd / allowance_usd) * 100
                return f"{percent_left:.1f}% Left"

            for key in ['session', 'weekly']:
                if key in inc and 'remaining_percent' in inc[key]:
                    return f"{inc[key]['remaining_percent']}%"

        return "Usage percentage not available"
    else:
        return f"Error: {response.status_code}"
