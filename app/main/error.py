from .import main
from flask import render_template


@main.app_errorhandler(404)
def four_Ow_four(error):
    """
    function to render not found page
    """
    return render_template('fourOwfour.html'),404