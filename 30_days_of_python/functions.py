items = ['Mic', "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 132]

str_items = []
num_items = []

for i in items:
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass

print(str_items)

print(num_items)

def parse_lists(some_list):
    str_list_items = []
    num_list_items = []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        elif isinstance(i, list):
        	s, n = parse_lists(i)
        	str_list_items += s
        	num_list_items += n
        else:
            pass
    return str_list_items, num_list_items

print(parse_lists(items))

item_list = ["asdasda", 123, 2222, 5555, "aaaaa"]
items2 = ['Mic', "Phone", item_list]

print(parse_lists(items2))

items3 = ['Mic', "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 132]

def my_sum(my_num_list):
    total = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
    return total

print(my_sum(items3))
# print(sum(items3))

def my_sum_and_count(my_num_list):
    total = 0
    count = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
            count += 1
    return total, count


def my_avg(my_num_list):
    the_sum, num_of_items = my_sum_and_count(my_num_list)
    return the_sum / (num_of_items * 1.0)


print(my_avg(items3))