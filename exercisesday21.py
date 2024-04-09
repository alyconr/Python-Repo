quality_standard = int(input("Enter the quality standard: "), 2)

# validate if the quality standard is   a binary number

quality_bin = (bin(quality_standard))[2:]


for i in quality_bin:
    if i == "1":
        acpeted = True
    else:
        acpeted = False
        break

if acpeted is True:
    print("The quality standard is accepted")
else:
    print("The quality standard is not accepted")