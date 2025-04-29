from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def process_project_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')

    if button_python:
        return redirect("https://github.com/YigitTalhaGurbuz123/Korsan-Avi-Oyunu.git")  
    elif button_discord:
        return redirect("https://github.com/YigitTalhaGurbuz123/Talha-Bot.git")  
    elif button_html:
        return redirect("https://github.com/YigitTalhaGurbuz123/Diary.git")  
    elif button_db:
        return redirect("https://github.com/YigitTalhaGurbuz123/Diary") 

    return render_template('index.html')



@app.route('/feedback', methods=['POST'])
def process_feedback_form():
    email = request.form.get('email')  
    text = request.form.get('text')  
    print("mail")
    

    with open("feedback.txt", "a") as file:
        file.write(f"Email: {email}\n")
        file.write(f"Yorum: {text}\n")
        file.write("-" * 40 + "\n")


    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
