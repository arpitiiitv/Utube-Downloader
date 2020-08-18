from flask import Flask, render_template , request , send_file
import pafy
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():

    try:
        url = request.form["videolink"]
        type = request.form["downloadtype"]
        # filename = pafy.new(url).getbest(preftype='mp4').download(quiet=False)
        # print(type(filename) + "ARPIT")
        return send_file('profilePic.jpg' , as_attachment=True)

    except Exception as e:
        print(e)
        return "Please try again"


if __name__ == '__main__':
    app.run(debug=True)
