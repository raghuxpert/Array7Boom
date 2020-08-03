#Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
#D 100
#W 200
#D means deposit while W means withdrawal.
#Suppose the following input is supplied to the program:
#D 300
#D 300
#W 200
#D 100
#Then, the output should be:
#500

insert = True
deposite = []
withdraw = []

while(insert):
    txn = input("insert next trxn, once done press 'N' : ")
    if txn[0] == 'D':
        deposite.append(int(txn[2:(len(txn))]))
    if txn[0] == 'W':
        withdraw.append(int(txn[2:(len(txn))]))
    if txn[0] == 'N':
        insert = False

print(sum(deposite) - sum(withdraw))
