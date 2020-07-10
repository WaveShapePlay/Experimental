//
//  ViewController.swift
//  PersonalFinance
//
//  Created by Robert John on 7/10/20.
//  Copyright © 2020 Robert John. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
   
    @IBOutlet weak var salaryTextInput: UITextField!
    @IBOutlet weak var raiseTextInput: UITextField!
    @IBOutlet weak var totalValueLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    @IBAction func calculateButtion(_ sender: Any) {
        var userSalary: String = salaryTextInput.text!
        var userRaise: String = raiseTextInput.text!
        
        var financeData = FinanceModelController()
        
        financeData.salary = Float(userSalary)!
        financeData.payRaise = Float(userRaise)!
        
        
        let totalValue : Float = financeData.salary * (1 + financeData.payRaise/100.0)
        
        totalValueLabel.text = String(totalValue)
        //print(totalValue)
        
    }


}

