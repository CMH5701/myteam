from django.db import models

# Create your models here.

#자유게시판 
class Free(models.Model):
    p_title = models.CharField(max_length=200)
    user = models.ForeignKey('account.Profile', on_delete=models.CASCADE, null = True)
    p_date = models.DateTimeField('data published')
    p_body = models.TextField()
    p_photo = models.ImageField(upload_to='images/', blank = True)
    hashtags = models.ManyToManyField('main.Hashtag', blank = True, null=True, editable=True)

    def __str__(self) : 
        return self.p_title

#좋아요
class Free_Like(models.Model) : 
    p_id = models.ForeignKey(Free, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('account.Profile', on_delete=models.CASCADE, null = True)
    p_like = models.ManyToManyField('account.Profile', related_name='p_likes', blank=True)
    p_likes = models.CharField(max_length=20, null = True, blank = True)

#조회수    
class Free_Clip(models.Model) : 
    p_id = models.ForeignKey(Free, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('account.Profile', on_delete=models.CASCADE, null = True)
    p_clip = models.ManyToManyField('account.Profile', related_name='p_clip', blank=True)
    p_clicks = models.PositiveIntegerField(default=1, verbose_name='조회수')

    @property
    def p_update_counter(self) :
        self.p_clicks += 1 
        self.save() 

#댓글
class p_comment(models.Model) :
    def __str__(self) :
        return self.text

    p_id = models.ForeignKey(Free, on_delete=models.CASCADE, null=True, related_name='p_comments')
    text = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now=True)
    name = models.ForeignKey('account.Profile', on_delete=models.DO_NOTHING, null = True)
    p_parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null = True) 