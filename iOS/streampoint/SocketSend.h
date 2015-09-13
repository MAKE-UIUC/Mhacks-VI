//
//  SocketSend.h
//  streampoint
//
//  Created by Abhishek Modi on 9/13/15.
//  Copyright (c) 2015 MAKE. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface SocketSend : NSObject <NSStreamDelegate> {
@public

    NSString *host;
    int port;
}

- (void)setup;
- (void)open;
- (void)close;
- (void)stream:(NSStream *)stream handleEvent:(NSStreamEvent)event;
- (void)readIn:(NSString *)s;
- (void)writeOut:(NSString *)s;

@end
