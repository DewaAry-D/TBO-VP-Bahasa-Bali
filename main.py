import pandas as pd
from rule import grammar_bali, lexicon_bali

class CYKParser:
    def __init__(self, grammar, lexicon):
        self.grammar = grammar
        self.lexicon = lexicon

    def parse(self, sentence):
        words = sentence.lower().split()
        n = len(words)
        
        # Inisialisasi Tabel (n x n)
        table = [[[] for _ in range(n)] for _ in range(n)]

        # --- TAHAP 1: MENGISI DIAGONAL (Kata Dasar) ---
        print(f"\nMenganalisis Kata Dasar:")
        for i, word in enumerate(words):
            if word in self.lexicon:
                tags = self.lexicon[word]
                for tag in tags:
                    # Node Terminal: (Label, Word, None)
                    table[i][i].append((tag, word, None))
                    print(f"    - Kata '{word}' dikenali sebagai <{tag}>")
            else:
                print(f"ERROR: Kata '{word}' tidak ditemukan di kamus!")
                return None

        # --- TAHAP 2: MENGISI SEGITIGA ATAS (Kombinasi Frase) ---
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    left_cell = table[i][k]
                    right_cell = table[k + 1][j]

                    # Cek aturan grammar: Head -> Left Right
                    for head, productions in self.grammar.items():
                        for left_sym, right_sym in productions:
                            for l_node in left_cell:
                                for r_node in right_cell:
                                    if l_node[0] == left_sym and r_node[0] == right_sym:
                                        new_node = (head, l_node, r_node)
                                        table[i][j].append(new_node)

        # --- TAHAP 3: CEK HASIL AKHIR ---
        final_cell = table[0][n - 1]
        for node in final_cell:
            if node[0] == 'S': 
                return node 
        return None

    def print_tree(self, node, level=0):
        indent = "    " * level
        label = node[0]
        
        if node[2] is None: # Terminal
            print(f"{indent}└── [{label}] : '{node[1]}'")
        else: # Non-Terminal
            print(f"{indent}└── [{label}]")
            self.print_tree(node[1], level + 1)
            self.print_tree(node[2], level + 1)



if __name__ == "__main__":
    parser = CYKParser(grammar_bali, lexicon_bali)

    input_text = input("\nMasukkan Kalimat Bahasa Bali: ")
    
    if not input_text.strip():
        input_text = "Ngalihang Bapa I Meme saang uli alase"

    print(f"\nMemproses: \"{input_text}\"")
    tree = parser.parse(input_text)

    if tree:
        print("\nVALID: Kalimat diterima oleh Grammar.")
        print("\n[Visualisasi Tree]")
        parser.print_tree(tree)
    else:
        print("\nINVALID: Kalimat ditolak / Struktur salah.")