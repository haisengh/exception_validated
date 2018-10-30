import requests
from bs4 import BeautifulSoup
from urllib import parse

with open("exception_li", "rt", encoding = "utf-8") as f:
		exception_list = list(f)

def get_search_result_url(keyword):
	cookies =dict(BFB="ARDtJluLNTlV5pPqHOGg5602NAcfudXlY5kONqXxiROM1waTc3rLiCve5KRVlADfM41faV8xM7FVnsLLSsv0buGALX6okIhbnusaUQNWH9QehpLXEyfe7eOX6akim3-XNY_-rYhe8hIlkb-vCJuuACwcvsNjwrmCCs3JW5HksmGcaQ",
	BFBD="yQokMTAxMzUwMGItYTgwZS00MDg2LWJmNjctN2EwMmZjOTNkZGFlyxQNARAKAgjLChEByNOd8%2FjujNQDyx4RAcrjs6GXqJLUA8soEAEC0DIAyzwRAcjTnfP47ozUA8tGEAG%2BOAAAywoRAYK9irKa7ozUA8seEQHOyMPumu6M1APLKBABAtAyAMs8EQGCvYqymu6M1APLRhABnjgAAA%3D%3D",
	BFBUSR="BAWAS=1",
	MSCC="1",
	MUID="3D15225AFC3E638F2D112E4BF83E65BA",
	MUIDB="3D15225AFC3E638F2D112E4BF83E65BA",
	MicrosoftApplicationsTelemetryDeviceId="632be508-e8c8-4d4c-d782-f8e1fdc145ed",
	MicrosoftApplicationsTelemetryFirstLaunchTime="1.54089E+12",
	OID="ARAUEqspYGEDaO4ShwSVMD1NWkdeaqnVwCzS-AQwSo9Pt8T3rArzJL9kGNGS8ykeWzIm7AN9GVGRErtAgOzuf5DsRo7M-SPxuWlGnSCZ5VXIfibHhZi9bUg-Y9rcFXU6JPzf7dFEjbBJCqDvPN-K83va",
	OIDI="gRCHo3ePtIOypkBNnbWHBW4xZTc6t7bj0zakBjfN-5J89S7O66L1gwiO1DHa_Fy3RAgm3HrJqdW-S3YNJerKfPBAefAKdwjPl7JuQTqi3UP-uOC6LiQtY6j4L3-iJ4YNRlWLYzxtvZmU2gXo8Kn8Tr9KE56zmk4zm0PNcxzAeEB9GxU-VRbgSmwB9N6YK2RSTEBZdfuXkms01KMkRgMqljOOUlX7lOiGVyJFeKwDWKzrhAEX3fqXjX2tYvsnZE49FvwlxZazE6zBGjKVOyWUcgXGIYjcUpzegFVddzGpY8Ds9sARXHiuX8mqXDYPyzVtbNlNg5oGGAQNaZGvUF3lpdeLdxNbYb5z1sH1XJ7ux3XgeC4tONpO45m67yuuh6YzqsqrEt6prMn-b7fXDWtL8MZs2xHFxmzDObR4y0qE2Xn5Dmu1oKS-bR24TmL96xej1DkXBNVhqO4lja0xE8H_kFMW7u7JBZnJzKOqnvdCnQEbWAzClpDWmGIVIm4gPc526vvPRTzodnb-n3o30Ai_5kFwoNufjHVQcpM3VG_bw03hwyKzc3R9ZQT43UaN1r-KqylV0jQ1Sra8o8IEpXJkBOc7h4uB1yb8mTmjHAN0MNXlgXmfYaPM2phzenhBfFLRnTSsNNNkKtgPqxuQtGIXgX1dO25Gga2ombgyU3MPYB103cmfZ03wQeCY9yWWWpPvr91PqrxMB5OHzakNTbIcwcBJHczidRjl3nQl-oRJTspBCQsyFgxlvr6igPya2gIwnb60iF38iLBzJ5QSu03pGeJruo2LdCeMCIiCgLtD-EW2nqAvtfETzYIe5PnyjsRIwHOKDzY96ryndvG_X3p7UnBW-7lE_mN-t98IKH6-Qyja7r6ms7NVhk1DhPhU7ogCsT9U0ZOUoQF0IAAq-qhzs0mMpwtvHXx7p_Tat19gXd899Bqs9mhd6VViZVe9tLzz57qbT84Nzqx2Ji7cD2LPm0oLrHrw96FX8_1JoZA",
	OIDR="gRB1ssgEoWe6h_VvZyh8Gk4ZNXqvzOtuVMuTPJioujOCCa3Cp3nn3vQ2s6iSww94ZoMet4FLNOQptC2-pzsU30PVIPZnheLye7fgiD6RZgDv7QrouOplzhgl9qqvu6fyjqXD5rGFOUsdtAma4XFyzEE4sXUcGehV7Q2q4wgGgZbZBtnJwZdlhGr86WHB7R1m8GQAeKlNy84KEY-3QiqTExFvNpjfy1ynyoCsC8LByFCsIAUiqDyKT_Er0UYrfYzob6Qi7hBYzDt4ukfsgFvHMnJnPhutu5-qIS6ybWcnaN3eU4EC2IJhNza9w3AHhwIARcJcodaGcDiXNJ8TMBXmzHtfBdMTXjWsvHuslNXfxic52Z29Ypvymx_exUf0LmWWIKeoZOd5zK8jgmKJUTsdiPgAMI6esVNn6YozOB8_Ub39coDekDOGBkzcF_XrG0V74Bg_1sURKPYJT3I4j7Fsi3S7mINFcn8wzt_eSdJruMz9l50NvlueWpMDLkmHxtDshJZIszmYP0s0tA3vt3veeCo4exhRqvoagh49X78EXqF3JDOkECbCldiyTjJM3SopguEI6iKKy5nvgxd31qOmVWEKEapwkNSn2Rb5AC5Do4BEjJq99RprVFhD7lglzHQEiYMxDerFb73O-a5HXnl7BRA-tkOtBQcrGKVXVN7BBVbVelb5MitNFRB7qfipiawmB4CwKiFIDD5X-212WGJvND5GqRbVruhFtaWnVYU5S6g0XxrF2zSsoCPaJY4gnos3XzVVX1zT2VZgynPRsIWC6K1vQOTHPI6JcJJSizwzg3vk3SrobbdsziE9921VU5eIRaEUELWxIzv2Eb_PGyty9duwZ8Lek_g-ci8bDvo0dvola85Q2hBf8dIOYR3ATQNxbqGY4o3vGwqA5ydMr-BzD2OkFhjdSBwDJhOqXcV87COLGXt8rkdKJ8YkD_7aZLVwRO2breFOmfQIdsyfyqKzRkfjt37Hy3k3PXilm3M",
	SNRHOP="TS=636765031238968464&I=1",
	SRCHD="AF=NOFORM",
	SRCHHPGUSR="CW=1046&CH=952&DPR=1&UTC=480&WTS=63676490497",
	SRCHUID="V=2&GUID=14A5B342C3CD4EA69C9C991B64DA1E51&dmnchg=1",
	SRCHUSR="DOB=20181022&T=1540893839000",
	_EDGE_S="mkt=zh-cn&SID=2C0BCDA0A4D16B8F3B8EC138A5AE6A5B",
	_ITAB="STAB=TR",
	_RwBf="s=70&o=18",
	_SS="SID=2C0BCDA0A4D16B8F3B8EC138A5AE6A5B&bIm=328517&HV=1540905825",
	_TTSS_OUT='hist=["en"]',
	ipv6="hit=1540906574824&t=4",
	undefined="undefined=undefined")



	query = parse.quote(keyword)

	url = "https://www.bing.com/search?q="+query+"&cvid=C0BE9A2949194003BE3FBEB6FF1FE692"
	
	try:
		bing_document = requests.get(url,cookies=cookies).text
	except:
		return 0
	# with open("result.html", "wt", encoding = "utf-8") as f:
	# 	# f.write(str(BeautifulSoup(bing_document, "lxml").find(id = "b_content").contents))
	# 	f.write(bing_document.)
		
	search_result = BeautifulSoup(bing_document, "lxml").find(id = "b_results")
	try:
		algos = search_result.select(".b_algo")
	except:
		return 0
	algo_urls = []
	for algo in algos:
		algo_urls.append(algo.find("h2").find("a")["href"])
	return algo_urls


def extract_domain(url):
	start = url.find("//") + 2
	end = url[start:].find("/") + start
	url = url[start:end]
	domain_name = url.split(".")[-2]
	if domain_name == "com":
		domain_name = url.split(".")[-3]
	return domain_name

def exception_test(query, exception_list = exception_list):
	url_list = get_search_result_url(query)
	if url_list == 0:
		return "no_result"
	for url in url_list:
		domain_name = extract_domain(url) + "\n"
		if domain_name not in exception_list:
			return domain_name
	return True


if __name__ == "__main__":
	print("习近平", exception_test("习近平", exception_list))


