//
//  ViewController.h
//  streampoint
//
//  Created by Abhishek Modi on 9/12/15.
//  Copyright (c) 2015 MAKE. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <SpeechKit/SpeechKit.h>
#import "AppDelegate.h"
#import "SocketSend.h"

@interface ViewController : UIViewController <SpeechKitDelegate, SKRecognizerDelegate>
@property (strong, nonatomic) SKRecognizer* voiceSearch;
@property (strong, nonatomic) AppDelegate *appDelegate;
@property (weak, nonatomic) IBOutlet UIButton *RecordButton;
- (IBAction)NextSlide:(id)sender;
- (IBAction)Record_Down:(id)sender;
- (IBAction)Record_UpIn:(id)sender;

@end

