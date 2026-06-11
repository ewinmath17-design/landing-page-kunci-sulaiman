import streamlit as st
from PIL import Image
import os

# Konfigurasi Halaman (Premium Look)
st.set_page_config(
    page_title="Kunci Sulaiman Berkah",
    page_icon="🗝️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS Kustom untuk Tampilan Premium & Profesional
st.markdown('''
<style>
    /* Warna Utama: Dark Blue & Gold/Bronze */
    :root {
        --primary-blue: #0F2027;
        --secondary-blue: #203A43;
        --gold: #D4AF37;
        --white: #FFFFFF;
    }
    
    .main {
        background-color: #FAFAFA;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    h1, h2, h3, h4 {
        color: var(--primary-blue) !important;
        text-align: center;
        font-weight: bold;
    }
    
    .hero-section {
        background: linear-gradient(to right, var(--primary-blue), var(--secondary-blue), #2C5364);
        color: white !important;
        padding: 3rem 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
    }
    
    .hero-section h1 {
        color: var(--gold) !important;
        font-size: 2.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin-bottom: 1rem;
    }
    
    .hero-section p {
        color: #E0E0E0 !important;
        font-size: 1.2rem;
        margin-top: 1rem;
        line-height: 1.6;
    }
    
    .cta-button {
        display: inline-block;
        background: linear-gradient(to bottom, #FFDF00, #D4AF37);
        color: #0F2027 !important;
        padding: 18px 35px;
        font-size: 1.4rem;
        font-weight: 800;
        border-radius: 50px;
        text-decoration: none;
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
        transition: all 0.3s ease;
        margin: 25px 0;
        text-align: center;
        border: 2px solid #FFF;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .cta-button:hover {
        transform: translateY(-3px) scale(1.02);
        background: linear-gradient(to bottom, #FFE533, #D4AF37);
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.6);
    }
    
    .section-box {
        background: white;
        padding: 2.5rem;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.06);
        margin-bottom: 2.5rem;
        border-top: 4px solid var(--gold);
    }
    
    .price-strike {
        text-decoration: line-through;
        color: #E74C3C;
        font-size: 1.3rem;
    }
    
    .price-final {
        color: #27AE60;
        font-size: 3rem;
        font-weight: 900;
        margin: 10px 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .testimonial {
        font-style: italic;
        border-left: 5px solid var(--gold);
        margin: 20px 0;
        background: #F8F9FA;
        padding: 20px;
        border-radius: 0 12px 12px 0;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #444;
    }
    
    .center-text {
        text-align: center;
    }
    
    ul {
        line-height: 1.8;
        font-size: 1.1rem;
        color: #333;
    }
</style>
''', unsafe_allow_html=True)

# Fungsi bantuan untuk memuat gambar
def load_image(img_name):
    if os.path.exists(img_name):
        return Image.open(img_name)
    return None

# --- SECTION 1: HERO / ATTENTION ---
st.markdown('''
<div class="hero-section">
    <h1>Sudah Banting Tulang Tapi Rezeki Masih Seret?</h1>
    <h2 style="color: white !important; font-size: 1.6rem; font-weight: 500;">Temukan Kunci Rahasia Nabi Sulaiman untuk Menarik Keberlimpahan & Kekayaan Berkah Sekarang Juga!</h2>
    <p>Pelajari metode teruji yang mengubah hidup ribuan orang, membuka pintu rezeki dari arah tak terduga, dan hidup tenang tanpa khawatir masalah finansial, bahkan jika Anda merasa sudah mencoba segalanya!</p>
</div>
''', unsafe_allow_html=True)

hero_img = load_image("Gemini_Generated_Image_7n2xf17n2xf17n2x.png")
if hero_img:
    st.image(hero_img, use_container_width=True)

st.markdown('<div class="center-text"><a href="https://wa.me/6282293274916?text=Halo%20Admin,%20saya%20mau%20pesan%20E-book%20Kunci%20Sulaiman%20Berkah%20dengan%20harga%20promo%20Rp99.000." target="_blank" class="cta-button">YA! SAYA MAU KUNCI REZEKI BERKAH!</a></div>', unsafe_allow_html=True)

# --- SECTION 2: PROBLEM / AGITATION ---
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown('<h3>💔 Apakah Ini Yang Anda Rasakan Saat Ini?</h3>', unsafe_allow_html=True)
st.markdown('''
* **Frustrasi:** Anda sudah bekerja keras, pagi hingga malam, mengorbankan waktu, tenaga, bahkan kesehatan. Tapi mengapa rezeki terasa begitu sulit digenggam?
* **Khawatir:** Setiap akhir bulan, Anda dihantui rasa cemas tentang tagihan, utang yang menumpuk, dan masa depan finansial yang tidak pasti.
* **Bingung:** Sudah mencoba berbagai tips dan trik, tapi hasilnya nihil. Anda merasa terjebak dalam lingkaran kemiskinan dan tidak tahu harus mulai dari mana.
* **Putus Asa:** Melihat orang lain sukses dan kaya raya, Anda merasa iri dan bertanya-tanya, "Kapan giliran saya?" Anda merasa takdir Anda memang begini-begini saja.
* **Mencari Kedamaian:** Anda ingin sukses finansial, tapi juga mendambakan ketenangan batin dan keberkahan dalam setiap rezeki yang didapat, bukan sekadar kekayaan duniawi.

*Jika salah satu atau semua poin di atas menggambarkan kondisi Anda, maka Anda BUKANLAH satu-satunya. Jutaan orang di luar sana merasakan hal yang sama. Dan tahukah Anda? Ini BUKAN salah Anda. Anda hanya belum menemukan "kunci" yang tepat.*

Bayangkan jika kondisi ini terus berlanjut... Stres akan semakin menguasai hidup Anda, hubungan dengan keluarga bisa terganggu, dan impian-impian besar Anda akan terkubur dalam-dalam.
''')
st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 3: PROMISE / OUTCOME ---
st.markdown('<div class="section-box" style="background-color: #F0F8FF; border-top: 4px solid #2980B9;">', unsafe_allow_html=True)
st.markdown('<h3>🌈 Bayangkan Hidup Anda Berubah Drastis...</h3>', unsafe_allow_html=True)
st.markdown('''
Bagaimana jika Anda bisa:
* **Menarik Rezeki Berlimpah:** Uang mengalir dari berbagai arah, bahkan dari sumber yang tidak terduga, dengan cara yang halal dan berkah.
* **Hidup Bebas Khawatir:** Tidak lagi pusing memikirkan tagihan, utang lunas, dan mampu menabung untuk masa depan yang cerah.
* **Meraih Impian:** Mampu membeli rumah idaman, menyekolahkan anak ke tempat terbaik, naik haji/umroh, atau membantu orang tua.
* **Merasakan Ketenangan Hati:** Merasa lebih dekat dengan Tuhan, bersyukur atas setiap karunia, dan memiliki hati yang lapang.
* **Menjadi Magnet Kebaikan:** Keberlimpahan yang Anda dapatkan menjadi jalan untuk berbuat lebih banyak kebaikan bagi sesama.

Semua ini BUKANLAH mimpi. Ini adalah realitas yang bisa Anda ciptakan dengan "Kunci Sulaiman Berkah".
''')
st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 4: UNIQUE MECHANISM ---
st.markdown('<h3>🔑 Memperkenalkan: Kunci Sulaiman Berkah</h3>', unsafe_allow_html=True)
st.markdown('<p class="center-text" style="font-size: 1.2rem; color:#203A43; margin-bottom: 30px;"><strong>Rahasia di Balik Keberlimpahan Luar Biasa Nabi Sulaiman yang Kini Bisa Anda Miliki!</strong></p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.5])
with col1:
    img_bundle = load_image("Gemini_Generated_Image_3iy7r33iy7r33iy7.png")
    if img_bundle:
        st.image(img_bundle, use_container_width=True)
with col2:
    st.markdown('''
    Ini BUKAN sekadar buku motivasi biasa. Ini BUKAN ritual mistis atau ajaran sesat.
    
    "Kunci Sulaiman Berkah" adalah sebuah sistem holistik yang kami rangkum dari prinsip-prinsip spiritual, mental, dan praktis yang digunakan oleh Nabi Sulaiman AS, seorang Nabi yang dianugerahi kekayaan, kekuasaan, dan hikmah yang tak tertandingi.
    
    Anda akan belajar bagaimana:
    * **Menyelaraskan Niat:** Membangun fondasi niat yang kuat dan benar.
    * **Mengubah Frekuensi Diri:** Memprogram ulang pikiran bawah sadar Anda menjadi "magnet rezeki".
    * **Mengoptimalkan Tindakan:** Menggabungkan usaha lahiriah dengan kekuatan spiritual untuk hasil maksimal.
    * **Membuka Pintu Rezeki Tak Terduga:** Memahami cara kerja alam semesta.
    ''')

# --- SECTION 5: WHAT YOU GET / BENEFITS ---
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown('<h3>🎁 Inilah Yang Akan Anda Dapatkan:</h3>', unsafe_allow_html=True)
st.markdown('''
Di dalam E-book "Kunci Sulaiman Berkah":
* **Bab 1:** Memahami Konsep Rezeki Berkah ala Nabi Sulaiman
* **Bab 2:** 5 Pilar Keberlimpahan Nabi Sulaiman
* **Bab 3:** Teknik Membangun Mindset Magnet Rezeki
* **Bab 4:** Rahasia Doa & Dzikir Pembuka Pintu Langit
* **Bab 5:** Strategi Tindakan Lahiriah yang Selaras
* **Bab 6:** Mengelola Rezeki dengan Bijak
* **Bab 7:** Studi Kasus & Kisah Inspiratif
''')
st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 7: PROOF / TESTIMONIALS ---
st.markdown('<h3>💬 Apa Kata Mereka?</h3>', unsafe_allow_html=True)
st.markdown('''
<div class="testimonial">
    "Alhamdulillah! Setelah membaca dan mempraktikkan Kunci Sulaiman Berkah, rezeki saya mulai mengalir dari arah yang tidak terduga. Utang lunas, dan sekarang bisa menabung untuk masa depan anak. Terima kasih banyak!"<br>
    <strong>— Ibu Aminah, Pedagang Online, Jakarta</strong>
</div>
<div class="testimonial">
    "Awalnya saya ragu, apakah metode spiritual seperti ini bisa membantu. Tapi setelah mencoba, pikiran saya jadi lebih positif, dan benar saja, orderan di toko saya meningkat drastis. Luar biasa!"<br>
    <strong>— Bapak Budi, Pemilik Warung Kelontong, Surabaya</strong>
</div>
<div class="testimonial">
    "Saya merasa lebih tenang dan bersyukur. Bukan hanya uang yang bertambah, tapi hubungan dengan keluarga juga membaik. Ini lebih dari sekadar buku tentang uang, ini tentang kehidupan."<br>
    <strong>— Mbak Sita, Karyawan Swasta, Bandung</strong>
</div>
''', unsafe_allow_html=True)

# --- SECTION 8: OFFER STACK / BONUS ---
st.markdown('<div id="offer-section" class="section-box" style="border: 4px solid var(--gold); background-color: #FFFAFA; padding: 3rem 2rem;">', unsafe_allow_html=True)
st.markdown('<h3>🎯 Dapatkan E-book Hari Ini + 3 BONUS SPESIAL!</h3>', unsafe_allow_html=True)

st.markdown('<p style="font-size: 1.1rem; text-align: center; margin-bottom: 2rem;">Ini adalah kesempatan Anda untuk memiliki panduan lengkap menuju keberlimpahan sejati.</p>', unsafe_allow_html=True)

st.markdown('**Anda Akan Mendapatkan:**')
st.markdown('✅ **E-book "Kunci Sulaiman Berkah"** (Nilai Asli: Rp350.000)')

st.markdown('**PLUS 3 BONUS EKSKLUSIF SENILAI Rp297.000, GRATIS UNTUK ANDA!**')

b_col1, b_col2, b_col3 = st.columns(3)
with b_col1:
    img_b1 = load_image("Gemini_Generated_Image_atp2l1atp2l1atp2.png")
    if img_b1: st.image(img_b1, caption="Bonus 1: 7 Amalan E-book")
    st.caption("Amalan harian penarik rezeki.")
with b_col2:
    img_b2 = load_image("Gemini_Generated_Image_81nsdc81nsdc81ns.png")
    if img_b2: st.image(img_b2, caption="Bonus 2: Audio Hipnoterapi")
    st.caption("Reprogram pikiran bawah sadar.")
with b_col3:
    img_b3 = load_image("Gemini_Generated_Image_tqbe2ztqbe2ztqbe.png")
    if img_b3: st.image(img_b3, caption="Bonus 3: Jurnal Syukur")
    st.caption("Latih rasa syukur harian.")

st.markdown('<div class="center-text" style="margin-top: 30px;">', unsafe_allow_html=True)
st.markdown('<p>Total Nilai Semua Produk Ini: <span class="price-strike">Rp647.000</span></p>', unsafe_allow_html=True)
st.markdown('<p style="font-size:1.4rem; font-weight:bold; color: #333;">TAPI HARI INI SAJA, CUKUP DENGAN INVESTASI SEBESAR:</p>', unsafe_allow_html=True)
st.markdown('<p class="price-final">Rp 99.000,- SAJA!</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 9 & 10: URGENCY & GARANSI ---
st.error('⏰ **Jangan Lewatkan Kesempatan Emas Ini!** Penawaran spesial ini HANYA BERLAKU UNTUK 100 PEMBELI PERTAMA atau sampai akhir minggu ini saja.')
st.success('💎 **Garansi 30 Hari Uang Kembali 100% Tanpa Ribet!** Kami sangat yakin dengan kekuatan "Kunci Sulaiman Berkah". Jika dalam 30 hari Anda merasa tidak ada perubahan positif sedikit pun, kami akan kembalikan 100% uang Anda tanpa pertanyaan.')

# --- SECTION 11: CTA AKHIR ---
st.markdown('<div class="center-text" style="margin-top: 40px; margin-bottom: 60px;">', unsafe_allow_html=True)
st.markdown('<h3>🚀 Ambil Tindakan Sekarang & Buka Pintu Rezeki Berkah Anda!</h3>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 1.1rem; margin-bottom: 20px;">Ribuan orang telah merasakan manfaatnya, sekarang giliran Anda!</p>', unsafe_allow_html=True)
st.markdown('<a href="https://wa.me/6282293274916?text=Halo%20Admin,%20saya%20mau%20pesan%20E-book%20Kunci%20Sulaiman%20Berkah%20dengan%20harga%20promo%20Rp99.000." target="_blank" class="cta-button">YA! SAYA MAU KUNCI REZEKI BERKAH!</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
