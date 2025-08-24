from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

class IndexView(View):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        """统一管理所有上下文数据"""
        context = {}
        context['students']=Student.objects.all()    #使用标准查询集
        context['form']=StudentForm()
        return context

    def get(self, request,*args,**kwargs):
        """处理get请求"""
        return render(request, self.template_name,context=self.get_context_data())

    def post(self, request):
        '''处理post请求'''
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')   #简化重定向

        context = self.get_context_data()
        context['form']=form    #覆盖为带错误的表单
        return render(request, self.template_name, context)