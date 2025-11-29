from django.db import models

# Create your models here.
class DSATopics(models.Model):
    topic_name = models.CharField(max_length=200)

    def patterns(self):
        if self.id:
            return DSAPattern.objects.filter(topic_id=self.id)

class DSAPattern(models.Model):
    topic = models.ForeignKey(DSATopics, on_delete=models.RESTRICT)
    pattern_name = models.CharField(max_length=200)

    def questions(self):
        if self.id:
            return DSAPatternQuestions.objects.filter(pattern_id = self.id)

class DSAPatternQuestions(models.Model):
    pattern = models.ForeignKey(DSAPattern, on_delete=models.RESTRICT)
    question_heading = models.CharField(max_length=1000)
    question_URL = models.URLField(null=True, blank=True)
    solved = models.BooleanField(default=False)
    solved_date = models.DateTimeField(null=True, blank=True)

    def have_url(self):
        return self.question_URL != None
    
    