import streamlit as st
import time
import random
import pandas as pd
import os

st.set_page_config(page_title="الجيم الذهني - نادي الفرسان", page_icon="🥋", layout="wide")

st.sidebar.title("🥋 بوابة الإعداد النفسي")
app_mode = st.sidebar.radio("اختر القسم:", ["🎮 الجيم الذهني (التدريب التفاعلي)", "📈 اختبار التطور التتبعي (بعد فترة تدريب)", "📖 دليل البطل (طريقة اللعب)"])

# ----------------- 1. قسم دليل البطل -----------------
if app_mode == "📖 دليل البطل (طريقة اللعب)":
    st.title("📖 دليل البطل: كيف تخوض التحدي الذهني؟")
    st.markdown("""
    ### أهلاً بك يا بطل المستقبل! 🥋
    هذا التدريب مصمم خصيصاً لتقوية **أعصابك وثباتك الداخلي** لتصبح لا تهتز أمام أي حكم أو منافس على البساط.
    
    #### 🚦 قواعد اللعبة:
    1. **ادخل وضع الاستعداد (Yoi):** اجلس أو قف بظهر مستقيم وركز نظرك في منتصف الشاشة.
    2. **الشاشة الحمراء (اختبار الصبر وكبح الاندفاع):** 
       * إياك أن تضغط نهائياً! الضغط أثناء اللون الأحمر يعني أنك تسرعت وأضعت إيقاع الكاتا والـ Kime، وستخسر نقاطاً فوراً.
    3. **الشاشة الخضراء (لحظة الانفجار الحركي والكياي!):**
       * أول ما تراها، اضغط بأقصى سرعة ممكنة دون تردد، فالبرنامج يقيس سرعة عقلك بالمللي ثانية!
    4. **سلم المستويات:**
       * **المستوى 1:** لتدريب الهدوء وضبط ضربات القلب.
       * **المستوى 2:** لتدريب سرعة اتخاذ القرار والتخلص من التردد.
       * **المستوى 3:** محاكاة أجواء البطولات والمواقف الصعبة!
    """)

# ----------------- 2. قسم الجيم الذهني (التدريب التفاعلي) -----------------
elif app_mode == "🎮 الجيم الذهني (التدريب التفاعلي)":
    st.title("🧠 الجيم الذهني - مختبر الثبات الانفعالي")
    st.write("تدريب عصبي تفاعلي لقياس وسرعة القرار، التحكم في الاندفاع، والثبات تحت الضغط.")

    col1, col2 = st.columns(2)
    with col1:
        player_name = st.text_input("اسم البطل:", placeholder="اكتب اسمك هنا...")
    with col2:
        level = st.selectbox("المستوى التدريبي:", ["المستوى 1: ضبط الاندفاع والهدوء", "المستوى 2: سرعة القرار بلا تردد", "المستوى 3: محاكاة بساط البطولة"])

    if "stage" not in st.session_state: st.session_state.stage = "idle"
    if "start_time" not in st.session_state: st.session_state.start_time = 0
    if "target_delay" not in st.session_state: st.session_state.target_delay = 0

    st.markdown("---")

    if not player_name:
        st.info("👋 اكتب اسمك أولاً في الأعلى للانطلاق في التحدي!")
    else:
        st.subheader(f"🥋 تحدي اليوم للبطل: {player_name}")
        
        if "المستوى 1" in level:
            wait_min, wait_max = 2.0, 4.0
        elif "المستوى 2" in level:
            wait_min, wait_max = 1.5, 3.0
        else:
            wait_min, wait_max = 1.0, 2.5

        if st.session_state.stage == "idle":
            if st.button("🟢 اضغط هنا لبدء التحدي (ادخل في وضع الاستعداد)"):
                st.session_state.stage = "waiting"
                st.session_state.target_delay = random.uniform(wait_min, wait_max)
                st.session_state.start_time = time.time()
                st.rerun()

        elif st.session_state.stage == "waiting":
            elapsed = time.time() - st.session_state.start_time
            if elapsed < st.session_state.target_delay:
                st.warning("🛑 انتبه! الشاشة حمراء.. تنفس بهدوء ولا تضغط نهائياً حتى تصبح خضراء!")
                if st.button("💥 ضربة الـ KIME الآن!"):
                    st.session_state.stage = "early_fault"
                    st.rerun()
                time.sleep(0.1)
                st.rerun()
            else:
                st.session_state.stage = "ready_to_strike"
                st.session_state.signal_time = time.time()
                st.rerun()

        elif st.session_state.stage == "ready_to_strike":
            st.success("🟢🟢🟢 انطلق الآن! كيااااي! اضغط بأقصى سرعة!")
            if st.button("🥋 تنفيذ الضربة فوراً!"):
                reaction_time = (time.time() - st.session_state.signal_time) * 1000
                st.session_state.reaction_time = reaction_time
                st.session_state.stage = "finished"
                st.rerun()

        elif st.session_state.stage == "early_fault":
            st.error("❌ خطأ تسرع واندفاع (Over-Arousal)!")
            st.write("تعجلت وضغطت قبل الإشارة! في الكاتا التسرع يضيع التوازن والـ Kime.")
            score = 45
            st.metric("الدرجة الذهنية:", f"{score} / 100")
            
            record = {"اللاعب": player_name, "النوع": "تدريب تفاعلي", "المستوى": level, "الدرجة": score, "زمن الاستجابة": "تسرع", "الحالة": "اندفاع مفرط", "التاريخ": time.strftime("%Y-%m-%d %H:%M")}
            pd.DataFrame([record]).to_csv("athletes_scores.csv", mode="a", header=not os.path.exists("athletes_scores.csv"), index=False, encoding="utf-8-sig")
            
            if st.button("🔄 إعادة المحاولة بتنفس أهدأ"):
                st.session_state.stage = "idle"
                st.rerun()

        elif st.session_state.stage == "finished":
            r_time = round(st.session_state.reaction_time)
            st.balloons()
            
            if r_time < 350:
                score, status = 95, "استجابة انفجارية وثبات نخبوي ممتاز"
            elif r_time < 500:
                score, status = 85, "تركيز عالي وسرعة جيدة جداً"
            elif r_time < 750:
                score, status = 70, "استجابة مقبولة مع تردد طفيف"
            else:
                score, status = 55, "تردد وبطء استجابة (تحتاج تعزيز ثقة)"

            st.success(f"🎯 التقييم: {status}")
            c1, c2 = st.columns(2)
            c1.metric("الدرجة الإجمالية:", f"{score} / 100")
            c2.metric("زمن رد الفعل:", f"{r_time} مللي ثانية")
            
            record = {"اللاعب": player_name, "النوع": "تدريب تفاعلي", "المستوى": level, "الدرجة": score, "زمن الاستجابة": f"{r_time} ms", "الحالة": status, "التاريخ": time.strftime("%Y-%m-%d %H:%M")}
            pd.DataFrame([record]).to_csv("athletes_scores.csv", mode="a", header=not os.path.exists("athletes_scores.csv"), index=False, encoding="utf-8-sig")
            
            st.info("✅ تم تسجيل نتيجتك وحفظها في تقرير المدرب بنجاح!")
            if st.button("🔄 خوض تحدٍ جديد"):
                st.session_state.stage = "idle"
                st.rerun()

# ----------------- 3. قسم اختبار التطور التتبعي -----------------
elif app_mode == "📈 اختبار التطور التتبعي (بعد فترة تدريب)":
    st.title("📈 مقياس التطور الذهني التتبعي (المرحلة 2)")
    st.write("أجب عن هذه المواقف بعد مرور أسبوعين إلى شهر من التدريب لقياس نسبة تطور ثباتك الانفعالي.")
    
    t_name = st.text_input("اسم اللاعب للاختبار التتبعي:")
    st.markdown("---")
    
    q1 = st.radio("س1: مقارنة ببداية الموسم.. عندما تقف الآن على خط البداية أمام الحكام:",
                  ["ما زلت أشعر بتسارع ضربات القلب وصعوبة التنفس", "أصبحت أسيطر على نفسي بتمارين التنفس وأدخل بتركيز وهدوء"])
    q2 = st.radio("س2: لو اختل توازنك أو نسيت نقلة بسيطة أثناء الكاتا في تمرين اليوم:",
                  ["أتوتر وأتوقف أو أتأثر نفسياً في باقي الحركات", "أطبق قاعدة الـ 3 ثوانٍ وأكمل الكاتا فوراً بنفس القوة والإصرار"])
    q3 = st.radio("س3: مدى التزامك بتمارين التنفس والتخيل الذهني في المنزل:",
                  ["أمارسها نادراً أو أنساها", "أمارسها بانتظام 3 إلى 5 مرات أسبوعياً"])
    
    if st.button("تسجيل قياس التطور 📊"):
        if not t_name:
            st.warning("يرجى كتابة اسم اللاعب أولاً.")
        else:
            prog_score = 0
            if "أصبحت" in q1: prog_score += 35
            if "أطبق" in q2: prog_score += 35
            if "أمارسها بانتظام" in q3: prog_score += 30
            
            st.success(f"نتيجة قياس التطور للبطل: {t_name}")
            st.metric("معدل الصلابة والتطور الذهني:", f"{prog_score}%")
            
            if prog_score >= 70:
                st.info("🔥 رائع جداً! استجابة عصبية ممتازة وتطور ملحوظ في التحكم في الضغوط.")
            else:
                st.warning("⚠️ يحتاج إلى الاستمرار في تدريبات التنفس المنزلي والمحاكاة لرفع الثبات.")
                
            rec = {"اللاعب": t_name, "النوع": "مقياس تطور", "المستوى": "تتبعي", "الدرجة": prog_score, "زمن الاستجابة": "-", "الحالة": f"تطور {prog_score}%", "التاريخ": time.strftime("%Y-%m-%d %H:%M")}
            pd.DataFrame([rec]).to_csv("athletes_scores.csv", mode="a", header=not os.path.exists("athletes_scores.csv"), index=False, encoding="utf-8-sig")

st.sidebar.markdown("---")
with st.sidebar.expander("📊 سجل جميع النتائج (المدرب)"):
    if os.path.exists("athletes_scores.csv"):
        st.dataframe(pd.read_csv("athletes_scores.csv", encoding="utf-8-sig"))
    else:
        st.write("لا توجد بيانات مسجلة بعد.")