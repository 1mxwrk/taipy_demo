from taipy.gui import navigate
from taipy import Gui as tpg

from pages import login_page, home_page

root_md="""
# Taipy demo app
<|navbar|>
<|menu|label=Menu|lov={[('login', 'Log In'), ('app_state', 'App State')]}|on_action=menu_option_selected|>
<|{login_dialog_is_visible}|dialog|title=Form|on_action=show_or_hide_login_dialog|
<|login|>
|>
<|content|>
This application was created with [Taipy](https://www.taipy.io/).
"""

about_md="## About"

pages = {
    "/": root_md,
    "home": home_page,
    "about": about_md
}

username = "Guest"
login_dialog_is_visible = False

def on_login(state, id, login_args):
    username, password = login_args["args"][:2]
    if username is None: # The user canceled the login request
        print("anonymous")
        # return navigate(s, "anonymous")

    state.username = username
    state.login_dialog_is_visible = not state.login_dialog_is_visible
    # navigate(state, "home")

def show_or_hide_login_dialog(state):
    state.login_dialog_is_visible = not state.login_dialog_is_visible

def on_init(state):
    state.username = username
    state.login_dialog_is_visible = False

def menu_option_selected(state, action, info):
    page = info["args"][0]
    if page == 'login':
        state.login_dialog_is_visible = True
    elif page == 'appstate':
        navigate(state, to='/taipy.status.json')

if __name__ == "__main__":
    tpg(pages=pages).run()