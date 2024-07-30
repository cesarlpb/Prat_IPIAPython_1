from django.shortcuts import render
import time

def longest_unique_substring(s):
    n = len(s)
    max_len = 0
    start = 0
    seen = {}
    for end in range(n):
        if s[end] in seen:
            start = max(start, seen[s[end]] + 1)
        seen[s[end]] = end
        max_len = max(max_len, end - start + 1)
    return max_len

def evaluate_password_strength(password):
    length = longest_unique_substring(password)
    if length >= 8:
        return "Alta fortaleza"
    elif length >= 5:
        return "Media fortaleza"
    else:
        return "Baja fortaleza"

def home(request):
    print("home")
    return render(request, 'home.html')

def result(request):
    query = request.GET.get('q', '')
    start_time = time.time()
    longest_length = longest_unique_substring(query)
    strength = evaluate_password_strength(query)
    end_time = time.time()
    execution_time = end_time - start_time

    context = {
        'query': query,
        'longest_length': longest_length,
        'strength': strength,
        'execution_time': execution_time
    }
    return render(request, 'result.html', context) #prueba

