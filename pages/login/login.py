from taipy.gui import Markdown, State, navigate

def on_login(state: State, id, login_args):
    username, password = login_args["args"][:2]
    if username is None: # The user canceled the login request
        print("anonymous")
        # return navigate(s, "anonymous")

    state.username = username
    navigate(state, "home")

login_page = Markdown('pages/login/login.md')