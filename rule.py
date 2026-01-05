grammar_bali = {
    # ---------------------------------------------------------
    # LEVEL KALIMAT (K)
    # ---------------------------------------------------------
    "K": [
        ("P", "X"),  # PRIORITAS 1: Struktur Kompleks (P + O + S)
        ("P", "S"),  # Prioritas 2: Struktur Sederhana (P + S)
    ],

    # ---------------------------------------------------------
    # LEVEL X (Variabel Perantara CNF) - BERSIH / MURNI
    # ---------------------------------------------------------
    "X": [
        ("O", "S"), ("S", "O"), 
        ("O", "Pel"), ("Pel", "S"), 
        ("S", "Pel"), ("S", "Ket"),
        ("O", "Ket"), ("Pel", "Ket"), 
        ("X", "Pel"), ("X", "Ket"), 
        ("X", "X"), ("S", "X"),
        ("O", "X"), 
    ],

    # ---------------------------------------------------------
    # LEVEL PREDIKAT (P)
    # ---------------------------------------------------------
    "P": [
        ("Aux", "Verb"),
        ("Verb", "Adj"),
        ("Adv", "Verb"),
        # ("Verb", "Noun"),
    ],

    # ---------------------------------------------------------
    # LEVEL FRASE (VP & NP)
    # ---------------------------------------------------------
    "VP": [
        ("Verb", "Noun"), ("VP", "Noun"), ("Aux", "Verb"),
        ("Verb", "Adj"), ("VP", "NP"), 
        ("Adv", "Verb"),
    ],

    "NP": [
        ("Noun", "Noun"), ("Noun", "Pronoun"), ("Noun", "Adj"),
        ("Noun", "Det"), ("Noun", "Num"), ("Det", "Noun"),
        ("NP", "Det"), ("NP", "Adj"), ("NP", "VP"),
        ("NP", "NP"),("NP", "Num"), ("Noun", "NP"),
        ("NP", "Noun"),
    ],

    # ---------------------------------------------------------
    # LEVEL FUNGSI (S, O, Pel, Ket) - SUBSTITUSI LENGKAP
    # ---------------------------------------------------------
    "S": [ 
        ("Det", "Noun"), ("Noun", "Det"), ("Noun", "Noun"), 
        ("NP", "NP"), ("Noun", "Pronoun"), ("Noun", "Adj"),
        ("Noun", "Num"), ("NP", "Det"), ("NP", "Adj"),
        ("NP", "Num"), ("NP", "Noun"), 
    ],

    "O": [ 
        ("Det", "Noun"), ("Noun", "Det"), ("NP", "Noun"),
        ("Noun", "Noun"), ("NP", "NP"), ("Noun", "Pronoun"),
        ("Noun", "Adj"), ("Noun", "Num"), ("NP", "Det"),
        ("NP", "Adj"), ("NP", "Num"), ("Noun", "NP"),
    ],

    "Pel": [ 
        ("Verb", "Noun"), ("VP", "NP"), ("Det", "Noun"),
        ("Adv", "Verb"), ("Noun", "Det"), ("Noun", "Noun"),
        ("Noun", "Pronoun"), ("Noun", "Adj"), ("Noun", "Num"),
        ("NP", "Det"), ("NP", "Adj"), ("Noun", "NP"),
    ],

    "Ket": [
        ("Prep", "Adv"), ("Prep", "Noun"), ("Prep", "NP"),
        ("PP", "Noun"), ("PP", "NP"), ("Adv", "Noun"),
        ("Adv", "NP")
    ],

    "PP": [
        ("Prep", "Noun"), ("Prep", "NP"),
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
    
    # Kata Kerja yang bisa jadi Terminal/Noun di konteks tertentu
    "melajah":  ["Verb", "P", "Pel"], 
    "mekarya":  ["Verb", "P"], 
    "dadi":     ["Verb", "P"], 
    "dados":    ["Verb", "P"],  

    # ==================================
    # NOUN (Kata Benda)
    # ==================================
    "anak": ["Noun"], "kedis": ["Noun"], "bayi": ["Noun"], 
    "bapak": ["Noun"], "bapa": ["Noun"], "meme": ["Noun"], 
    "nasi": ["Noun"], "siswa": ["Noun"], "murid": ["Noun"], 
    "guru": ["Noun"], "petani": ["Noun"], 
    
    "pesaur": ["Noun"], "tugas": ["Noun"], "okan": ["Noun"], 
    "biang": ["Noun"], "dewi": ["Noun"], "sepatu": ["Noun"], 
    "gamelan": ["Noun"], "baleganjur": ["Noun"], 
    "pria": ["Noun"], "motor": ["Noun"], 
    "pegawai": ["Noun"], "staff": ["Noun"], "panak": ["Noun"], 
    "belin": ["Noun"], "ketua": ["Noun"], "stt": ["Noun"], 
    "kepala": ["Noun"], "bagian": ["Noun"], "dokter": ["Noun"], 
    "mahasiswa": ["Noun"], "asisten": ["Noun"], "dosen": ["Noun"], 
    "ajus": ["Noun"], "wi": ["Noun"], "adi": ["Noun"], 
    "tamiu": ["Noun"], "teh": ["Noun"], "ajik": ["Noun"], 
    "koster": ["Noun"], "krama": ["Noun"], "gubernur": ["Noun"], 
    "putu": ["Noun"], "bekel": ["Noun"], "timpalne": ["Noun"], 
    "pancing": ["Noun"], "sampi": ["Noun"], "sampine": ["Noun"],
    "padang": ["Noun"], "bli": ["Noun"], "agus": ["Noun"], 
    "kendang": ["Noun"], "tiang": ["Noun", "Pronoun"], 
    "guli": ["Noun"], 
    "sisin": ["Noun"], "pasih": ["Noun"], 
    "yowanane": ["Noun"], "lagu": ["Noun"], "banjar": ["Noun"], 
    "istri": ["Noun"], "wantilan": ["Noun"], 
    "pekak": ["Noun"], "tegal": ["Noun"], 
    "pewaregan": ["Noun"], "ia": ["Noun", "Pronoun"], "sayur": ["Noun"], 
    "peken": ["Noun"], "nelayan": ["Noun"], "bendegane": ["Noun"], 
    "be": ["Noun"], "luh": ["Noun"], "sari": ["Noun"], 
    "tunangan": ["Noun"], "mobil": ["Noun"], "lapangan": ["Noun"], 
    "ketut": ["Noun"], "peteng": ["Noun"], 
    "sopir": ["Noun"], "denpasar": ["Noun"], "jauk": ["Noun"], 
    "sanggar": ["Noun"], "kadek": ["Noun"], "perbekel": ["Noun"], 
    "desa": ["Noun"], "sanur": ["Noun"], "don": ["Noun"], 
    "kopi": ["Noun"], "sisia": ["Noun"], "aksara": ["Noun"], 
    "bali": ["Noun"], "kelas": ["Noun"], "tulis": ["Noun"], 
    "tengai": ["Noun"], "saang": ["Noun"], "alase": ["Noun"], 
    "pedagang": ["Noun"], "turisne": ["Noun"], "kamben": ["Noun"], 
    "tongos": ["Noun"], "tamiune": ["Noun"], "buah": ["Noun"], 
    "stroberi": ["Noun"], "gurune": ["Noun"],
    "bapane": ["Noun"], "gambar": ["Noun"], "pemacul": ["Noun"],
    "pegawe": ["Noun"], "yowanene": ["Noun"], "paon": ["Noun"],
    "wayan": ["Noun"], "baline": ["Noun"], "wisate": ["Noun"],

    # ==================================
    # OBJEK
    # ==================================
    "buku": ["O", "Noun"], "nasi": ["O","Noun"], "padi": ["O","Noun"],
    "adine": ["O", "S", "Noun"], "putu": ["O", "Noun"], "jukung": ["O", "Noun"],
    "wastra": ["O", "Noun"],

    # ==================================
    # Subjek
    # ==================================
    "susu": ["S","Noun"], "made": ["S", "Noun"], "ipun": ["S", "Noun"],
    "komang": ["S", "Noun"], "bapane": ["S" ,"Noun"], "wresa": ["S", "Noun"],

    # ==================================
    # PRONOUN (Kata Ganti)
    # ==================================
    "tiang": ["S", "O", "Pel", "Pronoun", "Noun"], 
    "bapa": ["S", "O", "Pel", "Pronoun", "Noun"],
    "meme": ["S", "O", "Pel", "Pronoun", "Noun"],
    "anak": ["S", "O", "Pel", "Pronoun", "Noun"], 
    "ida": ["S", "Pel", "Pronoun", "Noun"],
    "ia": ["S", "O", "Pel", "Pronoun", "Noun"],
    "murid":["Pronoun", "Noun"],
    "guru":["Pronoun", "Noun"],
    "gurune":["S", "O", "Pel", "Pronoun", "Noun"],

    # ==================================
    # ADJ (Kata Sifat)
    # ==================================
    "cenik": ["Adj"], "rajin": ["Adj"], "lingsir": ["Adj"], "anyar": ["Adj"],
    "truna": ["Adj"], "gede": ["Adj"], "kelih": ["Adj"], "anget": ["Adj"],
    "pait": ["Adj"], "lanang": ["Adj"], "cerik": ["Adj"],

    # ==================================
    # ADV (Keterangan/Adverb)
    # ==================================
    "buin": ["Adv"], "mani": ["Adv"], "ibi": ["Adv"], "sanja": ["Adv"],
    "mare": ["Adv"],
    
    # ==================================
    # DET (Determiner)
    # ==================================
    "i": ["Det"], "ento": ["Det"], "punika": ["Det"], "nika": ["Det"],
    "pare": ["Det"], "tiange": ["Det"],
    
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
    "nem": ["Num"]
}