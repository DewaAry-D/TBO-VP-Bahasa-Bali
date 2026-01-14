grammar_bali = {
    # ---------------------------------------------------------
    # LEVEL KALIMAT (K)
    # ---------------------------------------------------------
    "K": [
        ("X2", "O"),
        ("X1", "S"),
        ("X2", "X10"),
        ("X1", "X9"),
        ("X2", "X7"),
        ("X1", "X6"),
        ("X2", "X8"),
        ("X3", "X6"),
        ("X2", "X5"),
        ("X1", "X4"),
        ("X3", "S"),
        ("X2", "Pel"),
        ("P", "S"),
    ],

    # ---------------------------------------------------------
    # LEVEL X (Variabel Perantara CNF) - BERSIH / MURNI
    # ---------------------------------------------------------
    "X1": [ ("P", "O") ],
    "X2": [ ("P", "S") ],
    "X3": [ ("P", "Pel") ],
    "X4": [ ("S", "Pel") ],
    "X5": [ ("O", "Pel") ],
    "X6": [ ("S", "Ket") ],
    "X7": [ ("O", "Ket") ],
    "X8": [ ("Pel", "Ket") ],
    "X9": [ ("X4", "Ket") ],
    "X10": [ ("X5", "Ket") ],

    # ---------------------------------------------------------
    # LEVEL PREDIKAT (P)
    # ---------------------------------------------------------
    "P": [
        ("Adv", "Verb"),
        ("Aux", "Verb"),
        # ("Verb", "Adj"),
        ("Verb", "Verb"),
    ],

    # ---------------------------------------------------------
    # LEVEL FRASE (VP & NP)
    # ---------------------------------------------------------
    "VP": [
        ("Verb", "Noun"), 
        ("VP", "Noun"), 
        ("Aux", "Verb"),
        ("Verb", "Adj"), 
        ("VP", "NP"), 
        ("Adv", "Verb"),
    ],

    "NP": [
        ("Noun", "Pronoun"), 
        ("Noun", "Adj"),
        ("Noun", "Num"), 
        ("NP", "Adj"), 
        ("NP", "Num"), 
        ("NP", "Propnoun"),
        ("Noun", "Propnoun"),
        ("Noun", "Noun"), 
        # ("NP", "Noun"),
    ],

    # ---------------------------------------------------------
    # LEVEL FUNGSI (S, O, Pel, Ket) - SUBSTITUSI LENGKAP
    # ---------------------------------------------------------
    "S": [ 
        ("Noun", "Det"), 
        ("Noun", "Pronoun"), 
        ("Noun", "Adj"),
        ("Noun", "Num"),  
        ("Part", "Noun"),
        ("Part", "Propnoun"),
        ("NP", "Propnoun"),
        ("NP", "Adj"),
        ("NP", "Num"),
        ("NP", "Det"), 
        ("Det", "NP"),
        ("NP", "Noun"), 
        ("Noun", "Noun"), 
    ],

    "O": [ 
        ("Noun", "Det"),
        ("Noun", "Pronoun"),
        ("Noun", "Adj"), 
        ("Noun", "Num"), 
        ("NP", "Det"), 
        ("NP", "Noun"),
        ("NP", "Adj"), 
        ("NP", "Num"), 
        ("Noun", "NP"),
        ("Part", "Noun"),
    ],

    "Pel": [ 
        ("Verb", "Noun"), 
        ("VP", "NP"),
        ("Adv", "Verb"), 
        ("Noun", "Det"), 
        ("Noun", "Noun"),
        ("Noun", "Pronoun"), 
        ("Noun", "Adj"), 
        ("Noun", "Num"),
        ("NP", "Det"), 
        ("NP", "Adj"), 

    ],

    "Ket": [
        ("Prep", "Adv"), 
        ("Prep", "Noun"),
        ("Prep", "NounT"), 
        ("Prep", "Propnoun"), 
        ("Prep", "NP"), 
        ("PP", "Noun"), 
        ("PP", "NP"), 
        ("Adv", "Noun"),
        ("Adv", "NP"),
        ("NounT", "NP"), 
        ("NounT", "NounT"),
    ],

    "PP": [
        ("Prep", "Noun"), 
        ("Prep", "NP"),
    ],
}

lexicon_bali = {
    # ==================================
    # VERB
    # ==================================
    "melaib":   ["Verb", "P"], 
    "makeber":  ["Verb", "P"],  
    "ngeling":  ["Verb", "P"],  
    "sirep":    ["Verb", "P"], 
    "negak":    ["Verb", "P"],  
    "menek":    ["Verb", "P"],  
    "lekad":    ["Verb", "P"], 
    "melali":   ["Verb", "P", "Pel"], 
    "ngigel":   ["Verb", "P"], 
    "maprakara": ["Verb", "P"], 
    "meplayanan": ["Verb", "P"], 
    "megae":    ["Verb", "P"], 
    "merayunan": ["Verb", "P"], 
    "ngajeng":  ["Verb", "P"], 
    "ngamah":   ["Verb", "P"],  
    "nyakan":   ["Verb", "P"],  
    "nulis":    ["Verb", "P"],  
    "numbas":   ["Verb", "P"], 
    "ngwacen":  ["Verb", "P"], 
    "ngajin":   ["Verb", "P"], 
    "minum":    ["Verb", "P"], 
    "nabuh":    ["Verb", "P"], 
    "ngai":     ["Verb", "P"], 
    "nyait":    ["Verb", "P"], 
    "mubut":    ["Verb", "P"], 
    "ngadol":   ["Verb", "P"], 
    "ngejuk":   ["Verb", "P"], 
    "nyetir":   ["Verb", "P"], 
    "ngincen":  ["Verb", "P"],  
    "ngendingang": ["Verb", "P"], 
    "nyeduhang": ["Verb", "P"], 
    "ngurukang": ["Verb", "P"],  
    "nepak":    ["Verb", "P"], 
    "nawahang": ["Verb", "P"], 
    "ngajahang": ["Verb", "P"], 
    "ngalapang": ["Verb", "P"], 
    "nyilihang": ["Verb", "P"], 
    "ngainang": ["Verb", "P"], 
    "nyalon":   ["Verb", "P"], 
    "engsap":   ["Verb", "P"], 
    "demen":    ["Verb", "P"], 
    "milih":    ["Verb", "P"], 
    "nyemakang": ["Verb", "P"], 
    "ngalihang": ["Verb", "P"], 
    "numbasang": ["Verb", "P"], 
    "ngemaang": ["Verb", "P"], 
    "ngebaang": ["Verb", "P"], 
    "ngicen":   ["Verb", "P"], 
    "meplalian": ["Verb", "P"], 
    "mula":     ["Verb", "P"], 
    "nyampat": ["Verb", "P"], 
    "melajah":  ["Verb", "P", "Pel"], 
    "mekarya":  ["Verb", "P"], 
    "dadi":     ["Verb", "P"], 
    "dados":    ["Verb", "P"],  
    "ngarit":    ["Verb", "P"],  
    "malali":    ["Verb", "P"],

    # ==================================
    # NOUN (Kata Benda)
    # ==================================
    "anak": ["NP", "Noun"], "kedis": ["NP", "Noun"], "bayi": ["NP", "Noun"], 
    "bapak": ["NP", "Noun"], "meme": ["NP", "Noun"], 
    "siswa": ["NP", "Noun"], "murid": ["NP", "Noun"], 
    "petani": ["NP", "Noun"], 
    "pesaur": ["NP", "Noun"], "tugas": ["NP", "Noun"], "okan": ["NP", "Noun"], 
    "biang": ["NP", "Noun"], "dewi": ["NP", "Noun"], "sepatu": ["NP", "Noun"], 
    "gamelan": ["NP", "Noun"], "baleganjur": ["NP", "Noun"], 
    "pria": ["NP", "Noun"], "motor": ["NP", "Noun"], 
    "pegawai": ["NP", "Noun"], "staff": ["NP", "Noun"], "panak": ["NP", "Noun"], 
    "belin": ["NP", "Noun"], "ketua": ["NP", "Noun"], "stt": ["NP", "Noun"], 
    "kepala": ["NP", "Noun"], "bagian": ["NP", "Noun"],
    "mahasiswa": ["NP", "Noun"], "asisten": ["NP", "Noun"], "dosen": ["NP", "Noun"], 
    "wi": ["NP", "Noun"], "adi": ["NP", "Noun"], 
    "tamiu": ["NP", "Noun"], "teh": ["NP", "Noun"], "ajik": ["NP", "Noun"], 
    "krama": ["NP", "Noun"], "gubernur": ["NP", "Noun"], 
    "pancing": ["NP", "Noun"], "sampi": ["NP", "Noun"], "sampine": ["NP", "Noun"],
    "bli": ["NP", "Noun"], "agus": ["NP", "Noun"], 
    "kendang": ["NP", "Noun"], "tiang": ["Noun", "Pronoun"], "guli": ["NP", "Noun"], 
    "sisin": ["NP", "Noun"], "pasih": ["NP", "Noun"], 
    "lagu": ["NP", "Noun"], "banjar": ["NP", "Noun"], 
    "istri": ["NP", "Noun"], "wantilan": ["NP", "Noun"], 
    "pekak": ["NP", "Noun"], "tegal": ["NP", "Noun"], 
    "pewaregan": ["NP", "Noun"], "ia": ["Noun", "Pronoun"], "sayur": ["NP", "Noun"], 
    "peken": ["NP", "Noun"], "nelayan": ["NP", "Noun"],
    "be": ["NP", "Noun"], "luh": ["NP", "Noun"], 
    "tunangan": ["NP", "Noun"], "mobil": ["NP", "Noun"], "lapangan": ["NP", "Noun"], 
    "peteng": ["NP", "Noun"], "sopir": ["NP", "Noun"], "jauk": ["NP", "Noun"], 
    "sanggar": ["NP", "Noun"], "perbekel": ["NP", "Noun"], 
    "desa": ["NP", "Noun"], "don": ["NP", "Noun"], 
    "kopi": ["NP", "Noun"], "sisia": ["NP", "Noun"], "aksara": ["NP", "Noun"], 
    "kelas": ["NP", "Noun"], "tulis": ["NP", "Noun"], 
    "tengai": ["NP", "Noun"], "alase": ["NP", "Noun"], 
    "turisne": ["NP", "Noun"], "kamben": ["NP", "Noun"], 
    "tongos": ["NP", "Noun"], "buah": ["NP", "Noun"], 
    "stroberi": ["NP", "Noun"],
    "gambar": ["NP", "Noun"], "pemacul": ["NP", "Noun"],
    "pegawe": ["NP", "Noun"], "paon": ["NP", "Noun"],
    "baline": ["NP", "Noun"], "wisate": ["NP", "Noun"],
    "lanang": ["NP", "Noun"],
    "jukung": ["NP", "Noun"],
    "sela": ["NP", "Noun"],
    "jukut": ["NP", "Noun"],
    "ares": ["NP", "Noun"],
    "yeh": ["NP", "Noun"],

    "carik": ["NP", "Noun"],
    "pura": ["NP", "Noun"],
    "paon": ["NP", "Noun"],
    "mobil": ["NP", "Noun"],
    "mobil": ["NP", "Noun"],
    "sekolah": ["NP", "Noun"],
    "jumah": ["NP", "Noun"],

    # ==================================
    # OBJEK
    # ==================================
    "nasi": [ "O", "Noun", "NP"], "buku": [ "Noun", "O", "NP"],
    "padi": [ "Noun", "O", "NP"], "susu": [ "Noun", "O", "NP"],
    "tamiune": [ "Noun", "O", "NP"],
    "adine": ["O", "S", "Noun"],
    "lagu": ["O", "NP", "Noun"],
    "wastra": ["O", "NP", "Noun"],
    "padang": ["O", "NP", "Noun"],
    "sampi": ["O", "NP", "Noun"],
    "timpalne": ["O", "NP", "Noun"], 

    "bekel": ["Pel", "NP", "Noun"],
    "saang": ["Pel", "NP", "Noun"],
    "guru": ["Pel","NP", "Noun"],
    "dokter": ["Pel","NP", "Noun"], 

    # ==================================
    # Subjek dan PROPNOUN dan Pronoun
    # ==================================
    "gurune": ["S", "NP", "Noun"],
    "pedagang": ["S", "NP", "Noun"],
    "bendegane": ["S", "NP", "Noun"], 
    "yowanane": ["S", "NP", "Noun"],
    "bapa": [ "O", "S", "NP", "Noun"],
    "bapane": [ "S", "NP", "Noun"],
    "made": [ "Propnoun", "S", "NP"],
    "komang": [ "Propnoun", "S", "NP"],
    "ajus": [ "Propnoun", "S", "NP"],
    "koster": [ "Propnoun", "S", "NP"],
    "putu": [ "O", "Propnoun", "S", "NP"],
    "sari": [ "Propnoun", "S", "NP"],
    "ketut": [ "Propnoun", "S", "NP", "Noun"],
    "denpasar": [ "Propnoun", "S", "NP"],
    "bandung": [ "Propnoun", "S", "NP"],
    "kadek": [ "Propnoun", "S", "NP"],
    "sanur": [ "Propnoun", "Noun", "NP"],
    "bali": [ "Propnoun", "S", "NP"],
    "wayan": [ "Propnoun", "S", "NP"],
    "wresa": [ "Propnoun", "S", "NP"],
    "ida": [ "Propnoun", "S", "NP"],
    "gede": [ "Propnoun", "S", "NP"],

    "ipun": [ "Pronoun", "S", "NP"],
    "tiang": [ "Pronoun", "S", "NP"],
    "ia": [ "Pronoun", "S", "NP"],

    # ==================================
    # NounT (NounT)
    # ==================================
    "ibi": ["NounT"], "mani": ["NounT"], "tengai": ["NounT"],

    # ==================================
    # ADJ (Kata Sifat)
    # ==================================
    "cenik": ["Adj"], "rajin": ["Adj"], "lingsir": ["Adj"], "anyar": ["Adj"],
    "truna": ["Adj"], "gede": ["Adj"], "kelih": ["Adj", "Pel"], "anget": ["Adj"],
    "pait": ["Adj"], "cerik": ["Adj"],
    # "lanang": ["Adj"],

    # ==================================
    # ADV (Keterangan/Adverb)
    # ==================================
    "sesai": ["Adv"],
    
    # ==================================
    # DET (Determiner)
    # ==================================
    "ento": ["Det"], "punika": ["Det"], "nika": ["Det"],
    "pare": ["Det"], "tiange": ["Det"], "ene": ["Det"],

    # ==================================
    # Part (Partikel)
    # ==================================
    "i": ["Part"],


    # ==================================
    # AUX (Kata Kerja Bantu)
    # ==================================
    "nu": ["Aux"], "lakar": ["Aux"], "kari": ["Aux"], "wau": ["Aux"], "wawu": ["Aux"],

    # ==================================
    # PREP (Preposisi)
    # ==================================
    "di": ["Prep"], "ring": ["Prep"], "uli": ["Prep"], "ka": ["Prep"],
    
    # ==================================
    # NUM (Numerik)
    # ==================================
    "nem": ["Num"], "liu": ["Num"],
}