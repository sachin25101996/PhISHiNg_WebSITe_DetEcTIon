from django.shortcuts import render
import pickle
import sklearn
# Create your views here.

loaded_model = pickle.load(open('./static/phishing_logistic_regression.pkl', 'rb'))

def homepage(request):
    return render(request,'index.html')

# Create your views here.
def url_predict(request):
    url=[]
    if request.method=="POST":
        url=request.POST['search']
        print(url)
    result = loaded_model.predict([url])
    color=''
    message=''
    if result[0]=='bad':
        message='Phishing URL'
        #color='red'
    else:
        message='Clean URL'
        #color='green'
    return render(request,'index.html',{'output':message,'text_color':color})

	
