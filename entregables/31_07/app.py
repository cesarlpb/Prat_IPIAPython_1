from flask import Flask, request, jsonify, render_template
import time
import random

app = Flask(__name__)

def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def linear_search(arr, x):
    for i, val in enumerate(arr):
        if val == x:
            return i
    return -1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    arr = data['array']
    x = data['target']
    
    arr = sorted(arr)
    
    start_time = time.perf_counter()
    binary_result = binary_search(arr, x)
    binary_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    linear_result = linear_search(arr, x)
    linear_time = time.perf_counter() - start_time

    results = {
        'binary': {'result': binary_result, 'time': binary_time},
        'linear': {'result': linear_result, 'time': linear_time}
    }

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
