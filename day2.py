id = input("Enter Student ID: ")
email_id = input("Enter Student Email ID: ")
password = input("Enter Password: ")
code = input("Enter Referral Code: ")
if (id[0]== "C") and (id[1]=="S") and (id[2]=="E") and (id[3]=="-") and ('0'<=id[4]<='9')and ('0'<=id[5]<='9')and ('0'<=id[6]<='9'):
    if ('a' <= email_id[0] <= 'z') or ('A' <= email_id[0] <= 'Z') or ('0' <= email_id[0] <= '9') and email_id.count(
            "@") == 1  and email_id.count(" ") == 0 and email_id[-1]=='u' and email_id[-2]=='d' and email_id[-3]=='e' and email_id[-4]==".":
     if (len(password)>=8) and ('A' <= password[0] <= 'Z') and password.count(" ")==0 and  (
     ('0' <= password[1] <= '9') or
     ('0' <= password[2] <= '9') or
     ('0' <= password[3] <= '9') or
     ('0' <= password[4] <= '9') or
     ('0' <= password[5] <= '9') or
     ('0' <= password[6] <= '9') or
     ('0' <= password[7] <= '9')
   ):
         if (code[0]=="R") and (code[1]=="E") and (code[2]=="F") and ('0'<=code[3]<='9')and ('0'<=code[4]<='9') and (code[5]=='@'):
             print("ACCEPTED")
         else:
             print("REJECTED")
     else:
         print("REJECTED")
    else:
         print("REJECTED")
else:
         print("REJECTED")