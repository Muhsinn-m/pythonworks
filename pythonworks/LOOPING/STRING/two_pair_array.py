num=[2,3,4,5]
sum=int(input("enter the sum"))
lf=0

rg=len(num)-1

curr_sum=0

while(lf<rg):

    curr_sum[lf]+num[rg]

    if curr_sum==sum:

        print(num[lf],num[rg])

        break

    elif curr_sum>sum:

        rg=rg-1

    elif curr_sum<sum:
        lf=lf+1





    





