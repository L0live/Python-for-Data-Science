from datetime import datetime as dt

currentTime = dt.now()
inSeconds = "{:,}".format(currentTime.timestamp())
inSciNotation = "{:.2e}".format(currentTime.timestamp())
simpleDate = currentTime.strftime("%b %d %Y")

lineBegin = "Seconds since January 1, 1970:"
lineEnd = "in scientific notation"
print(lineBegin, inSeconds, "or", inSciNotation, lineEnd)
print(simpleDate)
