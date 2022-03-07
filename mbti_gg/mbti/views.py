from django.shortcuts import render


# Create your views here.
def index(request):
    print('>>> MBTI - Index')

    if 'mbti' in request.GET:
        selected_mbti = request.GET['mbti']
    else:
        selected_mbti = ''

    context = {
        'title': 'MBTI',
        'nav_link_active': 'mbti',
        'selected_mbti': selected_mbti,
    }
    return render(request, 'mbti/index.html', context)

