from django.shortcuts import render
  from django.views.generic import TemplateView

# Create your views here.
  def home(request):
      """
      http://127.0.0.1:8000/で表示されるページ
      """
      return render(request, 'home.html')
# Create your views here.
