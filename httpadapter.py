import time
import requests
from requests.adapters import HTTPAdapter



def retry():
	s = requests.Session()
	s.mount('http://', HTTPAdapter(max_retries=3))
	s.mount('https://', HTTPAdapter(max_retries=3))
	
	try:
	    print(f"请求开始记录时间{time.strftime('%Y-%m-%d %H:%M:%S')}")
	    r = s.get('https://twitter.com', timeout=2)
	    print('请求成功了')
	    return r.text
	except requests.exceptions.RequestException as e:
	    print(f"重试后超时抛异常时间{time.strftime('%Y-%m-%d %H:%M:%S')}")
	    print(e)

retry()