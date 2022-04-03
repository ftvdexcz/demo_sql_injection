from flask import Flask, request, flash, redirect, url_for, render_template
from sql import SQL_Server

app = Flask(__name__)
app.secret_key = 'mykey'

sql = SQL_Server()

login_query = ''


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global login_query
        user = ''
        password = ''
        user = request.form['nm']
        password = request.form['pass']
        # print(user, password)
        flag, login_query = sql.select_by_name_pass(user, password)
        if flag:
            return redirect(url_for('home'))
        else:
            flash('Không tìm thấy tài khoản hoặc mật khẩu trùng')
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        item = ''
        item = request.form['search']
        data, search_query = sql.search_item(item)
        return render_template('home.html', login_query=login_query, search_query=search_query, data=data,  len=len(data))
    else:
        data = []
        return render_template('home.html', login_query=login_query, data=data,  len=len(data))


if __name__ == '__main__':
    app.run(debug=True)
