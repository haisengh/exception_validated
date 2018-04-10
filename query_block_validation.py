import requests
from bs4 import BeautifulSoup

def get_search_result_url(keyword):
	url = "http://bing.com/search?q=" + keyword
	bing_document = requests.get(url).text
	search_result = BeautifulSoup(bing_document, "html.parser").find(id = "b_results")
	algos = search_result.select(".b_algo")
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

def exception_test(url_list, exception_list):
	for url in url_list:
		domain_name = extract_domain(url) + "\n"
		if domain_name not in exception_list:
			return False
	return True


if __name__ == "__main__":
	url_list = get_search_result_url("习近平")
	with open("exception_li", "rt", encoding = "utf-8") as f:
		exception_list = list(f)
	print("习近平", exception_test(url_list, exception_list))


