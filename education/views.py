from django.shortcuts import render,HttpResponse,redirect
from education.models import CustomerInfo,Article,Comment
from django.forms import ModelForm
from django.contrib.auth import authenticate,login,logout
from education import permissions
from education.models import Area
import json
def acc_login(request):
    if request.method == 'POST':
         username=request.POST.get('username')
         password=request.POST.get('password')
         m=authenticate(username=username,password=password)
         if m:

             login(request,m)

             return redirect('/showdata')
         else:
             return HttpResponse('error')
    return render(request,'login.html')



class Userinfo(ModelForm):
    class Meta:
        model=CustomerInfo
        fields=['id','name','age']
        error_messages={'name':{'required':'不能为空'}

        }

    def __init__(self, *args, **kwargs):
        # self.readonly=['source','consultant']
        super(Userinfo, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
        #     if field in self.readonly:
        #              self.fields[field].widget.attrs.update({
            #             'disabled': True  })

            self.fields[field].widget.attrs.update({
                    'class': 'form-control'
            })

from django.contrib.auth.decorators import login_required


@permissions.check_permission
@login_required
def test(request,*args,**kwargs):

    if request.method == 'GET':

        obj_nid = CustomerInfo.objects.filter(id=args[0]).first()
        obj = Userinfo(instance=obj_nid)
        return render(request, 'edit.html', locals())
    elif request.method == "POST":
        obj_nid2 = CustomerInfo.objects.filter(id=args[0]).first()
        obj = Userinfo(request.POST, instance=obj_nid2)
        if obj.is_valid():
            obj.save()

            return redirect('/showdata')
        else:
            return render(request, 'edit.html', locals())


@login_required
def  add_list(request):

    if request.method == 'GET':
        obj = Userinfo()
        return render(request, 'add.html', locals())
    else:
        obj = Userinfo(request.POST)
        if obj.is_valid():

            obj.save()
        return redirect('/add')

@login_required
def show_data(requeset):
    obj=CustomerInfo.objects.all()
    return render(requeset,'table_list.html',locals())

@permissions.check_permission
@login_required
def delete(request,*args,**kwargs):
      CustomerInfo.objects.filter(id=args[0]).delete()

      return redirect('/showdata')

def acc_logout(request):
    logout(request)
    return redirect("/login/")


def article_list(request):
    obj=Article.objects.get(id=1)
    obj_comment=Comment.objects.all()
    obj_comment_list={}

    for row in  obj_comment:


         obj_comment_list[row.id]=[row.comment,row.user.name,row.ctime,row.reply,{'child':[]}]
    print(obj_comment_list)
    #
    for k,v in obj_comment_list.items():
          if v[3]:
    #
             obj_comment_list[v[3].id][4]['child'].append(v)
          else:
              obj_comment_list[k]=v

    print('2----',obj_comment_list)
    new_obj={}
    for k, v in obj_comment_list.items():

        if v[3]:
            pass
        else:
            new_obj[k]=v

    print('new_obj======',new_obj)
    new_obj_list=[]
    # for k,v in new_obj.items():
    #
    #     if v[4]['child']==[]:
    #         new_obj[k][4]=None
    for k, v in new_obj.items():
        new_obj_list.append(v)
    #
    print('1111',new_obj_list)
    respon = ''
    for row in new_obj_list:

            tpl = """
              <div class="item ">
                  <div class="title">%s<a href="">%s</a>发表于<a >%s</a></div>
              
                  
                  <div class="content">%s</div>
              </div>
              """


            content=row[4]['child']
            content=func(content,row[1])
            tpl=tpl%(row[0],row[1],row[2],content)
            respon += tpl

    # print('000',respon)

    return render(request,'article_list.html',locals())

def func(content,x):
    respon = ''
    for i in content:
         tpl = """
                <div style="margin-left: 20px ;color: red" >
                    <div class="title">回复@<a >%s</a>%s<a href="">%s</a>发表于<a >%s</a></div>
                    
                    <div class="content">%s</div>
                </div>
                """
         content = func(i[4]['child'],i[1])

         tpl = tpl % (x,i[0],i[1],i[2], content)
         respon+=tpl

    return respon


def demo(request):
    # obj_comment = Comment.objects.all()
    # obj_list=[]
    # for row in obj_comment:
    #     row2={}
    #     row2[row.id]={'id':row.id,'comment':row.comment,'ctime':row.ctime,'relpy':row.reply,'child':[]}
    #     obj_list.append(row2)
    # print(obj_list)

    from django.contrib.auth.hashers import make_password, check_password

    from education.models import UserProfile
    object=UserProfile.objects.get(email='131448410@136.com')

    kk = '123456'
    v = make_password(kk, '123')
    object.password=v
    object.save()


    return HttpResponse('ok')

def city(request):
    if request.method=='POST':
        print(request.POST)
    return render(request,'citycode.html')
def province(request):

    province_list=list(Area.objects.filter(nextname__isnull=True).values_list('id','name'))
    # print(province_list)
    return HttpResponse(json.dumps(province_list))


def city1(request,pid):

    cityList = list(Area.objects.filter(nextname_id=pid).values_list('id','name'))


    return HttpResponse(json.dumps(cityList))
def county(request,pid):
    county_list = list(Area.objects.filter(nextname_id=pid).values_list('id','name'))
    # print(county_list)
    return HttpResponse(json.dumps(county_list))
