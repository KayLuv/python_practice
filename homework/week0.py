def function(x,list):
    sortList =  sorted(list)
    sum = 0;
    for i in range(len(list)):
        sum += list[i]
        if(sum > x):
            print i
            break;
function(10,[1,1,1,1,2,5])