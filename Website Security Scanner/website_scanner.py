import requests

def get_target_url():
    """ Prompts the user for the URL and validates it """
    while True:
        url = input("Enter the target URL (http:// or https://): ")
        if url.startswith("http://") or url.startswith("https://"):
            return url
        else:
            print("Invalid URL format. Please enter a valid URL starting with http:// or https://")

def send_request(url, method="GET", headers={}, data={}):
    """
    Sends an HTTP request to the specifies URL with given method, headers, and data.
    """
    try:
        response = requests.request(method, url, headers=headers, data=data)
        return response
    except requests.exceptions.RequestException as e:
        print(f'Error sending request: {e}')
        return None

def test_sql_injection(url):
    """
    Tests for basic SQL injection vulnerability by injecting a simple test string.
    """
    original_response = send_request(url)
    if original_response is None:
        return
    injected_url = url + "?id=1' AND '1' = '1" #Simple Test
    injected_response = send_request(injected_url)
    if injected_response and injected_response.content != original_response.content:
        print(f"Potential SQL injection vulnerability found in {url}")

    else:
        print('This website is safe from SQL injection.')

def main():
    target_url = get_target_url()
    test_sql_injection(target_url)

if __name__ == '__main__':
    main()