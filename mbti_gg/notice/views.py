from django.shortcuts   import render, redirect
from user.views import context_login
from .models            import *

# Create your views here.

def index(request) :
    n_boards = Notice.objects.all().order_by('-nno')
    context = {
        'n_boards' : n_boards
    }
    print(">>>>>>>>>> notice index")
    return render(request, 'notice/index.html', context)

def writing_form(request) :
    print(">>>> writing_form")
    return render(request, 'notice/writing_form.html')

def writing(request) :
    print(">>>> notice writing")
    title   = request.POST['title']
    writer  = request.POST['writer']
    content = request.POST['content']
    print('debuge - ', title, writer, content)

    notice_db = Notice(title=title, writer=writer, content=content)
    notice_db.save()

    return redirect('notice_index')

def read(request) :
    print('>>>> notice read')
    nno = request.GET['nno']
    print('debuge - ', nno)
    # select
    n_board = Notice.objects.get(nno=nno)
    # update - commit - save()
    n_board.viewcnt = n_board.viewcnt + 1
    n_board.save()

    context = {
        'n_board' : n_board
    }
    return render(request, 'notice/read.html', context)

def delete(request) :
    print('>>>>> notice delete')
    nno = request.GET['nno']
    print('>>>>> debuge :', nno)
    # orm - delete
    n_board = Notice.objects.get(nno=nno)
    n_board.delete()

    return redirect('notice_index')

def modify(request) :
    print('>>>>> notice modify')
    nno     = request.GET['nno']
    title   = request.GET['title']
    content = request.GET['content']
    print('>>>>> debuge :', nno, title, content)
    # orm - update
    n_board = Notice.objects.get(nno=nno)
    n_board.title = title
    n_board.content = content
    n_board.save()

    return redirect('notice_index')