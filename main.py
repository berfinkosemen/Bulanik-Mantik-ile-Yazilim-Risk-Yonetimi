import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt
import tkinter as tk

def fuzzy_calculate(input_ph, input_zf, input_ai, input_i, input_kc, input_pd, input_ed, input_gb, input_gs):
    # zf kisminda kullanici tarafindan girilen zaman dilimi degerini alan
    # bu degeri araliktaki kismini bulan method yazilacak

    # Değişkenlerin oluşturulması
    # 1- ph(Proje Surecine hakimiyet)
    # 2- zf(Zaman Dilimi Farkliligi)
    # 3- ai(Adim Adim Ilerleme)
    # 4- i(iletisim)
    # 5- pd(Proje Deneyimi)
    # 6- ed(ekibin deneyimmli olmasi)
    # 7- gb(Gorevlerin Birbirine Bagliligi)
    # 8- gs(Gerekliliklerin Sabit Kalmasi)
    # 9- kc(Kaynak Cesitliligi),

    plt.close()

    ph = np.arange(0, 101, 1)
    zf = np.arange(0, 101, 1)
    ai = np.arange(0, 101, 1)
    i = np.arange(0, 101, 1)
    pd = np.arange(0, 101, 1)
    ed = np.arange(0, 101, 1)
    gb = np.arange(0, 101, 1)
    gs = np.arange(0, 101, 1)
    kc = np.arange(0, 101, 1)
    risk = np.arange(0, 101, 1)

    # Üyelik fonksiyonlarının oluşturulması

    ph_low = mf.trimf(ph, [0, 0, 50])
    ph_med = mf.trimf(ph, [0, 50, 100])
    ph_hig = mf.trimf(ph, [50, 100, 100])

    zf_low = mf.trimf(zf, [0, 0, 50])
    zf_med = mf.trimf(zf, [0, 50, 100])
    zf_hig = mf.trimf(zf, [50, 100, 100])

    ai_very_low = mf.trimf(ai, [0, 0, 100])
    ai_very_hig = mf.trimf(ai, [0, 100, 100])

    i_low = mf.trimf(i, [0, 0, 50])
    i_med = mf.trimf(i, [0, 50, 100])
    i_hig = mf.trimf(i, [50, 100, 100])

    pd_very_low = mf.trimf(pd, [0, 0, 25])
    pd_low = mf.trimf(pd, [0, 25, 50])
    pd_med = mf.trimf(pd, [25, 50, 75])
    pd_hig = mf.trimf(pd, [50, 75, 100])
    pd_very_hig = mf.trimf(pd, [75, 100, 100])

    ed_very_low = mf.trimf(ed, [0, 0, 25])
    ed_low = mf.trimf(ed, [0, 25, 50])
    ed_med = mf.trimf(ed, [25, 50, 75])
    ed_hig = mf.trimf(ed, [50, 75, 100])
    ed_very_hig = mf.trimf(ed, [75, 100, 100])

    gb_low = mf.trimf(gb, [0, 0, 50])
    gb_med = mf.trimf(gb, [0, 50, 100])
    gb_hig = mf.trimf(gb, [50, 100, 100])

    gs_low = mf.trimf(gs, [0, 0, 50])
    gs_med = mf.trimf(gs, [0, 50, 100])
    gs_hig = mf.trimf(gs, [50, 100, 100])

    kc_very_low = mf.trimf(kc, [0, 0, 25])
    kc_low = mf.trimf(kc, [0, 25, 50])
    kc_med = mf.trimf(kc, [25, 50, 75])
    kc_hig = mf.trimf(kc, [50, 75, 100])
    kc_very_hig = mf.trimf(kc, [75, 100, 100])

    risk_very_hig = mf.trimf(risk, [0, 0, 25])
    risk_hig = mf.trimf(risk, [0, 25, 50])
    risk_med = mf.trimf(risk, [25, 50, 75])
    risk_low = mf.trimf(risk, [50, 75, 100])
    risk_very_low = mf.trimf(risk, [75, 100, 100])

    # Veri görselleştirme
    #ax3, ax4, ax5, ax6, ax7, ax8, ax9

    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(6, 10))

    ax0.plot(ph, ph_low, 'r', linewidth=2, label='Düşük')
    ax0.plot(ph, ph_med, 'g', linewidth=2, label='Orta')
    ax0.plot(ph, ph_hig, 'b', linewidth=2, label='Yüksek')
    ax0.set_title('Proje Süreci Hakimiyeti')
    ax0.legend()

    ax1.plot(zf, zf_low, 'r', linewidth=2, label='Düşük')
    ax1.plot(zf, zf_med, 'g', linewidth=2, label='Orta')
    ax1.plot(zf, zf_hig, 'b', linewidth=2, label='Yüksek')
    ax1.set_title('Zaman Dilimi Farklılığı')
    ax1.legend()

    ax2.plot(ai, ai_very_low, 'r', linewidth=2, label='Düşük')
    ax2.plot(ai, ai_very_hig, 'b', linewidth=2, label='Yüksek')
    ax2.set_title('Adım Adım İlerleme')
    ax2.legend()

    plt.tight_layout()

    fig, (ax3, ax4, ax5) = plt.subplots(nrows=3, figsize=(6, 10))

    ax3.plot(i, i_low, 'r', linewidth=2, label='Düşük')
    ax3.plot(i, i_med, 'g', linewidth=2, label='Orta')
    ax3.plot(i, i_hig, 'b', linewidth=2, label='Yüksek')
    ax3.set_title('İletişim')
    ax3.legend()

    ax4.plot(pd, pd_very_low, 'y', linewidth=2, label='Çok Düşük')
    ax4.plot(pd, pd_low, 'r', linewidth=2, label='Düşük')
    ax4.plot(pd, pd_med, 'g', linewidth=2, label='Orta')
    ax4.plot(pd, pd_hig, 'b', linewidth=2, label='Yüksek')
    ax4.plot(pd, pd_very_hig, 'k', linewidth=2, label='Çok Yüksek')
    ax4.set_title('Proje Deneyimi')
    ax4.legend()

    ax5.plot(ed, ed_very_low, 'y', linewidth=2, label='Çok Düşük')
    ax5.plot(ed, ed_low, 'r', linewidth=2, label='Düşük')
    ax5.plot(ed, ed_med, 'g', linewidth=2, label='Orta')
    ax5.plot(ed, ed_hig, 'b', linewidth=2, label='Yüksek')
    ax5.plot(ed, ed_very_hig, 'k', linewidth=2, label='Çok Yüksek')
    ax5.set_title('Ekip Deneyimi')
    ax5.legend()

    plt.tight_layout()

    fig, (ax6, ax7, ax8, ax9) = plt.subplots(nrows=4, figsize=(6, 10))

    ax6.plot(gb, gb_low, 'r', linewidth=2, label='Düşük')
    ax6.plot(gb, gb_med, 'g', linewidth=2, label='Orta')
    ax6.plot(gb, gb_hig, 'b', linewidth=2, label='Yüksek')
    ax6.set_title('Görevlerin Birbirine Bağımlılığı')
    ax6.legend()

    ax7.plot(gs, gs_low, 'r', linewidth=2, label='Düşük')
    ax7.plot(gs, gs_med, 'g', linewidth=2, label='Orta')
    ax7.plot(gs, gs_hig, 'b', linewidth=2, label='Yüksek')
    ax7.set_title('Gerekliliklerin Sabit kalması')
    ax7.legend()

    ax8.plot(kc, kc_very_low, 'y', linewidth=2, label='Çok Düşük')
    ax8.plot(kc, kc_low, 'r', linewidth=2, label='Düşük')
    ax8.plot(kc, kc_med, 'g', linewidth=2, label='Orta')
    ax8.plot(kc, kc_hig, 'b', linewidth=2, label='Yüksek')
    ax8.plot(kc, kc_very_hig, 'k', linewidth=2, label='Çok Yüksek')
    ax8.set_title('Kaynak Çeşitliliği')
    ax8.legend()

    ax9.plot(risk, risk_very_low, 'y', linewidth=2, label='Çok Düşük')
    ax9.plot(risk, risk_low, 'r', linewidth=2, label='Düşük')
    ax9.plot(risk, risk_med, 'g', linewidth=2, label='Orta')
    ax9.plot(risk, risk_hig, 'b', linewidth=2, label='Yüksek')
    ax9.plot(risk, risk_very_hig, 'k', linewidth=2, label='Çok Yüksek')
    ax9.set_title('Risk Oranı')
    ax9.legend()

    plt.tight_layout()

    # input_ph
    # input_zf
    # input_ai
    # input_i
    # input_dp
    # input_ed
    # input_gb
    # input_gs
    # input_kc

    # Üyelik derecelerinin hesaplanması

    ph_fit_low = fuzz.interp_membership(ph, ph_low, input_ph)
    ph_fit_med = fuzz.interp_membership(ph, ph_med, input_ph)
    ph_fit_hig = fuzz.interp_membership(ph, ph_hig, input_ph)


    zf_fit_low = fuzz.interp_membership(zf, zf_low, input_zf)
    zf_fit_med = fuzz.interp_membership(zf, zf_med, input_zf)
    zf_fit_hig = fuzz.interp_membership(zf, zf_hig, input_zf)


    ai_fit_very_low = fuzz.interp_membership(ai, ai_very_low, input_ai)
    ai_fit_very_hig = fuzz.interp_membership(ai, ai_very_hig, input_ai)


    i_fit_low = fuzz.interp_membership(i, i_low, input_i)
    i_fit_med = fuzz.interp_membership(i, i_med, input_i)
    i_fit_hig = fuzz.interp_membership(i, i_hig, input_i)


    pd_fit_very_low = fuzz.interp_membership(pd, pd_very_low, input_pd)
    pd_fit_low = fuzz.interp_membership(pd, pd_low, input_pd)
    pd_fit_med = fuzz.interp_membership(pd, pd_med, input_pd)
    pd_fit_hig = fuzz.interp_membership(pd, pd_hig, input_pd)
    pd_fit_very_hig = fuzz.interp_membership(pd, pd_very_hig, input_pd)


    ed_fit_very_low = fuzz.interp_membership(ed, ed_very_low, input_ed)
    ed_fit_low = fuzz.interp_membership(ed, ed_low, input_ed)
    ed_fit_med = fuzz.interp_membership(ed, ed_med, input_ed)
    ed_fit_hig = fuzz.interp_membership(ed, ed_hig, input_ed)
    ed_fit_very_hig = fuzz.interp_membership(ed, ed_very_hig, input_ed)


    gb_fit_low = fuzz.interp_membership(gb, gb_low, input_gb)
    gb_fit_med = fuzz.interp_membership(gb, gb_med, input_gb)
    gb_fit_hig = fuzz.interp_membership(gb, gb_hig, input_gb)


    gs_fit_low = fuzz.interp_membership(gs, gs_low, input_gs)
    gs_fit_med = fuzz.interp_membership(gs, gs_med, input_gs)
    gs_fit_hig = fuzz.interp_membership(gs, gs_hig, input_gs)


    kc_fit_very_low = fuzz.interp_membership(kc, kc_very_low, input_kc)
    kc_fit_low = fuzz.interp_membership(kc, kc_low, input_kc)
    kc_fit_med = fuzz.interp_membership(kc, kc_med, input_kc)
    kc_fit_hig = fuzz.interp_membership(kc, kc_hig, input_kc)
    kc_fit_very_hig = fuzz.interp_membership(kc, kc_very_hig, input_kc)


    # Kuralların tabanları

    # PH GB GS ZF

    rule11 = np.fmin(ph_fit_hig, risk_very_low)
    rule12 = np.fmin(ph_fit_med, risk_med)
    rule13 = np.fmin(ph_fit_low, risk_very_hig)

    rule14 = np.fmin(zf_fit_hig, risk_hig)
    rule15 = np.fmin(zf_fit_med, risk_med)
    rule16 = np.fmin(zf_fit_low, risk_low)

    rule17 = np.fmin(gs_fit_hig, risk_low)
    rule18 = np.fmin(gs_fit_med, risk_med)
    rule19 = np.fmin(gs_fit_low, risk_hig)

    rule110 = np.fmin(gb_fit_hig, risk_very_hig)
    rule111 = np.fmin(gb_fit_med, risk_med)
    rule112 = np.fmin(gb_fit_low, risk_very_low)


    rule1_1 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_hig), gb_fit_hig), zf_fit_hig), risk_med)
    rule1_2 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_hig), gb_fit_hig), zf_fit_med), risk_med)
    rule1_3 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_hig), gb_fit_hig), zf_fit_low), risk_med)

    rule1_4 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_hig), gb_fit_med), zf_fit_hig), risk_med)
    rule1_5 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_hig), gb_fit_med), zf_fit_med), risk_med)
    rule1_6 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_hig), gb_fit_med), zf_fit_low), risk_med)

    rule1_7 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_hig), gb_fit_low), zf_fit_hig), risk_med)
    rule1_8 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_hig), gb_fit_low), zf_fit_med), risk_med)
    rule1_9 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_hig), gb_fit_low), zf_fit_low), risk_low)



    rule1_10 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_med), gb_fit_hig), zf_fit_hig), risk_hig)
    rule1_11 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_med), gb_fit_hig), zf_fit_med), risk_med)
    rule1_12 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_med), gb_fit_hig), zf_fit_low), risk_med)

    rule1_13 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_med), gb_fit_med), zf_fit_hig), risk_med)
    rule1_14 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_med), gb_fit_med), zf_fit_med), risk_med)
    rule1_15 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_med), gb_fit_med), zf_fit_low), risk_med)

    rule1_16 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_med), gb_fit_low), zf_fit_hig), risk_med)
    rule1_17 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_med), gb_fit_low), zf_fit_med), risk_med)
    rule1_18 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_med), gb_fit_low), zf_fit_low), risk_med)



    rule1_19 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_low), gb_fit_hig), zf_fit_hig), risk_hig)
    rule1_20 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_low), gb_fit_hig), zf_fit_med), risk_hig)
    rule1_21 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_low), gb_fit_hig), zf_fit_low), risk_hig)

    rule1_22 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_low), gb_fit_med), zf_fit_hig), risk_hig)
    rule1_23 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_low), gb_fit_med), zf_fit_med), risk_hig)
    rule1_24 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_low), gb_fit_med), zf_fit_low), risk_hig)

    rule1_25 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_low), gb_fit_low), zf_fit_hig), risk_hig)
    rule1_26 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_low), gb_fit_low), zf_fit_med), risk_hig)
    rule1_27 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_hig, gs_fit_low), gb_fit_low), zf_fit_low), risk_med)



    rule1_28 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_hig), gb_fit_hig), zf_fit_hig), risk_hig)
    rule1_29 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_hig), gb_fit_hig), zf_fit_med), risk_med)
    rule1_30 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_hig), gb_fit_hig), zf_fit_low), risk_med)

    rule1_31 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_hig), gb_fit_med), zf_fit_hig), risk_hig)
    rule1_32 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_hig), gb_fit_med), zf_fit_med), risk_med)
    rule1_33 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_hig), gb_fit_med), zf_fit_low), risk_med)

    rule1_34 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_hig), gb_fit_low), zf_fit_hig), risk_med)
    rule1_35 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_hig), gb_fit_low), zf_fit_med), risk_med)
    rule1_36 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_hig), gb_fit_low), zf_fit_low), risk_med)



    rule1_37 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_med), gb_fit_hig), zf_fit_hig), risk_hig)
    rule1_38 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_med), gb_fit_hig), zf_fit_med), risk_hig)
    rule1_39 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_med), gb_fit_hig), zf_fit_low), risk_hig)

    rule1_40 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_med), gb_fit_med), zf_fit_hig), risk_hig)
    rule1_41 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_med), gb_fit_med), zf_fit_med), risk_hig)
    rule1_42 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_med), gb_fit_med), zf_fit_low), risk_hig)

    rule1_43 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_med), gb_fit_low), zf_fit_hig), risk_hig)
    rule1_44 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_med), gb_fit_low), zf_fit_med), risk_hig)
    rule1_45 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_med), gb_fit_low), zf_fit_low), risk_med)



    rule1_46 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_low), gb_fit_hig), zf_fit_hig), risk_very_hig)
    rule1_47 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_low), gb_fit_hig), zf_fit_med), risk_hig)
    rule1_48 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_low), gb_fit_hig), zf_fit_low), risk_hig)

    rule1_49 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_low), gb_fit_med), zf_fit_hig), risk_hig)
    rule1_50 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_low), gb_fit_med), zf_fit_med), risk_hig)
    rule1_51 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_low), gb_fit_med), zf_fit_low), risk_hig)

    rule1_52 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_low), gb_fit_low), zf_fit_hig), risk_hig)
    rule1_53 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_low), gb_fit_low), zf_fit_med), risk_hig)
    rule1_54 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_med, gs_fit_low), gb_fit_low), zf_fit_low), risk_hig)

    rule1_55 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_hig), gb_fit_hig), zf_fit_hig), risk_hig)
    rule1_56 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_hig), gb_fit_hig), zf_fit_med), risk_hig)
    rule1_57 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_hig), gb_fit_hig), zf_fit_low), risk_hig)

    rule1_58 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_hig), gb_fit_med), zf_fit_hig), risk_hig)
    rule1_59 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_hig), gb_fit_med), zf_fit_med), risk_hig)
    rule1_60 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_hig), gb_fit_med), zf_fit_low), risk_hig)

    rule1_61 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_hig), gb_fit_low), zf_fit_hig), risk_hig)
    rule1_62 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_hig), gb_fit_low), zf_fit_med), risk_hig)
    rule1_63 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_hig), gb_fit_low), zf_fit_low), risk_med)

    rule1_64 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_med), gb_fit_hig), zf_fit_hig), risk_very_hig)
    rule1_65 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_med), gb_fit_hig), zf_fit_med), risk_hig)
    rule1_66 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_med), gb_fit_hig), zf_fit_low), risk_hig)

    rule1_67 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_med), gb_fit_med), zf_fit_hig), risk_hig)
    rule1_68 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_med), gb_fit_med), zf_fit_med), risk_hig)
    rule1_69 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_med), gb_fit_med), zf_fit_low), risk_hig)

    rule1_70 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_med), gb_fit_low), zf_fit_hig), risk_hig)
    rule1_71 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_med), gb_fit_low), zf_fit_med), risk_hig)
    rule1_72 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_med), gb_fit_low), zf_fit_low), risk_hig)

    rule1_73 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_low), gb_fit_hig), zf_fit_low), risk_hig)
    rule1_74 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_low), gb_fit_hig), zf_fit_hig), risk_very_hig)
    rule1_75 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_low), gb_fit_hig), zf_fit_med), risk_very_hig)

    rule1_76 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_low), gb_fit_med), zf_fit_hig), risk_very_hig)
    rule1_77 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_low), gb_fit_med), zf_fit_med), risk_very_hig)
    rule1_78 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_low), gb_fit_med), zf_fit_low), risk_hig)

    rule1_79 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_low), gb_fit_low), zf_fit_hig), risk_very_hig)
    rule1_80 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_low), gb_fit_low), zf_fit_med), risk_very_hig)
    rule1_81 = np.fmin(np.fmin(np.fmin(np.fmin(ph_fit_low, gs_fit_low), gb_fit_low), zf_fit_low), risk_hig)

    #ED KÇ I

    rule2_1 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_very_low), i_fit_low), risk_hig)
    rule2_2 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_very_low), i_fit_med), risk_hig)
    rule2_3 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_very_low), i_fit_hig), risk_hig)

    rule2_4 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_low), i_fit_low), risk_hig)
    rule2_5 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_low), i_fit_med), risk_med)
    rule2_6 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_low), i_fit_hig), risk_med)

    rule2_7 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_med), i_fit_low), risk_med)
    rule2_8 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_med), i_fit_med), risk_med)
    rule2_9 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_med), i_fit_hig), risk_med)

    rule2_10 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_hig), i_fit_low), risk_med)
    rule2_11 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_hig), i_fit_med), risk_med)
    rule2_12 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_hig), i_fit_hig), risk_low)

    rule2_13 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_very_hig), i_fit_low), risk_med)
    rule2_14 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_very_hig), i_fit_med), risk_low)
    rule2_15 = np.fmin(np.fmin(np.fmin(ed_fit_very_low, kc_fit_very_hig), i_fit_hig), risk_low)

    rule2_16 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_very_low), i_fit_low), risk_hig)
    rule2_17 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_very_low), i_fit_med), risk_hig)
    rule2_18 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_very_low), i_fit_hig), risk_med)

    rule2_19 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_low), i_fit_low), risk_hig)
    rule2_20 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_low), i_fit_med), risk_med)
    rule2_21 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_low), i_fit_hig), risk_med)

    rule2_22 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_med), i_fit_low), risk_med)
    rule2_23 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_med), i_fit_med), risk_med)
    rule2_24 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_med), i_fit_hig), risk_med)

    rule2_25 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_hig), i_fit_low), risk_med)
    rule2_26 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_hig), i_fit_med), risk_low)
    rule2_27 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_hig), i_fit_hig), risk_low)

    rule2_28 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_very_hig), i_fit_low), risk_low)
    rule2_29 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_very_hig), i_fit_med), risk_low)
    rule2_30 = np.fmin(np.fmin(np.fmin(ed_fit_low, kc_fit_very_hig), i_fit_hig), risk_low)

    rule2_31 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_very_low), i_fit_low), risk_hig)
    rule2_32 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_very_low), i_fit_med), risk_med)
    rule2_33 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_very_low), i_fit_hig), risk_med)

    rule2_34 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_low), i_fit_low), risk_med)
    rule2_35 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_low), i_fit_med), risk_med)
    rule2_36 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_low), i_fit_hig), risk_med)

    rule2_37 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_med), i_fit_low), risk_med)
    rule2_38 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_med), i_fit_med), risk_med)
    rule2_39 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_med), i_fit_hig), risk_low)

    rule2_40 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_hig), i_fit_low), risk_med)
    rule2_41 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_hig), i_fit_med), risk_low)
    rule2_42 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_hig), i_fit_hig), risk_low)

    rule2_43 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_very_hig), i_fit_low), risk_low)
    rule2_44 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_very_hig), i_fit_med), risk_low)
    rule2_45 = np.fmin(np.fmin(np.fmin(ed_fit_med, kc_fit_very_hig), i_fit_hig), risk_very_low)

    rule2_46 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_very_low), i_fit_low), risk_med)
    rule2_47 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_very_low), i_fit_med), risk_med)
    rule2_48 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_very_low), i_fit_hig), risk_med)

    rule2_49 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_low), i_fit_low), risk_med)
    rule2_50 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_low), i_fit_med), risk_med)
    rule2_51 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_low), i_fit_hig), risk_low)

    rule2_52 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_med), i_fit_low), risk_med)
    rule2_53 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_med), i_fit_med), risk_low)
    rule2_54 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_med), i_fit_hig), risk_low)

    rule2_55 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_hig), i_fit_low), risk_low)
    rule2_56 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_hig), i_fit_med), risk_low)
    rule2_57 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_hig), i_fit_hig), risk_low)

    rule2_58 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_very_hig), i_fit_low), risk_low)
    rule2_59 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_very_hig), i_fit_med), risk_low)
    rule2_60 = np.fmin(np.fmin(np.fmin(ed_fit_hig, kc_fit_very_hig), i_fit_hig), risk_very_low)

    rule2_61 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_very_low), i_fit_low), risk_med)
    rule2_62 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_very_low), i_fit_med), risk_med)
    rule2_63 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_very_low), i_fit_hig), risk_med)

    rule2_64 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_low), i_fit_low), risk_med)
    rule2_65 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_low), i_fit_med), risk_low)
    rule2_66 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_low), i_fit_hig), risk_low)

    rule2_67 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_med), i_fit_low), risk_low)
    rule2_68 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_med), i_fit_med), risk_low)
    rule2_69 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_med), i_fit_hig), risk_low)

    rule2_70 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_hig), i_fit_low), risk_low)
    rule2_71 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_hig), i_fit_med), risk_low)
    rule2_72 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_hig), i_fit_hig), risk_very_low)

    rule2_73 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_very_hig), i_fit_low), risk_low)
    rule2_74 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_very_hig), i_fit_med), risk_very_low)
    rule2_75 = np.fmin(np.fmin(np.fmin(ed_fit_very_hig, kc_fit_very_hig), i_fit_hig), risk_very_low)

    rule2_111 = np.fmin(ed_fit_very_hig, risk_very_low)
    rule2_112 = np.fmin(ed_fit_hig, risk_low)
    rule2_113 = np.fmin(ed_fit_med, risk_med)
    rule2_114 = np.fmin(ed_fit_low, risk_hig)
    rule2_115 = np.fmin(ed_fit_very_low, risk_very_hig)

    rule2_211 = np.fmin(kc_fit_very_hig, risk_very_low)
    rule2_212 = np.fmin(kc_fit_very_hig, risk_low)
    rule2_213 = np.fmin(kc_fit_med, risk_med)
    rule2_214 = np.fmin(kc_fit_low, risk_hig)
    rule2_215 = np.fmin(kc_fit_very_low, risk_very_hig)

    rule2_311 = np.fmin(i_fit_hig, risk_low)
    rule2_312 = np.fmin(i_fit_med, risk_med)
    rule2_313 = np.fmin(i_fit_low, risk_hig)

    
    #PD GS Aİ

    rule3_1 = np.fmin(np.fmin(np.fmin(pd_fit_very_low, gs_fit_low), ai_fit_very_hig), risk_med)

    rule3_2 = np.fmin(np.fmin(np.fmin(pd_fit_very_low, gs_fit_low), ai_fit_very_low), risk_hig)

    rule3_3 = np.fmin(np.fmin(np.fmin(pd_fit_very_low, gs_fit_med), ai_fit_very_hig), risk_med)

    rule3_4 = np.fmin(np.fmin(np.fmin(pd_fit_very_low, gs_fit_med), ai_fit_very_low), risk_med)

    rule3_5 = np.fmin(np.fmin(np.fmin(pd_fit_very_low, gs_fit_hig), ai_fit_very_hig), risk_med)

    rule3_6 = np.fmin(np.fmin(np.fmin(pd_fit_very_low, gs_fit_hig), ai_fit_very_low), risk_med)

    rule3_7 = np.fmin(np.fmin(np.fmin(pd_fit_low, gs_fit_low), ai_fit_very_hig), risk_med)

    rule3_8 = np.fmin(np.fmin(np.fmin(pd_fit_low, gs_fit_low), ai_fit_very_low), risk_med)

    rule3_9 = np.fmin(np.fmin(np.fmin(pd_fit_low, gs_fit_med), ai_fit_very_hig), risk_med)

    rule3_10 = np.fmin(np.fmin(np.fmin(pd_fit_low, gs_fit_med), ai_fit_very_low), risk_med)

    rule3_11 = np.fmin(np.fmin(np.fmin(pd_fit_low, gs_fit_hig), ai_fit_very_hig), risk_low)

    rule3_12 = np.fmin(np.fmin(np.fmin(pd_fit_low, gs_fit_hig), ai_fit_very_low), risk_med)

    rule3_13 = np.fmin(np.fmin(np.fmin(pd_fit_med, gs_fit_low), ai_fit_very_hig), risk_med)

    rule3_14 = np.fmin(np.fmin(np.fmin(pd_fit_med, gs_fit_low), ai_fit_very_low), risk_med)

    rule3_15 = np.fmin(np.fmin(np.fmin(pd_fit_med, gs_fit_med), ai_fit_very_hig), risk_low)

    rule3_16 = np.fmin(np.fmin(np.fmin(pd_fit_med, gs_fit_med), ai_fit_very_low), risk_med)

    rule3_17 = np.fmin(np.fmin(np.fmin(pd_fit_med, gs_fit_hig), ai_fit_very_hig), risk_low)

    rule3_18 = np.fmin(np.fmin(np.fmin(pd_fit_med, gs_fit_hig), ai_fit_very_low), risk_low)

    rule3_19 = np.fmin(np.fmin(np.fmin(pd_fit_hig, gs_fit_low), ai_fit_very_hig), risk_low)

    rule3_20 = np.fmin(np.fmin(np.fmin(pd_fit_hig, gs_fit_low), ai_fit_very_low), risk_med)

    rule3_21 = np.fmin(np.fmin(np.fmin(pd_fit_hig, gs_fit_med), ai_fit_very_hig), risk_low)

    rule3_22 = np.fmin(np.fmin(np.fmin(pd_fit_hig, gs_fit_med), ai_fit_very_low), risk_low)

    rule3_23 = np.fmin(np.fmin(np.fmin(pd_fit_hig, gs_fit_hig), ai_fit_very_hig), risk_low)

    rule3_24 = np.fmin(np.fmin(np.fmin(pd_fit_hig, gs_fit_hig), ai_fit_very_low), risk_low)

    rule3_25 = np.fmin(np.fmin(np.fmin(pd_fit_very_hig, gs_fit_low), ai_fit_very_hig), risk_low)

    rule3_26 = np.fmin(np.fmin(np.fmin(pd_fit_very_hig, gs_fit_low), ai_fit_very_low), risk_med)

    rule3_27 = np.fmin(np.fmin(np.fmin(pd_fit_very_hig, gs_fit_med), ai_fit_very_hig), risk_low)

    rule3_28 = np.fmin(np.fmin(np.fmin(pd_fit_very_hig, gs_fit_med), ai_fit_very_low), risk_low)

    rule3_29 = np.fmin(np.fmin(np.fmin(pd_fit_very_hig, gs_fit_hig), ai_fit_very_hig), risk_very_low)

    rule3_30 = np.fmin(np.fmin(np.fmin(pd_fit_very_hig, gs_fit_hig), ai_fit_very_low), risk_low)

    rule31 = np.fmin(pd_fit_very_low, risk_very_hig)
    rule32 = np.fmin(pd_fit_low, risk_hig)
    rule33 = np.fmin(pd_fit_med, risk_med)
    rule34 = np.fmin(pd_fit_hig, risk_low)
    rule35 = np.fmin(pd_fit_very_hig, risk_very_low)

    rule36 = np.fmin(gs_fit_low, risk_hig)
    rule37 = np.fmin(gs_fit_med, risk_med)
    rule38 = np.fmin(gs_fit_hig, risk_low)
    rule39 = np.fmin(ai_fit_very_low, risk_very_hig) # adim adim ilerleme
    rule310 = np.fmin(ai_fit_very_hig, risk_very_low)

    # Birleşim kümelerinin oluşturulması


    list_very_hig = [rule1_46, rule1_64, rule1_74, rule1_75, rule1_76, rule1_77, rule1_79, rule1_80, rule1_78,
                    rule2_19, rule31, rule39, rule2_115, rule2_215]

    list_hig = [rule1_10, rule1_19, rule1_20, rule1_21, rule1_22, rule1_23, rule1_24, rule1_25, rule1_26, rule1_28,
                            rule1_31, rule1_37, rule1_38, rule1_39, rule1_40, rule1_41, rule1_42,
                            rule1_43, rule1_44, rule1_47, rule1_48, rule1_49, rule1_50, rule1_51, rule1_52,
                            rule1_53, rule1_54, rule1_55, rule1_56, rule1_57, rule1_58, rule1_59, rule1_60, rule1_61,
                            rule1_62, rule1_65, rule1_66, rule1_67, rule1_68, rule1_69, rule1_70, rule1_71, rule1_72,
                            rule1_73, rule1_79, rule1_81, rule2_1, rule2_2, rule2_3, rule2_4, rule2_16, rule2_17, rule2_31,
                            rule3_2, rule32, rule36, rule2_114, rule2_214, rule2_313, rule13, rule14, rule19, rule110]

    list_med = [rule1_1, rule1_2, rule1_3, rule1_4, rule1_5, rule1_6, rule1_7,
                            rule1_8, rule1_11, rule1_12, rule1_13, rule1_14, rule1_15, rule1_16, rule1_17, rule1_18,
                            rule1_27, rule1_29, rule1_30, rule1_32, rule1_33, rule1_34, rule1_35, rule1_36, rule1_45,
                            rule1_63, rule2_5, rule2_6, rule2_7, rule2_8, rule2_9, rule2_10, rule2_11, rule2_13,
                            rule2_18, rule2_20, rule2_21, rule2_22, rule2_23, rule2_24, rule2_25, rule2_32,
                            rule2_33, rule2_34, rule2_35, rule2_36, rule2_37, rule2_38, rule2_40, rule2_46,
                            rule2_47, rule2_48, rule2_49, rule2_50, rule2_52, rule2_61, rule2_62, rule2_63,
                            rule2_64, rule3_1, rule3_3, rule3_4, rule3_5, rule3_6, rule3_7,
                            rule3_8, rule3_9, rule3_10, rule3_12, rule3_13, rule3_14,
                            rule3_16, rule3_20, rule3_26, rule33, rule37, rule2_113, rule2_213, rule2_312, rule12, rule15, rule18, rule111]
    list_low = [rule2_12, rule2_14, rule2_15, rule2_26, rule2_27, rule2_28, rule2_29, rule2_30, rule2_39, rule2_41,
                            rule2_42,
                            rule2_43, rule2_44, rule2_51, rule2_53, rule2_54, rule2_55, rule2_56, rule2_57, rule2_58, rule2_59,
                            rule2_65,
                            rule2_66, rule2_67, rule2_68, rule2_69, rule2_70, rule2_71, rule2_73, rule3_11, rule3_15, rule3_17,
                            rule3_18,
                            rule3_19, rule3_21, rule3_22, rule3_23, rule3_24, rule3_25, rule3_27, rule3_28, rule3_30, rule1_9, rule34,
                             rule38, rule2_112, rule2_212, rule2_311, rule16, rule17, rule112]
    list_very_low = [rule2_45, rule2_60, rule2_72, rule2_74, rule2_75, rule3_29, rule35, rule310, rule2_111, rule2_211, rule11]



    out_very_hig = []
    out_hig = []
    out_med = []
    out_low = []
    out_very_low = []

    n=0
    first = list_very_hig[n]
    for n in range(len(list_very_hig)-1):
        out_very_hig = np.fmax(first, list_very_hig[n+1])
        first = out_very_hig

    n = 0
    first = list_hig[n]
    for n in range(len(list_hig) - 1):
        out_hig = np.fmax(first, list_hig[n + 1])
        first = out_hig

    n = 0
    first = list_med[n]
    for n in range(len(list_med) - 1):
        out_med = np.fmax(first, list_med[n + 1])
        first = out_med

    n = 0
    first = list_low[n]
    for n in range(len(list_low) - 1):
        out_low = np.fmax(first, list_low[n + 1])
        first = out_low

    n = 0
    first = list_very_low[n]
    for n in range(len(list_very_low) - 1):
        out_very_low = np.fmax(first, list_very_low[n + 1])
        first = out_very_low

    # Veri görselleştirme

    risk0 = np.zeros_like(risk)

    fig, ax11 = plt.subplots(figsize=(10, 4))

    ax11.fill_between(risk, risk0, out_very_hig, facecolor='r', alpha=0.7)
    ax11.plot(risk, out_very_hig, 'r', linestyle='--')

    ax11.fill_between(risk, risk0, out_hig, facecolor='g', alpha=0.7)
    ax11.plot(risk, out_hig, 'k', linestyle='--')

    ax11.fill_between(risk, risk0, out_med, facecolor='g', alpha=0.7)
    ax11.plot(risk, out_med, 'y', linestyle='--')

    ax11.fill_between(risk, risk0, out_low, facecolor='g', alpha=0.7)
    ax11.plot(risk, out_low, 'y', linestyle='--')

    ax11.fill_between(risk, risk0, out_very_low, facecolor='g', alpha=0.7)
    ax11.plot(risk, out_very_low, 'y', linestyle='--')
    ax11.set_title('Risk Çıkışı')

    plt.tight_layout()


    # Durulaştırma

    out_list = [out_very_hig, out_hig, out_med, out_low, out_very_low]

    n = 0
    first = out_list[n]
    for n in range(len(out_list) - 1):
        out_risk = np.fmax(first, out_list[n + 1])
        first = out_risk

    defuzzified = fuzz.defuzz(risk, out_risk, 'centroid')

    result = fuzz.interp_membership(risk, out_risk, defuzzified)

    # Sonuç

    print("Başarı Değeri:", defuzzified)
    myLabel = tk.Label(root, text=100-defuzzified, font=("Calibri", 13))
    myLabel.place(relwidth=0.22, relheight=0.08, relx=0.75, rely=0.8)


    # Veri Görselleştirme

    risk0 = np.zeros_like(risk)
    fig, ax10 = plt.subplots(figsize=(7, 4))

    ax10.plot(risk, out_very_hig, 'b', linewidth=0.5, linestyle='--')
    ax10.plot(risk, out_hig, 'b', linewidth=0.5, linestyle='--')
    ax10.plot(risk, out_med, 'b', linewidth=0.5, linestyle='--')
    ax10.plot(risk, out_low, 'b', linewidth=0.5, linestyle='--')
    ax10.plot(risk, out_very_low, 'b', linewidth=0.5, linestyle='--')
    ax10.fill_between(risk, risk0, out_risk, facecolor='Orange', alpha=0.7)
    ax10.plot([defuzzified, defuzzified], [0, result], 'k', linewidth=1.5, alpha=0.9)
    ax10.set_title('Ağırlık Merkezi ile Durulaştırma')

    plt.tight_layout()
    plt.show()

    return defuzzified


def get_parameters():
    input_ph = entry_ph.get()
    input_zf_first = entry_zf.get()
    input_ai = entry_ai.get()
    input_i= entry_i.get()
    input_kc = entry_kc.get()
    input_pd = entry_pd.get()
    input_ed = entry_ed.get()
    input_gb = entry_gb.get()
    input_gs = entry_gs.get()
    input_zf = int(input_zf_first)*100/12

    fuzzy_calculate(input_ph, input_zf, input_ai, input_i, input_kc, input_pd, input_ed, input_gb, input_gs)


root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=800, bg="#263D42")
canvas.pack()


# Creating a Label Widget
myLabel = tk.Label(root, text="YAZILIM RİSK YÖNETİMİ", font=("Calibri",25), bg="#263D42", fg="white")
myLabel.place(relwidth=0.75, relheight=0.1, relx= 0.15, rely=0.05)

myLabel = tk.Label(root, text="Proje Sürecine Hakimiyet :", font=("Calibri",14), bg="#263D42", fg="white")
myLabel.place(relwidth=0.25, relheight=0.07, relx= 0.04, rely=0.2)

myLabel = tk.Label(root, text="Zaman Dilimi Farklılığı :", font=("Calibri",14), bg="#263D42", fg="white")
myLabel.place(relwidth=0.25, relheight=0.07, relx= 0.04, rely=0.32)

myLabel = tk.Label(root, text="Adım Adım İLerleme :", font=("Calibri",14), bg="#263D42", fg="white")
myLabel.place(relwidth=0.25, relheight=0.07, relx= 0.04, rely=0.44)

myLabel = tk.Label(root, text="İletişim :", font=("Calibri",14), bg="#263D42", fg="white")
myLabel.place(relwidth=0.25, relheight=0.07, relx= 0.04, rely=0.56)

myLabel = tk.Label(root, text="Kaynak Yeterliliği :", font=("Calibri",14),bg="#263D42", fg="white")
myLabel.place(relwidth=0.25, relheight=0.07, relx= 0.04, rely=0.68)

myLabel = tk.Label(root, text="Proje Deneyimi :", font=("Calibri",14), bg="#263D42", fg="white")
myLabel.place(relwidth=0.25, relheight=0.07, relx= 0.55, rely=0.2)

myLabel = tk.Label(root, text="Ekip Deneyimi :", font=("Calibri",14), bg="#263D42", fg="white")
myLabel.place(relwidth=0.25, relheight=0.07, relx= 0.55, rely=0.32)

myLabel = tk.Label(root, text="Görevlerin Birbirine bağlılığı :", font=("Calibri",14), bg="#263D42", fg="white")
myLabel.place(relwidth=0.28, relheight=0.07, relx= 0.55, rely=0.44)

myLabel = tk.Label(root, text="Gerekliliklerin Sabit Kalması :", font=("Calibri",14), bg="#263D42", fg="white")
myLabel.place(relwidth=0.28, relheight=0.07, relx= 0.55, rely=0.56)


#girişlerin oluşturulması
entry_ph = tk.Entry(root)
entry_ph.place(relwidth=0.12, relheight=0.07, relx= 0.32, rely=0.2)

entry_zf = tk.Entry(root)
entry_zf.place(relwidth=0.12, relheight=0.07, relx= 0.32, rely=0.32)

entry_ai = tk.Entry(root)
entry_ai.place(relwidth=0.12, relheight=0.07, relx= 0.32, rely=0.44)

entry_i = tk.Entry(root)
entry_i.place(relwidth=0.12, relheight=0.07, relx= 0.32, rely=0.56)

entry_kc = tk.Entry(root)
entry_kc.place(relwidth=0.12, relheight=0.07, relx= 0.32, rely=0.68)

entry_pd = tk.Entry(root)
entry_pd.place(relwidth=0.12, relheight=0.07, relx= 0.86, rely=0.2)

entry_ed = tk.Entry(root)
entry_ed.place(relwidth=0.12, relheight=0.07, relx= 0.86, rely=0.32)

entry_gb = tk.Entry(root)
entry_gb.place(relwidth=0.12, relheight=0.07, relx= 0.86, rely=0.44)

entry_gs = tk.Entry(root)
entry_gs.place(relwidth=0.12, relheight=0.07, relx= 0.86, rely=0.56)

calculate = tk.Button(root, text="Hesapla", padx=12, pady=5, font=("Calibri",15), command= get_parameters)
calculate.place( relx= 0.55, rely=0.8)


root.mainloop()
