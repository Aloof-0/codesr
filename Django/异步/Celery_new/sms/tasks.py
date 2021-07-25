from Celery_new.main importcelery_app

@celery_app.task(name="code")
def code(mobile):
    return result