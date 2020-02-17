# Filter using traditional function ========================
def filtered_list_mono(p_pattern, in_list):
    filtered_list = []
    for el in in_list:
        if p_pattern in el:
            filtered_list.append(el)
    return filtered_list


# Filter using list comprehension ===========================
def filtered_list_comp(p_pattern, in_list):
    filtered_list = [el if p_pattern in el else None for el in in_list]
    while None in filtered_list:
        filtered_list.remove(None)
    return filtered_list


# Filter using yield =======================================
def check_pattern(p_pattern, p_in_list):
    for el in p_in_list:
        if p_pattern in el:
            yield el


def filtered_list_yield(p_pattern, p_in_list):
    return list(check_pattern(p_pattern, p_in_list))


# Filter using built-in filter =============================
def filtered_list_filter(p_pattern, in_list):
    return list(filter(lambda x: p_pattern in x, in_list))


if __name__ == '__main__':
    PATTERN = 'filtered_list'
    print(filtered_list_mono  (PATTERN, dir()))
    print(filtered_list_comp  (PATTERN, dir()))
    print(filtered_list_yield (PATTERN, dir()))
    print(filtered_list_filter(PATTERN, dir()))


# Example ONLY of filters - note tag
# filter1 = {"Name": "name", "Values": ["12chairs.com", "bytemple.com"]}
# filter2 = {"Name": "tag:Env", "Values": ["TestInstance", "testinstance"]}
#
# bucket_list_filtered = s3_console_resource.buckets.filter(Filter=[filter1, filter2])
