# Django

> **Django**는 웹사이트를 쉽고 빠르게 개발할 수 있도록 도움을 주는 *웹 프레임워크*이다. 프랜차이즈 시스템 아래에서 더 쉽게 카페 창업을 할 수 있는 것을 생각하면 쉽게 이해할 수 있다. Django는 분류된 파일들에 대해 일련의 단계를 수행하는 코드로 구성되어 있다.

![django](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction/basic-django.png)

## MVT(Model View Template)
|elements|description|
|---|---|
|URLs|분리된 뷰 함수를 작성하여 각각의 리소스 유지보수를 용이하게 함|
|View|HTTP 요청을 수신하고 응답을 반환하는 요청 처리 함수|
|Models|응용프로그램의 데이터 구조를 정의하고 db의 기록을 관리하고 쿼리하는 방법을 제공하는 파이썬 객체|
|Templates|파일의 구조 및 레이아웃 정의, 실제 내용을 보여주는 데 사용되는 텍스트 파일|

## Django project
```
# 1. install Django 및 시작
# project를 시작할 폴더에 장고 설치
pip install django

# project file 생성
django-admin startproject 00_Intro

# 2. app 생성
python manage.py startapp first_app

# app을 생성했으면 먼저 intro 폴더의 
# settings.py > installed_app 부분에 first_app을 입력한다.(출생신고)
```


3. views.py
- `from django.shortcuts import render, redirect, get_object_or_404)`
- `from django.views.decorators.http`로부터 `require_safe, require_http_methods(), require)POST`를 import할 수 있다.

|method|description|
|---|---|
|`require_http_methods(['POST', 'GET'])`|view 함수가 특정한 method만 허용하도록 함|
|`require_POST`|POST 방식의 request만 처리|
|`require_safe`|GET, HEAD method 방식만 처리|

- `HttpResponse 또는 render`을 사용해서 function view를 만든다. (함수 생성)
- `redirect`를 이용하여 특정한 페이지(html)로 이동할 수 있게 만들 수 있다.
- 각 함수 위에 `@require_safe` 형식으로 표시

### 로그인을 해야만 볼 수 있는 조건 생성
- `from django.contrib.auth.decorators import login_required`
- `views.py`의 함수들 위에 `@login_required`를 표시하면 특정 함수의 기능/페이지가 login이 된 상태에서만 조회 가능하게 설정됨


4. tempaltes 생성과 html 파일 생성
- views.py 안의 함수들은 개개인의 html 파일을 templates이라는 폴더를 만들어 생성해야 한다.
- html 파일 내에는 실제로 웹에서 어떻게 보일지를 조정한다.
- `render(request, 'lotto.html', context)`에서 context를 마지막에 붙였다. return 이전에 context를 dictioanry로 지정해주면 지정된 값은 lotto.html 파일에서 사용될 수 있다. 따라서 코드로 계산된 값들이나 텍스트 등을 html로 끌고 와서 사용할 수 있게 된다.

5. urls.py

|urls.py|description|
|---|---|
|intro의 urls.py|`include`를 이용해 first_app과 추후의 다른 second_app에 포함되는 function view를 분권화함. first와 second의 views를 명확히 구분시키기 위함.|
|first_app의 urls.py|자동으로 생성되지 않기 때문에 따로 만들어준다. first_app에 포함되는 함수들을 urlpattern에 넣는다.|

- 따라서 intro의 urls.py는 `path('first_app', include(first_app.urls))`로
- first_app의 urls.py 파일에 있는 views를 불러온다.
- first_app의 urls.py 파일에서 views는 views.py로부터 불러온다.

6. runserver
`python manage.py runserver`을 실행하고 고정값 http://127.0.0.1:8000/ 뒤에 customizing 해주면 원하는 function view의 html 파일을 웹으로 확인할 수 있다.
- (Ex) http://127.0.0.1:8000/first_app/lotto/

### base.html
- 반복되는 !DOCTYPE format을 base.html로 통일시킴
- 여러 html 파일을 하나의 base.html 파일에서 이용
- 프로젝트 파일 BASE_DIR의 바로 하위에 있는 templates에 base.html을 생성한다.
- `<nav>` 안에 `<li>`, `<a>`를 이용해서 list의 요소들을 클릭하면 특정 html을 하이퍼링크로 이동하게 설정 가능.

```
# base.html에 사용될 html 파일들에는 base.html을 extend 해줌
{% raw %}{% extends "base.html" %} {% endraw %}  

# base.html 파일에서 정의한 block을 다른 html 파일에 사용하여 base.html에서 사용될 내용을 각각의 html 파일의 block에 지정한다.

{% raw %}
{% block content %}
<h1>This is index</h1>
{% endblock content %}
{% endraw %}
```

## Form
- 입력폼 html 생성
- 입력 값 검증
- 검증 통과했으면 사전타입으로 제공

### 변수
생성한 app의 urls.py와 views.py에서 함수를 생성할 때 keyword argument를 삽입하고 싶을 때
```
# urls.py
# 변수명이 name인데 변수를 받으면 str로 인식한다.
path('hello/<str:name>/', views.hello)

# views.py
# urls.py에서 변수를 지정한 함수는 keyword argument로 name을 받는다.
# 변수가 변함에 따라 변수가 사용된 콘텐츠도 변할 수 있다.
def hello(request, name):
    print(name)   # keyword argument
    message = f'반갑습니다. {name}'
    return render(request, 'user_input/hello.html', {
        'message': message,
    })
```
- 변수를 이용한 text 또는 다른 형태의 값들은 context를 이용하여 base.html 파일에서도 사용할 수 있다.

### Form과 input

아래의 표에 나오는 tag는 ping.html의 block에서 사용되는 예시

|tag|description|
|---|---|
|`<form action="/user_input/pong/">`|입력한 input 값을 보내는 목적지가 "/user_input/pong/"이다.|
|`<label for="username">Username: </label>`|label값/ 입력창 옆에 표시되는 label명 지정|
|`<input type="text" id="username" name="username">`|text `type`으로 input을 받고 지정한 label값은 `id` "username"과 연동되며 key값이 `name`으로 지정한 username, value값이 입력한 값이 됨|
|`<input type="submit" value="Enter">`|"Enter"이라는 버튼을 누르면 입력된 값을 지정된 목적지로 보낼 수 있다. form tag 내에 위치해 있어야 작동이 된다.|
|`request.GET['key']`|위에서 name을 지정한 input tag의 사용법에 따르면 입력값은 dictionary 형태로 지정된다. views.py 파일에서 입력받은 value값을 이용하기 위해서는 request.GET['key명']을 통해 value의 값을 받아야 한다. 지정한 value 값을 context로 지정하면 목적지인 pong.html에서도 이 입력값들을 사용할 수 있다.|

- input의 타입은 html의 input type attribute value이며, text, color, date, password, submit 등 다양하다.


## models.py
> 데이터에 대한 하나의 정보 소스
> 일반적으로 `models.py`에 생성되는 model class들은 하나의 DB 테이블에 mapping된다.

```
from django.contrib.auth import get_user_model()

User = get_user_model()

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
```

|models.py|description|비고|
|---|---|---|
|`get_user_model()`|현재 활성화된 User model 반환/ 그렇지 않은 경우 User(default) model 반환/ 객체 인스턴스를 리턴한다.|항상 유효한 사용자 모델 객체를 리턴한다는 보장 X|
|`settings.AUTH_USER_MODEL`|외래키 모델을 전달할 때 문자열로 전달함. |항상 올바른 사용자 모델을 얻을 수 있음|
|`on_delete=models.CASCADE`|상위 필드가 삭제될 때 하위 필드도 저절로 삭제되게 하는 것|
|`models.ForeignKey`|테이블과 테이블을 연결하기 위해 사용되는 외래키로, 테이블의 필드 중에서 다른 테이블의 행과 식별할 수 있는 키이다.|

### Timestamp 생성시간, 수정시간 자동 생성
```
created_at = models.DateTimeField(auto_now_add=True, null=True)
updated_at = models.DateTimeField(auto_now=True)
```


## forms.py
```
from django import forms
from .models import Student
```
- django에서 forms를 import하고 models.py의 모델을 불러온다.

```
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age']
```
- model form을 이용하여 모델을 가져오고, `field` 또는 `exclude`를 통해 필드의 값을 재정의하여 불러올 수 있다.
- `views.py`에서 `form = StudentForm`으로 지정한 form을 rendering 해주어 context로 보내면 form을 사용하고자하는 html 파일로 context를 보낸다.
-html 파일에서는 `{{ form }}`으로 불러낼 수 있는데, 더 깔끔하게 `{{ form.as_p }}` 또는 `<table>{{ form.as_table }}</table>`로 form을 불러낼 수 있다.

### views.py에서 ModelForm을 호출하였을 때 form의 유효성 확인
- `form = StudentForm()`과 같이 빈 form을 받거나, `form = StudentForm(data=request.POST)`와 같이 

## Crawling
> JSON은 데이터 형식이며 json 형식의 데이터에서 필요한 데이터를 crawling 해올 수 있다.
> BeautifulSoup으로부터 `soup.select_one('#id')`를 통해 id에 해당하는 내용을 가져올 수 있다. 
> F12키 -> copy -> copy selector을 이용해 #id의 값을 복사할 수 있다.