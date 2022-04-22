from flask import Flask
from flask import render_template, redirect, request, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate_risk', methods=['GET', 'POST'])
def risk():
    if request.method == 'POST':
        risk_score = 0
        form = request.form
        # pull in textbox values
        name = form['org_name']
        email = form['org_email']
        #pull in radio button values
        backups = float(request.form['backup_svr'])
        pen_test = float(request.form['pen_test'])
        # pull in drop down lists
        industry = float(request.form['industry'])
        
        #pull in checkbox list
        nat_disaster = 0
        nat_dis_list = form.getlist('natural_disasters')
        for i in nat_dis_list:
                if(i == 'hurricane'):
                    nat_disaster = nat_disaster + 5
                
                if(i == 'tornado'):
                    nat_disaster = nat_disaster + 5

                if(i == 'flood'):
                    nat_disaster = nat_disaster + 5
        

        #debugging
        print(name)
        print(email)
        print(backups)
        print(nat_disaster)
        
        #calculate risk score
        risk_score = backups + pen_test + industry + nat_disaster
        
        #may not need this
        org = name + " || " + email
        
        return render_template('risk.html', org_details = org, risk_value=risk_score)
    return render_template('risk.html')



if __name__ == '__main__':
    app.run(debug=True)