# inkywhat-writer
Tool to display arbitrary text on a Pimoroni Inky wHAT e-paper display.

Takes any text as input, turns it into an Inky wHAT compatible image,
then displays it. Requires PIL, the Inky pHAT/wHAT libraries, Python.

Current version designed for use with dailyschedule.sh script, example
output from which is provided; turns first five lines (date header)
red while printing the rest black.

Uses PIL variant of Robey's Tom Thumb 4x6 font:
https://robey.lag.net/2010/01/23/tiny-monospace-font.html

# Usage
At its simplest, inkywhat-writer takes text and prints it to the wHAT.

$ ./inkywhat-writer.py < scheduleexample.txt

The Tom Thumb font doesn't exactly cover the full UTF-8 character set,
though, so you'll likely need to pass your text through iconv first:

$ iconv -f UTF-8 -t ISO-8859-1//TRANSLIT scheduleexample.txt |\
./inkywhat-writer.py

If, like me, you're using the output of dailyschedule.sh as the text
to print, there's another step: getting rid of those wind-direction
arrows that iconv will just mojibake into a question mark:

$ sed 's/← \|→ \|↓ \|↑ \|↘ \|↙ \|↖ \|↗ //g' scheduleexample.txt |\
iconv -f UTF-8 -t ISO-8859-1//TRANSLIT | ./inkywhat-writer.py

If you're *not* using the output of dailyschedule.sh as the text to
print, then this version of inkywhat-writer probably isn't the best:
it automatically makes the first five lines print in red, which looks
great for dailyschedule.sh but will look daft for anything without a
five-line header.
