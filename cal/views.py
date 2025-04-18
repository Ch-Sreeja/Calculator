
from django.shortcuts import render

def calculator_view(request):
    result = ''
    expression = ''
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            # Safe evaluation: only allow numbers and math symbols
            result = str(eval(expression))
        except:
            result = 'Error'
    return render(request, 'cal/index.html', {
    'result': result,
    'expression': expression,
    'button_list': ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", "C", "=", "+"]
})



