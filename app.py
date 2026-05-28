import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import os
import io
import time


st.set_page_config(
    page_title="PixelCrush Image Compressor",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Outfit:wght@300;400;500;600;700;800&display=swap');

html, body ,  [class*="css"]    {
    font-family: 'Outfit', sans-serif;
    background: #080b14;
    color: #e2e8f0;
}
.stApp { background:     #080b14;   }

/* noise grain overlay */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
    opacity: 0.4;
}
.block-container {
    position: relative;
    z-index: 1;
    max-width: 1200px;
    padding: 2rem 2rem 4rem;
}
#MainMenu, footer, header { visibility: hidden; }

/* ── top bar ── */
.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 3rem;
    padding-bottom: 1.2rem;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}
.logo {
    font-family: 'Space Mono', monospace;
    font-size: 1.3rem;
    font-weight: 700;
    letter-spacing: -0.5px;
    color: #fff;
}
.logo span {
    color: #6366f1;
}
.logo-tag {
    font-family: 'Space Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 3px;
    color: rgba(255,255,255,0.25);
    text-transform: uppercase;
    margin-top: 2px;
}

/* ── hero ── */
.hero {
    text-align: center;
    margin-bottom: 3rem;
}
.hero-eyebrow {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 4px;
    color: #6366f1;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.hero-title {
    font-size: 3.5rem;
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -1.5px;
    color: #fff;
    margin-bottom: 0.8rem;
}
.hero-title em {
    font-style: normal;
    color: transparent;
    -webkit-text-stroke: 1px rgba(255,255,255,0.4);
}
.hero-sub {
    font-size: 1rem;
    font-weight: 300;
    color: rgba(200,210,230,0.55);
    max-width: 520px;
    margin: 0 auto;
    line-height: 1.7;
}

/* ── upload zone ── */
.upload-hint {
    text-align: center;
    font-size: 0.78rem;
    color: rgba(180,190,220,0.40);
    letter-spacing: 1px;
    margin-top: 0.5rem;
    font-family: 'Space Mono', monospace;
}

/* override streamlit uploader */
div[data-testid="stFileUploader"] {
    background: rgba(99,102,241,0.04) !important;
    border: 1.5px dashed rgba(99,102,241,0.35) !important;
    border-radius: 16px !important;
    padding: 1rem !important;
    transition: border-color 0.3s !important;
}
div[data-testid="stFileUploader"]:hover {
    border-color: rgba(99,102,241,0.65) !important;
}

/* ── slider section ── */
.slider-wrap {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 1.6rem 2rem;
    margin: 1.5rem 0;
}
.slider-title {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 3px;
    color: rgba(180,190,220,0.45);
    text-transform: uppercase;
    margin-bottom: 1rem;
}

/* widget labels */
label[data-testid="stWidgetLabel"] p {
    color: rgba(200,210,235,0.75) !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    font-family: 'Outfit', sans-serif !important;
}

/* ── compress button ── */
div[data-testid="stButton"] button {
    width: 100%;
    background: #6366f1;
    color: #fff;
    font-family: 'Space Mono', monospace;
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    border: none;
    border-radius: 12px;
    padding: 0.85rem 2rem;
    cursor: pointer;
    box-shadow: 0 4px 24px rgba(99,102,241,0.35);
    transition: all 0.25s ease;
    margin-top: 0.5rem;
}
div[data-testid="stButton"] button:hover {
    background: #818cf8;
    transform: translateY(-1px);
    box-shadow: 0 8px 32px rgba(99,102,241,0.50);
}

/* ── section divider ── */
.section-divider {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin: 2.5rem 0 1.8rem;
}
.section-divider-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 3px;
    color: rgba(180,190,220,0.35);
    text-transform: uppercase;
    white-space: nowrap;
}
.section-divider-line {
    flex: 1;
    height: 1px;
    background: rgba(255,255,255,0.06);
}

/* ── image containers ── */
.img-card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 18px;
    overflow: hidden;
}
.img-card-header {
    padding: 0.85rem 1.2rem;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.img-card-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(180,190,220,0.45);
}
.img-card-size {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    font-weight: 700;
    color: #6366f1;
}
.img-card-body { padding: 1rem; }

/* ── stats row ── */
.stats-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 2rem 0;
}
.stat-box {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 1.2rem 1rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.stat-box::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #6366f1, transparent);
}
.stat-val {
    font-family: 'Space Mono', monospace;
    font-size: 1.5rem;
    font-weight: 700;
    color: #fff;
    line-height: 1;
    margin-bottom: 0.4rem;
}
.stat-val.green { color: #34d399; }
.stat-val.purple { color: #a78bfa; }
.stat-val.orange { color: #fb923c; }
.stat-lbl {
    font-size: 0.68rem;
    color: rgba(180,190,220,0.40);
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-family: 'Space Mono', monospace;
}

/* ── color palette ── */
.palette-section {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 18px;
    padding: 1.6rem 2rem;
    margin: 1.5rem 0;
}
.palette-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.2rem;
}
.palette-title {
    font-family: 'Space Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: rgba(180,190,220,0.45);
}
.palette-row {
    display: flex;
    gap: 0.6rem;
    flex-wrap: wrap;
    align-items: center;
}
.color-swatch {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.35rem;
}
.swatch-block {
    width: 48px;
    height: 48px;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
.swatch-hex {
    font-family: 'Space Mono', monospace;
    font-size: 0.52rem;
    color: rgba(180,190,220,0.45);
}

/* ── download section ── */
.download-section {
    background: linear-gradient(135deg, rgba(99,102,241,0.08), rgba(139,92,246,0.05));
    border: 1px solid rgba(99,102,241,0.20);
    border-radius: 18px;
    padding: 1.8rem 2rem;
    margin-top: 1.5rem;
    text-align: center;
}
.download-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #fff;
    margin-bottom: 0.3rem;
}
.download-sub {
    font-size: 0.82rem;
    color: rgba(180,190,220,0.45);
    margin-bottom: 1.2rem;
}

/* download button override */
div[data-testid="stDownloadButton"] button {
    background: transparent !important;
    border: 1.5px solid rgba(99,102,241,0.50) !important;
    color: #a5b4fc !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 2px !important;
    border-radius: 10px !important;
    padding: 0.65rem 1.5rem !important;
    transition: all 0.25s !important;
}
div[data-testid="stDownloadButton"] button:hover {
    background: rgba(99,102,241,0.12) !important;
    border-color: #6366f1 !important;
    color: #fff !important;
}

/* progress bar color */
div[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, #6366f1, #a78bfa) !important;
}

/* selectbox */
div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
}

.footer {
    text-align: center;
    color: rgba(180,190,220,0.18);
    font-family: 'Space Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 2px;
    margin-top: 4rem;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)

# Top bar 
st.markdown("""
<div class="topbar">
  <div>
    <div class="logo">Pixel<span>Crush</span></div>
    <div class="logo-tag">KMeans Image Compression</div>
  </div>
  <div style="font-family:'Space Mono',monospace;font-size:0.62rem;
              letter-spacing:2px;color:rgba(180,190,220,0.25);text-transform:uppercase;">
    Built with Scikit-learn · Streamlit
  </div>
</div>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">KMeans Clustering · Color Quantization</div>
  <div class="hero-title">Compress Images<br>with <em>Machine Learning</em></div>
  <div class="hero-sub">Reduce any image to K colors using KMeans clustering.
  See the before and after, size saved — and download instantly.</div>
</div>
""", unsafe_allow_html=True)

# upload 
uploaded_file = st.file_uploader(
    "Drop your image here",
    type=["jpg", "jpeg", "png", "webp"],
    label_visibility="collapsed"
)
st.markdown('<div class="upload-hint">JPG · PNG · WEBP · Max 10MB recommended</div>',
            unsafe_allow_html=True)

if uploaded_file is not None:

    # Settings
    st.markdown('<div class="slider-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="slider-title">Compression Settings</div>', unsafe_allow_html=True)

    col_s1, col_s2, col_s3 = st.columns([2, 2, 1])
    with col_s1:
        k = st.slider(
            "Number of Colors (K)",
            min_value=2, max_value=64, value=16, step=1,
            help="Lower K = more compression, fewer colors. Higher K = better quality, more colors."
        )
    with col_s2:
        output_format = st.selectbox(
            "Output Format",
            ["JPEG", "PNG", "WEBP"],
            help="JPEG gives smallest size. PNG preserves quality. WEBP is modern and efficient."
        )
    with col_s3:
        st.markdown("<br>", unsafe_allow_html=True)
        run = st.button("Compress Image")
    st.markdown('</div>', unsafe_allow_html=True)

    # Load image 
    original_pil   = Image.open(uploaded_file).convert("RGB")
    original_array = np.array(original_pil)
    h, w, _        = original_array.shape

    # Original file size
    uploaded_file.seek(0)
    original_bytes    = uploaded_file.read()
    original_size_kb  = len(original_bytes) / 1024

    if run:
        #KMeans compression
        progress_bar = st.progress(0, text="Reading pixels...")
        time.sleep(0.2)

        pixels = original_array.reshape(-1, 3).astype(np.float32)
        progress_bar.progress(20, text="Fitting KMeans clustering...")

        kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
        kmeans.fit(pixels)
        progress_bar.progress(65, text="Replacing pixels with cluster centers...")

        compressed_pixels = kmeans.cluster_centers_[kmeans.labels_].astype(np.uint8)
        new_image_array   = compressed_pixels.reshape(original_array.shape)
        progress_bar.progress(85, text="Building compressed image...")

        compressed_pil = Image.fromarray(new_image_array)

        # Save
        fmt = output_format.upper()
        buf = io.BytesIO()
        save_kwargs = {"format": fmt}
        if fmt == "JPEG":
            save_kwargs["quality"] = 85
        elif fmt == "WEBP":
            save_kwargs["quality"] = 85
        compressed_pil.save(buf, **save_kwargs)
        compressed_bytes   = buf.getvalue()
        compressed_size_kb = len(compressed_bytes) / 1024

        progress_bar.progress(100, text="Done!")
        time.sleep(0.4)
        progress_bar.empty()

        # Stats :
        size_reduction    = ((original_size_kb - compressed_size_kb) / original_size_kb) * 100
        original_colors   = len(np.unique(pixels.astype(np.uint8), axis=0))
        color_reduction   = ((original_colors - k) / original_colors) * 100

        st.markdown(f"""
        <div class="stats-row">
          <div class="stat-box">
            <div class="stat-val">{original_size_kb:.0f}<span style="font-size:0.8rem;color:rgba(255,255,255,0.4)"> KB</span></div>
            <div class="stat-lbl">Original Size</div>
          </div>
          <div class="stat-box">
            <div class="stat-val green">{compressed_size_kb:.0f}<span style="font-size:0.8rem;color:rgba(255,255,255,0.4)"> KB</span></div>
            <div class="stat-lbl">Compressed Size</div>
          </div>
          <div class="stat-box">
            <div class="stat-val orange">{size_reduction:.1f}<span style="font-size:0.9rem;color:rgba(255,255,255,0.4)">%</span></div>
            <div class="stat-lbl">Size Reduced</div>
          </div>
          <div class="stat-box">
            <div class="stat-val purple">{original_colors:,}<span style="font-size:0.65rem"> → </span>{k}</div>
            <div class="stat-lbl">Colors Reduced</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        #Before & after
        st.markdown("""
        <div class="section-divider">
          <div class="section-divider-line"></div>
          <div class="section-divider-label">Before vs After</div>
          <div class="section-divider-line"></div>
        </div>
        """, unsafe_allow_html=True)

        col_before, col_after = st.columns(2)

        with col_before:
            st.markdown(f"""
            <div class="img-card">
              <div class="img-card-header">
                <span class="img-card-label">Original</span>
                <span class="img-card-size">{original_size_kb:.1f} KB</span>
              </div>
            </div>
            """, unsafe_allow_html=True)
            st.image(original_pil, use_container_width=True)
            st.caption(f"{w} × {h} px  ·  {original_colors:,} unique colors")

        with col_after:
            st.markdown(f"""
            <div class="img-card">
              <div class="img-card-header">
                <span class="img-card-label">Compressed — {k} Colors</span>
                <span class="img-card-size" style="color:#34d399">{compressed_size_kb:.1f} KB</span>
              </div>
            </div>
            """, unsafe_allow_html=True)
            st.image(compressed_pil, use_container_width=True)
            st.caption(f"{w} × {h} px  ·  {k} colors  ·  {size_reduction:.1f}% smaller")



        # download
        ext = fmt.lower().replace("jpeg", "jpg")
        filename = f"pixelcrush_k{k}_compressed.{ext}"
        mime_map  = {"JPEG": "image/jpeg", "PNG": "image/png", "WEBP": "image/webp"}

        st.markdown("""
        <div class="section-divider">
          <div class="section-divider-line"></div>
          <div class="section-divider-label">Download</div>
          <div class="section-divider-line"></div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="download-section">
          <div class="download-title">Your compressed image is ready</div>
          <div class="download-sub">
            {original_size_kb:.1f} KB → {compressed_size_kb:.1f} KB
            &nbsp;·&nbsp; Saved {size_reduction:.1f}%
            &nbsp;·&nbsp; {k} colors &nbsp;·&nbsp; {output_format} format
          </div>
        </div>
        """, unsafe_allow_html=True)

        col_d1, col_d2, col_d3 = st.columns([1, 2, 1])
        with col_d2:
            st.download_button(
                label=f"DOWNLOAD  {filename.upper()}",
                data=compressed_bytes,
                file_name=filename,
                mime=mime_map[fmt],
                use_container_width=True,
            )

        # Summary note :-
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);
                    border-radius:14px;padding:1.2rem 1.6rem;margin-top:1.5rem;">
          <div style="font-family:'Space Mono',monospace;font-size:0.6rem;
                      letter-spacing:3px;color:rgba(180,190,220,0.35);
                      text-transform:uppercase;margin-bottom:0.6rem;">How It Works</div>
          <div style="font-size:0.83rem;color:rgba(180,190,220,0.55);line-height:1.7;">
            Your image had <strong style="color:#a5b4fc">{original_colors:,} unique colors</strong>.
            KMeans grouped all pixels into <strong style="color:#a5b4fc">{k} clusters</strong>,
            then replaced every pixel with its nearest cluster center color.
            The result is a visually similar image that is
            <strong style="color:#34d399">{size_reduction:.1f}% smaller</strong> — no deep learning required.
          </div>
        </div>
        """, unsafe_allow_html=True)

else:
    # placeholder state
    st.markdown("""
    <div style="text-align:center;padding:4rem 2rem;
                background:rgba(255,255,255,0.02);
                border:1px dashed rgba(255,255,255,0.07);
                border-radius:20px;margin-top:1.5rem;">
      <div style="font-size:3rem;margin-bottom:1rem;">🖼️</div>
      <div style="font-family:'Space Mono',monospace;font-size:0.65rem;
                  letter-spacing:3px;color:rgba(180,190,220,0.25);text-transform:uppercase;">
        Upload an image above to get started
      </div>
    </div>
    """, unsafe_allow_html=True)

#footer
st.markdown("""
<div class="footer">
  PixelCrush · KMeans Image Compression · Scikit-learn + Streamlit
</div>
""", unsafe_allow_html=True)