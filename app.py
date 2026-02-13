ممكن تخليه اجمل ومع خلفية جميلة  وهذا كوده import streamlit as st

# -----------------------------
# قاعدة بيانات العناصر
# -----------------------------

elements = {
    "Hydrogen": {
        "symbol": "H",
        "atomic_number": 1,
        "mass_number": 1,
        "charge": "+1",
        "properties": "غاز عديم اللون، خفيف جداً، قابل للاشتعال.",
        "nature": "يوجد في الماء والنجوم.",
        "color": "#3498db"
    },
    "Oxygen": {
        "symbol": "O",
        "atomic_number": 8,
        "mass_number": 16,
        "charge": "-2",
        "properties": "غاز ضروري للتنفس ويدعم الاحتراق.",
        "nature": "يوجد في الهواء والماء.",
        "color": "#e74c3c"
    },
    "Carbon": {
        "symbol": "C",
        "atomic_number": 6,
        "mass_number": 12,
        "charge": "±4",
        "properties": "عنصر أساسي في المركبات العضوية.",
        "nature": "يوجد في الكائنات الحية والفحم.",
        "color": "#2c3e50"
    },
    "Sodium": {
        "symbol": "Na",
        "atomic_number": 11,
        "mass_number": 23,
        "charge": "+1",
        "properties": "فلز قلوي شديد التفاعل.",
        "nature": "يوجد في ملح الطعام.",
        "color": "#f39c12"
    },
    "Nitrogen": {
        "symbol": "N",
        "atomic_number": 7,
        "mass_number": 14,
        "charge": "-3",
        "properties": "غاز عديم اللون يشكل معظم الغلاف الجوي.",
        "nature": "يوجد في الهواء والبروتينات.",
        "color": "#9b59b6"
    },
    "Iron": {
        "symbol": "Fe",
        "atomic_number": 26,
        "mass_number": 56,
        "charge": "+2, +3",
        "properties": "فلز قوي يستخدم في البناء.",
        "nature": "يوجد في خامات الحديد والدم.",
        "color": "#95a5a6"
    }
}

# -----------------------------
# إعداد الصفحة
# -----------------------------

st.set_page_config(
    page_title="🧪 العناصر الكيميائية",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# تنسيق CSS متقدم
# -----------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Cairo', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .search-container {
        background: rgba(255, 255, 255, 0.95);
        padding: 3rem;
        border-radius: 30px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        max-width: 800px;
        margin: 2rem auto;
        backdrop-filter: blur(10px);
        animation: fadeIn 0.8s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .title {
        text-align: center;
        color: #2c3e50;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .element-card {
        background: linear-gradient(135deg, var(--element-color) 0%, var(--element-color-dark) 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .element-symbol {
        font-size: 5rem;
        font-weight: 700;
        text-align: center;
        margin: 1rem 0;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
    }
    
    .element-info {
        background: rgba(255,255,255,0.2);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        backdrop-filter: blur(5px);
    }
    
    .info-row {
        display: flex;
        justify-content: space-between;
        padding: 0.5rem 0;
        border-bottom: 1px solid rgba(255,255,255,0.3);
    }
    
    .info-label {
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    .info-value {
        font-size: 1.1rem;
    }
    
    .periodic-table-btn {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        border: none;
        font-size: 1.2rem;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        margin: 2rem auto;
        display: block;
    }
    
    .periodic-table-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    
    .elements-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .element-preview {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .element-preview:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .preview-symbol {
        font-size: 3rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    .preview-name {
        font-size: 1.2rem;
        color: #2c3e50;
        font-weight: 600;
    }
    
    .preview-number {
        font-size: 0.9rem;
        color: #7f8c8d;
    }
    
    /* تحسين حقل الإدخال */
    .stTextInput > div > div > input {
        border-radius: 15px;
        border: 2px solid #667eea;
        padding: 1rem;
        font-size: 1.2rem;
        text-align: center;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #764ba2;
        box-shadow: 0 0 0 0.2rem rgba(118, 75, 162, 0.25);
    }
    
    /* تحسين الأزرار */
    .stButton > button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 0.8rem 2rem;
        border-radius: 50px;
        border: none;
        font-size: 1.1rem;
        font-weight: 600;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    
    .footer {
        text-align: center;
        color: white;
        margin-top: 3rem;
        padding: 1rem;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# العنوان الرئيسي
# -----------------------------

st.markdown('<div class="search-container">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🧪 استكشف العناصر الكيميائية</h1>', unsafe_allow_html=True)

# -----------------------------
# عرض جميع العناصر المتاحة
# -----------------------------

with st.expander("📚 العناصر المتاحة - اضغط للعرض", expanded=False):
    cols = st.columns(3)
    for idx, (name, data) in enumerate(elements.items()):
        with cols[idx % 3]:
            st.markdown(
                f"""
                <div class="element-preview" style="border-top: 4px solid {data['color']}">
                    <div class="preview-number">العدد الذري: {data['atomic_number']}</div>
                    <div class="preview-symbol" style="color: {data['color']}">{data['symbol']}</div>
                    <div class="preview-name">{name}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# البحث عن العنصر
# -----------------------------

query = st.text_input(
    "",
    placeholder="🔍 اكتب اسم العنصر بالإنجليزية... (مثال: Hydrogen)",
    label_visibility="collapsed"
)

# -----------------------------
# عرض النتائج
# -----------------------------

if query:
    # البحث بدون حساسية لحالة الأحرف
    element = None
    element_name = None
    for name, data in elements.items():
        if name.lower() == query.lower():
            element = data
            element_name = name
            break
    
    if element:
        # حساب اللون الداكن
        color = element['color']
        
        st.markdown(
            f"""
            <div class="element-card" style="--element-color: {color}; --element-color-dark: {color}dd;">
                <div class="element-symbol">{element['symbol']}</div>
                <h2 style="text-align: center; margin: 1rem 0;">{element_name}</h2>
                
                <div class="element-info">
                    <div class="info-row">
                        <span class="info-label">⚛️ العدد الذري:</span>
                        <span class="info-value">{element['atomic_number']}</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">⚖️ العدد الكتلي:</span>
                        <span class="info-value">{element['mass_number']}</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">⚡ الشحنة:</span>
                        <span class="info-value">{element['charge']}</span>
                    </div>
                </div>
                
                <div class="element-info">
                    <div class="info-label">🔬 الخصائص:</div>
                    <p style="margin: 0.5rem 0;">{element['properties']}</p>
                </div>
                
                <div class="element-info">
                    <div class="info-label">🌍 الموقع في الطبيعة:</div>
                    <p style="margin: 0.5rem 0;">{element['nature']}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("❌ العنصر غير موجود في قاعدة البيانات. جرب أحد العناصر المتاحة أعلاه.")

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# زر عرض الجدول الدوري
# -----------------------------

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    show_table = st.button("📊 عرض الجدول الدوري الكامل")

if show_table:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="background: white; padding: 2rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
            <h2 style="text-align: center; color: #2c3e50;">📊 الجدول الدوري للعناصر</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/0/01/Periodic_table_large.svg",
        use_container_width=True
    )

# -----------------------------
# Footer
# -----------------------------

st.markdown(
    """
    <div class="footer">
        <p>✨ تم التطوير بواسطة Blackbox AI | 2026 🧪</p>
        <p>اكتشف عالم الكيمياء بطريقة تفاعلية وممتعة</p>
    </div>
    """,
    unsafe_allow_html=True
)
