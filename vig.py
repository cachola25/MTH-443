from mappings import char_to_int_a0 as c2i
from mappings import int_to_char_a0 as i2c
skip = 4
# message = "TWV CFJ FAH XOC PBH ZMH ZZQ BUX SXI DLH VSZ RFX YIG KMZ ZHW GLQ QMO IQF RFK HVM KLQ GIC HYI IXS PCI HQK PRU GVU GJM DCI FAL VSZ WME VAS JXZ HUM BKI DXZ XWE KBH ZMH ZZQ BUX SXI DUB XVV CFA HXG GVQ MAC WEX QKL WHZ RST JSB KVM WPG HZS Z"
# message = "TWV CFJ FAH XOC PBH ZMH ZZQ BUX SXI DLH VSZ RFX YIG KMZ ZHW GLQ QMO IQF RFK HVM KLQ GIC HYI IXS PCI HQK PRU GVU GJM DCI FAL VSZ WME VAS JXZ HUM BKI DXZ XWE KBH ZMH ZZQ BUX SXI DUB XVV CFA HXG GVQ MAC WEX QKL WHZ RST JSB KVM WPG HZS Z"
# message = "YMI INB CXX YUM MPU EOI XGE IJE ZQH WGN HUQ SHS BIW PQL EQB KWL IJY FPC BKX SXU UZE RQQ HKS GXO RHR HVS PGQ HHP VWB XRV DAZ IEO PIV LVL MKU JYR MAW GIK NBC PIB WUP MYU IKE YYF IST QFM PRE AEP VBY SJV WUV SZQ ARM SYW SMZ ZOW XNF ISV OES RSO EXC PBL YWQ RXY WNH INE TBE LFS LVL SQN FIS VSQ GMP LIJ EVR XCQ LVI FMJ RVL SQG XCW QBD MXV BIC XC"
# message = "OTG WRV RHU GXO XUQ UEK VYO TSE NYU NSI YSH MHB BUR ZTR CCD DAK MHC ALI OJZ UOT JYC KFN KIO THO GWK Z"
message = "LTG ZRH JGJ WYE DRK XUC SLK SCG UGZ KWI LXF CSA QUL JRA SWD HZZ HBG NHU MAH RUY PIY LES SSG SLJ RAG DOH NWZ CXK WGZ MIT LJR ABW JSZ SEZ KKD BJO KOZ GQS GJW VOK WVG L"
message = message.replace(" ", "")
print(len(message))
occurences = dict()
multiple = []
diffs = []
for i in range(0, len(message),3):
    char = message[i:i+3]
    if char in occurences:
        occurences[char] += 1
    else:
        occurences[char] = 1

for occur in occurences:
    if occurences[occur] > 1:
        print(occur, occurences[occur])
        multiple.append(occur)

reset =  message
for occur in multiple:
    first = message.find(occur)
    message = message[first+3:]
    second = message.find(occur)
    second += first + 3
    print(f"Difference is {second - first} for {occur}")
    diffs.append(second - first)
    message = reset

# find common divisors between the differences
        
char = " "
for j in range(skip):
    for i in range(j,len(message),skip):
        print(message[i], end=char)
    print()
    
# other = "APR OOF THA TAL LPO SIT IVE INT EGE RSA REI NTE RES TIN GAS SUM ETH ECO NTR ARY THE NBY THE WEL LOR DER ING PRI NCI PLE THE REI SAL OWE STN ONI NTE RES TIN GPO SIT IVE INT EGE RBU THE YTH ATS PRE TTY INT ERE STI NGA CON TRA DIC TIO N"
# other = "ISE EAL ITT LES ILH OUE TTO OFA MAN SCA RAM OUC HES CAR AMO UCH EWI LLY OUD OTH EFA NDA NGO THU NDE RBO LTA NDL IGH TNI NGV ERY VER YFR IGH TEN ING MEG ALI LEO GAL ILE OGA LIL EOG ALI LEO GAL ILE OFI GAR OMA GNI FIC OIM JUS TAP OOR BOY NOB ODY LOV ESM EHE SJU STA POO RBO YFR OMA POO RFA MIL YSP ARE HIM HIS LIF EFR OMT HIS MON STR OSI TY"
other = "IFA HOT DOG ISM ADE FRO MTH EWO RST STU FFC OMI NGF ROM MEA TTH ENA VEG GIE DOG MUS TBE MAD EFR OMA LLT HEW ORS TST UFF FRO MVE GET ABL ESA NDW HAT ONE ART HIS THA T"
other = other.replace(" ", "")
print("\n\n")
char = " "
for j in range(skip):
    for i in range(j,len(message),skip):
        print(other[i], end=char)
    print()
        
    
