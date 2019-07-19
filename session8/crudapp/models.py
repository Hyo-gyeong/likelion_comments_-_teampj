from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    contents = models.CharField(max_length=500)

    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.contents

class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replys', null=True)
    contents = models.CharField(max_length=500)

    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.contents