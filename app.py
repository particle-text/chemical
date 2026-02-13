


# -----------------------------
# قاعدة بيانات العناصر (تقدر توسّعها)
# -----------------------------

elements = {
    "Hydrogen": {
        "symbol": "H",
        "atomic_number": 1,
        "mass_number": 1,
        "charge": "+1",
        "properties": "غاز عديم اللون، خفيف جداً، قابل للاشتعال.",
        "nature": "يوجد في الماء والنجوم."
    },
    "Oxygen": {
        "symbol": "O",
        "atomic_number": 8,
        "mass_number": 16,
        "charge": "-2",
        "properties": "غاز ضروري للتنفس ويدعم الاحتراق.",
        "nature": "يوجد في الهواء والماء."
    },
    "Carbon": {
        "symbol": "C",
        "atomic_number": 6,
        "mass_number": 12,
        "charge": "±4",
        "properties": "عنصر أساسي في المركبات العضوية.",
        "nature": "يوجد في الكائنات الحية والفحم."
    },
    "Sodium": {
        "symbol": "Na",
        "atomic_number": 11,
        "mass_number": 23,
        "charge": "+1",
        "properties": "فلز قلوي شديد التفاعل.",
        "nature": "يوجد في ملح الطعام."
    }
}

# -----------------------------
# إعداد الصفحة
# -----------------------------

st.set_page_config(
    page_title="العناصر الكيميائية",
    page_icon="🧪",
    layout="centered"
)

# -----------------------------
# تنسيق CSS (لتوسيط البحث + زر الزاوية)
# -----------------------------

st.markdown(
    """
    <style>
    .center-box {
        text-align: center;
        margin-top: 150px;
    }

    .corner-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #ff9800;
        color: white;
        padding: 12px 18px;
        border-radius: 30px;
        font-size: 16px;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# واجهة البحث (في النصف)
# -----------------------------

st.markdown('<div class="center-box">', unsafe_allow_html=True)

st.title("🔬 البحث عن عنصر كيميائي")

# الإدخال
query = st.text_input("اكتب اسم العنصر بالإنجليزي ثم اضغط Enter")

# -----------------------------
# عرض النتائج
# -----------------------------

if query:
    element = elements.get(query)

    if element:
        st.success("تم العثور على العنصر ✅")

        st.write(f"**الرمز:** {element['symbol']}")
        st.write(f"**العدد الذري:** {element['atomic_number']}")
        st.write(f"**العدد الكتلي:** {element['mass_number']}")
        st.write(f"**الشحنة:** {element['charge']}")
        st.write(f"**الخصائص:** {element['properties']}")
        st.write(f"**موقعه في الطبيعة:** {element['nature']}")

    else:
        st.error("العنصر غير موجود في قاعدة البيانات ❌")

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# زر الزاوية + عرض الجدول الدوري
# -----------------------------

show_table = st.button("📊 عرض الجدول الدوري")

if show_table:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/0/01/Periodic_table_large.svg",
        caption="الجدول الدوري للعناصر",
        use_container_width=True
    )

