import pandas as pd
from rule import grammar_bali, lexicon_bali
from kalimat import daftar_kalimat

class CYKParser:
    def __init__(self, grammar, lexicon):
        self.grammar = grammar
        self.lexicon = lexicon

    def parse(self, sentence):
        words = sentence.lower().split()
        n = len(words)

        table = [[[] for _ in range(n)] for _ in range(n)]

        for i, word in enumerate(words):
            if word in self.lexicon:
                tags = self.lexicon[word]
                for tag in tags:
                    table[i][i].append((tag, word, None))
                    print(f"    - '{word}' -> <{tag}>")
            else:
                return None

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    left_cell = table[i][k]
                    right_cell = table[k + 1][j]

                    for head, productions in self.grammar.items():
                        for left_sym, right_sym in productions:
                            for l_node in left_cell:
                                for r_node in right_cell:
                                    if l_node[0] == left_sym and r_node[0] == right_sym:
                                        new_node = (head, l_node, r_node)
                                        table[i][j].append(new_node)

        final_cell = table[0][n - 1]
        for node in final_cell:
            if node[0] == 'K': 
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

    # 2. Looping untuk mengecek setiap kalimat dalam array
    for i, kalimat in enumerate(daftar_kalimat, 1):
        print(f"KASUS #{i}: \"{kalimat}\"")
        print("-" * 40)
        
        tree = parser.parse(kalimat)

        if tree:
            print("\n✅ HASIL: VALID (Diterima Grammar)")
            print("\n[Visualisasi Tree]")
        else:
            print("\n❌ HASIL: INVALID (Ditolak / Struktur Salah)")
        
        print("\n" + "="*60 + "\n")