from flask import flash, render_template, redirect, request
from FlaskExercise import app, logger
from flask import Flask


@app.route('/')
def home():
    log = request.values.get('log_button')
    if log:
        if log == 'info':
            logger.info('No issue.')
        elif log == 'warning':
            logger.warning('Warning occurred.')
        elif log == 'error':
            logger.error('Error occurred.')
        elif log == 'critical':
            logger.critical('Critical error occurred.')
    return render_template(
        'index.html',
        log=log
    )
