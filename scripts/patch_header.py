from pathlib import Path

p = Path("index.html")
t = p.read_text(encoding="utf-8")

pt_old = "<p>Sem fins lucrativos. Nenhuma doa\u00e7\u00e3o \u00e9 pedida ou aceita. Sem direitos sobre Kardec ou a B\u00edblia. Nomes de institui\u00e7\u00f5es n\u00e3o s\u00e3o endosso. Uso: Lei 9.610/1998 art. 46.</p>"
pt_new = """<p>Sem fins lucrativos. Nenhuma doa\u00e7\u00e3o \u00e9 pedida ou aceita. Edi\u00e7\u00e3o digital educacional e gratuita para estudo da Doutrina Esp\u00edrita.</p>
<p>O texto franc\u00eas de Allan Kardec (falecido em 1869) est\u00e1 em dom\u00ednio p\u00fablico. As tradu\u00e7\u00f5es hist\u00f3ricas usadas no PDF das cinco obras b\u00e1sicas s\u00e3o de Guillon Ribeiro (26/10/1943; dom\u00ednio p\u00fablico no Brasil desde 01/01/2014) e de Manuel Quint\u00e3o (16/12/1955; dom\u00ednio p\u00fablico no Brasil desde 01/01/2026), Lei 9.610/1998 art. 41 e 45. O mesmo vale para o cap\u00edtulo 28 do Evangelho (Livro de Preces).</p>
<p>Este site n\u00e3o det\u00e9m direitos sobre Kardec, sobre a B\u00edblia, nem sobre marcas, capas ou edi\u00e7\u00f5es contempor\u00e2neas da FEB. Nomes de institui\u00e7\u00f5es n\u00e3o s\u00e3o endosso. Cita\u00e7\u00f5es curtas: art. 46. Proibida a venda.</p>"""

en_old = "<p>Not for profit. No donations asked or accepted. No rights claimed in Kardec or the Bible. Institutional names are not endorsements. Use: Brazilian Law 9.610/1998 art. 46.</p>"
en_new = """<p>Not for profit. No donations asked or accepted. Free educational digital edition for the study of Spiritist doctrine.</p>
<p>Allan Kardec\u2019s French text (d. 1869) is in the public domain. The historical Portuguese translations in the five-works PDF are by Guillon Ribeiro (26 Oct 1943; public domain in Brazil since 1 Jan 2014) and Manuel Quint\u00e3o (16 Dec 1955; public domain in Brazil since 1 Jan 2026), Law 9.610/1998 arts. 41 and 45. The same applies to Gospel chapter 28 (Book of Prayers).</p>
<p>This site claims no rights in Kardec, the Bible, or contemporary FEB marks, covers, or editions. Institutional names are not endorsements. Short quotations: art. 46. Sale is not allowed.</p>"""

if pt_old not in t:
    raise SystemExit("pt notes missing")
if en_old not in t:
    raise SystemExit("en notes missing")
t = t.replace(pt_old, pt_new, 1).replace(en_old, en_new, 1)
p.write_text(t, encoding="utf-8")
print("ok")
