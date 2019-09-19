from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .Neurotoxin import Classifier, reform_bin_class
from .models import point, male_compl, male_lethal, female_compl, female_lethal
from .data_refactoring import transform_post_to_ml,transform_post_to_mc,transform_post_to_fc,transform_post_to_fl
import numpy as np


# Create your views here.
def menu(request):
    return render(request, 'liver/menu.html')


def form(request, id_form):
    if id_form == 1:
        form_file = 'liver/male_let.html'
    elif id_form == 2:
        form_file = 'liver/male_comp.html'
    elif id_form == 3:
        form_file = 'liver/female_let.html'
    elif id_form == 4:
        form_file = 'liver/female_comp.html'
    else:
        raise Http404('Error, called number not specified')
    return render(request, form_file)


def calculate(request, id_type):
    data = request.POST
    # male_lethality
    if id_type == 1:
        # translation of sent data
        ml_data,error_list = transform_post_to_ml(data)
        # если данные некорректны - возврат назад
        if len(error_list):
            return render(request,'liver/male_let.html', {'error_message': error_list})
        # иначе - продолжает
        cls = Classifier()
        whole_query = male_lethal.objects.all()
        yt = []
        xt = []
        for t in whole_query:
            yt.append(t.result)
            xt.append([t.prot_time, t.mgp, t.meld, t.vrvp, t.bkk, t.mfa, t.sad, t.dad, t.score])
        try:
            pnt = point.objects.get(network_type='male_lethal')
            cls.set_network(np.array(xt), np.array(yt), 6, pnt.x, pnt.y)
            acc = pnt.acc_total
        except:
            tr_acc, te_acc, to_acc, xp, yp = cls.search_network(xt, yt, 6)
            pnt = point(network_type='male_lethal', x=xp, y=yp,
                        acc_train=tr_acc, acc_test=te_acc, acc_total=to_acc)
            pnt.save()
        result = cls.predict(ml_data)[0][1]

    # male_complications
    elif id_type == 2:
        # translation of sent data
        mc_data,error_list = transform_post_to_mc(data)
        # если данные некорректны - возврат назад
        if len(error_list):
            return render('liver/male_comp.html', {'error_message': error_list})
        # иначе - продолжает
        cls = Classifier()
        whole_query = male_compl.objects.all()
        yt = []
        xt = []
        # здесь баг с базой - булевские поля представалены в таблице как интовые
        for t in whole_query:
            yt.append(t.result)
            xt.append([t.lpvp, t.sd, t.chr_pan, t.psycho, t.activity, t.pg, t.dad])
        try:
            pnt = point.objects.get(network_type='male_compl')
            cls.set_network(np.array(xt), np.array(yt), 6, pnt.x, pnt.y)            
            acc = pnt.acc_total
        except:
            tr_acc, te_acc, to_acc, xp, yp = cls.search_network(xt, yt, 6)
            pnt = point(network_type='male_compl', x=xp, y=yp,
                        acc_train=tr_acc, acc_test=te_acc, acc_total=to_acc)
            pnt.save()
        result = cls.predict(mc_data)[0][0]

    # female_lethality
    elif id_type == 3:
        # translation of sent data
        fl_data,error_list=transform_post_to_fl(data)
        # если данные некорректны - возврат назад
        if len(error_list):
            return render(request, 'liver/female_lethal.html', {'error_message': error_list})
        # иначе - продолжает
        cls = Classifier()
        whole_query = female_lethal.objects.all()
        yt = []
        xt = []
        for t in whole_query:
            yt.append(t.result)
            xt.append([t.glucose, t.erythrocyte, t.actv, t.css, t.mfa, t.takrolimus, t.methylprednise, t.dad,
                       t.kokraf, t.mdrd, t.score])
        try:
            pnt = point.objects.get(network_type='female_lethal')
            cls.set_network(np.array(xt), np.array(yt), 5, pnt.x, pnt.y)            
            acc = pnt.acc_total
        except:
            tr_acc, te_acc, to_acc, xp, yp = cls.search_network(xt, yt, 5)
            pnt = point(network_type='female_lethal', x=xp, y=yp,
                        acc_train=tr_acc, acc_test=te_acc, acc_total=to_acc)
            pnt.save()
        result = cls.predict(fl_data)[0][1]
        
    # female_complications
    elif id_type == 4:
        # translation of sent data
        fc_data,error_list=transform_post_to_fc(data)
        # если данные некорректны - возврат назад
        if len(error_list):
            return render(request, 'liver/female_comp.html', {'error_message': error_list})
        # иначе - продолжает
        cls = Classifier()
        whole_query = female_compl.objects.all()
        yt = []
        xt = []
        for t in whole_query:
            yt.append(t.result)
            xt.append([t.actv, t.css, t.lp, t.mgp, t.zs, t.fv, t.ibs, t.csn, t.chr_pan, t.dad, t.emot_coeff,
                       t.comp_mor, t.score])
        try:
            pnt = point.objects.get(network_type='female_compl')
            cls.set_network(np.array(xt), np.array(yt), 5, pnt.x, pnt.y)            
            acc = pnt.acc_total
        except:
            tr_acc, te_acc, to_acc, xp, yp = cls.search_network(xt, yt, 5)
            pnt = point(network_type='female_compl', x=xp, y=yp,
                        acc_train=tr_acc, acc_test=te_acc, acc_total=to_acc)
            pnt.save()
        result = cls.predict(fc_data)[0][0]

    else:
        raise Http404('Error, called number not specified')

    return render(request, 'liver/calculate.html', {'resp':result,'id':id_type})


def details(request):
    # male lethality
    cls = Classifier()
    whole_query = male_lethal.objects.all()
    yt = []
    xt = []
    for t in whole_query:
        yt.append(t.result)
        xt.append([t.prot_time, t.mgp, t.meld, t.vrvp, t.bkk, t.mfa, t.sad, t.dad, t.score])
    try:
        pnt = point.objects.get(network_type='male_lethal')
        m_l_train = pnt.acc_train
        m_l_test = pnt.acc_test
    except:
        m_l_train, m_l_test, to_acc, xp, yp = cls.search_network(xt, yt, 6)
        pnt = point(network_type='male_lethal', x=xp, y=yp,
                    acc_train=m_l_train, acc_test=m_l_test, acc_total=to_acc)
        pnt.save()
    m_l_details = cls.set_network(xt, yt, 6, pnt.x, pnt.y, return_net_data=True)

    # male complications
    whole_query = male_compl.objects.all()
    yt = []
    xt = []
    for t in whole_query:
        yt.append(t.result)
        xt.append([t.lpvp, t.sd, t.chr_pan, t.psycho, t.activity, t.pg, t.dad])
    try:
        pnt = point.objects.get(network_type='male_compl')
        m_c_train = pnt.acc_train
        m_c_test = pnt.acc_test
    except:
        m_c_train, m_c_test, to_acc, xp, yp = cls.search_network(xt, yt, 6)
        pnt = point(network_type='male_compl', x=xp, y=yp,
                    acc_train=m_c_train, acc_test=m_c_test, acc_total=to_acc)
        pnt.save()
    m_c_details = cls.set_network(xt, yt, 6, pnt.x, pnt.y, return_net_data=True)

    # female lethality
    cls = Classifier()
    whole_query = female_lethal.objects.all()
    yt = []
    xt = []
    for t in whole_query:
        yt.append(t.result)
        xt.append([t.glucose, t.erythrocyte, t.actv, t.css, t.mfa, t.takrolimus, t.methylprednise, t.dad,
                   t.kokraf, t.mdrd, t.score])
    try:
        pnt = point.objects.get(network_type='female_lethal')
        f_l_train = pnt.acc_train
        f_l_test = pnt.acc_test
    except:
        f_l_train, f_l_test, to_acc, xp, yp = cls.search_network(xt, yt, 5)
        pnt = point(network_type='female_lethal', x=xp, y=yp,
                    acc_train=f_l_train, acc_test=f_l_test, acc_total=to_acc)
        pnt.save()
    f_l_details = cls.set_network(xt, yt, 5, pnt.x, pnt.y, return_net_data=True)

    # female complications
    cls = Classifier()
    whole_query = female_compl.objects.all()
    yt = []
    xt = []
    for t in whole_query:
        yt.append(t.result)
        xt.append([t.actv, t.css, t.lp, t.mgp, t.zs, t.fv, t.ibs, t.csn, t.chr_pan, t.dad, t.emot_coeff,
                   t.comp_mor, t.score])
    try:
        pnt = point.objects.get(network_type='female_compl')
        f_c_train = pnt.acc_train
        f_c_test = pnt.acc_test
    except:
        f_c_train, f_c_test, to_acc, xp, yp = cls.search_network(xt, yt, 5)
        pnt = point(network_type='female_compl', x=xp, y=yp,
                    acc_train=f_c_train, acc_test=f_c_test, acc_total=to_acc)
        pnt.save()
    f_c_details=cls.set_network(xt,yt,5,pnt.x,pnt.y,return_net_data=True)

    return  render(request, 'liver/details.html', {'ml_data':m_l_details, 'mc_data':m_c_details,
                                                   'fl_data':f_l_details, 'fc_data':f_c_details })