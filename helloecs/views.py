from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>You have successfully created an ECS EC2-launch type app!</H1><H2>Congratulations on learning the ECS EC2 fundamentals in the AWS Certified Architect Associate course!</H2>")