#https://blog.csdn.net/u011106915/article/details/108210623
import re
def is_id_number(id_number):
    if len(id_number) != 18:
        print("长度错误")
        return False
    regularExpression = "(^[1-9]\\d{5}(18|19|20)\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\\d{3}[0-9Xx]$)|" \
                        "(^[1-9]\\d{5}\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}$)"
    if re.match(regularExpression, id_number):
        if len(id_number) == 18:
            n = id_number.upper()
            #前十七位加权因子
            var = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            #这是除以11后，可能产生的11位余数对应的验证码
            var_id = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
            sum = 0
            for i in range(0, 17):
                sum += int(n[i]) * var[i]
            sum %= 11
            if (var_id[sum]) != str(n[17]):
                print("校验码错误")
                return False
            # 闰年
            year = int(n[6])*1000 + int(n[7])*100 + int(n[8])*10 + int(n[9])
            if(year % 4 != 0):
                if int(n[10]) == 0 and int(n[11]) == 2:
                    if int(n[12]) == 2:
                        if int(n[13]) == 9:
                            return False
            return True
        else:
            return False

if __name__ == '__main__':
    result = is_id_number('41000119900101007x')
    print(result)
