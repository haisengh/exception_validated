import requests
from bs4 import BeautifulSoup

with open("exception_li", "rt", encoding = "utf-8") as f:
		exception_list = list(f)

def get_search_result_url(keyword):
	url = "http://bing.com/search?q=" + keyword
	try:
		bing_document = requests.get(url).text
	except:
		return 0
	search_result = BeautifulSoup(bing_document, "html.parser").find(id = "b_results")
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
			return False
	return True


if __name__ == "__main__":
	print("习近平", exception_test("www.diyifang.org", exception_list))


