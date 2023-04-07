from django.db import models
from django.urls import reverse
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

    '''def get_queryset(self):
        return Question.obhects.order_by('-pub_date') Meta에서 사용'''
    # Meta 내부 클래스 : 장고에서는 모델 클래스의 필드는 아니지만 해당 모델에서 필요한 항목을 내부 클래스에서
    # 속성으로 정의해서 사용 할 수 있다. 즉, 모델의 필드 속성과 그 외 속성을 구분하여 

    # Meta 내부 클래스에서 자주 사용하는 속성
        # - ordering : 정렬하기 위하여 사용하는 속성, 따라서 모델의 필드 중에 하나를 지정한다.
        #                디폴트는 오름차순으로, -를 붙여서 내림차순으로 정렬하게된다
        # - db_table : 데이터베이스 테이블 이름을 지정한다. 이 항목을 지정하지 않게 되면 장고에서는
        #               디폴트로 앱명_클래스면(소문자)을 테이블 명으로 지정한다.
        #               현재 디폴트 테이블 명은 blog_post가 된다. 이 디폴트 테이블 명을 바꾸고 싶은 경우에는
        #               db_table 속성을 이용할 수 있다
        # - verbose_name : 사용자가 이해하기 쉬운 모델 객체의 가칭(별칭)을 지정하는 속성, 이 속성을 지정하지 않는 경우
        #                   모델 클래스 명을 변형해서 디폴트 verbose_name으로 사용한다.
        #                   모델 클래스명이 MyPost라고 한다면 디폴트 값은 my post가 된다.
        #                   이 디폴트 값을 변경하고자 할 경우에는 verbose_name 속성을 지정할 수 있다
        # - verbose_name_plural : verbose_name에 대한 복수 명칭을 지정하는 속성
        #               만일 지정하지 않으면 디폴트로 verbose_name + 's'가 사용된다.
        #               위의 예에서 MyPost라고 하면 myposts가 된다. 
    class Meta:
        ordering = ('-modify_date','title')
        db_table = 'my_post'
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # reverse()함수는 URL 패턴을 만들어 주는 내장 함수
        return reverse('blog:post_detail',args = (self.slug,))

