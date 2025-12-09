from flask import Flask
app = Flask(__name__)

@app.route('/')
def index() :
    return 'root : /'

# 동적 라우트
#@app.route('/user/list')
#@app.route('/user/view')
#@app.route('/user/create')

# /user | /user/ -> 동적라우트에 할당되지 않습니다
# /user
# /user/
# /user/<otion>

@app.route('/user/<option>')
def user(option):
    return option

# 하나의 함수에 정적 라우트 복수 할당
@app.route('/user')
@app.route('/user/')
def user_base():
    return 'user base'

# 정적, 동적 라우트 동시 할당
@app.route('/board')
@app.route('/board/')
@app.route('/board/<option>')
def board(option=None) :
    if option :
        data = option
    else :
        data = 'base'
    return data

# 동적 라우팅시, 변수에 할당되는 데이터는 str 타입입니다
@app.route('/reply/<option>/<number>')
def reply(option,number):
    try:
        print(type(number))
        number = int(number)
    except Exception as e:
        print(e)
        return '숫자를 입력해야합니다!!!'
    return f'option : {option} \n number : {number}'

# 동적 라우팅시, 변수에 할당되는 데이터는 타입을 고정
# /mypage/view/1
# /mypage/edit/5
# /mypage/delete/10
# /mypage/delete/abc -> 라우트하지 않음
@app.route('/mypage/<string:option>/<int:number>')
def mypage(option,number):
    print('option', type(option))
    print('number', type(number))
    return f'option : {option} \n number : {number}'

if __name__ == '__main__' :
    app.run(debug=True)