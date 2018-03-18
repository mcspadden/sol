import time

millis = int(time.time() * 1000)  # time from unix epoch in milliseconds according to your device (UTC)
JDUT = 2440587.5 + (millis / 86400000)  # Convert millis to Julian Date (UT) 8.64*10^7 = 86400000
T = (JDUT - 2451545.0) / 36525  # offset from J2000 epoch (UT)
TwoT = T * T  # T^2
ThreeT = TwoT * T  # T^3
FourT = ThreeT * T  # T^4
TTUTC = 69.184 + 59 * T - 51.2 * TwoT - 67.1 * ThreeT - 16.4 * FourT  # Terrestrial Time - UTC (32.184 + 37 = 69.184)
JDTT = JDUT + (TTUTC / 86400) # finding the Julian Date in terrestrial time
MTC = 24 % (24 * (((JDTT - 2451549.5) / 1.0274912517) + 44796.0 - 0.0009626)) # finding mtc
now = time.strftime("%H:%M:%S", time.gmtime(MTC)) # formatting mtc
print("MTC:" + now)
LMST = MTC - 13750.987068 # show calculation for last number
LMSt = time.strftime("%H:%M:%S", time.gmtime(LMST)) # formatting mtc
print(LMSt)

millis = millis / 1.02749125170
MSD = time.strftime("%H:%M:%S", time.gmtime(millis))
print(MSD)
