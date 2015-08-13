from app import app
from app.errors.custom_error_handler import attach_custom_error_handlers
from app.views import RootView

attach_custom_error_handlers()

app.add_url_rule('/',
                view_func=RootView.as_view('root_view'),
                methods=["GET","POST","PUT","DELETE"])