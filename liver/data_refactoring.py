import numpy as np


def is_in_range(value, border):
    """
    checks if sent value is in [0;border]
    :param value:
    number for check
    :param border:
     upper border where value should be
    :return:
    true if value is in line [0;border]
    false otherwise
    """
    if value > border or value < 0:
        return False
    else:
        return True



def transform_post_to_ml(post_data):
    """
    WARNING: only for use with data from male_let.html. If any inputs names in that will be changed - this
    function needs to be changed according to it!

    Transforms post data from male_let.html into two lists: ls which contains data for  machine learning prediction
    and err_list which contains all encountered errors during parsing of data
    :param post_data:
    dictionary which was posted from male_let.html
    :return: tuple of ls,err_list
    """
    data = post_data
    ls=[]
    err_list=[]
    if 'pt_resp' in data:
        sv = data['pt_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv,50):
                ls.append(sv)
            else:
                err_list.append("Введено значение прот. времени вне диапозона 0-50")
        except:
            err_list.append('Введено некорректное значение прот. времени')
    else:
        err_list.append('Значение прот. времени не указано')

    if 'mgp_resp' in data:
        sv = data['mgp_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 15):
                ls.append(sv)
            else:
                err_list.append("Введено значение МЖП вне диапозона 0-15")
        except:
            err_list.append('Введено некорректное значение МЖП')
    else:
        err_list.append('Значение МЖП не указано')

    if 'meld_resp' in data:
        sv = data['meld_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 50):
                ls.append(sv)
            else:
                err_list.append("Введено значение Meld вне диапозона 0-50")
        except:
            err_list.append('Введено некорректное значение Meld')
    else:
        err_list.append('Значение Meld не указано')

    # bool data
    if 'vrvp_resp' in data:
        ls += [1]
    else:
        ls += [0]

    if 'bkk_resp' in data:
        ls += [1]
    else:
        ls += [0]

    if 'mfa_resp' in data:
        ls += [1]
    else:
        ls += [0]

    # float data part 2
    if 'sad_resp' in data:
        sv = data['sad_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 200):
                ls.append(sv)
            else:
                err_list.append("Введено значение САД вне диапозона 0-200")
        except:
            err_list.append('Введено некорректное значение САД')
    else:
        err_list.append('Значение САД не указано')

    if 'dad_resp' in data:
        sv = data['dad_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 200):
                ls.append(sv)
            else:
                err_list.append("Введено значение ДАД вне диапозона 0-200")
        except:
            err_list.append('Введено некорректное значение ДАД')
    else:
        err_list.append('Значение ДАД не указано')

    if 'score_resp' in data:
        sv = data['score_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 5):
                ls.append(sv)
            else:
                err_list.append("Введено значение Score вне диапозона 0-5")
        except:
            err_list.append('Введено некорректное значение Score')
    else:
        err_list.append('Значение Score не указано')

    return np.array(ls).reshape(1,-1),err_list


def transform_post_to_mc(post_data):
    """
    WARNING: only for use with data from male_comp.html. If any inputs names in that will be changed - this
    function needs to be changed according to it!

    Transforms post data from male_comp.html into two lists: ls which contains data for  machine learning prediction
    and err_list which contains all encountered errors during parsing of data
    :param post_data:
    dictionary which was posted from male_comp.html
    :return: tuple of ls,err_list
    """
    data = post_data
    ls=[]
    err_list = []
    # float data
    if 'lpvp_resp' in data:
        sv = data['lpvp_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 5):
                ls.append(sv)
            else:
                err_list.append("Введено значение ЛПВП вне диапозона 0-5")
        except:
            err_list.append('Введено некорректное значение ЛПВП')
    else:
        err_list.append('Значение ЛПВП не указано')
    # bool data
    if 'sd_resp' in data:
        ls += [1]
    else:
        ls += [0]
    if 'chr_resp' in data:
        ls += [1]
    else:
        ls += [0]
    # int data
    if 'psycho_resp' in data:
        sv = data['psycho_resp']
        try:
            sv = int(sv)
            if is_in_range(sv, 100):
                ls.append(sv)
            else:
                err_list.append("Введено значение индекса психического здоровья вне диапозона 0-100")
        except:
            err_list.append('Введено некорректное значение индекса психического здоровья')
    else:
        err_list.append('Значение индекса психического здоровья не указано')
    if 'activity_resp' in data:
        sv = data['activity_resp']
        try:
            sv = int(sv)
            if is_in_range(sv, 100):
                ls.append(sv)
            else:
                err_list.append("Введено значение физической активности вне диапозона 0-100")
        except:
            err_list.append('Введено некорректное значение индекса физической активности')
    else:
        err_list.append('Значение индекса физической активности не указано')
    if 'pg_resp' in data:
        sv = data['pg_resp']
        try:
            sv = int(sv)
            if is_in_range(sv, 50):
                ls.append(sv)
            else:
                err_list.append("Введено значение ПЖ вне диапозона 0-50")
        except:
            err_list.append('Введено некорректное значение ПЖ')
    else:
        err_list.append('Значение индекса ПЖ не указано')
    if 'dad_resp' in data:
        sv = data['dad_resp']
        try:
            sv = int(sv)
            if is_in_range(sv, 200):
                ls.append(sv)
            else:
                err_list.append("Введено значение ДАД вне диапозона 0-200")
        except:
            err_list.append('Введено некорректное значение ДАД')
    else:
        err_list.append('Значение индекса ДАД неуказано')
    return np.array(ls).reshape(1,-1),err_list


def transform_post_to_fl(post_data):
    """
        WARNING: only for use with data from female_let.html. If any inputs names in that will be changed - this
        function needs to be changed according to it!

        Transforms post data from female_let.html into two lists: ls which contains data for  machine learning prediction
        and err_list which contains all encountered errors during parsing of data
        :param post_data:
        dictionary which was posted from female_let.html
        :return: tuple of ls,err_list
    """
    data = post_data
    err_list = []
    ls = []
    if 'glu_resp' in data:
        sv = data['glu_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 20):
                ls.append(sv)
            else:
                err_list.append("Введено значение глюкозы вне диапозона 0-20")
        except:
            err_list.append('Введено некорректное значение глюкозы')
    else:
        err_list.append('Значение глюкозы не указано')

    if 'ery_resp' in data:
        sv = data['ery_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 10):
                ls.append(sv)
            else:
                err_list.append("Введено значение эритроцитов вне диапозона 0-10")
        except:
            err_list.append('Введено некорректное значение эритроцитов')
    else:
        err_list.append('Значение эритроцитов не указано')

    if 'actv_resp' in data:
        sv = data['actv_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 6):
                ls.append(sv)
            else:
                err_list.append("Введено значение АЧТВ вне диапозона 0-6")
        except:
            err_list.append('Введено некорректное значение АЧТВ')
    else:
        err_list.append('Значение АЧТВ не указано')

    if 'css_resp' in data:
        sv = data['css_resp']
        try:
            sv = int(sv)
            if is_in_range(sv, 100):
                ls.append(sv)
            else:
                err_list.append("Введено значение ХСС вне диапозона 0-100")
        except:
            err_list.append('Введено некорректное значение ХСС')
    else:
        err_list.append('Значение ХСС неуказано')

    # bool data
    if 'mfa_resp' in data:
        ls += [1]
    else:
        ls += [0]

    if 'tkl_resp' in data:
        ls += [1]
    else:
        ls += [0]

    if 'mp_resp' in data:
        ls += [1]
    else:
        ls += [0]

    if 'dad_resp' in data:
        sv = data['dad_resp']
        try:
            sv = int(sv)
            if is_in_range(sv, 200):
                ls.append(sv)
            else:
                err_list.append("Введено значение ДАД вне диапозона 0-200")
        except:
            err_list.append('Введено некорректное значение ДАД')
    else:
        err_list.append('Значение ДАД неуказано')

    if 'kkr_resp' in data:
        sv = data['kkr_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 180):
                ls.append(sv)
            else:
                err_list.append("Введено значение кокараф вне диапозона 0-180")
        except:
            err_list.append('Введено некорректное значение кокраф')
    else:
        err_list.append('Значение кокраф не указано')

    if 'mdrd_resp' in data:
        sv = data['mdrd_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 150):
                ls.append(sv)
            else:
                err_list.append("Введено значение MDRD вне диапозона 0-150")
        except:
            err_list.append('Введено некорректное значение MDRD')
    else:
        err_list.append('Значение MDRD не указано')

    if 'score_resp' in data:
        sv = data['score_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 5):
                ls.append(sv)
            else:
                err_list.append("Введено значение Score вне диапозона 0-5")
        except:
            err_list.append('Введено некорректное значение Score')
    else:
        err_list.append('Значение Score не указано')

    return np.array(ls).reshape(1, -1), err_list


def transform_post_to_fc(post_data):
    """
    WARNING: only for use with data from female_comp.html. If any inputs names in that will be changed - this
    function needs to be changed according to it!

    Transforms post data from female_comp.html into two lists: ls which contains data for  machine learning prediction
    and err_list which contains all encountered errors during parsing of data
    :param post_data:
    dictionary which was posted from female_comp.html
    :return: tuple of ls,err_list
    """
    data = post_data
    ls=[]
    err_list = []
    # для порядка смотреть импорт из бд
    if 'actv_resp' in data:
        sv = data['actv_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 6):
                ls.append(sv)
            else:
                err_list.append("Введено значение АЧТВ вне диапозона 0-6")
        except:
            err_list.append('Введено некорректное значение АЧТВ')
    else:
        err_list.append('Значение АЧТВ не указано')

    if 'css_resp' in data:
        sv = data['css_resp']
        try:
            sv = int(sv)
            if is_in_range(sv, 100):
                ls.append(sv)
            else:
                err_list.append("Введено значение ХСС вне диапозона 0-100")
        except:
            err_list.append('Введено некорректное значение ХСС')
    else:
        err_list.append('Значение ХСС неуказано')

    if 'lp_resp' in data:
        sv = data['lp_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 70):
                ls.append(sv)
            else:
                err_list.append("Введено значение ЛП вне диапозона 0-70")
        except:
            err_list.append('Введено некорректное значение ЛП')
    else:
        err_list.append('Значение ЛП не указано')

    if 'mgp_resp' in data:
        sv = data['mgp_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 15):
                ls.append(sv)
            else:
                err_list.append("Введено значение МЖП вне диапозона 0-15")
        except:
            err_list.append('Введено некорректное значение МЖП')
    else:
        err_list.append('Значение МЖП не указано')

    if 'zs_resp' in data:
        sv = data['zs_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 15):
                ls.append(sv)
            else:
                err_list.append("Введено значение ЗС вне диапозона 0-15")
        except:
            err_list.append('Введено некорректное значение ЗС')
    else:
        err_list.append('Значение ЗС не указано')

    if 'fv_resp' in data:
        sv = data['fv_resp']
        try:
            sv = int(sv)
            if is_in_range(sv, 70):
                ls.append(sv)
            else:
                err_list.append("Введено значение ФВ вне диапозона 0-70")
        except:
            err_list.append('Введено некорректное значение ФВ')
    else:
        err_list.append('Значение ФВ неуказано')

    # bool data
    if 'ibs_resp' in data:
        ls += [1]
    else:
        ls += [0]

    if 'csn_resp' in data:
        ls += [1]
    else:
        ls += [0]

    if 'chr_resp' in data:
        ls += [1]
    else:
        ls += [0]

    if 'dad_resp' in data:
        sv = data['dad_resp']
        try:
            sv = int(sv)
            if is_in_range(sv, 200):
                ls.append(sv)
            else:
                err_list.append("Введено значение ФВ вне диапозона 0-200")
        except:
            err_list.append('Введено некорректное значение ДАД')
    else:
        err_list.append('Значение ДАД неуказано')

    if 'emot_resp' in data:
        sv = data['emot_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 100):
                ls.append(sv)
            else:
                err_list.append("Введено значение эмоционального коэффициента вне диапозона 0-100")
        except:
            err_list.append('Введено некорректное значение эмоционального коэффициента')
    else:
        err_list.append('Значение эмоционального коэффициента не указано')

    if 'cm_resp' in data:
        sv = data['cm_resp']
        try:
            sv = int(sv)
            if is_in_range(sv, 8):
                ls.append(sv)
            else:
                err_list.append("Введено значение комп. мор. вне диапозона 0-8")
        except:
            err_list.append('Введено некорректное значение комп. мор.')
    else:
        err_list.append('Значение комп. мор. неуказано')

    if 'score_resp' in data:
        sv = data['score_resp']
        sv = sv.replace(',', '.')
        try:
            sv = float(sv)
            if is_in_range(sv, 5):
                ls.append(sv)
            else:
                err_list.append("Введено значение Score вне диапозона 0-5")
        except:
            err_list.append('Введено некорректное значение Score')
    else:
        err_list.append('Значение Score не указано')
    return np.array(ls).reshape(1, -1), err_list