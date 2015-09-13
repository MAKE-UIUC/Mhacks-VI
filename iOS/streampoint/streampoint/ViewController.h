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
#import <Foundation/Foundation.h>

@import Foundation;

@interface ViewController : UIViewController <SpeechKitDelegate, SKRecognizerDelegate>
@property (strong, nonatomic) SKRecognizer* voiceSearch;
@property (strong, nonatomic) AppDelegate *appDelegate;
@property (weak, nonatomic) IBOutlet UIButton *RecordButton;
- (void)connection:(NSURLConnection *)connection didReceiveData:(NSData*)data;
- (IBAction)NextSlide:(id)sender;
- (IBAction)Record_Down:(id)sender;
- (IBAction)Record_UpIn:(id)sender;
- (void)createRequest:(NSString*)url singleval:(NSString*)val singlearg:(NSString*)arg;
@property (weak, nonatomic) IBOutlet UIImageView *ImageDisp;
@property (weak, nonatomic) IBOutlet UIButton *AskWolfram;

@end

