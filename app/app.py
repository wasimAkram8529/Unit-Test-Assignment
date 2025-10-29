from flask import Flask, request, jsonify, render_template_string
from .calc import add

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template_string('''
            <html>
            <body>
              <h1>Calculator</h1>
              <form id="add-form">
                <input id="a" type="number" name="a" />
                <input id="b" type="number" name="b" />
                <button id="add-btn" type="button" onclick="doAdd()">Add</button>
              </form>
              <div id="result"></div>
              <script>
                function doAdd(){
                  const a = document.getElementById('a').value;
                  const b = document.getElementById('b').value;
                  fetch(`/api/add?a=${a}&b=${b}`)
                    .then(r => r.json())
                    .then(j => { document.getElementById('result').innerText = j.result; });
                }
              </script>
            </body>
            </html>
        ''')

    @app.route('/api/add')
    def api_add():
        try:
            a = float(request.args.get('a', 0))
            b = float(request.args.get('b', 0))
        except ValueError:
            return jsonify({"error": "invalid input"}), 400
        return jsonify({"result": add(a, b)})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
