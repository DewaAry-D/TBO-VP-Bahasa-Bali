import pandas as pd
from rule import grammar_bali, lexicon_bali
from kalimat import daftar_kalimat

# =========================================================
# 1. PERSIAPAN DATASET & KUNCI JAWABAN
# =========================================================

list_label_jawaban = [
    # 1-4: Pola P - S (Intransitif)
    "P - S", "P - S", "P - S", "P - S",
    
    # 5-8: Pola P - O - S (Transitif VOS)
    "P - O - S", "P - O - S", "P - O - S", "P - O - S",
    
    # 9-12: Pola P - S - O (Transitif VSO)
    "P - S - O", "P - S - O", "P - S - O", "P - S - O",
    
    # 13-16: Pola P - Pel - S (Status/Definisi)
    "P - Pel - S", "P - Pel - S", "P - Pel - S", "P - Pel - S",
    
    # 17-20: Pola P - S - Pel (Pelengkap Status/Profesi)
    "P - S - Pel", "P - S - Pel", "P - S - Pel",  "P - S - Pel",
    
    # 21-24: Pola P - O - S - Pel (Benefaktif / Kata kerja -ang)
    "P - O - S - Pel", "P - O - S - Pel", "P - O - S - Pel", "P - O - S - Pel",

    # 25-28: Pola P - S - O - Pel
    "P - S - O - Pel", "P - S - O - Pel", "P - S - O - Pel", "P - S - O - Pel",

    # 29-32: Pola P - O - S - Ket (Transitif + Ket)
    "P - O - S - Ket", "P - O - S - Ket", "P - O - S - Ket", "P - O - S - Ket",
    
    # 33-36: Pola P - S - O - Ket (Transitif VSO + Ket)
    "P - S - O - Ket", "P - S - O - Ket", "P - S - O - Ket", "P - S - O - Ket",
    
    # 37-40: Pola P - Pel - S - Ket (PPelSKet)
    "P - Pel - S - Ket", "P - Pel - S - Ket", "P - Pel - S - Ket", "P - Pel - S - Ket",
    
    # 41-44: Pola P - S - Pel - Ket (PSPelKet)
    "P - S - Pel - Ket", "P - S - Pel - Ket", "P - S - Pel - Ket", "P - S - Pel - Ket",

    # 45-47: Pola P - O - S - Pel - Ket (POSPelKet)
    "P - O - S - Pel - Ket", "P - O - S - Pel - Ket", "P - O - S - Pel - Ket",

    # 48-50: Pola P - S - O - Pel - Ket (PSOPelKet)
    "P - S - O - Pel - Ket", "P - S - O - Pel - Ket", "P - S - O - Pel - Ket",

    # 51-70: Contoh Kalimat Negatif
    "INVALID", "INVALID", "INVALID", "INVALID", "INVALID",
    "INVALID", "INVALID", "INVALID", "INVALID", "INVALID",
    "INVALID", "INVALID", "INVALID", "INVALID", "INVALID",
    "INVALID", "INVALID", "INVALID", "INVALID", "INVALID",
]

dataset_uji = list(zip(daftar_kalimat, list_label_jawaban))

# =========================================================
# 2. KELAS PARSER & HELPER
# =========================================================
class CYKParser:
    def __init__(self, grammar, lexicon):
        self.grammar = grammar
        self.lexicon = lexicon

    def parse(self, sentence):
        words = sentence.lower().split()
        n = len(words)
        if n == 0: return None
        
        table = [[[] for _ in range(n)] for _ in range(n)]

        for i, word in enumerate(words):
            if word not in self.lexicon:
                return f"ERROR: Kata '{word}' tidak dikenal."
            for tag in self.lexicon[word]:
                table[i][i].append((tag, word, None))

        # --- FILL TRIANGLE ---
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    for head, rules in self.grammar.items():
                        for left_sym, right_sym in rules:
                            for l_node in table[i][k]:
                                for r_node in table[k + 1][j]:
                                    if l_node[0] == left_sym and r_node[0] == right_sym:
                                        new_node = (head, l_node, r_node)
                                        if new_node not in table[i][j]:
                                            table[i][j].append(new_node)

        # --- CEK HASIL ---
        for node in table[0][n - 1]:
            if node[0] == "K": return node
        return None

def get_pattern_string(node):
    """Mengambil pola sintaksis (P, S, O, Pel, Ket) dari tree."""
    if node is None: return []
    target_tags = {'S', 'P', 'O', 'Pel', 'Ket'}
    
    label = node[0]
    if label in target_tags:
        return [label]
    if node[2] is None:
        return []
        
    return get_pattern_string(node[1]) + get_pattern_string(node[2])

# =========================================================
# 3. PRINT TABEL
# =========================================================
RESET = "\033[0m"
GRAY = "\033[90m"
CYAN = "\033[96m"

def print_table_with_border(df, border_color=CYAN):
    df = df.astype(str)

    col_widths = {
        col: max(len(col), df[col].map(len).max())
        for col in df.columns
    }

    def line(char="-", cross="+"):
        return border_color + cross + cross.join(
            char * (col_widths[col] + 2) for col in df.columns
        ) + cross + RESET

    # Header
    print(line("="))
    header = "| " + " | ".join(col.ljust(col_widths[col]) for col in df.columns) + " |"
    print(header)
    print(line("="))

    # Rows
    for _, row in df.iterrows():
        row_line = "| " + " | ".join(
            row[col].ljust(col_widths[col]) for col in df.columns
        ) + " |"
        print(row_line)
        print(line("-"))

# =========================================================
# 4. FUNGSI UTAMA
# =========================================================
def jalankan_evaluasi():
    parser = CYKParser(grammar_bali, lexicon_bali)
    
    results = []
    jumlah_benar = 0
    total_data = len(dataset_uji)

    print(f"=== MEMULAI EVALUASI PADA {total_data} KALIMAT ===\n")

    for kalimat, pola_kunci in dataset_uji:
        # 1. Parsing
        tree_result = parser.parse(kalimat)
        
        # 2. Ekstraksi Pola
        pola_terdeteksi = "INVALID"
        catatan = ""

        if isinstance(tree_result, str): # Error String
            pola_terdeteksi = "ERROR (Lexicon)"
            catatan = tree_result
        elif tree_result is None: # None
            pola_terdeteksi = "INVALID (Struktur)"
        else: # Valid Tree
            raw_pattern = get_pattern_string(tree_result)
            pola_terdeteksi = " - ".join(raw_pattern)

        # 3. Cek Kebenaran
        status = "SALAH"
        if pola_terdeteksi == pola_kunci:
            status = "BENAR"
        elif pola_kunci == "INVALID" and ("ERROR" in pola_terdeteksi or "INVALID" in pola_terdeteksi):
            status = "BENAR"
        
        if status == "BENAR":
            jumlah_benar += 1
        
        # 4. Simpan ke Log
        results.append({
            "No": len(results) + 1,
            "Kalimat": kalimat,
            "Target": pola_kunci,
            "Terdeteksi": pola_terdeteksi,
            "Status": status
        })

    # 5. Output
    df = pd.DataFrame(results)
    akurasi = (jumlah_benar / total_data) * 100
    
    print("--- Sampel Hasil (Awal & Akhir) ---")
    print_table_with_border(df)

    
    print("\n" + "="*50)
    print(f"TOTAL DATA     : {total_data}")
    print(f"PREDIKSI BENAR : {jumlah_benar}")
    print(f"PREDIKSI SALAH : {total_data - jumlah_benar}")
    print(f"AKURASI        : {akurasi:.2f}%")
    print("="*50)

if __name__ == "__main__":
    jalankan_evaluasi()