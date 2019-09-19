from django.db import models


# Create your models here.
class male_lethal(models.Model):
    result = models.BooleanField()
    prot_time = models.FloatField()
    mgp = models.FloatField()
    meld = models.FloatField()
    vrvp = models.BooleanField()
    bkk = models.BooleanField()
    mfa = models.BooleanField()
    sad = models.FloatField()
    dad = models.FloatField()
    score = models.FloatField()


class female_lethal(models.Model):
    result = models.BooleanField()
    glucose = models.FloatField()
    erythrocyte = models.FloatField()
    actv = models.FloatField()
    css = models.IntegerField()
    mfa = models.BooleanField()
    takrolimus = models.BooleanField()
    methylprednise = models.BooleanField()
    dad = models.IntegerField()
    kokraf = models.FloatField()
    mdrd = models.FloatField()
    score = models.FloatField()


class male_compl(models.Model):
    result = models.IntegerField()
    lpvp = models.FloatField()
    sd = models.IntegerField()
    chr_pan = models.IntegerField()
    psycho = models.IntegerField()
    activity = models.IntegerField()
    pg = models.IntegerField()
    dad = models.IntegerField()


class female_compl(models.Model):
    result = models.BooleanField()
    actv = models.FloatField()
    css = models.IntegerField()
    lp = models.FloatField()
    mgp = models.FloatField()
    zs = models.FloatField()
    fv = models.IntegerField()
    ibs = models.BooleanField()
    csn = models.BooleanField()
    chr_pan = models.BooleanField()
    dad = models.IntegerField()
    emot_coeff = models.FloatField()
    comp_mor = models.IntegerField()
    score = models.FloatField()


class point(models.Model):
    network_type=models.CharField(max_length=20,default='none')
    x = models.IntegerField()
    y = models.IntegerField()
    acc_total = models.FloatField()
    acc_train = models.FloatField()
    acc_test = models.FloatField()


