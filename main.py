import tkinter as tk
from tkinter import ttk, messagebox
from rule import grammar_bali, lexicon_bali

# =========================================================
# 1. LOGIKA PENGGAMBAR TREE (VISUAL)
# =========================================================
class TreeDrawer:
    def __init__(self, canvas):
        self.canvas = canvas
        self.node_radius = 20
        self.level_height = 60
        self.font_label = ("Segoe UI", 9, "bold")
        self.font_word = ("Consolas", 10, "italic")

    def draw_tree(self, node, x, y, dx):
        label = node[0]
        
        # --- TERMINAL NODE ---
        if node[2] is None: 
            self.draw_node_circle(x, y, label, "#00ADB5", "#FFFFFF") 
            self.canvas.create_text(x, y + 35, text=f"'{node[1]}'", fill="#FFD700", font=self.font_word)
            return

        # --- NON-TERMINAL NODE ---
        left_child = node[1]
        right_child = node[2]
        next_y = y + self.level_height
        
        self.canvas.create_line(x, y + self.node_radius, x - dx, next_y - self.node_radius, fill="#666", width=2)
        self.canvas.create_line(x, y + self.node_radius, x + dx, next_y - self.node_radius, fill="#666", width=2)

        self.draw_node_circle(x, y, label, "#393E46", "#EEEEEE") 

        self.draw_tree(left_child, x - dx, next_y, dx * 0.55) 
        self.draw_tree(right_child, x + dx, next_y, dx * 0.55)

    def draw_node_circle(self, x, y, text, bg_color, text_color):
        r = self.node_radius
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=bg_color, outline="white", width=1.5)
        self.canvas.create_text(x, y, text=text, fill=text_color, font=self.font_label)

# =========================================================
# 2. LOGIKA PARSER (CYK)
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
            if word not in self.lexicon: return f"Kata tidak dikenal: '{word}'"
            for tag in self.lexicon[word]: table[i][i].append((tag, word, None))

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    for head, rules in self.grammar.items():
                        for left_sym, right_sym in rules:
                            for l_node in table[i][k]:
                                for r_node in table[k + 1][j]:
                                    if l_node[0] == left_sym and r_node[0] == right_sym:
                                        node = (head, l_node, r_node)
                                        if node not in table[i][j]: table[i][j].append(node)

        for node in table[0][n - 1]:
            if node[0] == "K": return node
        return None

# =========================================================
# 3. UI APLIKASI
# =========================================================
class BalineseParserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BaliSyntax – Balinese Sentence Parser")
        try: self.root.state('zoomed')
        except: self.root.attributes('-zoomed', True)
        self.root.configure(bg="#1E1E1E")

        self.parser = CYKParser(grammar_bali, lexicon_bali)
        self.setup_style()
        self.build_ui()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        self.bg = "#1E1E1E"
        self.card = "#2A2F36"
        self.accent = "#00ADB5"
        self.valid = "#00E676"
        self.invalid = "#FF5252"
        
        style.configure("Title.TLabel", background=self.bg, foreground=self.accent, font=("Segoe UI", 26, "bold"))
        style.configure("Sub.TLabel", background=self.bg, foreground="#BBBBBB", font=("Segoe UI", 11))
        style.configure("Card.TFrame", background=self.card, relief="flat")
        style.configure("Action.TButton", background=self.accent, foreground="white", font=("Segoe UI", 11, "bold"), padding=8)
        style.map("Action.TButton", background=[("active", "#00FFF5")])

    def build_ui(self):
        # Header
        header = tk.Frame(self.root, bg=self.bg)
        header.pack(pady=15)
        ttk.Label(header, text="BaliSyntax Parser", style="Title.TLabel").pack()
        ttk.Label(header, text="CYK-based Grammar Checker for Balinese Language", style="Sub.TLabel").pack()

        # Input Area
        input_card = ttk.Frame(self.root, style="Card.TFrame", padding=15)
        input_card.pack(fill="x", padx=30, pady=5)
        
        row = tk.Frame(input_card, bg=self.card)
        row.pack(fill="x")
        self.entry = tk.Entry(row, font=("Segoe UI", 14), bg="#1C1F24", fg="white", insertbackground="white", relief="flat")
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 15))
        self.entry.bind("<Return>", self.process)
        self.entry.focus_set()
        ttk.Button(row, text="Analisis Struktur", style="Action.TButton", command=self.process).pack(side="right")

        # Status Bar Utama
        self.lbl_main_status = tk.Label(self.root, text="READY", font=("Segoe UI", 12, "bold"), bg=self.card, fg="#AAAAAA", pady=8)
        self.lbl_main_status.pack(fill="x", padx=30, pady=(10, 0))

        # Output Area (Notebook)
        output_frame = tk.Frame(self.root, bg=self.bg)
        output_frame.pack(fill="both", expand=True, padx=30, pady=10)

        notebook = ttk.Notebook(output_frame)
        notebook.pack(fill="both", expand=True)

        # Tab Visual
        tree_tab = ttk.Frame(notebook)
        notebook.add(tree_tab, text="🌳 Visual Tree")
        
        h_scroll = tk.Scrollbar(tree_tab, orient="horizontal")
        v_scroll = tk.Scrollbar(tree_tab, orient="vertical")
        self.canvas_tree = tk.Canvas(tree_tab, bg="#222831", highlightthickness=0, 
                                    xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set, cursor="fleur")
        
        h_scroll.config(command=self.canvas_tree.xview)
        v_scroll.config(command=self.canvas_tree.yview)
        h_scroll.pack(side="bottom", fill="x")
        v_scroll.pack(side="right", fill="y")
        self.canvas_tree.pack(side="left", fill="both", expand=True)
        self.canvas_tree.bind("<ButtonPress-1>", self.start_pan)
        self.canvas_tree.bind("<B1-Motion>", self.pan_drag)
        self.drawer = TreeDrawer(self.canvas_tree)

        # Tab Info
        info_tab = ttk.Frame(notebook)
        notebook.add(info_tab, text="ℹ️ Log & Status")
        
        # === MODIFIKASI: Text dibuat disabled dari awal ===
        self.txt_info = tk.Text(
            info_tab, 
            font=("Consolas", 11), 
            bg="#181B20", 
            fg="#CCCCCC", 
            relief="flat", 
            padx=15, 
            pady=15,
            state="disabled" # KUNCI DARI AWAL
        )
        self.txt_info.pack(fill="both", expand=True)

    def start_pan(self, event):
        self.canvas_tree.scan_mark(event.x, event.y)
    def pan_drag(self, event):
        self.canvas_tree.scan_dragto(event.x, event.y, gain=1)

    def get_pattern(self, node):
        target_tags = {'S', 'P', 'O', 'Pel', 'Ket'}
        label = node[0]
        if label in target_tags: return [label]
        if node[2] is None: return []
        return self.get_pattern(node[1]) + self.get_pattern(node[2])

    # === HELPER: Fungsi khusus untuk menulis log read-only ===
    def write_log(self, text):
        self.txt_info.config(state="normal") # BUKA
        self.txt_info.delete("1.0", tk.END)  # BERSIHKAN
        self.txt_info.insert(tk.END, text)   # TULIS
        self.txt_info.config(state="disabled") # KUNCI LAGI

    def process(self, event=None):
        sentence = self.entry.get().strip()
        if not sentence:
            messagebox.showwarning("Info", "Masukkan kalimat terlebih dahulu.")
            return

        self.canvas_tree.delete("all")
        # Panggil fungsi helper untuk reset log
        self.write_log("") 
        self.root.update_idletasks()

        result = self.parser.parse(sentence)

        if isinstance(result, str): # Error
            self.lbl_main_status.config(text=f"✖ ERROR: {result}", bg=self.invalid, fg="white")
            self.write_log(f"Analisis gagal.\nPenyebab: {result}")
        
        elif result: # Valid
            self.lbl_main_status.config(text="✔ VALID (DITERIMA)", bg=self.valid, fg="#003300")
            
            # Hitung Kata & Pola
            word_count = len(sentence.split())
            pattern_list = self.get_pattern(result)
            pattern_str = " - ".join(pattern_list)

            info_text = (
                f"----------------------------------------\n"
                f"HASIL ANALISIS\n"
                f"----------------------------------------\n"
                f"Kalimat      : {sentence}\n"
                f"Jumlah Kata  : {word_count} kata\n"
                f"Status       : VALID\n"
                f"Pola Kalimat : {pattern_str}\n"
                f"----------------------------------------\n"
                f"Visualisasi tree telah digambar pada tab visual tree."
            )
            # Tulis ke log dengan helper
            self.write_log(info_text)
            
            # Gambar Tree
            canvas_w = self.canvas_tree.winfo_width()
            center_x = canvas_w / 2
            start_y = 50
            initial_dx = 120 + (word_count * 15) 

            self.drawer.draw_tree(result, x=center_x, y=start_y, dx=initial_dx)
            self.canvas_tree.configure(scrollregion=self.canvas_tree.bbox("all"))
            
        else: # Invalid Structure
            self.lbl_main_status.config(text="✖ INVALID (DITOLAK)", bg=self.invalid, fg="white")
            self.write_log("Kalimat ditolak karena struktur tidak sesuai dengan Grammar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BalineseParserApp(root)
    root.mainloop()