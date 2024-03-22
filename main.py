nric = input('Enter an NRIC number: ')

# Type your code below
NRIC_Error = "NRIC is invalid."
nric = nric.upper()
prefix = nric[0]
digits = nric[1:8]
suffix = nric[8:]
suffix_stringTS = "JZIHGFEDCBA"
suffix_stringFG = "XWUTRQPNMLK"
digit_str = "2765432"
if len(nric) != 9:
  print(NRIC_Error)
elif not digits.isdigit():
  print(NRIC_Error)
elif len(suffix) != 1 or not suffix.isalpha():
    print(NRIC_Error)
elif prefix not in "TSFG":
    print(NRIC_Error)
else:
     total = 0
     for i in range(len(digits)):
       total += int(digit_str[i])* int(digits[i])
     if prefix in "GT":
         total = total + 4
     if prefix in "TS":
       suffix_pos = total % 11
       suffix_check = suffix_stringTS[suffix_pos]
       if suffix_check == suffix:
         print("NRIC is valid.")
       else:
         print(NRIC_Error)

     elif prefix in "FG":
      suffix_pos = total % 11    
      suffix_check = suffix_stringFG[suffix_pos]
      if suffix_check == suffix:
          print("NRIC is valid.")
      else:
          print(NRIC_Error)


      