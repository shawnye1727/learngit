import time
import requests
from requests.adapters import HTTPAdapter


def api_sales_info(applychannel):

	s = requests.Session()
	s.mount('http://', HTTPAdapter(max_retries=3))
	s.mount('https://', HTTPAdapter(max_retries=3))

	url = 'http://xrc.yingzhongtong.com:8000/api/sales/info'
	body = {"applyChannel": applychannel}
	headers = {"Host": "xrc.yingzhongtong.com", "Content-Type": "application/json"}

	try:
		print(f"开始请求记录时间{time.strftime('%Y-%m-%d %H:%M:%S')}")
		response_tmp = s.post(url=url, json=body, headers=headers, timeout=(0.1,1))
		print('请求成功了')
		return response_tmp.text
		# if response_tmp.status_code == 200:
		# 	print(f"打印接口返回http状态码：{response_tmp.status_code}")
		# 	print(f"打印接口响应内容编码：{response_tmp.encoding}")
		# 	print(f"打印接口unicode响应内容：{response_tmp.text}")
		# 	print(f"打印接口二进制响应内容：{response_tmp.content}")
		# 	print(f"打印接口JSON解码后的响应内容：{response_tmp.json()}")
		# 	print(f"打印接口原始相应内容：{response_tmp.raw}")
		# 	return response_tmp
		# else:
		# 	print('不超时但是http的status_code非200')
		# 	return response_tmp.text
	except requests.exceptions.RequestException as e:
		print(f"重试后依旧超时抛出异常{time.strftime('%Y-%m-%d %H:%M:%S')}")
		print(e)


response = api_sales_info(100023627)

# with open("xrc_response_raw.text",'wb') as fd:
# 		for chunk in response.iter_content(100):
# 			fd.write(chunk)