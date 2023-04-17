# from django.db import models


class MoviesRouter:
    # default_app_list = []
    #
    # def db_for_read(self, model: models.Model, **_hints):
    #     if model._meta.app_label in self.default_app_list:
    #         return "default"
    #     return "default"
    #
    # def db_for_write(self, model: models.Model, **_hints):
    #     if model._meta.app_label in self.default_app_list:
    #         return "sync_mongo"
    #     return "default"
    #
    # # noinspection PyMethodMayBeStatic
    # def allow_relocation(self, _obj1: models.Model, _obj2: models.Model, **_hints):
    #     return True
    #
    # # noinspection PyMethodMayBeStatic
    # def allow_migrate(self, _db, _app_label, _model_name=None, **_hints):
    #     return True
    #
    # def allow_syncdb(self, _db, model: models.Model):
    #     if model._meta.app_label in self.default_app_list:
    #         return False
    #     return True
    pass
