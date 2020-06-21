//
//  ViewController.swift
//  BasicButtons
//
//  Created by Robert John on 6/16/20.
//  Copyright © 2020 Robert John. All rights reserved.
//
// https://www.simplifiedios.net/xcode-text-field-tutorial-ios-using-swift/

// https://docs.swift.org/swift-book/GuidedTour/GuidedTour.html

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    @IBOutlet weak var Button1: UIButton!
    @IBOutlet weak var Button2: UIButton!
    @IBOutlet weak var ButtonBasicsLabel: UILabel!
    @IBOutlet weak var UserTextBox: UITextField!
    @IBOutlet weak var DisplayTextLabel: UILabel!
    
    var UserTestBoxString: String = ""
    
    @IBAction func ActionButton1(_ sender: Any) {
        print("Pressed Button 1")
        UserTestBoxString = UserTextBox.text!
        print(UserTestBoxString)
    }
    
    @IBAction func ActionButton2(_ sender: Any) {
        print("Pressed Button 2")
        UserTestBoxString = UserTextBox.text! // First time I did not include this, and you will not get updated user Stings
        DisplayTextLabel.text = "You Entered: \(UserTestBoxString)"
    }
    

}

