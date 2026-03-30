from flask import Flask, render_template

app = Flask(__name__)

# 루트 주소(/)로 접속하면 복잡한 물리 시뮬레이션을 보여줍니다.
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # host='0.0.0.0'으로 설정해야 다른 학생들이 접속할 수 있습니다.
    # port는 5000번을 사용합니다.
    app.run(host='0.0.0.0', port=5000, debug=True)