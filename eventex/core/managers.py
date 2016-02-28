from django.db import models


class KindQuerySet(models.QuerySet):
    def emails(self):
        return self.filter(kind=self.model.EMAIL)

    def phones(self):
        return self.filter(kind=self.model.PHONE)


class PeriodQuerySet(models.QuerySet):
    MID_DAY = '12:00'
    def at_morning(self):
        return self.filter(start__lt=self.MID_DAY)

    def at_afternoon(self):
        return self.filter(start__gte=self.MID_DAY)


PeriodManager = models.Manager.from_queryset(PeriodQuerySet)