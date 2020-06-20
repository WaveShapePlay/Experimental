def currentValue(p,r,n,t):
    totalVaule = p*(1+(r/n))**(n*t)
    totalVaule = round(totalVaule,2)
    return totalVaule

def futureValue(monthlyPayment,r,n,t):
    FV = monthlyPayment*(((1+(r/n))**(n*t) - 1) / (r/n))
    FV = round(FV,0)
    return FV

def getMatch(s,matchPercent):
    matchAmountYear = s*matchPercent
    matchAmountMonth = matchAmountYear/12
    matchAmountMonth = round(matchAmountMonth,2)
    return matchAmountMonth

def getTotalBalances(p,r,n,t,monthlyContribution,s,match):
    startingP = currentValue(p,r,n,0)
    startingP = startingP
    principalList = list()
    principalList.append(startingP)
    t = int(t)
    for y in range(1,t+1):
        newTotal = currentValue(p,r,n,y)
        principalList.append(newTotal)

    futureValueList = list()
    monthlyContribution = monthlyContribution + getMatch(s,match)
    for i in range(1,t+1):
        
        #print(monthlyContribution)
        getFV = futureValue(monthlyContribution,r,n,i)
        futureValueList.append(getFV)

    totalBalanceList = list()
    for z in range(0,len(principalList)-1):
        totalBalance = futureValueList[z] + principalList[z+1]
        totalBalanceList.append(totalBalance)

    return totalBalanceList
