import requests
import hashlib


def request_api_data(query_char):
    # The API expects a 5-character SHA-1 hash prefix
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res.text


def get_password_leaks_count(hashes, hash_to_check):
    # Process the API response to find matches for the tail of the hash
    hashes = (line.split(':') for line in hashes.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return int(count)
    return 0


def pwned_api_check(password):
    # Hash the password
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # Split into first 5 chars (prefix) and the rest (tail)
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    # Query the API with the prefix
    response = request_api_data(first5_char)
    # Check for matches in the returned hash list
    return get_password_leaks_count(response, tail)


# Test the function with a password
password = "Ohmynassau123"
leaks_count = pwned_api_check(password)

if leaks_count:
    print(f'The password "{password}" was found {leaks_count} times. You should change it!')
else:
    print(f'The password "{password}" was NOT found. Carry on!')
