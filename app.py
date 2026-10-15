import streamlit as st

# ---------- KONFIGURASI HALAMAN ----------
st.set_page_config(
    page_title="Profil Saya",
    page_icon="👤",
    layout="centered",
)

# ---------- DATA PROFIL (EDIT BAGIAN INI) ----------
NAMA = "Nama Lengkap Anda"
PROFESI = "Mahasiswa / Web Developer / Data Analyst"
LOKASI = "Medan, Sumatera Utara"
EMAIL = "email@contoh.com"
TENTANG = (
    "Halo! Saya seorang yang antusias dalam dunia teknologi. "
    "Saya suka belajar hal baru, membangun proyek, dan berbagi pengetahuan. "
    "Ubah teks ini dengan deskripsi singkat tentang diri Anda."
)

# Isi dengan nama file lokal (contoh: "foto.jpg") atau link langsung ke foto
FOTO = "rrr.jpg"

KEAHLIAN = {
    "Python": 85,
    "HTML & CSS": 70,
    "SQL": 65,
    "Data Analysis": 75,
}

PROYEK = [
    {
        "judul": "Aplikasi Manajemen Tugas",
        "deskripsi": "Aplikasi sederhana untuk mencatat dan memantau tugas harian.",
        "tautan": "https://github.com/",
    },
    {
        "judul": "Dashboard Penjualan",
        "deskripsi": "Visualisasi data penjualan menggunakan Streamlit dan Pandas.",
        "tautan": "https://github.com/",
    },
    {
        "judul": "Website Portofolio",
        "deskripsi": "Website pribadi untuk menampilkan profil dan karya.",
        "tautan": "https://github.com/",
    },
]

SOSIAL_MEDIA = {
    "GitHub": "https://github.com/",
    "LinkedIn": "https://linkedin.com/",
    "Instagram": "https://instagram.com/",
}

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("📌 Menu")
    halaman = st.radio(
        "Pilih halaman:",
        ["🏠 Beranda", "💡 Keahlian", "📂 Proyek", "✉️ Kontak"],
    )
    st.divider()
    st.caption(f"© 2026 {NAMA}")


# ---------- HALAMAN ----------
def halaman_beranda():
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image(FOTO, use_container_width=True)
        except Exception:
            st.markdown(
                "<div style='font-size:110px; text-align:center;'>👤</div>",
                unsafe_allow_html=True,
            )
    with col2:
        st.title(NAMA)
        st.subheader(PROFESI)
        st.write(f"📍 {LOKASI}")
        st.write(f"📧 {EMAIL}")

    st.divider()
    st.header("Tentang Saya")
    st.write(TENTANG)

    st.subheader("Media Sosial")
    cols = st.columns(len(SOSIAL_MEDIA))
    for col, (nama, url) in zip(cols, SOSIAL_MEDIA.items()):
        col.link_button(nama, url, use_container_width=True)


def halaman_keahlian():
    st.header("💡 Keahlian")
    for skill, nilai in KEAHLIAN.items():
        st.write(f"**{skill}** — {nilai}%")
        st.progress(nilai / 100)


def halaman_proyek():
    st.header("📂 Proyek")
    for p in PROYEK:
        with st.container(border=True):
            st.subheader(p["judul"])
            st.write(p["deskripsi"])
            st.link_button("Lihat Proyek", p["tautan"])


def halaman_kontak():
    st.header("✉️ Hubungi Saya")
    with st.form("form_kontak", clear_on_submit=True):
        nama = st.text_input("Nama")
        email = st.text_input("Email")
        pesan = st.text_area("Pesan")
        kirim = st.form_submit_button("Kirim")

    if kirim:
        if nama and email and pesan:
            st.success(f"Terima kasih, {nama}! Pesan Anda sudah diterima.")
            # Catatan: pesan belum disimpan ke mana pun.
            # Anda bisa menambahkan logika kirim email atau simpan ke database.
        else:
            st.warning("Mohon lengkapi semua kolom terlebih dahulu.")


# ---------- ROUTING ----------
if halaman == "🏠 Beranda":
    halaman_beranda()
elif halaman == "💡 Keahlian":
    halaman_keahlian()
elif halaman == "📂 Proyek":
    halaman_proyek()
else:
    halaman_kontak()