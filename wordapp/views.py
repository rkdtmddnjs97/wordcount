from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')
def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary={}
    for word in word_list:
        #increase
        if word in word_dictionary:
            word_dictionary[word] +=1
           
        #넣어주기
        else:
            word_dictionary[word]=1
            if word=="시발"or"새끼"or"병신"or"개새끼"or"시발놈"or"씹"or"개병신"or"시발새끼"or"씨발"or"씨팔"or"ㅅㅂ"or"ㅄ"or"좆같네"or"좆까"or"좆"or"fuck"or"시발로마": #이거 적는데 저도 눈이 아프네요 죄송합니다 ㅠㅠ
                return render(request, 'warning.html')
    
    return render(request,'count.html',{'fulltext':full_text, 'total':len(word_list),'dictionary':word_dictionary.items()})
