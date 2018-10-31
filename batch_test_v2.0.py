from query_block_validation import exception_test
from multiprocessing import Pool

def get_query_list(file):
	with open(file, "rt", encoding = "utf-8") as f:
		query_list = [query.strip() for query in list(f)]
	return query_list

def test(query):
	is_blocked = (query,exception_test(query))
	return is_blocked


def main():
	query_list_file = "query"
	failed_list_file = "failed_list.txt"
	noresult_list_file = "noresult_list.txt"
	failed_list = []
	noresult_list = []
	blocked_list = []
	query_list = get_query_list(query_list_file)

	with Pool() as p:
		test_reult = p.map(test, query_list)

	for result in test_reult:
		if result[1] == 3:
			blocked_list.append(result[0])
		elif result[1] == 2:
			failed_list.append(result[0])
		elif result[1] == 1:
			noresult_list.append(result[0])

	with open(failed_list_file, "wt", encoding = "utf-8") as fail:
		for q in failed_list:
			fail.write(q+"\n")
	with open(noresult_list_file, "wt", encoding = "utf-8") as ns:
		for q in noresult_list:
			ns.write(q+"\n")

	description = "{} is blocked successfully, \n{} isn't blocked, \n{} have no result".format(len(blocked_list), len(failed_list), len(noresult_list))
	print(description)



if __name__ == '__main__':
	main()

