from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/<string:page_name>')
def index(page_name: None):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong'
