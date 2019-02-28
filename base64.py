import re

base64 = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M',"N",\
    'O','P','Q','R','S','T','U','V','W','X','Y','Z',\
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',\
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',\
    '0', '1', '2', '3', '4','5','6','7','8','9',\
    '+', '/']

def str_to_binary(string):
    res = ''
    for s in string:
        # if s == ' ':
        #     continue
        s_bin = bin(ord(s))[2:]
        if len(s_bin) != 8:
            s_bin='0'*(8-len(s_bin))+s_bin
        res += s_bin
    return res

def to_base_64(string):
    s_bin = str_to_binary(string)
    s_bin_sep = re.findall(r'.{6}', s_bin)
    s_rail = s_bin[(6 * len(s_bin_sep)) :]
    print(s_rail)
    if s_rail != '':
        s_rail += '0' * (6 - len(s_rail))
        s_bin_sep.append(s_rail)
    print(s_bin_sep)
    for i in range(len(s_bin_sep)):
        s_bin_sep[i] = int('0b' + s_bin_sep[i], 2)
    res = ''
    for x in s_bin_sep:
        res += base64[x]
    return res


def from_base_64(string):
    l1 = []
    # restore the 6 bit number
    for x in string:
        s1 =  bin(base64.index(x))[2:]
        s1 = '0'*(6-len(s1))+s1
        l1.append(s1)
    org = ''.join(l1)
    print(org)
    org_8bit = re.findall(r'.{8}', org)
    for i in range(len(org_8bit)):
        org_8bit[i] = chr(int(org_8bit[i], 2))
    print(org_8bit)
    return ''.join(org_8bit)

if __name__ == '__main__':
    # s = 'this is a string!!'
    # to_base_64(s)
    # print('\n')
    print(to_base_64('y7Z7AEF9'))