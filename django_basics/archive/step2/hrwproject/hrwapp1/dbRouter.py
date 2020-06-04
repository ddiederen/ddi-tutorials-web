class Hrwapp1DBRouter:
    """
    A router to control all database operations on models in the
    hrwapp1 application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read hrwapp1 models go to hrwapp1_db.
        """
        if model._meta.app_label == 'hrwapp1':
            return 'hrwapp1_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write hrwapp1 models go to hrwapp1_db.
        """
        if model._meta.app_label == 'hrwapp1':
            return 'hrwapp1_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the hrwapp1 app is involved.
        """
        if obj1._meta.app_label == 'hrwapp1' or \
           obj2._meta.app_label == 'hrwapp1':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the hrwapp1 app only appears in the 'hrwapp1_db'
        database.
        """
        if app_label == 'hrwapp1':
            return db == 'hrwapp1_db'
        return None