def translate_ONP_to_ordinary(phrase):
    #we are splitting string "phrase" into a list, avery element is separate by " "
    phrase=phrase.split()
    #showing split "phrase" list
    print(phrase)
    #setting queue that will contain numbers later used in math operations
    temp_queue=[]
    #setting variable that will contain information about size of "tep_queue"
    lenght_queue=0

    #we will transfer operate with every element form "phrase" list and after operation we will delete certain element from "phrase" list
    #we will do this as long as "phrase" contains no elements
    while(len(phrase)>0):
        
        #if on index 0 at list "phrase" will be "*", program will see it as multiply operator
        if phrase[0]=='*':
            #we will take 2 elements from top of queue (last two elements from list) and multiply them
            #then set result of last math operation on second element from top of queue "temp_queue" (second last index in list)
            temp_queue[lenght_queue-2]=int(temp_queue[lenght_queue-1])*int(temp_queue[lenght_queue-2])
            #now we have to delete top element form queue "temp_queue"
            temp_queue.pop()
            #size of a queue "temp_queue" is reduce by 1
            lenght_queue-=1
            #lets print information that now program works with operator "*"
            print("operator ", phrase[0])
            #then delete first element from "phrase" list, with we used for previous math operation
            #now size of "phrase" list is reduce by 1 and used operator has to be deleted
            phrase.pop(0)

        #if on index 0 at list "phrase" will be "/", program will see it as divided operator
        elif phrase[0]=='/':
            #now element on second last index in "temp_queue" will be result of subtracting  the second item from the end item by the last item from "temp_queue"
            temp_queue[lenght_queue-2]=int(temp_queue[lenght_queue-2])/int(temp_queue[lenght_queue-1])
            #after math operatrion we have to delete top element form queue "temp_queue"
            temp_queue.pop()
            #size of a queue "temp_queue" is reduce by 1
            lenght_queue-=1
            #lets print information that now program works with operator "/"
            print("operator ", phrase[0])
            #then delete first element from "phrase" list, with we used for previous math operation
            #now size of "phrase" list is reduce by 1 and used operator has to be deleted
            phrase.pop(0)
            
        #if on index 0 at list "phrase" will be "-", program will see it as subtraction operator
        elif phrase[0]=='-':
            #element on second last index in "temp queue" will be replaced by result of subtracting the second item from the end item by the last item from "temp_queue"
            temp_queue[lenght_queue-2]=int(temp_queue[lenght_queue-1])-int(temp_queue[lenght_queue-2])
            #after math operatrion we have to delete top element form queue "temp_queue"
            temp_queue.pop()
            #size of a queue "temp_queue" is reduce by 1
            lenght_queue-=1
            #lets print information that now program works with operator "-"
            print("operator ", phrase[0])
            #then delete first element from "phrase" list, with we used for previous math operation
            #now size of "phrase" list is reduce by 1 and used operator has to be deleted
            phrase.pop(0)

        #if on index 0 at list "phrase" will be "-", program will see it as addition operator
        elif phrase[0]=='+':
            #element on second last index in "temp queue" will be replaced by result of adding the two last items from "temp_queue"
            temp_queue[lenght_queue-2]=int(temp_queue[lenght_queue-1])+int(temp_queue[lenght_queue-2])
            #after math operatrion we have to delete top element form queue "temp_queue"
            temp_queue.pop()
            #size of a queue "temp_queue" is reduce by 1
            lenght_queue-=1
            #lets print information that now program works with operator "+"
            print("operator ", phrase[0])
            #then delete first element from "phrase" list, with we used for previous math operation
            #now size of "phrase" list is reduce by 1 and used operator has to be deleted
            phrase.pop(0)
        
        #checking if 0 index element on "phrase" list is number
        #not working on every number, i will change it later
        #(works only with numbers: 0-10, 12, 123, 23, 1234, 234, 34, 12345, 2345, 345, 45, etc)
        elif phrase[0] in '123456789010':
            #displaying information  that now we deal with a number, and displaying number
            print("number ", phrase[0])
            #adding to "temp_queue" number wchich we are currently working with
            temp_queue.append(phrase[0])
            #after adding number to "temp_queue" we have to delete top element form queue "phrase"
            phrase.pop(0)
            #size of a queue "temp_queue" has just increased by 1
            lenght_queue+=1
        #if "phrase" contain other element that was not mentioned before, we cant return correct result
        else:
            #printing information that there is mistake in input string "phrase"
            print("wrong data")
            break
        #after prevoius loop "phrase" shouldnt contain any element
        print(phrase)
        #after prevoius loop "temp_queue" should contain one element-our result
        print(temp_queue)

    #only for testing if program returs propear result
    #at the end queue "temp_queue" must include only one element
    print("lenght of a temporary queue: ", len(temp_queue))
    #at the end this one element from queue "temp_queue" is result we were looking for
    if(len(temp_queue)==1):
        return(temp_queue[0])
    #if size of "temp_queue" is not equal to 1 cant return proper result (input "phrase" is wrong)
    else:
        return("cant calculate")

#testing function "translate_ONP_to_ordinary" with correct exemple of string input "phrase"
print("answer is: ", translate_ONP_to_ordinary("12 2 3 4 * 10 5 / + * +"))
#testing function "translate_ONP_to_ordinary" with incorrect exemple of string input "phrase"
print("answer is: ", translate_ONP_to_ordinary("12 2 a"))
