//
//  ViewController.m
//  streampoint
//
//  Created by Abhishek Modi on 9/12/15.
//  Copyright (c) 2015 MAKE. All rights reserved.
//

#import "ViewController.h"
@import UIKit;

@interface ViewController ()

@end

const unsigned char SpeechKitApplicationKey[] = {0xd0, 0x2d, 0xc7, 0xf6, 0x45, 0x58, 0x06, 0xde, 0x2d, 0xf9, 0x76, 0x3f, 0x31, 0xc0, 0xaa, 0x5d, 0xf2, 0x1e, 0xe5, 0x77, 0x3c, 0x9f, 0x57, 0xbf, 0xc0, 0x14, 0xa4, 0xae, 0x5a, 0xe8, 0x80, 0x2b, 0x15, 0x47, 0x21, 0x5b, 0x9f, 0x27, 0x39, 0xcc, 0x20, 0xaf, 0x0c, 0x51, 0x6f, 0xb6, 0xae, 0x62, 0xd4, 0x93, 0xd9, 0x11, 0x32, 0x30, 0xd0, 0xf3, 0x44, 0x74, 0xa1, 0x9e, 0x5c, 0x21, 0xc9, 0x72};

NSString* imagePath = @"";
NSMutableArray* images;
UIImage *defInput;
NSString* buffer = @"";
NSInteger imgAt = 1;
CGPoint finger;
NSInteger scroly = 0;
NSInteger dtap = 0;


SocketSend *comms;

BOOL recordState = FALSE;

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.appDelegate = (AppDelegate *)[UIApplication sharedApplication].delegate;
    [self.appDelegate setupSpeechKitConnection];
    comms = [[SocketSend alloc] init];
    defInput = [self.ImageDisp image];

    comms->host = @"172.17.162.128";
    comms->port = 4252;
    images = [[NSMutableArray alloc] initWithCapacity:3];

//    UISwipeGestureRecognizer* nextImg = [[UISwipeGestureRecognizer alloc] initWithTarget:self action:@selector(imgScrollRight:)];
    

    [comms setup];
//    [comms open];

    // Do any additional setup after loading the view, typically from a nib.
}

-(void)imgScrollRight:(UISwipeGestureRecognizer*) sender{
    imgAt += 1;
    NSLog(@"RIGHT SWIPE DETECTED");
    if (imgAt == 3){
        imgAt = 0;
    }

    NSURL *url = [NSURL URLWithString:images[imgAt]];
    NSData *imgdata = [NSData dataWithContentsOfURL:url];
    UIImage *img = [[UIImage alloc] initWithData:imgdata];
    CGSize size = img.size;
    [self.ImageDisp setImage:img];


}

- (void)recognizerDidBeginRecording:(SKRecognizer *)recognizer {

    return;
}

- (void)recognizerDidFinishRecording:(SKRecognizer *)recognizer {

    return;
}

- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event {
    finger = [[[touches allObjects] objectAtIndex:0] locationInView:self];
    NSLog(@"FINGER AT POSITION");
}

- (IBAction)QuoteMe:(id)sender {
    NSString* wolfq = [[@"t " stringByAppendingString:self.RecordButton.currentTitle] stringByAppendingString:@"\r\n"];
    [comms writeOut:wolfq];
    return;

}

- (IBAction)imgScroll:(id)sender {
    dtap = 0;
    scroly += 1;
    NSLog(@"Scroly = %d", scroly);
    if (scroly == 3){
        scroly = 0;
        [self imgScrollRight:NULL];
    }
}



- (void)recognizer:(SKRecognizer *)recognizer didFinishWithResults:(SKRecognition *)results {
    long numOfResults = [results.results count];

    if (numOfResults > 0) {
        // update the text of text field with best result from SpeechKit
        //self.theLabel.text = [results firstResult];
        [self.RecordButton setTitle: [results firstResult] forState:(UIControlStateNormal)];
        NSString *keyword = [results firstResult];
        NSString *keywordReq = [@"t " stringByAppendingString:keyword];
        keywordReq = [keywordReq stringByAppendingString:@"\r\n"];
        [self createRequest:@"http://104.131.69.59:5000/process-keyword" singleval:@"text" singlearg:keyword];
    }

    if (self.voiceSearch) {
        [self.voiceSearch cancel];
    }
}

- (void)recognizer:(SKRecognizer *)recognizer didFinishWithError:(NSError *)error suggestion:(NSString *)suggestion {
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Error"
                                                    message:[error localizedDescription]
                                                   delegate:nil
                                          cancelButtonTitle:@"OK"
                                          otherButtonTitles:nil];
    [alert show];
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)NextSlide:(id)sender {
    dtap += 1;
    scroly = 0;
    if (dtap == 2){
        dtap = 0;
        //reset to red
        //self.RecordButton.backgroundColor = [UIColor colorWithRed:255.0f/255.0f
          //                                              green:0.0f/255.0f
            //                                             blue:0.0f/255.0f
              //                                          alpha:1.0f];

        imagePath = [@"i " stringByAppendingString:images[imgAt]];
        imagePath = [imagePath stringByAppendingString:@"\r\n"];
        [comms writeOut:imagePath];

        //[self.RecordButton setTitle: @"Record" forState:(UIControlStateNormal)];
        //[self.ImageDisp setImage:defInput];
        //[self.AskWolfram setTitle:@"AskWolfram" forState:UIControlStateNormal];
    }
}



- (IBAction)Record_Down:(id)sender {
    self.voiceSearch = [[SKRecognizer alloc] initWithType:SKSearchRecognizerType
                                               detection:SKShortEndOfSpeechDetection
                                                language:@"en_US"
                                                delegate:self];

    //Setting to recording green
    self.RecordButton.backgroundColor = [UIColor colorWithRed:39.0f/255.0f
                                                        green:153.0f/255.0f
                                                         blue:1.0f/255.0f
                                                        alpha:1.0f];
    recordState = TRUE;
    [self.RecordButton setTitle: @"Listening" forState:(UIControlStateNormal)];
}

- (IBAction)Record_UpIn:(id)sender {
    [self.voiceSearch stopRecording];
    recordState = FALSE;

    [self.RecordButton setTitle: @"Processing" forState:(UIControlStateNormal)];
    //Setting to All good blue
    self.RecordButton.backgroundColor = [UIColor colorWithRed:2.0f/255.0f
                                                        green:65.0f/255.0f
                                                         blue:255.0f/255.0f
                                                        alpha:1.0f];
}

- (void)createRequest:(NSString*)url singleval:(NSString*)val singlearg:(NSString*)arg{

    NSMutableData *response;
    NSString *post = [NSString stringWithFormat:@"text=%@", arg];
    NSData *postData = [post dataUsingEncoding:NSASCIIStringEncoding allowLossyConversion:YES];
    NSString *postLength = [NSString stringWithFormat:@"%lu", (unsigned long)[post length]];

    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] initWithURL:[NSURL URLWithString:@"http://104.131.69.59:5000/process-keyword"]];

    [request setHTTPMethod:@"POST"];
    [request setValue:postLength forHTTPHeaderField:@"Content-Length"];
    [request setHTTPBody:postData];

    NSURLConnection *theConnection = [[NSURLConnection alloc] initWithRequest:request delegate:self];
    [theConnection start];

    NSLog(@"\n\nCONNECTION %@", theConnection);

}

- (void)connection:(NSURLConnection *)connection didReceiveData:(NSData*)data{
    NSLog(@"\n\n ------ DID RECIEVE DATA ------ \n\n");
    NSError *error = nil;
    NSMutableString *DataString = [[NSMutableString alloc] initWithData:data encoding:nil];
    NSLog(@"%@", DataString);
        NSLog(@"\n\n ------ PRINTING NICE JSON ------ \n\n");
    NSArray *jsonArray = [NSJSONSerialization JSONObjectWithData:data options:kNilOptions error:&error];
    NSLog(@"%@", jsonArray);
    if (error){
        [self.RecordButton setTitle: @"KUUUZZZ.. waiy u do dis" forState:(UIControlStateNormal)];
        return;

    }
    NSLog(@"TRYING SOME NONSENSE \n\n");
    images[0] = [[[jsonArray valueForKey:@"results"] valueForKey:@"img"] objectAtIndex:0];
    images[1] = [[[jsonArray valueForKey:@"results"] valueForKey:@"img"] objectAtIndex:1];
    images[2] = [[[jsonArray valueForKey:@"results"] valueForKey:@"img"] objectAtIndex:2];

    imagePath = images[0];
    [self.AskWolfram setTitle:[[[jsonArray valueForKey:@"results"] valueForKey:@"wolfram"] objectAtIndex:0] forState:(UIControlStateNormal)];
    NSLog(@"%@", imagePath);

    NSURL *url = [NSURL URLWithString:imagePath];
    NSData *imgdata = [NSData dataWithContentsOfURL:url];
    UIImage *img = [[UIImage alloc] initWithData:imgdata];
    CGSize size = img.size;
    [self.ImageDisp setImage:img];

}

- (void)connection:(NSURLConnection *)connection didReceiveResponse:(NSURLResponse *)response:(NSData*)data{
    NSLog(@"\n\nRECEIVED POST\n\n");
}
- (IBAction)ChangeSlide:(id)sender {
    [comms writeOut:@"sn\r\n"];
}

- (IBAction)SendWolfram:(id)sender {
    NSString* wolfq = [[@"t " stringByAppendingString:self.AskWolfram.currentTitle] stringByAppendingString:@"\r\n"];
    [comms writeOut:wolfq];
    return;
}
@end