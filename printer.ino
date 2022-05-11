// This #include statement was automatically added by the Particle IDE.
#include "tt.h"


// This #include statement was automatically added by the Particle IDE.
#include <neopixel.h>

// Icon for birthday messages
#ifndef _cakeline_h_
#define _cakeline_h_

#define cakeline_width  400
#define cakeline_height 54



#endif // _cakeline2_h_

// icon for messages from Silver Lining team
#ifndef _Buddy_h_
#define _Buddy_h_

#define Buddy_width  400
#define Buddy_height 60



#endif // _Buddy_h_

#define PIXEL_COUNT 1
#define PIXEL_PIN D7
#define PIXEL_TYPE WS2812B
Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, PIXEL_TYPE);

int redValue = 255;
int greenValue = 255;
int blueValue = 255;


Thermal printer;

int sendMessage01(String cmd) {
    printer.println(cmd);
    return 1;

}

void setup()
{
    // Initialize printer
    Serial1.begin(19200);
    printer.begin(&Serial1);

    printSth();
    Particle.function("message", sendMessage01);

}

void loop()
{
    delay(1);
}



void printSth(void) {
    printer.println();
    printer.println();
    printer.println("--------------------------------");
    printer.println("Surprise!!!");
    printer.println("================================");
    printer.println();
    printer.println();

}
