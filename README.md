# inkywhat-writer
Tool to display arbitrary text on a Pimoroni Inky wHAT e-paper display.

Takes any text as input, turns it into an Inky wHAT compatible image,
then displays it. Requires PIL, the Inky pHAT/wHAT libraries, Python.

Current version designed for use with dailyschedule.sh script, example
output from which is provided; turns first five lines (date header)
red while printing the rest black.

Uses PIL variant of Robey's Tom Thumb 4x6 font:
https://robey.lag.net/2010/01/23/tiny-monospace-font.html
