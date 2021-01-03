## DESCRIPTION

API server designed to fetch data for sunrise and sunset app: https://github.com/xRomasik/sunrise-sunset-app-frontend \
Created mainly to move API keys from frontend to backend so nobody can access them.

## QUICK START

Setup the frontend part. \
Clone the repository using `git clone` command and the repository link. \
`cd` into cloned repository. \
Run `python -m venv venv` to create your virtual environment. \
Run `venv\Scripts\activate` to activate venv. \
Run `pip install -r requirements.txt` to install all requirements. \
Finally, you can start the server using `python server.py`. \

Make sure, that the frontend part is also running and open http://localhost:3000 in your browser. \
Now choose desired country and date, click on SHOW and it should work. You can also check the server response in your terminal.
