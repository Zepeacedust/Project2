def LuhnAlgorithm(cardNumber):
    numSum = 0
    lastNum = int(cardNumber[-1])
    cardNumberCalc = cardNumber.rstrip(cardNumber[-1])
    lenNum = len(cardNumberCalc)
    flag = True
    cardNumberList = []
    counter = 0
    for x in range(lenNum):
        if flag:
            cardNumberList.append(int(cardNumberCalc[x])*1)
        else:
            cardNumberList.append(int(cardNumberCalc[x])*2)
        flag = not flag
    for x in cardNumberList:
        if x >= 10:
            cardNumberList[counter] = (x-9)
        counter += 1
    numSum = sum(cardNumberList)
    checkDigit = (10-(numSum%10))%10
    if lastNum == checkDigit:
        return True
    else:
        return False

def monthExpiration(month):
    if month <= 12:
        if month >= 1:
            return True
    return False


def yearExpiration(date):
    if date == 4:
        return True
    return False

def CVC(number):
    if number == 3:
        return True
    return False
    

cartdNumber = input("please input your credit card number")
monthExpirationDate = input("please input your expiration month (1-12)")
yearExpirationDate = input("please input your expiration year (4 numbers)")
CVCnumber = input("please input your CVC number (3 numbers)")

def creditCardValidation(cartdNumber,monthExpirationDate,yearExpirationDate,CVCnumber):
    if LuhnAlgorithm(cartdNumber):
        if monthExpiration(monthExpirationDate):
            if yearExpiration(yearExpirationDate):
                if CVC(CVCnumber):
                    return True
    return False

creditCardValidation(cartdNumber,monthExpirationDate,yearExpirationDate,CVCnumber)