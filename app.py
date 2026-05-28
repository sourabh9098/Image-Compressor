# import streamlit as st
# import numpy as np
# from PIL import Image
# from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt
# import os
# import io

# st.set_page_config(
#     page_title="AI Image Compression Lab",
#     page_icon="🎨",
#     layout="wide"
# )

# # =========================
# # DARK THEME CUSTOM CSS
# # =========================
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #0f1117;
#         color: white;
#     }

#     h1, h2, h3, h4 {
#         color: white;
#     }

#     .main-title {
#         font-size: 3rem;
#         font-weight: 700;
#         text-align: center;
#         margin-bottom: 0.5rem;
#         color: #ffffff;
#     }

#     .subtitle {
#         text-align: center;
#         color: #b0b3b8;
#         font-size: 1.1rem;
#         margin-bottom: 2rem;
#     }

#     .metric-card {
#         background-color: #1a1d24;
#         padding: 1rem;
#         border-radius: 16px;
#         text-align: center;
#         border: 1px solid #2d3139;
#         margin-bottom: 1rem;
#     }

#     .metric-value {
#         font-size: 2rem;
#         font-weight: bold;
#         color: #4cc9f0;
#     }

#     .metric-label {
#         color: #b0b3b8;
#         font-size: 1rem;
#     }

#     .mode-box {
#         background-color: #1a1d24;
#         padding: 1rem;
#         border-radius: 12px;
#         border: 1px solid #2d3139;
#         margin-top: 1rem;
#     }

#     .footer {
#         text-align: center;
#         color: gray;
#         margin-top: 3rem;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # =========================
# # TITLE
# # =========================

# st.markdown('<div class="main-title">🎨 AI Image Compression Lab</div>', unsafe_allow_html=True)
# st.markdown(
#     '<div class="subtitle">KMeans Based Intelligent Image Compression & Color Quantization System</div>',
#     unsafe_allow_html=True
# )

# # =========================
# # FILE UPLOAD
# # =========================

# uploaded_file = st.file_uploader(
#     "Upload an image",
#     type=["jpg", "jpeg", "png"]
# )

# if uploaded_file is not None:

#     # =========================
#     # LOAD IMAGE
#     # =========================

#     image = Image.open(uploaded_file).convert("RGB")
#     image_array = np.array(image)

#     # =========================
#     # K VALUE INPUT
#     # =========================

#     st.sidebar.header("⚙ Compression Settings")

#     k = st.sidebar.slider(
#         "Select Number of Colors (K)",
#         min_value=2,
#         max_value=64,
#         value=16,
#         step=2
#     )

#     # =========================
#     # ARTISTIC MODES
#     # =========================

#     st.sidebar.markdown("## 🎭 Artistic Compression Modes")

#     if k <= 4:
#         mode = "🕹 Retro Pixel Art Mode"
#     elif k <= 8:
#         mode = "🎨 Cartoon Compression Mode"
#     elif k <= 16:
#         mode = "🌈 Anime Style Compression"
#     elif k <= 32:
#         mode = "📷 Balanced Compression"
#     else:
#         mode = "✨ High Quality Compression"

#     st.sidebar.markdown(f"### {mode}")

#     # =========================
#     # FLATTEN IMAGE
#     # =========================

#     pixels = image_array.reshape(-1, 3)

#     # =========================
#     # APPLY KMEANS
#     # =========================

#     with st.spinner("Compressing image using KMeans clustering..."):

#         kmeans = KMeans(n_clusters=k, random_state=42)
#         kmeans.fit(pixels)

#         compressed_pixels = kmeans.cluster_centers_[kmeans.labels_]
#         compressed_pixels = compressed_pixels.astype('uint8')

#         compressed_image = compressed_pixels.reshape(image_array.shape)

#     # =========================
#     # SIDE BY SIDE COMPARISON
#     # =========================

#     st.markdown("## 🖼 Original vs Compressed")

#     col1, col2 = st.columns(2)

#     with col1:
#         st.image(image_array, caption="Original Image", use_container_width=True)

#     with col2:
#         st.image(compressed_image, caption=f"Compressed Image ({k} Colors)", use_container_width=True)

#     # =========================
#     # SAVE TEMP FILES
#     # =========================

#     original_buffer = io.BytesIO()
#     compressed_buffer = io.BytesIO()

#     image.save(original_buffer, format="PNG")
#     Image.fromarray(compressed_image).save(compressed_buffer, format="PNG")

#     original_size = len(original_buffer.getvalue()) / 1024
#     compressed_size = len(compressed_buffer.getvalue()) / 1024

#     # =========================
#     # COLOR ANALYTICS
#     # =========================

#     original_colors = len(np.unique(pixels, axis=0))
#     compressed_colors = k

#     reduction = ((original_colors - compressed_colors) / original_colors) * 100

#     # =========================
#     # METRICS
#     # =========================

#     st.markdown("## 📊 Compression Analytics")

#     m1, m2, m3, m4 = st.columns(4)

#     with m1:
#         st.markdown(
#             f'''
#             <div class="metric-card">
#                 <div class="metric-value">{original_size:.1f} KB</div>
#                 <div class="metric-label">Original Size</div>
#             </div>
#             ''',
#             unsafe_allow_html=True
#         )

#     with m2:
#         st.markdown(
#             f'''
#             <div class="metric-card">
#                 <div class="metric-value">{compressed_size:.1f} KB</div>
#                 <div class="metric-label">Compressed Size</div>
#             </div>
#             ''',
#             unsafe_allow_html=True
#         )

#     with m3:
#         st.markdown(
#             f'''
#             <div class="metric-card">
#                 <div class="metric-value">{original_colors}</div>
#                 <div class="metric-label">Original Colors</div>
#             </div>
#             ''',
#             unsafe_allow_html=True
#         )

#     with m4:
#         st.markdown(
#             f'''
#             <div class="metric-card">
#                 <div class="metric-value">{compressed_colors}</div>
#                 <div class="metric-label">Compressed Colors</div>
#             </div>
#             ''',
#             unsafe_allow_html=True
#         )

#     # =========================
#     # COLOR REDUCTION
#     # =========================

#     st.markdown(
#         f'''
#         <div class="mode-box">
#             <h3>🎯 Color Reduction</h3>
#             <h2>{reduction:.2f}% Reduction in Colors</h2>
#         </div>
#         ''',
#         unsafe_allow_html=True
#     )
   




#     # =========================
#     # DOWNLOAD BUTTON
#     # =========================

#     st.markdown("## ⬇ Download Compressed Image")

#     compressed_pil = Image.fromarray(compressed_image)

#     download_buffer = io.BytesIO()
#     compressed_pil.save(download_buffer, format="PNG")

#     st.download_button(
#         label="Download Compressed Image",
#         data=download_buffer.getvalue(),
#         file_name="compressed_image.png",
#         mime="image/png"
#     )


#     # FOOTER


#     st.markdown(
#         '<div class="footer">Built with KMeans Clustering • Machine Learning • Computer Vision</div>',
#         unsafe_allow_html=True
#     )

# else:

#     st.info("📤 Upload an image to start AI compression analysis")

















# import streamlit as st
# from PIL import Image
# import numpy as np
# from sklearn.cluster import KMeans
# import io
# import os
# import time

# # ── Page config ───────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="PixelPress — Image Compressor",
#     page_icon="🎨",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ── Custom CSS ────────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;600&family=DM+Mono&display=swap');

# html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

# .stApp {
#     background: linear-gradient(145deg, #0a0a14 0%, #0d0d1f 50%, #080810 100%);
#     color: #e2e8f0;
# }
# #MainMenu, footer, header { visibility: hidden; }
# .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

# /* ── Hero ── */
# .hero {
#     background: linear-gradient(135deg,
#         rgba(139,92,246,0.14) 0%,
#         rgba(59,130,246,0.08) 50%,
#         rgba(236,72,153,0.06) 100%);
#     border: 1px solid rgba(139,92,246,0.25);
#     border-radius: 24px;
#     padding: 2.5rem 3rem;
#     margin-bottom: 2rem;
#     position: relative;
#     overflow: hidden;
# }
# .hero::before {
#     content:'';
#     position:absolute;
#     top:-100px; right:-80px;
#     width:300px; height:300px;
#     border-radius:50%;
#     background:rgba(139,92,246,0.08);
#     filter:blur(60px);
# }
# .hero::after {
#     content:'';
#     position:absolute;
#     bottom:-80px; left:-60px;
#     width:250px; height:250px;
#     border-radius:50%;
#     background:rgba(59,130,246,0.06);
#     filter:blur(50px);
# }
# .hero-badge {
#     display:inline-block;
#     background:rgba(139,92,246,0.15);
#     border:1px solid rgba(139,92,246,0.35);
#     color:#c4b5fd;
#     font-size:0.72rem;
#     font-weight:600;
#     letter-spacing:2px;
#     text-transform:uppercase;
#     padding:4px 14px;
#     border-radius:20px;
#     margin-bottom:1rem;
# }
# .hero-title {
#     font-family:'Syne',sans-serif;
#     font-size:2.8rem;
#     font-weight:800;
#     background:linear-gradient(90deg,#a78bfa,#60a5fa,#f472b6);
#     -webkit-background-clip:text;
#     -webkit-text-fill-color:transparent;
#     margin:0 0 0.5rem;
#     line-height:1.1;
# }
# .hero-sub {
#     font-size:0.97rem;
#     color:#94a3b8;
#     max-width:580px;
#     line-height:1.7;
#     margin:0;
# }

# /* ── Upload zone ── */
# .upload-zone {
#     background:rgba(139,92,246,0.05);
#     border:2px dashed rgba(139,92,246,0.3);
#     border-radius:16px;
#     padding:2rem;
#     text-align:center;
#     transition:all 0.3s;
# }
# .upload-zone:hover { border-color:rgba(139,92,246,0.6); }

# /* ── Slider override ── */
# .stSlider > div > div > div { background:rgba(139,92,246,0.25) !important; }
# .stSlider > div > div > div > div { background:#8b5cf6 !important; }
# .stSlider label { color:#94a3b8 !important; font-size:0.85rem !important; }

# /* ── Button ── */
# .stButton > button {
#     width:100%;
#     background:linear-gradient(135deg,#7c3aed,#2563eb) !important;
#     color:white !important;
#     font-family:'Syne',sans-serif !important;
#     font-size:1.05rem !important;
#     font-weight:700 !important;
#     padding:0.85rem 2rem !important;
#     border-radius:12px !important;
#     border:none !important;
#     letter-spacing:0.5px !important;
#     box-shadow:0 4px 20px rgba(124,58,237,0.35) !important;
#     transition:all 0.3s !important;
# }
# .stButton > button:hover {
#     transform:translateY(-2px) !important;
#     box-shadow:0 8px 30px rgba(124,58,237,0.5) !important;
# }

# /* ── Download button ── */
# .stDownloadButton > button {
#     width:100%;
#     background:linear-gradient(135deg,#059669,#0891b2) !important;
#     color:white !important;
#     font-family:'Syne',sans-serif !important;
#     font-size:0.95rem !important;
#     font-weight:700 !important;
#     padding:0.75rem 1.5rem !important;
#     border-radius:12px !important;
#     border:none !important;
#     box-shadow:0 4px 16px rgba(5,150,105,0.3) !important;
# }
# .stDownloadButton > button:hover {
#     transform:translateY(-2px) !important;
#     box-shadow:0 8px 24px rgba(5,150,105,0.5) !important;
# }

# /* ── Metric cards ── */
# .metric-row {
#     display:grid;
#     grid-template-columns:repeat(4,1fr);
#     gap:12px;
#     margin:1.5rem 0;
# }
# .metric-card {
#     background:rgba(255,255,255,0.03);
#     border:1px solid rgba(255,255,255,0.07);
#     border-radius:14px;
#     padding:16px 18px;
#     text-align:center;
#     position:relative;
#     overflow:hidden;
# }
# .metric-card::before {
#     content:'';
#     position:absolute;
#     top:0; left:0; right:0;
#     height:2px;
#     background:var(--accent-line, #8b5cf6);
# }
# .metric-val {
#     font-family:'Syne',sans-serif;
#     font-size:1.7rem;
#     font-weight:800;
#     color:var(--val-color, #a78bfa);
#     line-height:1;
#     margin-bottom:4px;
# }
# .metric-lbl {
#     font-size:0.72rem;
#     color:#64748b;
#     text-transform:uppercase;
#     letter-spacing:1.5px;
#     font-weight:600;
# }

# /* ── Image comparison ── */
# .img-label {
#     font-family:'Syne',sans-serif;
#     font-size:0.85rem;
#     font-weight:700;
#     text-align:center;
#     padding:8px 0;
#     border-radius:8px 8px 0 0;
#     letter-spacing:1px;
#     text-transform:uppercase;
# }
# .img-original { background:rgba(59,130,246,0.1); color:#60a5fa; border:1px solid rgba(59,130,246,0.2); }
# .img-compressed { background:rgba(139,92,246,0.1); color:#a78bfa; border:1px solid rgba(139,92,246,0.2); }

# /* ── Progress bar ── */
# .reduction-bar-wrap { margin:0.5rem 0 1.5rem; }
# .reduction-bar-label {
#     font-size:0.75rem;
#     color:#64748b;
#     letter-spacing:1px;
#     text-transform:uppercase;
#     margin-bottom:6px;
#     font-weight:600;
# }
# .reduction-bar-bg {
#     background:rgba(255,255,255,0.06);
#     border-radius:8px;
#     height:10px;
#     overflow:hidden;
# }
# .reduction-bar-fill {
#     height:100%;
#     border-radius:8px;
#     background:linear-gradient(90deg,#7c3aed,#2563eb,#0891b2);
#     transition:width 1s ease;
# }
# .reduction-pct {
#     font-family:'Syne',sans-serif;
#     font-size:1.1rem;
#     font-weight:800;
#     color:#a78bfa;
#     margin-top:4px;
# }

# /* ── K guide ── */
# .k-guide {
#     background:rgba(255,255,255,0.02);
#     border:1px solid rgba(255,255,255,0.06);
#     border-radius:12px;
#     padding:14px 16px;
#     margin-top:1rem;
# }
# .k-row {
#     display:flex;
#     justify-content:space-between;
#     align-items:center;
#     padding:5px 0;
#     border-bottom:1px solid rgba(255,255,255,0.04);
#     font-size:0.82rem;
# }
# .k-row:last-child { border-bottom:none; }
# .k-range { color:#a78bfa; font-family:'DM Mono',monospace; font-weight:600; }
# .k-label { color:#64748b; }
# .k-quality { font-weight:600; }

# /* ── Info box ── */
# .info-box {
#     background:rgba(139,92,246,0.06);
#     border:1px solid rgba(139,92,246,0.18);
#     border-radius:12px;
#     padding:1rem 1.2rem;
#     font-size:0.85rem;
#     color:#94a3b8;
#     line-height:1.7;
#     margin-top:0.8rem;
# }

# /* ── Sidebar ── */
# [data-testid="stSidebar"] {
#     background:rgba(8,8,20,0.97) !important;
#     border-right:1px solid rgba(255,255,255,0.05) !important;
# }

# /* ── Scrollbar ── */
# ::-webkit-scrollbar { width:4px; }
# ::-webkit-scrollbar-thumb { background:rgba(139,92,246,0.3); border-radius:2px; }

# /* ── Section title ── */
# .sec-title {
#     font-family:'Syne',sans-serif;
#     font-size:1rem;
#     font-weight:700;
#     color:#e2e8f0;
#     margin-bottom:1rem;
#     display:flex;
#     align-items:center;
#     gap:8px;
# }
# .sec-badge {
#     background:rgba(139,92,246,0.12);
#     border-radius:6px;
#     padding:3px 9px;
#     font-size:0.72rem;
#     color:#a78bfa;
#     font-family:'DM Mono',monospace;
# }

# /* ── vs divider ── */
# .vs-divider {
#     display:flex;
#     align-items:center;
#     justify-content:center;
#     font-family:'Syne',sans-serif;
#     font-size:1.4rem;
#     font-weight:800;
#     color:#475569;
#     height:100%;
#     padding-top:80px;
# }
# </style>
# """, unsafe_allow_html=True)


# # ── Sidebar ───────────────────────────────────────────────────────────────────
# with st.sidebar:
#     st.markdown("""
#     <div style='text-align:center;padding:1.2rem 0 1.5rem;'>
#       <div style='font-size:3rem'>🎨</div>
#       <div style='font-family:Syne,sans-serif;font-size:1.4rem;font-weight:800;
#                   background:linear-gradient(90deg,#a78bfa,#60a5fa);
#                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;'>
#         PixelPress
#       </div>
#       <div style='font-size:0.72rem;color:#475569;margin-top:4px;letter-spacing:2px;text-transform:uppercase;'>
#         KMeans Image Compressor
#       </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("---")
#     st.markdown("### 🧠 How It Works")
#     st.markdown("""
#     <div style='font-size:0.83rem;color:#64748b;line-height:1.8;'>
#     <b style='color:#a78bfa'>1.</b> Upload any image<br>
#     <b style='color:#a78bfa'>2.</b> Choose K (number of colors)<br>
#     <b style='color:#a78bfa'>3.</b> KMeans clusters all pixels into K color groups<br>
#     <b style='color:#a78bfa'>4.</b> Each pixel is replaced by its cluster center color<br>
#     <b style='color:#a78bfa'>5.</b> Result = same image, far fewer colors → smaller size
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("---")
#     st.markdown("### 📊 K Value Guide")
#     st.markdown("""
#     <div class='k-guide'>
#       <div class='k-row'>
#         <span class='k-range'>K = 2–8</span>
#         <span class='k-quality' style='color:#f87171'>Max Compression</span>
#       </div>
#       <div class='k-row'>
#         <span class='k-range'>K = 9–16</span>
#         <span class='k-quality' style='color:#fb923c'>High Compression</span>
#       </div>
#       <div class='k-row'>
#         <span class='k-range'>K = 17–32</span>
#         <span class='k-quality' style='color:#facc15'>Balanced</span>
#       </div>
#       <div class='k-row'>
#         <span class='k-range'>K = 33–64</span>
#         <span class='k-quality' style='color:#4ade80'>Good Quality</span>
#       </div>
#       <div class='k-row'>
#         <span class='k-range'>K = 65–128</span>
#         <span class='k-quality' style='color:#60a5fa'>Near Original</span>
#       </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("---")
#     st.markdown("""
#     <div style='font-size:0.75rem;color:#334155;line-height:1.6;'>
#     ⚠️ Higher K = better quality but slower processing.
#     Recommended starting point: <b style='color:#a78bfa'>K = 16</b>
#     </div>
#     """, unsafe_allow_html=True)


# # ── Hero ──────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="hero">
#   <div class="hero-badge">🎨 KMeans Clustering · Image Compression · ML</div>
#   <div class="hero-title">PixelPress</div>
#   <p class="hero-sub">
#     Upload any image, choose how many colors (K) to keep,
#     and watch KMeans clustering compress it in seconds.
#     Compare original vs compressed side-by-side with full size metrics.
#   </p>
# </div>
# """, unsafe_allow_html=True)


# # ── Upload + K input ──────────────────────────────────────────────────────────
# col_upload, col_k = st.columns([2, 1])

# with col_upload:
#     st.markdown('<div class="sec-title">📁 Upload Image <span class="sec-badge">JPG · PNG · JPEG · WEBP</span></div>', unsafe_allow_html=True)
#     uploaded_file = st.file_uploader(
#         "Drop your image here",
#         type=["jpg", "jpeg", "png", "webp"],
#         label_visibility="collapsed"
#     )

# with col_k:
#     st.markdown('<div class="sec-title">🎛️ Color Clusters <span class="sec-badge">K Value</span></div>', unsafe_allow_html=True)
#     k_value = st.slider(
#         "K — Number of Colors",
#         min_value=2,
#         max_value=128,
#         value=16,
#         step=1,
#         help="Lower K = more compression, fewer colors. Higher K = better quality, less compression."
#     )
#     st.markdown(f"""
#     <div class="info-box">
#       Selected <strong style='color:#a78bfa'>K = {k_value}</strong> — image will be
#       compressed to only <strong style='color:#a78bfa'>{k_value} colors</strong>.
#       {'⚡ Max compression!' if k_value <= 8 else
#        '🔥 High compression' if k_value <= 16 else
#        '⚖️ Balanced quality' if k_value <= 32 else
#        '✨ Good quality' if k_value <= 64 else
#        '🖼️ Near original quality'}
#     </div>
#     """, unsafe_allow_html=True)

# st.markdown("<div style='margin:1rem 0'></div>", unsafe_allow_html=True)


# # ── Helper functions ──────────────────────────────────────────────────────────
# def get_image_size_kb(img: Image.Image, fmt="JPEG") -> float:
#     """Get image size in KB by saving to buffer."""
#     buf = io.BytesIO()
#     img.save(buf, format=fmt)
#     return buf.tell() / 1024

# def compress_image(image: Image.Image, k: int):
#     """KMeans compression — exact same logic as notebook."""
#     image_array = np.array(image)
#     original_shape = image_array.shape

#     # Handle RGBA → RGB
#     if image_array.ndim == 2:
#         image_array = np.stack([image_array]*3, axis=-1)
#     if image_array.shape[2] == 4:
#         image_array = image_array[:, :, :3]

#     pixels = image_array.reshape(-1, 3)

#     # KMeans clustering
#     kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
#     kmeans.fit(pixels)

#     # Replace each pixel with its cluster center
#     compressed_pixels = kmeans.cluster_centers_[kmeans.labels_].astype('uint8')
#     new_image_array = compressed_pixels.reshape(image_array.shape)

#     compressed_img = Image.fromarray(new_image_array)

#     # Color stats
#     original_colors = len(np.unique(pixels, axis=0))
#     compressed_colors = k
#     color_reduction = ((original_colors - compressed_colors) / original_colors) * 100

#     return compressed_img, original_colors, compressed_colors, color_reduction

# def get_download_bytes(img: Image.Image) -> bytes:
#     buf = io.BytesIO()
#     img.save(buf, format="JPEG", quality=95)
#     return buf.getvalue()


# # ── Main logic ────────────────────────────────────────────────────────────────
# if uploaded_file is not None:

#     # Load image
#     original_img = Image.open(uploaded_file).convert("RGB")
#     orig_size_kb  = get_image_size_kb(original_img)
#     orig_w, orig_h = original_img.size

#     st.markdown("<div style='margin:0.5rem 0'></div>", unsafe_allow_html=True)

#     # ── Compress button ───────────────────────────────────────────────────────
#     compress_clicked = st.button(f"🚀 Compress with K = {k_value}", use_container_width=True)

#     if compress_clicked:
#         with st.spinner(f"Running KMeans with K={k_value} clusters... This may take a moment ⏳"):
#             t_start = time.time()
#             compressed_img, orig_colors, comp_colors, color_reduction = compress_image(original_img, k_value)
#             t_end   = time.time()

#         comp_size_kb  = get_image_size_kb(compressed_img)
#         size_reduction = max(0, ((orig_size_kb - comp_size_kb) / orig_size_kb) * 100)
#         time_taken     = round(t_end - t_start, 2)

#         # ── Metric cards ──────────────────────────────────────────────────────
#         st.markdown(f"""
#         <div class="metric-row">
#           <div class="metric-card" style="--accent-line:#60a5fa; --val-color:#60a5fa">
#             <div class="metric-val">{orig_size_kb:.1f} KB</div>
#             <div class="metric-lbl">Original Size</div>
#           </div>
#           <div class="metric-card" style="--accent-line:#a78bfa; --val-color:#a78bfa">
#             <div class="metric-val">{comp_size_kb:.1f} KB</div>
#             <div class="metric-lbl">Compressed Size</div>
#           </div>
#           <div class="metric-card" style="--accent-line:#4ade80; --val-color:#4ade80">
#             <div class="metric-val">{size_reduction:.1f}%</div>
#             <div class="metric-lbl">Size Reduced</div>
#           </div>
#           <div class="metric-card" style="--accent-line:#f472b6; --val-color:#f472b6">
#             <div class="metric-val">{color_reduction:.1f}%</div>
#             <div class="metric-lbl">Colors Reduced</div>
#           </div>
#         </div>
#         """, unsafe_allow_html=True)

#         # ── Size reduction bar ────────────────────────────────────────────────
#         st.markdown(f"""
#         <div class="reduction-bar-wrap">
#           <div class="reduction-bar-label">📉 File Size Reduction</div>
#           <div class="reduction-bar-bg">
#             <div class="reduction-bar-fill" style="width:{min(size_reduction, 100)}%"></div>
#           </div>
#           <div class="reduction-pct">{size_reduction:.1f}% smaller — {orig_size_kb:.1f} KB → {comp_size_kb:.1f} KB</div>
#         </div>
#         """, unsafe_allow_html=True)

#         # ── Color reduction bar ───────────────────────────────────────────────
#         st.markdown(f"""
#         <div class="reduction-bar-wrap">
#           <div class="reduction-bar-label">🎨 Color Palette Reduction</div>
#           <div class="reduction-bar-bg">
#             <div class="reduction-bar-fill" style="width:{min(color_reduction,100)}%;background:linear-gradient(90deg,#f472b6,#a78bfa)"></div>
#           </div>
#           <div class="reduction-pct" style="color:#f472b6">
#             {orig_colors:,} colors → {comp_colors} colors &nbsp;({color_reduction:.1f}% reduction)
#           </div>
#         </div>
#         """, unsafe_allow_html=True)

#         # ── Image comparison ──────────────────────────────────────────────────
#         st.markdown('<div class="sec-title" style="margin-top:1.5rem">🖼️ Original vs Compressed <span class="sec-badge">Side by Side</span></div>', unsafe_allow_html=True)

#         img_col1, vs_col, img_col2 = st.columns([10, 1, 10])

#         with img_col1:
#             st.markdown('<div class="img-label img-original">📷 Original</div>', unsafe_allow_html=True)
#             st.image(original_img, use_container_width=True)
#             st.markdown(f"""
#             <div style='text-align:center;margin-top:8px;'>
#               <span style='font-family:DM Mono,monospace;font-size:0.8rem;color:#64748b;'>
#                 {orig_w} × {orig_h} px &nbsp;·&nbsp;
#                 <strong style='color:#60a5fa'>{orig_size_kb:.1f} KB</strong> &nbsp;·&nbsp;
#                 {orig_colors:,} colors
#               </span>
#             </div>
#             """, unsafe_allow_html=True)

#         with vs_col:
#             st.markdown("<div class='vs-divider'>⇄</div>", unsafe_allow_html=True)

#         with img_col2:
#             st.markdown('<div class="img-label img-compressed">✨ Compressed</div>', unsafe_allow_html=True)
#             st.image(compressed_img, use_container_width=True)
#             st.markdown(f"""
#             <div style='text-align:center;margin-top:8px;'>
#               <span style='font-family:DM Mono,monospace;font-size:0.8rem;color:#64748b;'>
#                 {orig_w} × {orig_h} px &nbsp;·&nbsp;
#                 <strong style='color:#a78bfa'>{comp_size_kb:.1f} KB</strong> &nbsp;·&nbsp;
#                 K = {k_value} colors
#               </span>
#             </div>
#             """, unsafe_allow_html=True)

#         # ── Stats table ───────────────────────────────────────────────────────
#         st.markdown("<div style='margin-top:1.5rem'></div>", unsafe_allow_html=True)
#         st.markdown('<div class="sec-title">📊 Full Stats <span class="sec-badge">Comparison Table</span></div>', unsafe_allow_html=True)

#         stat_c1, stat_c2, stat_c3 = st.columns(3)
#         with stat_c1:
#             st.metric("⏱️ Processing Time",  f"{time_taken}s")
#             st.metric("📐 Dimensions",       f"{orig_w} × {orig_h}")
#         with stat_c2:
#             st.metric("📦 Original Size",    f"{orig_size_kb:.2f} KB")
#             st.metric("📦 Compressed Size",  f"{comp_size_kb:.2f} KB",
#                       delta=f"-{orig_size_kb - comp_size_kb:.2f} KB",
#                       delta_color="inverse")
#         with stat_c3:
#             st.metric("🎨 Original Colors",  f"{orig_colors:,}")
#             st.metric("🎨 Compressed Colors",f"{k_value}",
#                       delta=f"-{orig_colors - k_value:,}",
#                       delta_color="inverse")

#         # ── Download ──────────────────────────────────────────────────────────
#         st.markdown("<div style='margin-top:1.5rem'></div>", unsafe_allow_html=True)
#         st.markdown('<div class="sec-title">⬇️ Download <span class="sec-badge">Save Compressed Image</span></div>', unsafe_allow_html=True)

#         download_bytes = get_download_bytes(compressed_img)
#         original_name  = uploaded_file.name.rsplit(".", 1)[0]

#         dl_c1, dl_c2 = st.columns(2)
#         with dl_c1:
#             st.download_button(
#                 label=f"⬇️ Download Compressed (K={k_value})",
#                 data=download_bytes,
#                 file_name=f"{original_name}_compressed_k{k_value}.jpg",
#                 mime="image/jpeg",
#                 use_container_width=True
#             )
#         with dl_c2:
#             st.markdown(f"""
#             <div style='background:rgba(5,150,105,0.08);border:1px solid rgba(5,150,105,0.2);
#                         border-radius:12px;padding:12px 16px;font-size:0.85rem;color:#6ee7b7;
#                         line-height:1.6;'>
#               ✅ Saved <strong>{orig_size_kb - comp_size_kb:.1f} KB</strong> of space<br>
#               📉 <strong>{size_reduction:.1f}%</strong> smaller than original<br>
#               🎨 Using only <strong>{k_value}</strong> of {orig_colors:,} original colors
#             </div>
#             """, unsafe_allow_html=True)

# else:
#     # ── Empty state ───────────────────────────────────────────────────────────
#     st.markdown("""
#     <div style='text-align:center;padding:4rem 2rem;'>
#       <div style='font-size:4rem;margin-bottom:1rem;'>🖼️</div>
#       <div style='font-family:Syne,sans-serif;font-size:1.4rem;font-weight:700;
#                   color:#e2e8f0;margin-bottom:0.5rem;'>Upload an image to get started</div>
#       <div style='color:#475569;font-size:0.9rem;line-height:1.7;max-width:400px;margin:0 auto;'>
#         Supports JPG, PNG, JPEG, WEBP.<br>
#         Then pick your K value and hit Compress.
#       </div>
#     </div>
#     """, unsafe_allow_html=True)




















# # ════════════════════════════════════════════════
# #  app.py — Streamlit UI Only
# #  All ML logic is inside model.py
# # ════════════════════════════════════════════════

# import streamlit as st
# from PIL import Image
# import time

# # ── Import compression logic from model.py ────────────────────────────────────
# from model import compress_image, get_size_kb, get_download_bytes

# # ── Page config ───────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="PixelPress — Image Compressor",
#     page_icon="🎨",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ── Custom CSS ────────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;600&family=DM+Mono&display=swap');
# html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
# .stApp { background: linear-gradient(145deg, #0a0a14 0%, #0d0d1f 50%, #080810 100%); color: #e2e8f0; }
# #MainMenu, footer, header { visibility: hidden; }
# .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
# .hero { background: linear-gradient(135deg, rgba(139,92,246,0.14) 0%, rgba(59,130,246,0.08) 50%, rgba(236,72,153,0.06) 100%); border: 1px solid rgba(139,92,246,0.25); border-radius: 24px; padding: 2.5rem 3rem; margin-bottom: 2rem; position: relative; overflow: hidden; }
# .hero-badge { display:inline-block; background:rgba(139,92,246,0.15); border:1px solid rgba(139,92,246,0.35); color:#c4b5fd; font-size:0.72rem; font-weight:600; letter-spacing:2px; text-transform:uppercase; padding:4px 14px; border-radius:20px; margin-bottom:1rem; }
# .hero-title { font-family:'Syne',sans-serif; font-size:2.8rem; font-weight:800; background:linear-gradient(90deg,#a78bfa,#60a5fa,#f472b6); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin:0 0 0.5rem; line-height:1.1; }
# .hero-sub { font-size:0.97rem; color:#94a3b8; max-width:580px; line-height:1.7; margin:0; }
# .stSlider > div > div > div { background:rgba(139,92,246,0.25) !important; }
# .stSlider > div > div > div > div { background:#8b5cf6 !important; }
# .stButton > button { width:100%; background:linear-gradient(135deg,#7c3aed,#2563eb) !important; color:white !important; font-family:'Syne',sans-serif !important; font-size:1.05rem !important; font-weight:700 !important; padding:0.85rem 2rem !important; border-radius:12px !important; border:none !important; box-shadow:0 4px 20px rgba(124,58,237,0.35) !important; }
# .stDownloadButton > button { width:100%; background:linear-gradient(135deg,#059669,#0891b2) !important; color:white !important; font-family:'Syne',sans-serif !important; font-size:0.95rem !important; font-weight:700 !important; padding:0.75rem 1.5rem !important; border-radius:12px !important; border:none !important; }
# .metric-row { display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin:1.5rem 0; }
# .metric-card { background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.07); border-radius:14px; padding:16px 18px; text-align:center; position:relative; overflow:hidden; }
# .metric-card::before { content:''; position:absolute; top:0; left:0; right:0; height:2px; background:var(--accent-line,#8b5cf6); }
# .metric-val { font-family:'Syne',sans-serif; font-size:1.7rem; font-weight:800; color:var(--val-color,#a78bfa); line-height:1; margin-bottom:4px; }
# .metric-lbl { font-size:0.72rem; color:#64748b; text-transform:uppercase; letter-spacing:1.5px; font-weight:600; }
# .reduction-bar-wrap { margin:0.5rem 0 1.5rem; }
# .reduction-bar-label { font-size:0.75rem; color:#64748b; letter-spacing:1px; text-transform:uppercase; margin-bottom:6px; font-weight:600; }
# .reduction-bar-bg { background:rgba(255,255,255,0.06); border-radius:8px; height:10px; overflow:hidden; }
# .reduction-bar-fill { height:100%; border-radius:8px; background:linear-gradient(90deg,#7c3aed,#2563eb,#0891b2); }
# .reduction-pct { font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:800; color:#a78bfa; margin-top:4px; }
# .img-label { font-family:'Syne',sans-serif; font-size:0.85rem; font-weight:700; text-align:center; padding:8px 0; border-radius:8px 8px 0 0; letter-spacing:1px; text-transform:uppercase; }
# .img-original { background:rgba(59,130,246,0.1); color:#60a5fa; border:1px solid rgba(59,130,246,0.2); }
# .img-compressed { background:rgba(139,92,246,0.1); color:#a78bfa; border:1px solid rgba(139,92,246,0.2); }
# .info-box { background:rgba(139,92,246,0.06); border:1px solid rgba(139,92,246,0.18); border-radius:12px; padding:1rem 1.2rem; font-size:0.85rem; color:#94a3b8; line-height:1.7; margin-top:0.8rem; }
# .vs-divider { display:flex; align-items:center; justify-content:center; font-family:'Syne',sans-serif; font-size:1.4rem; font-weight:800; color:#475569; height:100%; padding-top:80px; }
# .sec-title { font-family:'Syne',sans-serif; font-size:1rem; font-weight:700; color:#e2e8f0; margin-bottom:1rem; display:flex; align-items:center; gap:8px; }
# .sec-badge { background:rgba(139,92,246,0.12); border-radius:6px; padding:3px 9px; font-size:0.72rem; color:#a78bfa; font-family:'DM Mono',monospace; }
# [data-testid="stSidebar"] { background:rgba(8,8,20,0.97) !important; border-right:1px solid rgba(255,255,255,0.05) !important; }
# ::-webkit-scrollbar { width:4px; }
# ::-webkit-scrollbar-thumb { background:rgba(139,92,246,0.3); border-radius:2px; }
# </style>
# """, unsafe_allow_html=True)


# # ── Sidebar ───────────────────────────────────────────────────────────────────
# with st.sidebar:
#     st.markdown("""
#     <div style='text-align:center;padding:1.2rem 0 1.5rem;'>
#       <div style='font-size:3rem'>🎨</div>
#       <div style='font-family:Syne,sans-serif;font-size:1.4rem;font-weight:800;
#                   background:linear-gradient(90deg,#a78bfa,#60a5fa);
#                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;'>
#         PixelPress
#       </div>
#       <div style='font-size:0.72rem;color:#475569;margin-top:4px;letter-spacing:2px;text-transform:uppercase;'>
#         KMeans Image Compressor
#       </div>
#     </div>
#     """, unsafe_allow_html=True)
#     st.markdown("---")
#     st.markdown("### 🧠 How It Works")
#     st.markdown("""
#     <div style='font-size:0.83rem;color:#64748b;line-height:1.9;'>
#       <b style='color:#a78bfa'>1.</b> Upload any image<br>
#       <b style='color:#a78bfa'>2.</b> Choose K (number of colors)<br>
#       <b style='color:#a78bfa'>3.</b> KMeans clusters all pixels into K groups<br>
#       <b style='color:#a78bfa'>4.</b> Each pixel replaced by its cluster center<br>
#       <b style='color:#a78bfa'>5.</b> Result = smaller file, fewer colors
#     </div>
#     """, unsafe_allow_html=True)
#     st.markdown("---")
#     st.markdown("### 📊 K Value Guide")
#     for rng, color, label in [
#         ("K = 2–8",    "#f87171", "Max Compression"),
#         ("K = 9–16",   "#fb923c", "High Compression"),
#         ("K = 17–32",  "#facc15", "Balanced"),
#         ("K = 33–64",  "#4ade80", "Good Quality"),
#         ("K = 65–128", "#60a5fa", "Near Original"),
#     ]:
#         st.markdown(
#             f"<div style='display:flex;justify-content:space-between;padding:5px 0;"
#             f"border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.82rem;'>"
#             f"<span style='color:#a78bfa;font-family:DM Mono,monospace'>{rng}</span>"
#             f"<span style='color:{color};font-weight:600'>{label}</span></div>",
#             unsafe_allow_html=True)
#     st.markdown("---")
#     st.markdown("<p style='font-size:0.75rem;color:#334155;'>⚠️ Higher K = better quality but slower.<br>Recommended: <b style='color:#a78bfa'>K = 16</b></p>", unsafe_allow_html=True)


# # ── Hero ──────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="hero">
#   <div class="hero-badge">🎨 KMeans Clustering · Image Compression · ML</div>
#   <div class="hero-title">PixelPress</div>
#   <p class="hero-sub">
#     Upload any image, pick your K value, and let KMeans clustering compress it.
#     Compare original vs compressed side-by-side with full metrics — then download instantly.
#   </p>
# </div>
# """, unsafe_allow_html=True)


# # ── Upload + K ────────────────────────────────────────────────────────────────
# col_up, col_k = st.columns([2, 1])
# with col_up:
#     st.markdown('<div class="sec-title">📁 Upload Image <span class="sec-badge">JPG · PNG · JPEG · WEBP</span></div>', unsafe_allow_html=True)
#     uploaded_file = st.file_uploader("Drop image here", type=["jpg","jpeg","png","webp"], label_visibility="collapsed")

# with col_k:
#     st.markdown('<div class="sec-title">🎛️ Color Clusters <span class="sec-badge">K Value</span></div>', unsafe_allow_html=True)
#     k_value = st.slider("K — Number of Colors", min_value=2, max_value=128, value=16, step=1)
#     quality_label = ("⚡ Max compression!" if k_value<=8 else "🔥 High compression" if k_value<=16 else "⚖️ Balanced quality" if k_value<=32 else "✨ Good quality" if k_value<=64 else "🖼️ Near original")
#     st.markdown(f'<div class="info-box">Selected <strong style="color:#a78bfa">K = {k_value}</strong> — image compressed to <strong style="color:#a78bfa">{k_value} colors</strong>. &nbsp;{quality_label}</div>', unsafe_allow_html=True)

# st.markdown("<div style='margin:1rem 0'></div>", unsafe_allow_html=True)

# # ── Main ──────────────────────────────────────────────────────────────────────
# if uploaded_file is not None:
#     original_img   = Image.open(uploaded_file).convert("RGB")
#     orig_size_kb   = get_size_kb(original_img)
#     orig_w, orig_h = original_img.size

#     compress_clicked = st.button(f"🚀 Compress Image with K = {k_value}", use_container_width=True)

#     if compress_clicked:
#         with st.spinner(f"Running KMeans (K={k_value})... ⏳"):
#             t0 = time.time()
#             compressed_img, orig_colors, comp_colors, color_reduction = compress_image(original_img, k_value)
#             t1 = time.time()

#         comp_size_kb   = get_size_kb(compressed_img)
#         size_reduction = max(0, ((orig_size_kb - comp_size_kb) / orig_size_kb) * 100)
#         time_taken     = round(t1 - t0, 2)

#         st.markdown(f"""
#         <div class="metric-row">
#           <div class="metric-card" style="--accent-line:#60a5fa;--val-color:#60a5fa"><div class="metric-val">{orig_size_kb:.1f} KB</div><div class="metric-lbl">Original Size</div></div>
#           <div class="metric-card" style="--accent-line:#a78bfa;--val-color:#a78bfa"><div class="metric-val">{comp_size_kb:.1f} KB</div><div class="metric-lbl">Compressed Size</div></div>
#           <div class="metric-card" style="--accent-line:#4ade80;--val-color:#4ade80"><div class="metric-val">{size_reduction:.1f}%</div><div class="metric-lbl">Size Reduced</div></div>
#           <div class="metric-card" style="--accent-line:#f472b6;--val-color:#f472b6"><div class="metric-val">{color_reduction:.1f}%</div><div class="metric-lbl">Colors Reduced</div></div>
#         </div>
#         """, unsafe_allow_html=True)

#         st.markdown(f"""
#         <div class="reduction-bar-wrap">
#           <div class="reduction-bar-label">📉 File Size Reduction</div>
#           <div class="reduction-bar-bg"><div class="reduction-bar-fill" style="width:{min(size_reduction,100)}%"></div></div>
#           <div class="reduction-pct">{size_reduction:.1f}% smaller &nbsp;·&nbsp; {orig_size_kb:.1f} KB → {comp_size_kb:.1f} KB</div>
#         </div>
#         <div class="reduction-bar-wrap">
#           <div class="reduction-bar-label">🎨 Color Palette Reduction</div>
#           <div class="reduction-bar-bg"><div class="reduction-bar-fill" style="width:{min(color_reduction,100)}%;background:linear-gradient(90deg,#f472b6,#a78bfa)"></div></div>
#           <div class="reduction-pct" style="color:#f472b6">{orig_colors:,} → {comp_colors} colors &nbsp;·&nbsp; {color_reduction:.1f}% reduction</div>
#         </div>
#         """, unsafe_allow_html=True)

#         st.markdown('<div class="sec-title" style="margin-top:1.5rem">🖼️ Original vs Compressed <span class="sec-badge">Side by Side</span></div>', unsafe_allow_html=True)
#         c1, cv, c2 = st.columns([10,1,10])
#         with c1:
#             st.markdown('<div class="img-label img-original">📷 Original</div>', unsafe_allow_html=True)
#             st.image(original_img, use_container_width=True)
#             st.markdown(f"<div style='text-align:center;margin-top:6px;font-family:DM Mono,monospace;font-size:0.78rem;color:#64748b;'>{orig_w}×{orig_h}px · <strong style='color:#60a5fa'>{orig_size_kb:.1f} KB</strong> · {orig_colors:,} colors</div>", unsafe_allow_html=True)
#         with cv:
#             st.markdown("<div class='vs-divider'>⇄</div>", unsafe_allow_html=True)
#         with c2:
#             st.markdown('<div class="img-label img-compressed">✨ Compressed</div>', unsafe_allow_html=True)
#             st.image(compressed_img, use_container_width=True)
#             st.markdown(f"<div style='text-align:center;margin-top:6px;font-family:DM Mono,monospace;font-size:0.78rem;color:#64748b;'>{orig_w}×{orig_h}px · <strong style='color:#a78bfa'>{comp_size_kb:.1f} KB</strong> · K={k_value} colors</div>", unsafe_allow_html=True)

#         st.markdown("<div style='margin-top:1.5rem'></div>", unsafe_allow_html=True)
#         st.markdown('<div class="sec-title">📊 Full Stats <span class="sec-badge">Comparison</span></div>', unsafe_allow_html=True)
#         s1, s2, s3 = st.columns(3)
#         with s1:
#             st.metric("⏱️ Processing Time", f"{time_taken}s")
#             st.metric("📐 Dimensions", f"{orig_w} × {orig_h}")
#         with s2:
#             st.metric("📦 Original Size",   f"{orig_size_kb:.2f} KB")
#             st.metric("📦 Compressed Size", f"{comp_size_kb:.2f} KB", delta=f"-{orig_size_kb-comp_size_kb:.2f} KB", delta_color="inverse")
#         with s3:
#             st.metric("🎨 Original Colors",  f"{orig_colors:,}")
#             st.metric("🎨 After Compression",f"{k_value}", delta=f"-{orig_colors-k_value:,}", delta_color="inverse")

#         st.markdown("<div style='margin-top:1.5rem'></div>", unsafe_allow_html=True)
#         st.markdown('<div class="sec-title">⬇️ Download <span class="sec-badge">Save Result</span></div>', unsafe_allow_html=True)
#         dl_bytes   = get_download_bytes(compressed_img)
#         fname_base = uploaded_file.name.rsplit(".", 1)[0]
#         d1, d2 = st.columns(2)
#         with d1:
#             st.download_button(label=f"⬇️ Download Compressed (K={k_value})", data=dl_bytes, file_name=f"{fname_base}_compressed_k{k_value}.jpg", mime="image/jpeg", use_container_width=True)
#         with d2:
#             st.markdown(f"""<div style='background:rgba(5,150,105,0.08);border:1px solid rgba(5,150,105,0.2);border-radius:12px;padding:12px 16px;font-size:0.85rem;color:#6ee7b7;line-height:1.8;'>✅ Saved <strong>{orig_size_kb-comp_size_kb:.1f} KB</strong><br>📉 <strong>{size_reduction:.1f}%</strong> smaller<br>🎨 <strong>{k_value}</strong> of {orig_colors:,} colors kept</div>""", unsafe_allow_html=True)

# else:
#     st.markdown("""
#     <div style='text-align:center;padding:4rem 2rem;'>
#       <div style='font-size:4.5rem;margin-bottom:1rem;'>🖼️</div>
#       <div style='font-family:Syne,sans-serif;font-size:1.4rem;font-weight:700;color:#e2e8f0;margin-bottom:0.5rem;'>Upload an image to get started</div>
#       <div style='color:#475569;font-size:0.9rem;line-height:1.7;'>Supports JPG · PNG · JPEG · WEBP<br>Pick your K value → Hit Compress → Download</div>
#     </div>
#     """, unsafe_allow_html=True)
































import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import os
import io
import time

st.set_page_config(
    page_title="PixelCrush — Image Compressor",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Outfit:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
    background: #080b14;
    color: #e2e8f0;
}
.stApp { background: #080b14; }

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

# ── Top Bar ───────────────────────────────────────────────────────────────────
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

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">KMeans Clustering · Color Quantization</div>
  <div class="hero-title">Compress Images<br>with <em>Machine Learning</em></div>
  <div class="hero-sub">Reduce any image to K colors using KMeans clustering.
  See the before and after, size saved — and download instantly.</div>
</div>
""", unsafe_allow_html=True)

# ── Upload ────────────────────────────────────────────────────────────────────
uploaded_file = st.file_uploader(
    "Drop your image here",
    type=["jpg", "jpeg", "png", "webp"],
    label_visibility="collapsed"
)
st.markdown('<div class="upload-hint">JPG · PNG · WEBP · Max 10MB recommended</div>',
            unsafe_allow_html=True)

if uploaded_file is not None:

    # ── Settings ──────────────────────────────────────────────────────────────
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
        # KMeans compression (from your notebook logic) 
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

        # Save to buffer for size calculation + download
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



        # Download
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

        # Summary note 
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