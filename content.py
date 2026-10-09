"""Original bilingual editorial copy for the home-measurement guides."""

SOURCES = {
    "nist": ("NIST — SI Units: Area", "https://www.nist.gov/pml/owm/metric-si/si-units-area"),
    "paint": ("Sherwin-Williams — Paint Calculator and coverage notes", "https://www.sherwin-williams.com/en-us/color/color-tools/paint-calculator"),
    "tile": ("The Home Depot — How to calculate square footage", "https://www.homedepot.com/c/ah/how-to-calculate-square-footage/9ba683603be9fa5395fab90647548f6"),
    "layout": ("Daltile — Floor patterns and planning", "https://www.daltile.com/how-to/floor-patterns"),
    "lead": ("US EPA — Lead Renovation, Repair and Painting", "https://www.epa.gov/lead/lead-renovation-repair-and-painting-program"),
}

# Each page adds a reproducible example and a practical limitation. Sources check
# concepts; their prose, photographs and diagrams are not republished here.
GUIDES = [
    {
        "slug": "ukur-ruang-persegi-panjang", "sources": ["nist", "tile"],
        "id": {
            "title": "Mengukur luas ruang persegi panjang", "summary": "Catat panjang dan lebar dari permukaan yang benar sebelum menghitung meter persegi.",
            "sections": [
                ("Mulai dari permukaan yang akan dikerjakan", "Untuk lantai persegi panjang, ukur sisi dalam yang benar-benar akan ditutup. Catat panjang dan lebar dalam meter. Tulis hasil pengukuran dan tanggalnya, bukan hanya hasil kali akhir. Jika sisi berlawanan tampak berbeda, ukur keduanya dan periksa apakah ruang benar-benar persegi panjang sebelum memakai rumus sederhana."),
                ("Hitung dan beri satuan", "Luas lantai = panjang × lebar. Dua ukuran dalam meter menghasilkan meter persegi (m²), bukan meter. Ukuran 320 cm harus diubah menjadi 3,20 m sebelum dikalikan dengan angka dalam meter. Untuk dinding, gunakan lebar dinding × tinggi dinding, lalu catat bukaan secara terpisah."),
                ("Periksa ulang di tempat", "Sketsa kecil dengan nama tiap sisi membantu menemukan angka yang tertukar. Ukur bagian yang tidak rata pada beberapa titik. Kalkulator memberi angka dari ukuran yang Anda masukkan; bentuk asli, celah, dan penghalang tetap perlu dicek di lapangan."),
            ],
            "example": "Lantai 4,20 m × 3,50 m = 14,70 m². Angka ini luas bidang dasar; kebutuhan keramik dapat bertambah karena potongan dan cadangan yang Anda pilih.",
            "pitfall": "Jangan mengalikan 420 cm dengan 3,50 m. Samakan satuan dahulu agar hasil tidak membesar 100 kali.",
        },
        "en": {
            "title": "Measure a rectangular room", "summary": "Record the right length and width for the surface you intend to cover.",
            "sections": [
                ("Start with the surface you will work on", "For a rectangular floor, measure the inside edges of the area to be covered. Record length and width in metres, along with the date and raw measurements. If opposite sides differ, check the actual shape before relying on a single rectangle."),
                ("Calculate with units", "Floor area = length × width. Two lengths in metres produce square metres (m²), not metres. Convert 320 cm to 3.20 m before multiplying it by a measurement in metres. For a wall, use wall width × wall height and record openings separately."),
                ("Check the site again", "A small labelled sketch makes swapped dimensions easier to spot. Measure uneven edges at several points. A calculator only uses the numbers entered; the actual shape, gaps and obstacles still need an on-site check."),
            ],
            "example": "A 4.20 m × 3.50 m floor has an area of 14.70 m². This is its base area; the tile order may increase with cuts and the allowance you choose.",
            "pitfall": "Do not multiply 420 cm by 3.50 m. Convert to consistent units first or the result will be 100 times too large.",
        },
    },
    {
        "slug": "ruang-bentuk-l", "sources": ["nist", "tile"],
        "id": {
            "title": "Menghitung ruang berbentuk L tanpa menghitung dua kali", "summary": "Bagi denah menjadi bidang yang tidak saling tumpang tindih, lalu jumlahkan luasnya.",
            "sections": [
                ("Buat sketsa pembagian", "Tarik garis bantu sehingga ruang berbentuk L menjadi dua persegi panjang yang tidak tumpang tindih. Beri nama A dan B. Catat sisi yang diukur langsung dan sisi yang didapat dari pengurangan; tandai mana yang perlu diperiksa ulang."),
                ("Jumlahkan luas, bukan panjang", "Luas total = panjang A × lebar A + panjang B × lebar B. Cara lain adalah menghitung persegi panjang besar lalu mengurangi sudut kosong. Kedua cara seharusnya memberi hasil sama jika ukuran dan pembagiannya konsisten."),
                ("Bedakan luas bidang dan pesanan", "Luas total hanya menjawab berapa permukaan yang ada. Pola pemasangan, ukuran potongan, dan kerusakan dapat menambah material yang diperlukan. Masukkan cadangan sebagai asumsi tersendiri agar pembaca dapat mengubahnya."),
            ],
            "example": "Bidang A 4,0 × 3,0 m = 12 m²; bidang B 2,0 × 1,5 m = 3 m². Jika tidak bertumpang tindih, totalnya 15 m².",
            "pitfall": "Jangan menggambar dua persegi panjang yang sama-sama mencakup sudut pertemuan; area itu akan terhitung dua kali.",
        },
        "en": {
            "title": "Calculate an L-shaped room without double counting", "summary": "Split the plan into non-overlapping rectangles and add their areas.",
            "sections": [
                ("Sketch the split", "Draw a line that divides the L shape into two rectangles with no overlap. Label them A and B. Record which lengths were measured and which were obtained by subtraction; flag any dimension that needs a second check."),
                ("Add areas, not lengths", "Total area = length A × width A + length B × width B. Alternatively, calculate the surrounding rectangle and subtract the missing corner. Both methods should agree when the sketch and measurements are consistent."),
                ("Separate area from the order", "The total describes the surface, not the final purchase quantity. Layout, cut pieces and breakage can change the order. Keep the allowance as a separate, editable assumption."),
            ],
            "example": "Section A is 4.0 × 3.0 m = 12 m²; section B is 2.0 × 1.5 m = 3 m². If they do not overlap, the total is 15 m².",
            "pitfall": "Avoid drawing two rectangles that both include the corner where they meet; that area would be counted twice.",
        },
    },
    {
        "slug": "luas-dinding-dan-bukaan", "sources": ["nist", "paint"],
        "id": {
            "title": "Menghitung luas dinding dan bukaan", "summary": "Pisahkan luas dinding kotor, pintu, jendela, dan bagian yang tetap akan dicat.",
            "sections": [
                ("Ukur dinding satu per satu", "Pada ruang biasa, jumlahkan lebar semua dinding lalu kalikan tinggi yang sama. Jika tinggi berbeda, hitung setiap dinding tersendiri. Catat sisi yang memakai warna atau produk berbeda; jangan gabungkan semuanya ke satu pesanan cat."),
                ("Kurangi hanya bidang yang tidak dicat", "Luas pintu dan jendela boleh dikurangi bila bidang tersebut tidak dicat. Kusen, ceruk, dan lis yang tetap dicat perlu dicatat lagi sebagai pekerjaan terpisah. Bukaan yang kecil kadang tidak dikurangi pada estimasi kasar, tetapi keputusan itu harus terlihat dalam asumsi."),
                ("Jangan samakan luas dengan liter", "Luas bersih adalah langkah pertama. Jumlah lapisan dan daya sebar per liter dari produk yang dipilih menentukan estimasi liter. Kondisi permukaan dan metode aplikasi dapat mengubah pemakaian nyata."),
            ],
            "example": "Keliling 14 m × tinggi 2,8 m = 39,2 m² dinding kotor. Jika pintu 2,0 m² dan jendela 2,5 m² tidak dicat, luas bersih = 34,7 m².",
            "pitfall": "Mengurangi seluruh area jendela lalu melupakan kusen yang perlu dicat akan membuat estimasi pekerjaan tidak lengkap.",
        },
        "en": {
            "title": "Calculate wall area and openings", "summary": "Keep gross wall area, doors, windows and still-painted details separate.",
            "sections": [
                ("Measure each wall", "In a simple room, add wall widths and multiply by their shared height. If heights differ, calculate each wall separately. Note any walls using a different colour or product rather than combining every surface into one paint order."),
                ("Subtract only what remains unpainted", "Subtract a door or window if its area will not receive paint. Frames, reveals and trim that will be painted belong in a separate measurement. An early rough estimate may leave small openings in, but that choice should be explicit."),
                ("Area is not litres", "Net area is only the first step. The number of coats and the selected product's coverage per litre determine the volume estimate. Surface condition and application method can change actual use."),
            ],
            "example": "A 14 m perimeter × 2.8 m height gives 39.2 m² gross wall area. If an unpainted door is 2.0 m² and windows are 2.5 m², net area is 34.7 m².",
            "pitfall": "Subtracting the window area but forgetting frames that need paint leaves part of the job out of the estimate.",
        },
    },
    {
        "slug": "cat-daya-sebar-lapisan", "sources": ["paint", "lead"],
        "id": {
            "title": "Membaca daya sebar cat dan jumlah lapisan", "summary": "Gunakan spesifikasi produk sendiri, bukan angka liter universal untuk semua dinding.",
            "sections": [
                ("Temukan daya sebar pada kemasan", "Cari perkiraan m² per liter untuk produk dan permukaan yang akan dipakai. Angka pemasaran dan hasil lapangan bisa berbeda. Periksa apakah petunjuk mengandaikan satu lapis, alat aplikasi tertentu, atau permukaan yang telah disiapkan."),
                ("Hitung tiap lapisan", "Liter perkiraan = luas bersih × jumlah lapisan ÷ daya sebar per liter per lapis. Jika primer dan cat akhir adalah produk berbeda, hitung masing-masing, bukan menjumlahnya seolah satu produk. Bulatkan jumlah pembelian sesuai ukuran kemasan yang benar-benar tersedia."),
                ("Periksa permukaan dan keselamatan", "Permukaan sangat berpori, kasar, atau warna lama yang kontras dapat memerlukan penanganan berbeda. Jangan mengikis atau mengamplas lapisan lama tanpa memeriksa risiko bahan berbahaya; panduan EPA tentang cat timbal berlaku untuk konteks Amerika Serikat dan bukan pengganti aturan setempat."),
            ],
            "example": "Luas 34,7 m², dua lapis, dan daya sebar yang Anda baca 10 m²/L/lapis menghasilkan 34,7 × 2 ÷ 10 = 6,94 L sebelum pembulatan kemasan.",
            "pitfall": "Jangan memakai 10 m²/L sebagai sifat semua cat. Masukkan nilai dari label produk pilihan dan cek syarat aplikasinya.",
        },
        "en": {
            "title": "Read paint coverage and coat count", "summary": "Use the selected product's specifications, not one universal litres-per-wall figure.",
            "sections": [
                ("Find coverage on the product label", "Look for estimated square metres per litre for your product and surface. A published estimate can differ from actual use. Check whether it assumes one coat, a particular application method, or a prepared surface."),
                ("Calculate each coat", "Estimated litres = net area × coat count ÷ coverage per litre per coat. If primer and finish paint are different products, estimate them separately. Round a purchase to the pack sizes actually offered by your supplier."),
                ("Check the surface and safety", "Very porous or rough surfaces and a strongly contrasting old colour may need a different approach. Do not scrape or sand old coatings without checking material hazards; the EPA lead-paint guidance applies to a US context and does not replace local rules."),
            ],
            "example": "For 34.7 m², two coats and a label value of 10 m²/L/coat, the estimate is 34.7 × 2 ÷ 10 = 6.94 L before rounding to a pack size.",
            "pitfall": "Do not treat 10 m²/L as a property of all paints. Enter the selected label's value and check its application conditions.",
        },
    },
    {
        "slug": "menghitung-keramik-per-kotak", "sources": ["nist", "tile", "layout"],
        "id": {
            "title": "Menghitung keramik per kotak", "summary": "Ubah luas lantai menjadi jumlah kotak dengan cakupan kemasan yang sebenarnya.",
            "sections": [
                ("Mulai dari luas yang sudah diperiksa", "Hitung bidang lantai atau dinding yang akan dipasang. Pisahkan bagian yang memiliki ukuran atau tipe keramik berbeda. Jangan menyalin luas rumah dari iklan properti sebagai pengganti ukuran bidang pemasangan."),
                ("Masukkan cakupan satu kotak", "Label kemasan biasanya menyebut luas cakupan atau jumlah keping. Gunakan angka luas per kotak yang tertulis, lalu hitung kebutuhan = luas pesanan ÷ cakupan kotak. Karena kotak tidak bisa dibeli sebagian, bulatkan ke atas."),
                ("Tambahkan cadangan secara terbuka", "Cadangan menangani potongan, kerusakan, pola, dan kemungkinan penggantian. Tidak ada persentase yang tepat untuk semua proyek. Kalkulator membiarkan Anda memasukkan sendiri persentasenya; bandingkan dengan tata letak dan petunjuk pemasok."),
            ],
            "example": "Luas 14,7 m² dan cadangan pilihan 10% menjadi 16,17 m². Jika satu kotak mencakup 1,44 m², 16,17 ÷ 1,44 = 11,23; rencanakan 12 kotak.",
            "pitfall": "Jangan membulatkan kotak ke bawah. Sebelas kotak pada contoh hanya mencakup 15,84 m², kurang dari luas pesanan 16,17 m².",
        },
        "en": {
            "title": "Estimate tile by the box", "summary": "Turn measured surface area into whole boxes using the actual package coverage.",
            "sections": [
                ("Start with a checked area", "Measure the floor or wall that will be tiled. Keep sections using different tile sizes or types separate. A property's advertised floor area is not a substitute for measuring the installation surface."),
                ("Enter coverage per box", "A package usually states an area or a tile count. Use its area coverage, then calculate boxes = order area ÷ box coverage. Since you cannot normally purchase a fraction of a box, round up."),
                ("Show the allowance", "An allowance accounts for cuts, breakage, pattern and possible future replacement. No one percentage suits every project. The calculator lets you enter your own; compare it with the layout and supplier guidance."),
            ],
            "example": "A 14.7 m² floor with a chosen 10% allowance becomes 16.17 m². At 1.44 m² per box, 16.17 ÷ 1.44 = 11.23, so plan for 12 boxes.",
            "pitfall": "Do not round boxes down. Eleven boxes in this example cover only 15.84 m², less than the 16.17 m² order area.",
        },
    },
    {
        "slug": "potongan-dan-pola-keramik", "sources": ["layout", "tile"],
        "id": {
            "title": "Mengapa pola dan potongan mengubah pesanan keramik", "summary": "Luas yang sama bisa memerlukan jumlah material berbeda karena tata letak.",
            "sections": [
                ("Buat rencana susunan", "Gambar garis awal pemasangan, arah ubin, ambang pintu, serta sisi yang akan menerima potongan. Pola diagonal dan susunan dengan banyak sudut dapat menghasilkan sisa potongan yang berbeda dari susunan lurus. Ukuran nat juga memengaruhi penempatan, walau kalkulator luas sederhana tidak mensimulasikannya."),
                ("Uji beberapa keping di denah", "Bandingkan ukuran keping dengan lebar bidang. Dua rencana dapat memiliki luas sama tetapi menghasilkan potongan tepi yang berbeda. Bila pola rumit, minta pemasang atau pemasok meninjau sketsa sebelum memesan; estimasi area hanya titik awal."),
                ("Catat asumsi cadangan", "Pilih persentase cadangan setelah mempertimbangkan pola, jumlah sudut, dan cadangan penggantian. Tulis alasan pilihan itu pada catatan pesanan. Jika hasil kotak dibulatkan ke atas, cakupan ekstra dari pembulatan tersebut terlihat terpisah dari cadangan persen."),
            ],
            "example": "Pada lantai 15 m², cadangan pilihan 8% menambah 1,2 m² sehingga luas pesanan 16,2 m² sebelum dibagi cakupan kotak.",
            "pitfall": "Jangan menganggap persentase cadangan sebagai jaminan cukup. Pola dan dimensi nyata tetap perlu ditinjau.",
        },
        "en": {
            "title": "Why tile cuts and layout change an order", "summary": "Identical floor areas can require different quantities because of layout.",
            "sections": [
                ("Plan the layout", "Sketch a starting line, tile direction, thresholds and the edges that need cuts. A diagonal or corner-heavy pattern can create different offcuts from a straight layout. Grout joints also affect placement, although a simple area calculator does not simulate them."),
                ("Try a few tiles on the plan", "Compare tile size with the width of the space. Two plans may cover the same area yet create different edge pieces. For a complex pattern, ask an installer or supplier to review the sketch before ordering; the area estimate is only a starting point."),
                ("Document the allowance", "Choose an allowance after considering the pattern, corners and future replacement. Record the reason on the order note. Extra coverage created by rounding up to whole boxes is separate from the percentage allowance."),
            ],
            "example": "For a 15 m² floor, an 8% chosen allowance adds 1.2 m², giving a 16.2 m² order area before dividing by box coverage.",
            "pitfall": "Do not treat an allowance percentage as a guarantee. The real pattern and dimensions still need review.",
        },
    },
    {
        "slug": "meter-sentimeter-meter-persegi", "sources": ["nist"],
        "id": {
            "title": "Meter, sentimeter, dan meter persegi", "summary": "Pahami kapan satuan panjang berubah menjadi satuan luas.",
            "sections": [
                ("Panjang dan luas berbeda", "Meter (m) mengukur satu arah. Meter persegi (m²) mengukur bidang. Karena 1 m = 100 cm, satu bidang 1 m × 1 m berukuran 100 cm × 100 cm = 10.000 cm². Angka 100 tidak cukup untuk mengonversi luas."),
                ("Konversi sebelum perkalian", "Jika panjang dan lebar ditulis dalam sentimeter, bagi masing-masing dengan 100 untuk mendapat meter, lalu kalikan. Atau kalikan dalam cm² dan bagi hasilnya dengan 10.000. Pilih satu cara dan tulis satuan di setiap langkah."),
                ("Jaga ketelitian yang masuk akal", "Ukuran yang dibulatkan dapat mengubah kebutuhan bahan. Catat ukuran mentah untuk tiap bidang, terutama bila ada beberapa sudut. Jangan tampilkan banyak angka desimal seolah pengukuran di lapangan setepat itu."),
            ],
            "example": "Ubin 60 cm × 60 cm adalah 0,60 m × 0,60 m = 0,36 m² secara geometris, sebelum memperhitungkan nat, potongan, dan cakupan yang tercetak pada kotak.",
            "pitfall": "Mengubah 3.600 cm² menjadi 36 m² dengan membagi 100 adalah salah; bagi 10.000 sehingga menjadi 0,36 m².",
        },
        "en": {
            "title": "Metres, centimetres and square metres", "summary": "Know when a length unit becomes an area unit.",
            "sections": [
                ("Length and area differ", "A metre (m) measures one direction; a square metre (m²) measures a surface. Since 1 m = 100 cm, a 1 m × 1 m square is 100 cm × 100 cm = 10,000 cm². Dividing an area by 100 is not enough."),
                ("Convert before multiplying", "For dimensions in centimetres, divide each by 100 to obtain metres and then multiply. Or multiply in cm² and divide the result by 10,000. Choose one method and write the units at every step."),
                ("Keep realistic precision", "Rounded dimensions can change an order. Record raw measurements for every section, especially around corners. Avoid many decimal places that imply more precision than your field measurements provide."),
            ],
            "example": "A 60 cm × 60 cm tile is geometrically 0.60 m × 0.60 m = 0.36 m², before joints, cuts and the box's stated coverage are considered.",
            "pitfall": "Turning 3,600 cm² into 36 m² by dividing by 100 is wrong; divide by 10,000 to get 0.36 m².",
        },
    },
    {
        "slug": "lembar-rencana-material", "sources": ["nist", "paint", "tile"],
        "id": {
            "title": "Membuat lembar rencana material yang dapat diperiksa", "summary": "Simpan ukuran, sumber spesifikasi, asumsi, dan pembulatan dalam satu catatan.",
            "sections": [
                ("Pisahkan data dan keputusan", "Tulis ukuran yang Anda ukur sendiri, satuannya, tanggal, dan lokasi bidang. Di kolom lain, catat angka dari label produk seperti daya sebar atau cakupan per kotak. Cadangan potongan dan jumlah lapisan adalah keputusan proyek; jangan menyamarkannya sebagai hasil pengukuran."),
                ("Hitung bertahap", "Catat luas kotor, bagian yang dikurangi, luas bersih, cadangan atau lapisan, lalu pembulatan kemasan. Urutan ini membuat selisih antara hasil kalkulator dan angka pada nota dapat dijelaskan. Simpan merek dan nomor produk yang dipilih karena spesifikasinya dapat berbeda."),
                ("Tinjau sebelum membeli", "Periksa kembali bidang yang tidak beraturan, warna atau jenis material yang berbeda, dan ketersediaan kemasan. Untuk pekerjaan yang melibatkan listrik, struktur, atau bahan berbahaya, gunakan tenaga yang memenuhi syarat dan aturan setempat; lembar ini hanya alat perencanaan ukuran."),
            ],
            "example": "Catatan cat: dinding kotor 39,2 m²; bukaan 4,5 m²; bersih 34,7 m²; dua lapis; label 10 m²/L/lapis; hasil 6,94 L; ukuran kaleng dipilih setelah harga dan stok dicek.",
            "pitfall": "Jangan menyimpan hanya angka akhir '7 liter' tanpa ukuran dan spesifikasi yang menghasilkan angka tersebut.",
        },
        "en": {
            "title": "Make a material plan you can check", "summary": "Keep dimensions, product specifications, assumptions and rounding in one note.",
            "sections": [
                ("Separate facts from choices", "Record your measured dimensions, units, date and surface. In another column, write label figures such as coverage per litre or per box. Cut allowance and coat count are project choices; do not present them as measured facts."),
                ("Calculate in stages", "Write gross area, deductions, net area, allowance or coats, and package rounding in order. This helps explain differences between a calculator result and a receipt. Save the selected brand and product number because specifications vary."),
                ("Review before buying", "Recheck irregular areas, surfaces needing different colours or materials, and available pack sizes. For work involving electricity, structure or hazardous materials, follow local rules and use qualified help; this sheet only plans measurements."),
            ],
            "example": "Paint note: 39.2 m² gross wall; 4.5 m² openings; 34.7 m² net; two coats; label at 10 m²/L/coat; result 6.94 L; choose can sizes after checking price and stock.",
            "pitfall": "Do not save only '7 litres' without the measurements and product specification behind that figure.",
        },
    },
]
