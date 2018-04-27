from query_block_validation import exception_test
with open("exception_li", "rt", encoding = "utf-8") as f:
		exception_list = list(f)
# print(exception_test(get_search_result_url("令计划"), exception_list))
with open("cache", "rt", encoding = "utf-8") as e:
	query_list = []
	for q in e:
		query_list.append(q.strip())

failed_list = []
succeeded_list = []
noresult_list = []

for query in query_list:
	test_result = exception_test(query)
	if test_result == True:
		succeeded_list.append(query)
	elif test_result == False:
		failed_list.append(query)
	else:
		noresult_list.append(query)

print("failed_list", len(failed_list))
print("succeeded_list", len(succeeded_list))
print("noresult_list", len(noresult_list))
with open("failed_list2.txt", "wt", encoding = "utf-8") as fl:
	for query in failed_list:
		fl.write(query + "\n")

