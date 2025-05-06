% GEJALA KERUSAKAN

% DATABASE
:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.

% FAKTA KERUSAKAN
kerusakan("Low Power Engine").
kerusakan("Engine Overheat").
kerusakan("Engine Won't Start").
kerusakan("Mounting Engine Failure").
kerusakan("Fuel System Failure").

% FAKTA GEJALA BERDASARKAN KERUSAKAN
gejala(fuel_filter_kotor_atau_bocor, "Low Power Engine").
gejala(saringan_udara_kotor, "Low Power Engine").
gejala(bahan_bakar_habis, "Low Power Engine").
gejala(injektor_tersumbat, "Low Power Engine").

gejala(saringan_udara_kotor, "Engine Overheat").
gejala(sistem_pendingin_bermasalah, "Engine Overheat").
gejala(mesin_bergetar_berlebihan, "Engine Overheat").
gejala(aftercooler_tidak_bisa_mendinginkan_udara, "Engine Overheat").

gejala(bahan_bakar_habis, "Engine Won't Start").
gejala(kebocoran_udara_di_pasokan_sistem_bahan_bakar, "Engine Won't Start").
gejala(mesin_bergetar_berlebihan, "Engine Won't Start").
gejala(kabel_atau_switch_putus, "Engine Won't Start").

gejala(mesin_bergetar_berlebihan, "Mounting Engine Failure").
gejala(terdengar_bunyi_dari_bagian_mesin, "Mounting Engine Failure").
gejala(kipas_pada_mesin_mulai_bergoyang, "Mounting Engine Failure").

gejala(fuel_filter_kotor_atau_bocor, "Fuel System Failure").
gejala(elenoid_injector_tidak_bekerja, "Fuel System Failure").
gejala(terdapat_kebocoran_pada_hose_atau_piping_dari_garis_bahan_bakar, "Fuel System Failure").

% PERTANYAAN TERKAIT GEJALA
pertanyaan(fuel_filter_kotor_atau_bocor, Y) :-
    Y = "Apakah fuel filter kotor atau bocor?".

pertanyaan(saringan_udara_kotor, Y) :-
    Y = "Apakah saringan udara kotor?".

pertanyaan(bahan_bakar_habis, Y) :-
    Y = "Apakah bahan bakar habis?".

pertanyaan(kebocoran_udara_di_pasokan_sistem_bahan_bakar, Y) :-
    Y = "Apakah kebocoran udara di pasokan sistem bahan bakar?".

pertanyaan(mesin_bergetar_berlebihan, Y) :-
    Y = "Apakah mesin bergetar berlebihan?".

pertanyaan(terdengar_bunyi_dari_bagian_mesin, Y) :-
    Y = "Apakah terdengar bunyi dari bagian mesin?".

pertanyaan(kipas_pada_mesin_mulai_bergoyang, Y) :-
    Y = "Apakah kipas pada mesin akan mulai bergoyang?".

pertanyaan(elenoid_injector_tidak_bekerja, Y) :-
    Y = "Apakah elenoid injector tidak bekerja?".

pertanyaan(terdapat_kebocoran_pada_hose_atau_piping_dari_garis_bahan_bakar, Y) :-
    Y = "Apakah terdapat kebocoran pada hose atau piping dari garis bahan bakar?".

pertanyaan(injektor_tersumbat, Y) :-
    Y = "Apakah injektor tersumbat?".

pertanyaan(kabel_atau_switch_putus, Y) :-
    Y = "Apakah kabel atau switch putus?".

pertanyaan(aftercooler_tidak_bisa_mendinginkan_udara, Y) :-
    Y = "Apakah aftercooler tidak bisa mendinginkan udara?".