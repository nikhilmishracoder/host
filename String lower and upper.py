def swap_case(s):
    a=''
    c='.,"'
    for i in range(len(s)):
        if s[i].isupper()==True:
            a+=s[i].replace(s[i].upper(),s[i].lower())
        elif s[i].islower()==True:
            a+=s[i].replace(s[i].lower(),s[i].upper())
        elif s[i].isdigit()==True:
            a+=s[i]
        elif s[i] in c:
            s[i].replace(s[i],c)
            a+=s[i]
        else:
            a+=' '
    result=a
    return result



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
