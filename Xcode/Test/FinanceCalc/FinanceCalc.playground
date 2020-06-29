import UIKit

var str = "Hello, playground"

class UserFinancialData{
//    Update these to explicitly be of type Float, then I can remove all the Floats() from the method calls
    var salary = 88000.0
    var priciple = 70000.0
    var invetmentPercent = 0.18
    var n = 12.0
    var time = 30.0
    var intrest = 0.07
    var employerMatchPercent = 0.04
    
}

class FinanceCalculations{
    
    func futureValueSingleValue(s: Float,p: Float, n: Float, t: Float, r: Float)->Float{
        // FV = p*(1+(r/n))**(n*t)
        var FV = p*(pow(1+(r/n),n*t))
        return FV
    }

    func futureValueWithAnnuity(monthlyPatment:Float,r: Float, n: Float, t: Float)->Float{
        var FV_A = monthlyPatment*((pow((1+r/n),n*t)-1)/(r/n))
        return FV_A
    }
    
    func employerMatch(s: Float,matchPercent: Float)->Float{
    
        var matchAmountYear = s*matchPercent
        var matchAmountMonth = matchAmountYear/12
        return matchAmountMonth
    }

//  totalFutureValue returns and array of future values of the initial principal by year
    func totalFutureValue(s: Float, p:Float, r:Float, n: Float, t: Float)->Array<Float>{
        var futureValueList: [Float] = []
        futureValueList.append(p)
        var currentFV : Float = 0.0
        
//      This loop gets the future values based off the intial principal and intrest only.
        for x in 1...Int(t){
            currentFV = futureValueSingleValue(s: Float(userInfo.salary), p: Float(userInfo.priciple), n: Float(userInfo.n),t: Float(x),r: Float(userInfo.intrest))
            futureValueList.append(currentFV)
        }
        return futureValueList
    }
    
//  monthlyContributionFV returns your monthly contribution baseed off salary, perecnt deducted from income which is invested and employee match
    
    func monthlyContributionCalc(s: Float, contributionPercent: Float, matchPercent: Float )->Float{
        var totalMonthlyContribution = (s*contributionPercent + s*matchPercent)/12
        return totalMonthlyContribution
    }

//  FV_monthlyContributions returns the future vales of eact monthly contribution.
    func FV_monthlyContributions(contribution: Float,s: Float,p: Float, n: Float, t: Float, r: Float)->Array<Float>{
        var FV_MC_List: [Float] = []
        var current_FV_MC: Float = 0.0
        
        FV_MC_List.append(0.0)
        for x in 1...Int(t){
            current_FV_MC = futureValueWithAnnuity(monthlyPatment: Float(contribution), r: Float(r), n: Float(n), t: Float(x))
            FV_MC_List.append(current_FV_MC)
        }
        return FV_MC_List
    }
    
    func FV_totalSum( FV_SingleValue: [Float], FV_Monthly: [Float],t:Float)->Array<Float>{
        print("-----------")
        print(FV_SingleValue)
        print(FV_Monthly)
        print("-----------")
        var FV_totals: [Float] = []
        
        for y in 0...Int(t){
            FV_totals.append(FV_SingleValue[y] + FV_Monthly[y])
        }
        
        return FV_totalsa
    }
    
}
var userInfo = UserFinancialData()
var getBalances = FinanceCalculations()
var sumOfTest = Float (userInfo.salary + userInfo.priciple)

var singleFutureValue = getBalances.futureValueSingleValue(s: Float(userInfo.salary), p: Float(userInfo.priciple), n: Float(userInfo.n),t: Float(userInfo.time),r: Float(userInfo.intrest))

var totalMonthlyInvested = getBalances.monthlyContributionCalc(s: Float(userInfo.salary), contributionPercent: Float(userInfo.invetmentPercent), matchPercent: Float(userInfo.employerMatchPercent))

var employerMatchValue = getBalances.employerMatch(s: Float(userInfo.salary), matchPercent: Float(userInfo.employerMatchPercent))

var TestTotlalFV = getBalances.totalFutureValue(s: Float(userInfo.salary), p: Float(userInfo.priciple), r: Float(userInfo.intrest), n: Float(userInfo.n), t: Float(userInfo.time))

var testMonthly_FC = getBalances.FV_monthlyContributions(contribution: Float(totalMonthlyInvested), s: Float(userInfo.salary), p: Float(userInfo.priciple), n: Float(userInfo.n), t: Float(userInfo.time), r: Float(userInfo.intrest))

var testTotalFV = getBalances.FV_totalSum(FV_SingleValue: TestTotlalFV, FV_Monthly: testMonthly_FC,t: Float(userInfo.time))

print(testTotalFV)



    


