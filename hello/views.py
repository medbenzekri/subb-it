from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Todoitem
from .forms import UploadFileForm
from translator_script import translatorf
# Create your views here.
def home(request):
	return render(request,'page.html')
    


def translate_page(request):
	return render(request,'translate_page.html')

def uploading(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			translatorf(request.FILES['file'])
			return HttpResponseRedirect('translate_page/')

        
                    
            


