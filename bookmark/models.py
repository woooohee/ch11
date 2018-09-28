from django.db import models
# 장고에서
# 테이블은 (django.dbmodels.Model을 상속받는) 클래스로 정의하고,
# 테이블 컬럼은 클래스 변수로 정의함


class Bookmark(models.Model):
    # id 필드(Integer, PK, Auto Increment)는 자동 생성됨
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

def __str__(self):
    return self.title