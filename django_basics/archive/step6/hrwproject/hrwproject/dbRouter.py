class HrwprojectDBRouter:
    """
    A router to catch all database operations on models except models routed to other databases
    """
    catchall = "hrwproject"    
    from django.conf import settings
    appsWithRouter = list(map(lambda x: str.split(x,sep=".")[0],settings.DATABASE_ROUTERS))
    appsWithRouter.remove(catchall)
    
    def db_for_read(self, model, appsWithRouter=appsWithRouter, **hints):
        """
        Attempts to read hrwproject models go to default.
        """
        if model._meta.app_label not in appsWithRouter:
            return 'default'
        return None

    def db_for_write(self, model, appsWithRouter=appsWithRouter, **hints):
        """
        Attempts to write hrwproject models go to default.
        """
        if model._meta.app_label not in appsWithRouter:
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, appsWithRouter=appsWithRouter, **hints):
        """
        Allow relations: all.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, appsWithRouter=appsWithRouter, **hints):
        """
        Catch all except with other routers.
        """
        if app_label not in appsWithRouter:
            return db == 'default'
        return None