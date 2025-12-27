for i, kalimat in enumerate(daftar_kalimat, 1):
        print(f"KASUS #{i}: \"{kalimat}\"")
        print("-" * 40)
        
        tree = parser.parse(kalimat)

        if tree:
            print("\n✅ HASIL: VALID (Diterima Grammar)")
            print("\n[Visualisasi Tree]")
            parser.print_tree(tree)
        else:
            print("\n❌ HASIL: INVALID (Ditolak / Struktur Salah)")
        
        print("\n" + "="*60 + "\n")