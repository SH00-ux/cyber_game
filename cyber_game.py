import streamlit as st
import random

# إعداد الصفحة واتجاه الكتابة
st.set_page_config(page_title="Cyber Security Challenge", layout="wide")

# كود CSS لتحسين الاستجابة على الهواتف مع تحسين النصوص
matrix_bg = """
<style>
    body {
        background-color: black;
        color: white;
        text-align: right;
        direction: rtl;
        font-family: "Courier New", Courier, monospace;
        text-shadow: 0 0 10px green, 0 0 20px green, 0 0 30px green; /* الظل تحت النصوص */
    }
    [data-testid="stAppViewContainer"] {
        background-color: black;
        background-image: url('https://www.hackingloops.com/wp-content/uploads/2020/09/hacker-background-1024x536.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .css-1d391kg {
        color: white !important;
        background-color: rgba(0, 0, 0, 0.6) !important; /* خلفية مظللة للنص */
        padding: 10px;
    }
    .stButton > button {
        background-color: green;
        color: white;
        width: 100%;  /* التأكد من أن الأزرار تغطي كامل العرض على الشاشات الصغيرة */
        font-size: 20px;
    }
    .stRadio label {
        color: white !important;
        font-size: 18px;
    }
    .stTextInput input {
        background-color: rgba(0, 0, 0, 0.5);
        color: white !important;
    }
    .stSlider > div {
        color: white !important;
    }

    /* تحسين استجابة التصميم للشاشات الصغيرة */
    @media only screen and (max-width: 768px) {
        .css-1d391kg {
            font-size: 18px;
        }
        .stButton > button {
            font-size: 18px;
        }
        .stRadio label {
            font-size: 16px;
        }
    }
</style>
"""

st.markdown(matrix_bg, unsafe_allow_html=True)

st.title("🛡️ تحدي الاختراق السيبراني")
st.write("📌 اختبر مهاراتك في الأمن السيبراني!")

# تهيئة session_state
if "player_name" not in st.session_state:
    st.session_state.player_name = None
if "score" not in st.session_state:
    st.session_state.score = 0
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = {}

# تسجيل اسم اللاعب
if st.session_state.player_name is None:
    player_name = st.text_input("🔹 أدخل اسمك للبدء:")
    if st.button("✅ ابدأ اللعبة") and player_name:
        st.session_state.player_name = player_name
        if player_name not in st.session_state.leaderboard:
            st.session_state.leaderboard[player_name] = 0  
        st.rerun()
    st.stop()

st.subheader(f"👤 اللاعب: {st.session_state.player_name}")

# قائمة الأسئلة الصعبة
questions = [
    {
        "question": "🔓 لديك وصول إلى شبكة داخلية لشركة عبر نقطة Wi-Fi ضعيفة التشفير. ما هو أول شيء يجب أن تفعله كمختبر اختراق أخلاقي؟",
        "options": [
            "التقاط وتحليل حركة المرور باستخدام Wireshark",
            "محاولة تسجيل الدخول إلى خوادم الشركة مباشرة",
            "إبلاغ الشركة دون جمع أي بيانات"
        ],
        "answer": "التقاط وتحليل حركة المرور باستخدام Wireshark",
    },
    {
        "question": "🛡️ أثناء اختبار اختراق لموقع ويب، وجدت أن إدخال ` OR 1=1 --` يسمح لك بتجاوز المصادقة. ماذا يعني هذا؟",
        "options": [
            "الموقع يستخدم كلمات مرور ضعيفة",
            "الموقع يعاني من ثغرة SQL Injection",
            "الموقع يسمح بتجاوز الحماية بسبب ضعف التشفير"
        ],
        "answer": "الموقع يعاني من ثغرة SQL Injection",
    },
    {
        "question": "💥 ماذا يعني مصطلح 'Zero-Day Attack' في مجال الأمن السيبراني؟",
        "options": [
            "هجوم يستغل ثغرة لم تُكتشف بعد من قبل شركة البرمجيات",
            "هجوم على شبكة Wi-Fi مفتوحة",
            "هجوم يستهدف تطبيقات الهواتف المحمولة"
        ],
        "answer": "هجوم يستغل ثغرة لم تُكتشف بعد من قبل شركة البرمجيات",
    },
    {
        "question": "🔍 كيف يتم التصدي لهجمات 'Man-in-the-Middle'؟",
        "options": [
            "استخدام بروتوكولات HTTPS",
            "تعطيل جدران الحماية",
            "إيقاف تشفير البيانات"
        ],
        "answer": "استخدام بروتوكولات HTTPS",
    },
    {
        "question": "🚨 إذا تم اكتشاف برمجية خبيثة في شبكة داخلية، ما هي الخطوة الأولى التي يجب اتخاذها؟",
        "options": [
            "إيقاف كافة الأنظمة المتأثرة على الفور",
            "مراقبة الأنظمة المتأثرة فقط دون اتخاذ إجراءات",
            "إبلاغ الجهات المعنية مع استمرار الأنظمة في العمل"
        ],
        "answer": "إيقاف كافة الأنظمة المتأثرة على الفور",
    },
    {
        "question": "🔐 ما هو الهدف من اختبار الاختراق في المؤسسات؟",
        "options": [
            "إيجاد نقاط ضعف في الأنظمة وتقديم الحلول لتأمينها",
            "إزالة جدران الحماية بالكامل",
            "اختراق الأنظمة للحصول على مكافآت مالية"
        ],
        "answer": "إيجاد نقاط ضعف في الأنظمة وتقديم الحلول لتأمينها",
    }
]

if "current_question" not in st.session_state or not st.session_state.remaining_questions:
    st.session_state.remaining_questions = questions.copy()
    st.session_state.current_question = random.choice(st.session_state.remaining_questions)

question = st.session_state.current_question
st.subheader(f"🤔 {question['question']}")
selected_option = st.radio("اختر الإجابة الصحيحة:", question["options"])

# زر الإجابة
if st.button("🚀 تحقق من الإجابة"):
    if selected_option == question["answer"]:
        st.session_state.score += 10
        st.success("✅ إجابة صحيحة! +10 نقاط")
    else:
        st.error("❌ إجابة خاطئة!")

    # إزالة السؤال المجاب عليه
    st.session_state.remaining_questions.remove(question)

    # إنهاء اللعبة إذا انتهت الأسئلة
    if not st.session_state.remaining_questions:
        st.session_state.leaderboard[st.session_state.player_name] = max(st.session_state.score, st.session_state.leaderboard[st.session_state.player_name])
        st.success("🎉 تهانينا! لقد أكملت التحدي.")
        if st.button("🔄 إعادة اللعب"):
            st.session_state.score = 0
            st.session_state.remaining_questions = {}
            st.rerun()
        st.stop()

    # اختيار سؤال جديد
    st.session_state.current_question = random.choice(st.session_state.remaining_questions)
    st.rerun()

# عرض النقاط
st.subheader(f"💯 النقاط: {st.session_state.score}")

# لوحة المتصدرين
st.subheader("🏅 لوحة المتصدرين")
sorted_leaderboard = sorted(st.session_state.leaderboard.items(), key=lambda x: x[1], reverse=True)[:5]
for i, (name, score) in enumerate(sorted_leaderboard, start=1):
    st.write(f"{i}. {name} - {score} نقطة")

# إعادة تشغيل اللعبة
if st.button("🔄 إعادة اللعبة"):
    st.session_state.score = 0
    st.session_state.remaining_questions = {}
    st.session_state.player_name = None
    st.rerun()
