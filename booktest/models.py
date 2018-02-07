from django.db import models
from tinymce.models import HTMLField

class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete=False)
    def create(self,btitle,bpub_date):
        b=BookInfo()
        b.btitle=btitle
        b.bpub_date=bpub_date
        b.bread=0
        b.bcommet=0
        b.isDelete=False
        return b

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField()

    def __str__(self):
        return self.btitle

    class Meta:
        db_table = 'bookinfo'

    # books1 = models.Manager()
    # books2 = BookInfoManager()

class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=1000)
    hbook=models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname

class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parea = models.ForeignKey('self', null=True, blank=True)

class Test1(models.Model):
    content = HTMLField()


