# Mit tartalmaz ez a PR?

- Típus: <!-- csomag (PKG-…) / fejezet-módosítás / fordítás / javítás / eszköz -->
- Érintett azonosítók: <!-- pl. PKG-14-1, II-13, I-10 -->
- Egy mondatban:

## A kapu — ellenőrzőlista (CONTRIBUTING, 10. pont)

- [ ] Minden érintett fájl fejléce kitöltött és érvényes értékű
- [ ] Számozás nem mozdult; új elem a sor végén
- [ ] Nincs duplikált állítás; az indexek csak linkelnek
- [ ] Linkek feloldódnak, azonos nyelvre mutatnak
- [ ] `$$` blokkok üres sorral határoltak; prózában nincs nyers `$`
- [ ] Proof-fájl import-számlával zárul; a fejléc `imports` mezője egyezik vele
- [ ] Változott `_hu` tartalomnál a `pair_status` átállítva

## Csak csomag-PR esetén (kapu-szabály)

- [ ] Az előző csomag be van olvasztva; ez a csomag csak annak **Kimenő állításaira** épít
- [ ] A csomag szerkezete teljes: Kérdés — Bemenetek — Levezetés — Ítélet — Kimenő állítások
- [ ] Szabálykönyv-csomagnál (PKG-NN-1): számolást nem tartalmaz
- [ ] A számoló kód a csomag mellett van, azonos névtővel, és a publikált értékeket adja
- [ ] A D függelék nyomvonala frissült (lezáró szintézis-PR-nél)
