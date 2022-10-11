from flask import Flask, request

app = Flask(__name__)

PASSWORD = "fishy_fish"

flag = "PbI6bI{f1l3s_s4y_3v3ryth1n6}"


@app.route('/')
def index():
	if request.args.get("pass") and PASSWORD in request.args.get("pass"):
		return flag
	else:
		return """
			Пароль: 
				<form>
					<input type="password" name="pass">
					<button type="submit">ага</button>
				</form>
		"""
