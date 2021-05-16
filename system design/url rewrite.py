def to_base_62(deci):
    s = '012345689abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    hash_str = ''
    while deci > 0:
        hash_str = s[deci % 62] + hash_str
        deci //= 62
    return hash_str


# print(to_base_62(999))
# print(to_base_62(998))
# print(to_base_62(997))
# print(to_base_62(996))
# print(to_base_62(995))
# print(to_base_62(994))
# print(to_base_62(993))
# print(to_base_62(992))
print(to_base_62(991))
