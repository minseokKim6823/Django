from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('TITLE', max_length= 100)
    # unique = True는 중복을 허용하지 않겠다는 제약조건, 이처름 unique가 true인 경우에는
    # 기본키를 대신해서 사용할 수 있다.
    # allow_unicode 는 한글 처리 여부지정
    # help_text는 해당 컬럼에 대한 설명 텍스트 지정

    # ***슬러그(SLUG) 개념 : 페이지나 포스트를 설명하는 핵심 키워드(단어)의 집합이다.
    # 웹 개발시에 콘텐츠의 고유 주소로 사용된다. 콘텐츠가 어떤 내용인지를 쉽게 이해 할 수 있도록 해준다
    # 슬러그는 전치사, 조사, 쉼표, 마침표 등을 빼고 띄어쓰기는 하이픈(-)으록 대체해서 만든다.
    # url에 사용함으로써 검색엔진에 더빠르게 검색할 수 있도록 해주며 정확도를 높여준다.

    # SlugField는 디폴트 길이는 50이다,
    slug = models.SlugField('SLUG', unique =True, allow_unicode=True, help_text='타이틀 별칭')
    # CharField 는 한 줄로 입력되는 데이터를 저장하는 필드
    description = models.CharField('DESCRIPTION',max_length=100, blank=True, help_text="포스터 요약 정보")
    # TextField 는 여러 줄로 입력되는 데이터를 저장할 수 있다. 
    content = models.TextField('CONTENT')
    # auto_now_date는 객체가 생성될 때 시각을 자동으로 기록해주는 지 여부 설정
    create_date = models.DateTimeField('CREATE DATE',auto_now_add=True)
    # auto_now는 객체가 데이터베이스에 저장될 때의 시각을 자동으로 기록해주는 지 여부 설정
    # 즉, True인 경우에는 객체의 변경이 있을 때마다 시각이 기록된다.
    modify_date = models.DateTimeField('MODIFY DATE',auto_now=True)

    class Meta:

