import boto3

print(dir(boto3))


def filter_func(p_pattern, in_list):
    for x in in_list:
        if p_pattern in x:
            yield x


print(list(filter_func('ex', dir(boto3))))

pattern = 'ex'
lambda_func = lambda x: pattern in x
print(list(filter(lambda_func, dir(boto3))))
