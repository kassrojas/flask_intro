# Flask

- Can use python to build backend servers
- Flask is a micro framework for building servers
  - Django is a large framework for building servers

## Installation

**BEFORE** installing _Flask_ :

- `cd into_your_project's_folder`
- `python3 -m venv venv` to create virtual environment
  - where the 2nd `venv` is whatever name you want for your virtual environment folder
  - Examples:
    - `python3 -m venv myVenv`
    - `python3 -m venv myProjectEnv`
- $ `. venv/bin/activate` where `venv` is the name of your virtual environment folder
  - terminal should now display `(venv) ~/your_project`
- ensure `pip --version` shows python verson 3.0+
  - Finally, **install flask** :
    - `pip install flask`

## Virtual Environment Key Notes

- venv manages files which are **not** yours
- venvs are _ephemeral infrastructure_
  - temporary resources or components that are **created dynamically** and **destroyed** as needed
- Place **your** files such as `main.py` directly in `myProject` or `myProjec/src`
  - When working with _Flask_ :
    - Do **not** name your application `flask.py` as this will conflict with _Flask_ itself
- _Can_ have multiple venvs for the same project
  - allows devs to test code with different versions of of Python or libraries your project depends on

## Flask

- To run the application:

  - `export FLASK_APP=hello.py` where `hello.py` is the name of your main file
  - `flask run` : _similar to `npm run start` for ReactJS_
    - `Debug mode: off` means that flask will **NOT** update changes from source code
    - `FLASK_ENV=development` or `export FLASK_DEBUG=1` turns `Debug mode: on`

- `render_template('index.html')` requires that we have a `templates` dir with all our `html` files contained in them
- create `static` folder for static files (such as css and js)
  - `url_for('static', filename='style.css')`
