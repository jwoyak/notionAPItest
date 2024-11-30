from flask import Flask, render_template, request
import re

app = Flask(__name__)

def generate_sigil(statement):
    # Clean the statement
    new_statement = ''.join(dict.fromkeys(statement).keys())

    ### Generate the sigil string ###
    # First make a new statement object
    upper_statement = ''.join(c.upper() for c in new_statement)

    # Remove vowels
    cons_statement = re.sub(r'[AEIOU]', '', upper_statement, flags=re.IGNORECASE)

    # Get rid of spaces
    nospace_statement = cons_statement.replace(" ", "")

    # Get rid of duplicates
    final_statement = ''.join(sorted(set(nospace_statement), key=nospace_statement.index))

    # Return the moidified string
    return final_statement
    
@app.route('/', methods=['GET', 'POST'])
def index():
    sigil="empty"
    if request.method == 'POST':
        statement = request.form['statement']
        sigil = generate_sigil(statement)
        return render_template('index.html', sigil=sigil)
    else:
        return render_template('index.html', sigil="test")
