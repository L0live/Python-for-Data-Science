import datetime

currentTime = datetime.datetime.now()
inSeconds = "{:,}".format(currentTime.timestamp())
inSciNotation = "{:.2e}".format(currentTime.timestamp())
simpleDate = currentTime.strftime("%b %d %Y")

print("Seconds since January 1, 1970:", inSeconds, "or", inSciNotation, "in scientific notation")
print(simpleDate)
