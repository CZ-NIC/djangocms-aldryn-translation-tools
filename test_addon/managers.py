from parler.managers import TranslatableManager, TranslatableQuerySet


class SimpleQuerySet(TranslatableQuerySet):
    pass


class SimpleManager(TranslatableManager):
    queryset_class = SimpleQuerySet

    def get_queryset(self):
        qs = SimpleQuerySet(self.model, using=self.db)
        return qs
