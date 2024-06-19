

from django.shortcuts import render
import math

def calculate_factorials(request):
    numbers = range(3, 9)
    factorials = {n: math.factorial(n) for n in numbers}
    return render(request, 'factorials.html', {'factorials': factorials})

