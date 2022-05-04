from sambho.models import Quize,Option
Quize.objects.all()
from django.utils import timezone
q = Quize(question_area='what is your name',published_date=timezone.now())
q.save()
print(q.id)
q.question_area
q.published_date

q.question_area = 'how are you man'
q.save()

Quize.objects.get(id=2)
Quize.objects.get(id=1)
r= Quize.objects.get(pk=1)
r.publisher_recently()