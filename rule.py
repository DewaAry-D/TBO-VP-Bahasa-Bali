grammar_bali = {
    
    #LEVEL KALIMAT (S)
    "S": [
        # POLA INTRANSITIF (PREDIKAT + SUBYEK)
        ("Vi", "NP"),
        ("Vi", "SB"),

        # POLA TRANSITIF (PREDIKAT FRASA + SUBYEK)
        ("VP", "NP"),
        ("VP", "SB"),

        # 3. POLA SUBYEK DI DEPAN (S-P)
        # ("NP", "VP"),
        # ("NP", "Vi"),
    ],

    # SISA BAGIAN KALIMAT (SB)
    "SB": [
        ("NP", "NP"),
        ("NP", "PP"),
        ("NP", "VP"),
        ("NP", "Vi"),
        ("NP", "AdvP"), 
        ("VP", "NP"),
        ("VP", "PP"),
        ("VP", "AdvP"),

        ("Adj", "NP"), 
        ("Adj", "SB"),

        # Pola Rekursif
        ("NP", "SB"),
        ("VP", "SB")
    ],

    # LEVEL FRASE KERJA (VP)
    "VP": [
        ("Vt", "NP"),
        ("Vt", "N"),
        ("Vt", "Adj"), 
        ("Vt", "VP"),
        ("Vt", "PP"),
        ("Vt", "SB"),

        ("Vt", "Vi"),

        ("Aux", "V"),  
        ("Aux", "Vi"),  
        ("Aux", "Vt"),
        ("Adv", "V"), 
        ("VP", "VP"),   
        ("VP", "PP"), 
        ("VP", "AdvP")
    ],

    # LEVEL FRASE BENDA (NP)
    "NP": [
        ("Det", "N"), ("N", "Det"),
        ("N", "N"),   ("N", "Adj"), 
        ("N", "Pro"), ("N", "Num"),
        
        # Rekursif NP
        ("NP", "Det"),
        ("NP", "Adj"),
        ("NP", "VP"),
        ("NP", "Vi"),
        ("NP", "PP"),
        ("NP", "NP")
    ],

    # LEVEL FRASE PREPOSISI (PP)
    "PP": [
        ("Prep", "N"), 
        ("Prep", "NP")
    ], 
    
    # LEVEL FRASE KETERANGAN (AdvP)
    "AdvP": [
        ("Adv", "N"), 
        ("Prep", "Adv")
    ], 
    
}

lexicon_bali = {
    # KATA KERJA INTRANSITIF (Vi)
    # Tidak butuh objek untuk jadi predikat
    "melaib":   ["Vi", "V"], 
    "makeber":  ["Vi", "V"], 
    "ngeling":  ["Vi", "V"], 
    "sirep":    ["Vi", "V"],
    "negak":    ["Vi", "V"], 
    "menek":    ["Vi", "V"], 
    "lekad":    ["Vi", "V"],
    "melali":   ["Vi", "V"],
    "ngigel":   ["Vi", "V"],
    "maprakara": ["Vi", "V"],
    "meplayanan": ["Vi", "V"],
    "merayunan": ["Vi", "V"],
    "ngajeng": ["Vi", "V"],
    "megae":    ["Vi", "V"],

    # KATA KERJA TRANSITIF (Vt)
    # Butuh objek (NP) untuk membentuk VP
    "ngamah":   ["Vt", "V"], 
    "nyakan":   ["Vt", "V"], 
    "nulis":    ["Vt", "V"], 
    "numbas":   ["Vt", "V"],
    "ngwacen":  ["Vt", "V"],
    "ngajin":   ["Vt", "V"],
    "minum":    ["Vt", "V"],
    "nabuh":    ["Vt", "V"],
    "ngai":     ["Vt", "V"],
    "nyait":    ["Vt", "V"],
    "mubut":    ["Vt", "V"],
    "ngadol":   ["Vt", "V"],
    "ngejuk":   ["Vt", "V"],
    "nyetir":   ["Vt", "V"],
    "ngincen":  ["Vt", "V"], 
    "ngendingang": ["Vt", "V"],
    "nyeduhang": ["Vt", "V"],
    "ngurukang": ["Vt", "V"], 
    "nepak":    ["Vt", "V"],
    "nawahang": ["Vt", "V"],
    "ngajahang": ["Vt", "V"],
    "ngalapang": ["Vt", "V"],
    "nyilihang": ["Vt", "V"],
    "ngainang": ["Vt", "V"],
    "nyalon":   ["Vt", "V"],
    "engsap":   ["Vt", "V"],
    "demen":    ["Vt", "V"],
    "milih":    ["Vt", "V"],
    "nyemakang": ["Vt", "V"],
    "ngalihang": ["Vt", "V"],
    "numbasang": ["Vt", "V"],
    "ngemaang": ["Vt", "V", "VP"],
    "ngebaang": ["Vt", "V"],
    "ngicen":   ["Vt", "V"],
    "meplalian": ["Vt", "V"],
    "mula": ["Vt", "V"],
    
    # Kata Kerja Khusus / Kopula
    "melajah":  ["Vi", "V", "Vt"],
    "mekarya":  ["Vi", "V", "VP"],
    "dadi":     ["Vt", "V", "VP"],
    "dados":    ["Vt", "V", "VP"], 

    # KATA BENDA (N) & FRASE BENDA (NP)
    "anak": ["NP", "N"], "kedis": ["NP", "N"], "bayi": ["NP", "N"], 
    "bapak": ["NP", "N"], "bapa": ["NP", "N"], "meme": ["NP", "N"], 
    "nasi": ["NP", "N"], "siswa": ["NP", "N"], "murid": ["NP", "N"], 
    "buku": ["NP", "N"], "guru": ["NP", "N"], "petani": ["NP", "N"], 
    "padi": ["NP", "N"], "susu": ["NP", "N"], "made": ["NP", "N"], 
    "pesaur": ["NP", "N"], "tugas": ["NP", "N"], "okan": ["NP", "N"], 
    "biang": ["NP", "N"], "dewi": ["NP", "N"], "sepatu": ["NP", "N"], 
    "ipun": ["NP", "N"], "gamelan": ["NP", "N"], "baleganjur": ["NP", "N"], 
    "pria": ["NP", "N"], "motor": ["NP", "N"], "komang": ["NP", "N"], 
    "pegawai": ["NP", "N"], "staff": ["NP", "N"], "panak": ["NP", "N"], 
    "belin": ["NP", "N"], "ketua": ["NP", "N"], "stt": ["NP", "N"], 
    "kepala": ["NP", "N"], "bagian": ["NP", "N"], "dokter": ["NP", "N"], 
    "mahasiswa": ["NP", "N"], "asisten": ["NP", "N"], "dosen": ["NP", "N"], 
    "ajus": ["NP", "N"], "wi": ["NP", "N"], "adi": ["NP", "N"], 
    "tamiu": ["NP", "N"], "teh": ["NP", "N"], "ajik": ["NP", "N"], 
    "koster": ["NP", "N"], "krama": ["NP", "N"], "gubernur": ["NP", "N"], 
    "putu": ["NP", "N"], "bekel": ["NP", "N"], "timpalne": ["NP", "N"], 
    "pancing": ["NP", "N"], "sampi": ["NP", "N"], "sampine": ["NP", "N"],
    "padang": ["NP", "N"], "bli": ["NP", "N"], "agus": ["NP", "N"], 
    "kendang": ["NP", "N"], "tiang": ["NP", "N"], "guli": ["NP", "N"], 
    "jukung": ["NP", "N"], "sisin": ["NP", "N"], "pasih": ["NP", "N"], 
    "yowanane": ["NP", "N"], "lagu": ["NP", "N"], "banjar": ["NP", "N"], 
    "wastra": ["NP", "N"], "istri": ["NP", "N"], "wantilan": ["NP", "N"], 
    "pekak": ["NP", "N"], "tegal": ["NP", "N"], "ida": ["NP", "N"], 
    "pewaregan": ["NP", "N"], "ia": ["NP", "N"], "sayur": ["NP", "N"], 
    "peken": ["NP", "N"], "nelayan": ["NP", "N"], "bendegane": ["NP", "N"], 
    "be": ["NP", "N"], "luh": ["NP", "N"], "sari": ["NP", "N"], 
    "tunangan": ["NP", "N"], "mobil": ["NP", "N"], "lapangan": ["NP", "N"], 
    "ketut": ["NP", "N"], "peteng": ["NP", "N"], "wresa": ["NP", "N"], 
    "sopir": ["NP", "N"], "denpasar": ["NP", "N"], "jauk": ["NP", "N"], 
    "sanggar": ["NP", "N"], "kadek": ["NP", "N"], "perbekel": ["NP", "N"], 
    "desa": ["NP", "N"], "sanur": ["NP", "N"], "don": ["NP", "N"], 
    "kopi": ["NP", "N"], "sisia": ["NP", "N"], "aksara": ["NP", "N"], 
    "bali": ["NP", "N"], "kelas": ["NP", "N"], "tulis": ["NP", "N"], 
    "tengai": ["NP", "N"], "saang": ["NP", "N"], "alase": ["NP", "N"], 
    "pedagang": ["NP", "N"], "turisne": ["NP", "N"], "kamben": ["NP", "N"], 
    "tongos": ["NP", "N"], "tamiune": ["NP", "N"], "buah": ["NP", "N"], 
    "stroberi": ["NP", "N"], "gurune": ["NP", "N"], "adine": ["NP", "N"],
    "bapane": ["NP", "N"], "gambar": ["NP", "N"], "pemacul": ["NP", "N"],
    "pegawe": ["NP", "N"], "yowanene": ["NP", "N"],"paon": ["NP", "N"],
    "wayan": ["NP", "N"],

    # SIFAT (Adj)
    "cenik": ["Adj"], "rajin": ["Adj"], "lingsir": ["Adj"], "anyar": ["Adj"],
    "truna": ["Adj"], "gede": ["Adj"], "kelih": ["Adj"], "anget": ["Adj"],
    "pait": ["Adj"], "lanang": ["Adj"], "cerik": ["Adj"],

    # KETERANGAN (Adv)
    "buin": ["Adv"], "mani": ["Adv"], "ibi": ["Adv"], "sanja": ["Adv"],
    "mare": ["Adv"],
    
    # KATA BANTU (Det)
    "i": ["Det"], "ento": ["Det"], "punika": ["Det"], "nika": ["Det"],
    "pare": ["Det"], "tiange": ["Det"],
    
    # AUXILIARY (Aux)
    "nu": ["Aux"], "lakar": ["Aux"], "kari": ["Aux"], "wau": ["Aux"], "wawu": ["Aux"],

    # PREPOSISI (Prep)
    "di": ["Prep"], "ring": ["Prep"], "uli": ["Prep"], "ka": ["Prep"],
    
    # NUMERIK (Num)
    "nem": ["Num"]
}