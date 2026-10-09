"""Build the framework-free, bilingual Rumah Terukur site into dist/."""
from __future__ import annotations

import html
import json
import shutil
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree

from content import GUIDES, SOURCES

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dist"
SITE = "https://rumah.vijeron.com"
UPDATED = "2026-10-09"
URLS: list[str] = []

T = {
    "id": {
        "name": "Rumah Terukur", "eyebrow": "VIJERON / RUANG & MATERIAL", "home": "Beranda", "guides": "Panduan", "tools": "Kalkulator", "method": "Metode & sumber", "about": "Tentang", "privacy": "Privasi", "contact": "Kontak", "skip": "Lewati ke isi",
        "hero": "Ukur ruang. Rencanakan material dengan jelas.", "hero_desc": "Panduan pengukuran ruang dan kalkulator cat serta keramik dengan rumus terbuka. Anda mengisi dimensi, spesifikasi produk, dan cadangan sesuai proyek sendiri.",
        "start": "Pelajari cara mengukur", "calc": "Buka kalkulator", "hero_note": "Pengukuran lebih penting daripada angka cepat", "hero_note_body": "Bentuk ruang, bukaan, pola pemasangan, dan spesifikasi kemasan menentukan hasil. Simpan sketsa dan periksa ulang ukuran sebelum membeli.",
        "steps": "Dari sketsa ke daftar belanja", "step1": "Ukur bidang yang benar-benar akan dikerjakan dan tulis satuannya.", "step2": "Pisahkan ukuran lapangan dari angka pada label produk.", "step3": "Hitung luas, tampilkan asumsi, lalu bulatkan ke ukuran kemasan.",
        "tool_heading": "Dua alat, satu tujuan: asumsi terlihat", "tool_intro": "Semua hitungan berjalan di peramban. Angka yang Anda masukkan tidak dikirim ke server Vijeron.", "paint": "Estimasi cat dinding", "paint_desc": "Hitung luas bersih, lapisan, dan liter berdasarkan daya sebar cat yang Anda masukkan.", "tile": "Estimasi keramik", "tile_desc": "Hitung luas, cadangan, dan jumlah kotak berdasarkan cakupan pada kemasan.", "open": "Gunakan alat", "read": "Baca panduan",
        "guide_heading": "Delapan panduan untuk keputusan yang lebih jelas", "guide_intro": "Mulai dari meter persegi dan sketsa, lalu lanjut ke cat, keramik, dan catatan pesanan. Tiap panduan memuat contoh dan kesalahan yang perlu dihindari.",
        "source_note": "Ditulis untuk Vijeron. Sumber digunakan untuk memeriksa konsep; teks dan gambar sumber tidak diterbitkan ulang.", "worked": "Contoh hitung", "pitfall": "Kesalahan yang perlu dihindari", "references": "Rujukan", "next": "Panduan berikutnya", "updated": "Diperbarui 9 Oktober 2026", "footer": "Panduan perencanaan ukuran rumah. Hasil alat adalah estimasi, bukan survei bangunan atau penawaran pemasok.",
        "method_title": "Metode, rumus, dan sumber", "method_desc": "Cara kami menghitung, memilih contoh, dan membatasi hasil estimasi.", "about_title": "Tentang Rumah Terukur", "about_desc": "Proyek Vijeron yang membantu pembaca merencanakan material dari ukuran dan spesifikasi yang dapat diperiksa.", "privacy_title": "Kebijakan privasi", "privacy_desc": "Cara kalkulator, analitik, dan iklan bekerja pada Rumah Terukur.",
        "paint_title": "Hitung kebutuhan cat dinding", "paint_intro": "Ukur panjang dan lebar ruang persegi panjang, tinggi dinding, dan total bukaan yang tidak dicat. Masukkan daya sebar per liter dari label produk.",
        "tile_title": "Hitung kebutuhan keramik per kotak", "tile_intro": "Masukkan luas bidang sederhana atau hasil sketsa Anda, cakupan satu kotak dari kemasan, dan cadangan yang Anda pilih.",
        "length": "Panjang ruang (m)", "width": "Lebar ruang (m)", "height": "Tinggi dinding (m)", "openings": "Luas bukaan yang tidak dicat (m²)", "coats": "Jumlah lapisan", "coverage": "Daya sebar cat (m²/L/lapis)", "floor_area": "Luas bidang yang akan dipasang (m²)", "allowance": "Cadangan potongan/kerusakan (%)", "box_coverage": "Cakupan satu kotak (m²)", "calculate": "Hitung estimasi", "result": "Hasil perencanaan", "empty_result": "Isi ukuran dan tekan tombol. Data tetap di peramban Anda.",
        "paint_formula": "Luas dinding kotor = 2 × (panjang + lebar) × tinggi. Luas bersih = luas kotor − bukaan. Liter = luas bersih × lapisan ÷ daya sebar per liter per lapis.",
        "tile_formula": "Luas pesanan = luas bidang × (1 + cadangan ÷ 100). Jumlah kotak = pembulatan ke atas dari luas pesanan ÷ cakupan per kotak.",
        "paint_limit": "Rumus ini untuk empat dinding ruang persegi panjang dengan tinggi sama. Langit-langit, kusen, primer, tekstur, dan ukuran kaleng belum dihitung.",
        "tile_limit": "Rumus ini tidak mensimulasikan arah pemasangan, nat, potongan tepi, atau beda ukuran kemasan. Cocokkan hasil dengan sketsa dan pemasok.",
    },
    "en": {
        "name": "Measured Home", "eyebrow": "VIJERON / SPACE & MATERIALS", "home": "Home", "guides": "Guides", "tools": "Calculators", "method": "Method & sources", "about": "About", "privacy": "Privacy", "contact": "Contact", "skip": "Skip to content",
        "hero": "Measure the room. Plan materials with clarity.", "hero_desc": "Room-measurement guides and paint and tile calculators with open formulas. You enter the dimensions, product specifications and allowance for your own project.",
        "start": "Learn to measure", "calc": "Open calculators", "hero_note": "Measurement matters more than a quick number", "hero_note_body": "Room shape, openings, layout and package specifications all affect the answer. Save a sketch and recheck dimensions before buying.",
        "steps": "From a sketch to an order note", "step1": "Measure the exact surface to be worked on and record units.", "step2": "Keep field measurements separate from product-label figures.", "step3": "Calculate area, show assumptions and then round to available packs.",
        "tool_heading": "Two tools that show their assumptions", "tool_intro": "Calculations run in your browser. Your numbers are not sent to a Vijeron server.", "paint": "Wall paint estimate", "paint_desc": "Calculate net area, coats and litres using the product coverage you enter.", "tile": "Tile box estimate", "tile_desc": "Calculate area, allowance and whole boxes from the package's coverage.", "open": "Use tool", "read": "Read guide",
        "guide_heading": "Eight guides for clearer decisions", "guide_intro": "Start with square metres and sketches, then move to paint, tile and an order note. Each guide has a worked example and a pitfall.",
        "source_note": "Written for Vijeron. Sources verify concepts; their text and images are not republished.", "worked": "Worked example", "pitfall": "Pitfall to avoid", "references": "References", "next": "Next guide", "updated": "Updated 9 October 2026", "footer": "A home-measurement planning guide. Tool results are estimates, not a building survey or supplier quotation.",
        "method_title": "Method, formulas and sources", "method_desc": "How we calculate, choose examples and limit the estimates.", "about_title": "About Measured Home", "about_desc": "A Vijeron project helping readers plan materials from checkable dimensions and product specifications.", "privacy_title": "Privacy policy", "privacy_desc": "How calculators, analytics and advertising work on Measured Home.",
        "paint_title": "Estimate wall paint", "paint_intro": "Measure a rectangular room's length, width and wall height, plus unpainted openings. Enter coverage per litre from your selected product's label.",
        "tile_title": "Estimate tile by the box", "tile_intro": "Enter a simple surface area or the result of your sketch, coverage per box from the package, and your chosen allowance.",
        "length": "Room length (m)", "width": "Room width (m)", "height": "Wall height (m)", "openings": "Unpainted openings (m²)", "coats": "Number of coats", "coverage": "Paint coverage (m²/L/coat)", "floor_area": "Surface to cover (m²)", "allowance": "Cut/breakage allowance (%)", "box_coverage": "Coverage per box (m²)", "calculate": "Calculate estimate", "result": "Planning result", "empty_result": "Enter dimensions and calculate. Values stay in your browser.",
        "paint_formula": "Gross wall area = 2 × (length + width) × height. Net area = gross area − openings. Litres = net area × coats ÷ coverage per litre per coat.",
        "tile_formula": "Order area = surface area × (1 + allowance ÷ 100). Boxes = round up order area ÷ coverage per box.",
        "paint_limit": "This formula covers four walls of a rectangular room at one height. Ceiling, trim, primer, texture and can sizes are not included.",
        "tile_limit": "This formula does not simulate layout direction, grout joints, edge cuts or package differences. Check the result against a sketch and your supplier.",
    },
}


def e(value: object) -> str:
    return html.escape(str(value), quote=True)


def path(lang: str, suffix: str = "") -> str:
    return ("/en/" if lang == "en" else "/") + suffix


def write(target: str, data: str) -> None:
    file = OUT / target.lstrip("/")
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(data, encoding="utf-8")


def add_url(lang: str, suffix: str = "") -> None:
    URLS.append(SITE + path(lang, suffix))


def head(lang: str, suffix: str, title: str, desc: str, kind: str = "WebPage", ads: bool = True) -> str:
    url = SITE + path(lang, suffix)
    other = "en" if lang == "id" else "id"
    schema = {"@context": "https://schema.org", "@type": kind, "name": title, "description": desc, "url": url,
              "inLanguage": lang, "datePublished": UPDATED, "dateModified": UPDATED,
              "author": {"@type": "Organization", "name": "Vijeron", "url": "https://vijeron.com/"},
              "publisher": {"@type": "Organization", "name": "Vijeron", "url": "https://vijeron.com/"},
              "isPartOf": {"@type": "WebSite", "name": "Rumah Terukur | Vijeron", "url": SITE + "/"}}
    consent = ("<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}"
               "gtag('consent','default',{ad_storage:'denied',analytics_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',wait_for_update:500});</script>"
               "<script async src='https://fundingchoicesmessages.google.com/i/pub-6180580801533680?ers=1'></script>"
               "<script async src='https://www.googletagmanager.com/gtag/js?id=G-79X7K7H4MJ'></script>"
               "<script>gtag('js',new Date());gtag('config','G-79X7K7H4MJ');</script>"
               "<script async crossorigin='anonymous' src='https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6180580801533680'></script>") if ads else ""
    alternates = "".join(f"<link rel='alternate' hreflang='{code}' href='{e(SITE + path(code, suffix))}'>" for code in ("id", "en"))
    alternates += f"<link rel='alternate' hreflang='x-default' href='{e(SITE + path('id', suffix))}'>"
    return (f"<!doctype html><html lang='{lang}'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>{e(title)} | Vijeron</title><meta name='description' content='{e(desc)}'><meta name='theme-color' content='#18382f'>"
            f"<link rel='canonical' href='{e(url)}'>{alternates}<link rel='icon' type='image/svg+xml' href='/assets/icon.svg'>"
            f"<link rel='stylesheet' href='/assets/site.css'><meta property='og:type' content='{'article' if kind == 'Article' else 'website'}'>"
            f"<meta property='og:title' content='{e(title)}'><meta property='og:description' content='{e(desc)}'><meta property='og:url' content='{e(url)}'>"
            f"<script type='application/ld+json'>{json.dumps(schema, ensure_ascii=False).replace('<', '\\u003c')}</script>{consent}</head><body>")


def chrome(lang: str, suffix: str) -> str:
    t = T[lang]
    other = "en" if lang == "id" else "id"
    return (f"<a class='skip' href='#main'>{e(t['skip'])}</a><header class='site-header'><div class='wrap header-inner'>"
            f"<a class='brand' href='{path(lang)}' aria-label='{e(t['name'])}'>"
            "<span class='brand-mark' aria-hidden='true'>⌂</span><span class='brand-words'><strong>RUMAH TERUKUR</strong><small>VIJERON / MEASURED HOME</small></span></a>"
            f"<nav aria-label='{e(t['guides'])}'><a href='{path(lang)}#panduan'>{e(t['guides'])}</a><a href='{path(lang)}#alat'>{e(t['tools'])}</a>"
            f"<a href='{path(lang, 'metode/')}'>{e(t['method'])}</a></nav><div class='lang' aria-label='Language / Bahasa'>"
            f"<a href='{path(lang, suffix)}' aria-current='page'>{'ID' if lang == 'id' else 'EN'}</a><span>/</span>"
            f"<a href='{path(other, suffix)}'>{'EN' if lang == 'id' else 'ID'}</a></div></div></header>")


def finish(lang: str, script: bool = False) -> str:
    t = T[lang]
    js = "<script defer src='/assets/calculator.js'></script>" if script else ""
    return (f"<footer class='site-footer'><div class='wrap footer-inner'><div><strong>{e(t['name'])}</strong><p>{e(t['footer'])}</p></div>"
            f"<nav><a href='{path(lang, 'metode/')}'>{e(t['method'])}</a><a href='{path(lang, 'tentang/')}'>{e(t['about'])}</a>"
            f"<a href='{path(lang, 'privasi/')}'>{e(t['privacy'])}</a><a href='https://vijeron.com/kontak.html'>{e(t['contact'])}</a>"
            "<a href='https://vijeron.com/'>Vijeron.com</a></nav></div><div class='wrap footer-bottom'>© Vijeron · "
            f"{e(t['updated'])}</div></footer>{js}</body></html>")


def source_links(keys: list[str]) -> str:
    return "<ul class='source-list'>" + "".join(f"<li><a href='{e(SOURCES[k][1])}' rel='noopener noreferrer'>{e(SOURCES[k][0])} ↗</a></li>" for k in keys) + "</ul>"


def home(lang: str) -> None:
    t = T[lang]
    cards = "".join(
        f"<article class='guide-card'><span class='card-number'>{i+1:02d} / 08</span><h3><a href='{path(lang, 'panduan/' + guide['slug'] + '/')}'>{e(guide[lang]['title'])}</a></h3>"
        f"<p>{e(guide[lang]['summary'])}</p><a class='card-link' href='{path(lang, 'panduan/' + guide['slug'] + '/')}'>{e(t['read'])} ↗</a></article>"
        for i, guide in enumerate(GUIDES))
    steps = "".join(f"<li><span>0{i}</span>{e(t['step'+str(i)])}</li>" for i in (1, 2, 3))
    body = (f"<main id='main'><section class='hero'><div class='wrap hero-grid'><div class='hero-copy'><p class='eyebrow'>{e(t['eyebrow'])}</p>"
            f"<h1>{e(t['hero'])}</h1><p class='lead'>{e(t['hero_desc'])}</p><div class='actions'><a class='button' href='{path(lang, 'panduan/ukur-ruang-persegi-panjang/')}'>{e(t['start'])} ↗</a>"
            f"<a class='button button-light' href='#alat'>{e(t['calc'])}</a></div></div><div class='plan-art' role='img' aria-label='Sketch of a rectangular room with measured edges'>"
            "<span class='plan-top'>4,20 m</span><span class='plan-side'>3,50 m</span><div class='plan-room'><span>14,70 <small>m²</small></span><i class='plan-door'></i></div><small class='plan-caption'>A = panjang × lebar / L × W</small></div></div></section>"
            f"<section class='wrap note-band'><div><span class='eyebrow'>FIELD NOTE / 01</span><h2>{e(t['hero_note'])}</h2></div><p>{e(t['hero_note_body'])}</p></section>"
            f"<section class='wrap section steps'><div class='section-head'><span class='eyebrow'>01 / PROCESS</span><h2>{e(t['steps'])}</h2></div><ol>{steps}</ol></section>"
            f"<section class='tools-section' id='alat'><div class='wrap section'><div class='section-head'><span class='eyebrow'>02 / TOOLS</span><h2>{e(t['tool_heading'])}</h2><p>{e(t['tool_intro'])}</p></div>"
            f"<div class='tool-cards'><article><span class='tool-icon'>01 / L</span><h3>{e(t['paint'])}</h3><p>{e(t['paint_desc'])}</p><a href='{path(lang, 'alat/cat/')}'>{e(t['open'])} ↗</a></article>"
            f"<article><span class='tool-icon'>02 / m²</span><h3>{e(t['tile'])}</h3><p>{e(t['tile_desc'])}</p><a href='{path(lang, 'alat/keramik/')}'>{e(t['open'])} ↗</a></article></div></div></section>"
            f"<section class='wrap section' id='panduan'><div class='section-head'><span class='eyebrow'>03 / GUIDES</span><h2>{e(t['guide_heading'])}</h2><p>{e(t['guide_intro'])}</p></div><div class='guide-grid'>{cards}</div></section>"
            f"<section class='wrap source-note'><span class='eyebrow'>EDITORIAL NOTE</span><p>{e(t['source_note'])}</p><a href='{path(lang, 'metode/')}'>{e(t['method'])} ↗</a></section></main>")
    write(path(lang) + "index.html", head(lang, "", t["name"], t["hero_desc"]) + chrome(lang, "") + body + finish(lang))
    add_url(lang)


def guide_page(lang: str, article: dict, index: int) -> None:
    t, item = T[lang], article[lang]
    suffix = "panduan/" + article["slug"] + "/"
    next_item = GUIDES[(index + 1) % len(GUIDES)]
    sections = "".join(f"<section class='prose-section'><h2>{e(title)}</h2><p>{e(body)}</p></section>" for title, body in item["sections"])
    body = (f"<main id='main' class='wrap article-layout'><article><nav class='crumb'><a href='{path(lang)}'>{e(t['home'])}</a><span> / </span>{e(t['guides'])} {index+1:02d}</nav>"
            f"<header class='article-head'><p class='eyebrow'>FIELD GUIDE / {index+1:02d}—08</p><h1>{e(item['title'])}</h1><p class='lead'>{e(item['summary'])}</p><p class='byline'>Vijeron · {e(t['updated'])}</p></header>"
            f"<div class='prose'>{sections}<aside class='example'><span class='eyebrow'>{e(t['worked'])}</span><p>{e(item['example'])}</p></aside>"
            f"<aside class='pitfall'><strong>{e(t['pitfall'])}</strong><p>{e(item['pitfall'])}</p></aside><section class='references'><h2>{e(t['references'])}</h2>{source_links(article['sources'])}</section></div>"
            f"<p class='next-guide'><span>{e(t['next'])}</span><a href='{path(lang, 'panduan/' + next_item['slug'] + '/')}'>{e(next_item[lang]['title'])} ↗</a></p></article>"
            f"<aside class='article-aside'><div class='aside-panel'><span class='eyebrow'>TOOLS / 01—02</span><h2>{e(t['tool_heading'])}</h2>"
            f"<p>{e(t['tool_intro'])}</p><a href='{path(lang, 'alat/cat/')}'>{e(t['paint'])} ↗</a><a href='{path(lang, 'alat/keramik/')}'>{e(t['tile'])} ↗</a></div>"
            f"<div class='aside-panel'><h2>{e(t['method'])}</h2><p>{e(t['source_note'])}</p><a href='{path(lang, 'metode/')}'>{e(t['read'])} ↗</a></div></aside></main>")
    write(path(lang, suffix) + "index.html", head(lang, suffix, item["title"], item["summary"], "Article") + chrome(lang, suffix) + body + finish(lang))
    add_url(lang, suffix)


def field(name: str, label: str, value: str, maximum: str, minimum: str = "0", step: str = "any") -> str:
    return (f"<label class='field' for='{name}'><span>{e(label)}</span><input id='{name}' name='{name}' type='number' required inputmode='decimal'"
            f" min='{minimum}' max='{maximum}' step='{step}' value='{value}'></label>")


def tool_page(lang: str, kind: str) -> None:
    t = T[lang]
    paint = kind == "cat"
    suffix = "alat/" + kind + "/"
    title = t["paint_title"] if paint else t["tile_title"]
    intro = t["paint_intro"] if paint else t["tile_intro"]
    fields = (field("length", t["length"], "4.2", "1000", "0.01") + field("width", t["width"], "3.5", "1000", "0.01") +
              field("height", t["height"], "2.8", "100", "0.01") + field("openings", t["openings"], "4.5", "100000") +
              field("coats", t["coats"], "2", "20", "1", "1") + field("coverage", t["coverage"], "10", "1000", "0.01")) if paint else (
              field("floor-area", t["floor_area"], "14.7", "1000000", "0.01") +
              field("allowance", t["allowance"], "10", "100", "0") +
              field("box-coverage", t["box_coverage"], "1.44", "1000", "0.01"))
    formula = t["paint_formula"] if paint else t["tile_formula"]
    limit = t["paint_limit"] if paint else t["tile_limit"]
    related = GUIDES[3 if paint else 4]
    body = (f"<main id='main' class='wrap tool-page'><nav class='crumb'><a href='{path(lang)}'>{e(t['home'])}</a><span> / </span>{e(t['tools'])}</nav>"
            f"<header class='tool-head'><p class='eyebrow'>CALCULATOR / {'01' if paint else '02'}</p><h1>{e(title)}</h1><p class='lead'>{e(intro)}</p></header>"
            f"<div class='calculator-grid'><form id='calculator' data-kind='{kind}' data-lang='{lang}'><div class='fields'>{fields}</div>"
            f"<button class='button' type='submit'>{e(t['calculate'])} ↗</button></form><div class='result-panel' id='result' role='status' aria-live='polite'>"
            f"<span class='eyebrow'>{e(t['result'])}</span><strong>—</strong><p>{e(t['empty_result'])}</p></div></div>"
            f"<div class='tool-explain'><section><h2>{e(t['method'])}</h2><p>{e(formula)}</p><p>{e(limit)}</p><a href='{path(lang, 'metode/')}'>{e(t['method'])} ↗</a></section>"
            f"<section><h2>{e(t['next'])}</h2><p>{e(related[lang]['summary'])}</p><a href='{path(lang, 'panduan/' + related['slug'] + '/')}'>{e(related[lang]['title'])} ↗</a></section></div></main>")
    write(path(lang, suffix) + "index.html", head(lang, suffix, title, intro) + chrome(lang, suffix) + body + finish(lang, True))
    add_url(lang, suffix)


def info_page(lang: str, kind: str) -> None:
    t = T[lang]
    info = {
        "metode": (t["method_title"], t["method_desc"], [
            ("Rumus / Formulas", ("Cat: luas kotor = 2 × (panjang + lebar) × tinggi; luas bersih = luas kotor − bukaan; liter = luas bersih × lapisan ÷ daya sebar. Keramik: luas pesanan = luas bidang × (1 + cadangan/100); kotak = pembulatan ke atas dari luas pesanan ÷ cakupan satu kotak." if lang == "id" else "Paint: gross area = 2 × (length + width) × height; net area = gross area − openings; litres = net area × coats ÷ coverage. Tile: order area = surface × (1 + allowance/100); boxes = round up order area ÷ coverage per box.")),
            ("Asumsi / Assumptions", ("Alat cat menganggap empat dinding ruang persegi panjang dengan tinggi sama. Alat keramik memakai luas yang Anda masukkan, bukan simulasi susunan keping. Daya sebar, cakupan kotak, dan cadangan berasal dari pengguna. Harga, ongkos kerja, pajak, primer, dan kemasan cat tidak dihitung." if lang == "id" else "The paint tool assumes four walls of a rectangle at one height. The tile tool uses your entered area, not a tile-layout simulation. Users provide product coverage and allowance. Prices, labour, taxes, primer and paint-can sizes are excluded.")),
            ("Proses editorial / Editorial process", ("Panduan dan contoh ditulis khusus untuk Vijeron pada 9 Oktober 2026. Rujukan di bawah digunakan untuk mengecek satuan, batas daya sebar, dan perencanaan material. Tidak ada hasil pengujian produk, foto proyek nyata, atau sertifikasi profesional yang diklaim. Perubahan penting dicatat lewat Git." if lang == "id" else "Guides and examples were written for Vijeron on 9 October 2026. References below check units, coverage limits and material planning. We claim no product tests, real-project photos or professional certification. Material changes are recorded in Git.")),
        ]),
        "tentang": (t["about_title"], t["about_desc"], [
            ("Tujuan / Purpose", ("Rumah Terukur membantu pembaca mengubah sketsa dan label kemasan menjadi perkiraan yang dapat dihitung ulang. Situs ini bahan literasi perencanaan, bukan jasa ukur, desain struktur, pemasangan, atau penjualan bahan." if lang == "id" else "Measured Home helps readers turn sketches and package labels into reproducible estimates. It is a planning-literacy resource, not a measuring, structural-design, installation or material-sales service.")),
            ("Penerbit / Publisher", ("Vijeron menerbitkan panduan ini sebagai bagian dari katalog di vijeron.com. Organisasi yang ditautkan sebagai sumber tidak berafiliasi dengan kami. Kirim koreksi melalui halaman kontak portal beserta URL dan rincian yang perlu diperiksa." if lang == "id" else "Vijeron publishes this guide as part of its catalog at vijeron.com. Linked source organizations are not affiliated with us. Send corrections through the portal contact page with a URL and the passage to review.")),
            ("Iklan / Ads", ("Kode Google AdSense ada pada halaman konten. Penayangan bergantung pada persetujuan AdSense dan pilihan privasi yang berlaku. Iklan tidak menentukan rumus atau rekomendasi editorial. Tidak ada tautan afiliasi produk pada peluncuran ini." if lang == "id" else "Google AdSense code is present on content pages. Serving depends on AdSense approval and applicable privacy choices. Ads do not determine formulas or editorial recommendations. This launch has no product affiliate links.")),
        ]),
        "privasi": (t["privacy_title"], t["privacy_desc"], [
            ("Data kalkulator / Calculator data", ("Dimensi, bukaan, jumlah lapisan, daya sebar, luas, cadangan, dan cakupan kemasan diproses di peramban. Situs ini tidak mengirim atau menyimpan angka yang Anda masukkan pada server Vijeron." if lang == "id" else "Dimensions, openings, coats, paint coverage, surface area, allowance and box coverage are processed in your browser. This site does not send or store your inputs on a Vijeron server.")),
            ("Analitik / Analytics", ("Google Analytics 4 dipakai untuk kunjungan dan peristiwa pemakaian alat. Peristiwa hanya berisi nama alat dan bahasa halaman, tanpa input atau hasil. Ketersediaannya bergantung pada pilihan persetujuan." if lang == "id" else "Google Analytics 4 measures visits and tool-use events. Events contain only the tool name and page language, not inputs or results. Availability depends on consent choices.")),
            ("Iklan dan persetujuan / Advertising and consent", ("Kode AdSense dan Google Funding Choices dapat dimuat pada halaman konten. Penyimpanan iklan, personalisasi, dan analitik dimulai dalam keadaan ditolak hingga pilihan persetujuan yang berlaku diperoleh. Google dapat memproses data menurut kebijakan layanannya." if lang == "id" else "AdSense and Google Funding Choices code may load on content pages. Ad storage, personalization and analytics storage start denied until applicable consent is obtained. Google may process data under its service policies.")),
            ("Kontak / Contact", ("Untuk pertanyaan privasi atau koreksi, gunakan halaman kontak Vijeron. Jangan mengirim denah rumah atau alamat pribadi yang tidak diperlukan." if lang == "id" else "Use the Vijeron contact page for privacy questions or corrections. Do not send unnecessary home plans or private addresses.")),
        ]),
    }
    title, desc, sections = info[kind]
    suffix = kind + "/"
    paragraphs = "".join(f"<section class='prose-section'><h2>{e(h)}</h2><p>{e(p)}</p></section>" for h, p in sections)
    refs = f"<section class='references'><h2>{e(t['references'])}</h2>{source_links(list(SOURCES))}</section>" if kind == "metode" else ""
    body = (f"<main id='main' class='wrap info-page'><nav class='crumb'><a href='{path(lang)}'>{e(t['home'])}</a><span> / </span>{e(title)}</nav>"
            f"<p class='eyebrow'>{e(t['eyebrow'])}</p><h1>{e(title)}</h1><p class='lead'>{e(desc)}</p><div class='prose'>{paragraphs}{refs}</div></main>")
    write(path(lang, suffix) + "index.html", head(lang, suffix, title, desc, ads=kind != "privasi") + chrome(lang, suffix) + body + finish(lang))
    add_url(lang, suffix)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    for asset in ("site.css", "calculator.js", "icon.svg"):
        shutil.copy2(ROOT / "assets" / asset, OUT / "assets" / asset)
    for lang in ("id", "en"):
        home(lang)
        for index, article in enumerate(GUIDES):
            guide_page(lang, article, index)
        for kind in ("cat", "keramik"):
            tool_page(lang, kind)
        for kind in ("metode", "tentang", "privasi"):
            info_page(lang, kind)
    write("404.html", "<!doctype html><html lang='id'><meta charset='utf-8'><title>Halaman tidak ditemukan | Vijeron</title><link rel='stylesheet' href='/assets/site.css'><main class='wrap info-page'><h1>Halaman tidak ditemukan</h1><p>Kembali ke <a href='/'>Rumah Terukur</a>.</p></main></html>")
    write("robots.txt", "User-agent: *\nAllow: /\nSitemap: https://rumah.vijeron.com/sitemap.xml\n")
    write("ads.txt", "google.com, pub-6180580801533680, DIRECT, f08c47fec0942fa0\n")
    write("_headers", "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  Cache-Control: public, max-age=0, must-revalidate\n\n/assets/*\n  Cache-Control: public, max-age=3600, must-revalidate\n\n/sitemap.xml\n  Content-Type: application/xml; charset=utf-8\n\n/ads.txt\n  Content-Type: text/plain; charset=utf-8\n")
    xml = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url in URLS:
        node = SubElement(xml, "url")
        SubElement(node, "loc").text = url
        SubElement(node, "lastmod").text = UPDATED
    ElementTree(xml).write(OUT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    print(f"Built {len(URLS)} public pages in {OUT}")


if __name__ == "__main__":
    main()
