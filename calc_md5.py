'''
@author:lsd
@time:16.08.2023 15:57
'''
import hashlib
import urllib.request


def calculate_md5(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    return md5_hash.hexdigest()


def read_md5_file_from_url(url):
    try:
        response = urllib.request.urlopen(url)
        md5_text = response.read().decode('utf-8')
        md5_list = md5_text.strip().split(',')
        return md5_list
    except Exception as e:
        print(f"Error reading MD5 file: {e}")
        return []


if __name__ == "__main__":
    remote_url = r"file:////192.168.1.4/产品库/6.发布版本_new/2023/HitPaw/HitPaw%20Voice%20Changer/win/1.0.1/MD5.txt"
    md5_list = read_md5_file_from_url(remote_url)

    if md5_list:
        print("MD5 values:")
        for md5 in md5_list:
            print(md5)
    else:
        print("No MD5 values found or error occurred.")

