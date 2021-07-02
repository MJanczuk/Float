

def Dash():
    print("--------------")

def HexFPP(HexInput):
    # Do przechowywania liczby wykorzystuje się 32 bity – 1 bit znaku (S), 7 bitów wykładnika (E) i 24 bity mantysy (M):
    # MMMM MMMM MMMM MMMM MMMM MMMM SEEE EEEE
    # (-1)^S * 2^(E-64) * M/268435456
    MM = (HexInput & 0xFFFFFF00) >> 8
    SS = HexInput & 0x00000080
    EE = HexInput & 0x0000007F
    #print("Mantysa:"+str(MM))
    #print("Sign:"+str(SS))
    #print("Exponent:"+str(EE))
    Sign = (-1)**SS
    Eksponens = 2**(EE-64)
    Mantys = MM/0x1000000
    #print(Sign)
    #print(Eksponens)
    #print(Mantys)
    return(Mantys*Eksponens*Sign)

def HexIEEE(HexInp):
    # Do przechowania liczby wykorzystuje się 32 bity – 1 bit znaku (S), 8 bitów wykładnika (E) i 23 bity mantysy (M):
    # SEEE EEEE EMMM MMMM MMMM MMMM MMMM MMMM
    # Liczba = (-1)S * 2E-127 * (1+0.1*(M/8388608))
    SS = (HexInp & 0x80000000) != 0
    EE = (HexInp & 0x7F800000) >> 23
    MM = HexInp & 0x007FFFFF
    #print("Mantysa:"+str(MM))
    #print("Sign:"+str(SS))
    #print("Exponent:"+str(EE))
    #Dash()
    Sign = (-1)**SS
    Eksponens = 2**(EE-127)
    Mantys = 1+(MM/0x800000)
    #print(Sign)
    #print(Eksponens)
    #print(Mantys)
    return (Mantys*Eksponens*Sign)

def swap32(x):
    return (((x << 24) & 0xFF000000) |
            ((x <<  8) & 0x00FF0000) |
            ((x >>  8) & 0x0000FF00) |
            ((x >> 24) & 0x000000FF))

def AnalyzeHex(Hex):
    SHex = swap32(Hex)
    print("IEEE:"+str(HexIEEE(Hex))+" Swap:"+str(HexIEEE(SHex)))
    print("FPP:"+str(HexFPP(Hex))+" Swap:"+str(HexFPP(SHex)))
    Dash()  
Inp = int(("40 91 ca 6f").replace(" ",""),16)
AnalyzeHex(Inp)

#AnalyzeHex(0x4091ca6f)

