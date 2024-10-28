from flask import Flask, render_template, redirect, url_for, flash
from forms import UniqueDigitsForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def has_unique_digits(number):
    return len(str(number)) == len(set(str(number)))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UniqueDigitsForm()
    if form.validate_on_submit():
        number = form.number.data
        if has_unique_digits(number):
            flash('усі цифри унікальні!', 'success')
            return render_template('output.html', unique=True)
        else:
            flash('не всі цифри унікальні', 'danger')
            return render_template('output.html', unique=False)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
