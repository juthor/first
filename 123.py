
#Likelion=7

#if Likelion==6:
#    print("likelion")

#else:
#    print("nop")


#######################################################################################################

#likelion=8
#if likelion==8:
#    print("멋쟁이 사자처럼 8기 입니당")
#elif likelion==7:
#    print("멋쟁이 사자처럼 7기 입니당") 
#else : 
#    print("멋쟁이 사자처럼 6기 이하이거나 멋쟁이 사자처럼 해당 기수 학생이 아닙니당")


#######################################################################################################

#likelion=1
#while likelion:
#    print("멋쟁이 사자처럼", likelion, "기 입니다.")

#    likelion=likelion+1
#    if(likelion==7):
#        print("2019 멋쟁이 사자처럼 7기!!")
#        break;


########################################################################################################

lion_we_know={'hyojin', 'seol', 'eunjin', 'kijung'}
lion_meet={'hyojin', 'eunjin', 'bak'}

for lion in lion_meet:
    if lion in lion_we_know:
        print("hello")
    else:
        print("first meet")