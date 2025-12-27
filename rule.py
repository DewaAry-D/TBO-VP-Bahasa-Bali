grammar_bali = {

    "S": [
        ("VP", "NP"), 
        ("VP", "X1")   
    ],

    # VARIABEL X1
    "X1": [
        ("NP", "NP"),
        ("NP", "PP"),
        ("NP", "VP"),
        ("NP", "AdvP"),
        
        # Jika kalimat masih panjang maka X1 memanggil X2
        ("NP", "X2"),
        ("VP", "X2")
    ],

    # VARIABEL X2
    "X2": [
        ("NP", "NP"),
        ("NP", "PP"),
        ("NP", "VP"),
        ("NP", "AdvP"),

        ("VP", "PP"),
        ("VP", "PP"),
        
        # Jika kalimat masih panjang Maka X2 memanggil X3
        ("NP", "X3")
    ],

    # VARIABEL X3
    "X3": [
        ("NP", "PP"),
        ("NP", "AdvP"),
        ("NP", "NP")
    ],

    # LEVEL FRASE
    "NP": [
        ("Det", "N"),   ("N", "Det"),  
        ("N", "N"),     ("N", "Adj"),                   
        ("N", "Pro"),   ("N", "A1"), 
        ("NP", "VP")      
    ],       

    "PP": [("Prep", "N"), ("Prep", "NP")], 
    
    "AdvP": [("Adv", "N"), ("Prep", "Adv")], 

    "VP": [
        ("Aux", "V"), ("V", "N"), ("V", "Adj"),
        ("VP", "VP"), ("Adv", "V"),
    ], 

    "A1": [
        ("N", "N"), ("N", "Num"), ("N", "Adj"),
        ("N", "Det"), ("N", "A2"), ("Adj", "Det")
    ],

    "A2": [ ("Adj", "V") ]
}


lexicon_bali = {
    #KATA KERJA (V) & PREDIKAT (VP)
    "melaib": ["V", "VP"], "makeber": ["V", "VP"], "ngeling": ["V", "VP"], "sirep": ["V", "VP"],
    "nyakan": ["V", "VP"], "ngwacen": ["V", "VP"], "ngajin": ["V", "VP"], "mula": ["V", "VP"],
    "minum": ["V", "VP"], "nulis": ["V", "VP"], "numbas": ["V", "VP"], "nabuh": ["V", "VP"],
    "dadi": ["V", "VP"], "negak": ["V", "VP"], "mekarya": ["VP", "V"], "menek": ["V", "VP"],
    "maprakara": ["V", "VP"], "numbasang": ["V", "VP"], "nyeduhang": ["V", "VP"], "milih": ["V", "VP"],
    "nyemakang": ["V", "VP"], "ngalihang": ["V", "VP"], "ngurukang": ["V", "VP"], "nepak": ["V"],
    "ngincen": ["V", "VP"], "meplayanan": ["V", "VP"], "ngai": ["V", "VP"], "ngendingang": ["V", "VP"],
    "nyait": ["V", "VP"], "mubut": ["V", "VP"], "ngamah": ["V", "VP"], "merayunan": ["V", "VP"],
    "ngadol": ["V", "VP"], "ngejuk": ["V", "VP"], "melajah": ["V", "VP"], "nyetir": ["V"],
    "demen": ["V", "VP"], "melali": ["VP", "V"], "engsap": ["V", "VP"], "megae": ["V", "VP"],
    "ngigel": ["V"], "nyalon": ["V", "VP"], "ngainang": ["V", "VP"], "nyilihang": ["V", "VP"],
    "ngalapang": ["V", "VP"], "nawahang": ["V", "VP"], "ngajahang": ["V", "VP"], "lekad": ["V"],
    "dados": ["V"], "ngemaang": ["V", "VP"], "ngebaang": ["V", "VP"], "ngicen": ["V", "VP"],
    "meplalian": ["V", "VP"],


    #KATA BENDA (N) & FRASE BENDA (NP)
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

    #Adj
    "cenik": ["Adj"], "rajin": ["Adj"], "lingsir": ["Adj"], "anyar": ["Adj"],
    "truna": ["Adj"], "gede": ["Adj"], "kelih": ["Adj"], "anget": ["Adj"],
    "pait": ["Adj"], "lanang": ["Adj"], "cerik": ["Adj"],

    #Adv
    "buin": ["Adv"], "mani": ["Adv"], "ibi": ["Adv"], "sanja": ["Adv"],
    "mare": ["Adv"],
    
    #Det
    "i": ["Det"], "ento": ["Det"], "punika": ["Det"], "nika": ["Det"],
    "pare": ["Det"], "tiange": ["Det"],
    
    #Aux
    "nu": ["Aux"], "lakar": ["Aux"], "kari": ["Aux"], "wau": ["Aux"], "wawu": ["Aux"],

    #Prep
    "di": ["Prep"], "ring": ["Prep"], "uli": ["Prep"], "ka": ["Prep"],
    
    #Num
    "nem": ["Num"]
}