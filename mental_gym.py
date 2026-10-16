import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json
import time
import os

st.set_page_config(page_title="الجيم الذهني - نادي الفرسان", page_icon="🥋", layout="wide")

st.sidebar.title("🥋 بوابة الإعداد النفسي")
app_mode = st.sidebar.radio(
    "اختر القسم:",
    [
        "📋 استبيان الإعداد النفسي وخطط التدريب (تحليل فوري)",
        "🎮 الجيم الذهني (رد الفعل والثبات الحقيقي)",
        "🎯 اختبار القرار والتحكم العصبي (Go / No-Go)",
        "📈 اختبار التطور التتبعي (بعد فترة تدريب)",
        "📖 دليل البطل (طريقة اللعب)"
    ]
)

# ----------------- 1. قسم استبيان الإعداد النفسي والتشخيص -----------------
if app_mode == "📋 استبيان الإعداد النفسي وخطط التدريب (تحليل فوري)":
    st.title("📋 استبيان الأداء الذهني والتنافسي — ناشئين وشباب")
    st.markdown("**برنامج التحليل السلوكي ومواجهة الضغوط التنافسية (نادي الفرسان)**")
    st.info("💡 أدخل بيانات اللاعب وإجاباته من الاستمارة الورقية للحصول على التقرير النفسي الفوري والبرنامج التدريبي المخصص (المنزلي والميداني).")

    with st.form("athlete_profile_form"):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            name = st.text_input("اسم اللاعب:", value="معتز غالب الغامدي")
        with col2:
            age = st.text_input("السن (سنة الميلاد):", value="14 (2012)")
        with col3:
            rank = st.text_input("الدرجة / الحزام:", value="بني كيو 1")
        with col4:
            kata = st.text_input("الكاتا الأساسية:", value="الكنقوشو (Kanku Sho)")

        st.markdown("---")
        st.subheader("📝 إجابات الاستبيان التنافسي:")

        q1 = st.radio(
            "1. في منطقة الإحماء الرسمية قبل الصعود للبساط بـ 5 إلى 10 دقائق:",
            [
                "برودة بالأطراف، تسارع نبضات القلب، اضطراب بالمعدة، وتخوف من نسيان الحركات أو سوء الأداء.",
                "طاقة وحماس مفرط، رغبة في التسريع والضرب بقوة في الإحماء دون أخذ راحة كافية أو تنظيم نفس.",
                "إحساس بالثقل أو الخمول وضعف الاستثارة العصبية وصعوبة في إشعال الحافز الداخلي للمباراة.",
                "ثبات وانضباط، تركيز كامل على إيقاع الكاتا والتنفس المنتظم مع استرجاع ذهني هادئ للتكنيك."
            ],
            index=0
        )

        q2 = st.radio(
            "2. أثناء أداء الكاتا الرسمية أمام لجنة الحكام، حدث اهتزاز مفاجئ في وقفة أو حركة:",
            [
                "أفقد التركيز فوراً، وتسيطر علي فكرة أن المباراة ضاعت، فينعكس الارتباك على الحركات المتبقية.",
                "أستمر فوراً بنفس الهدوء والإيقاع وكأن شيئاً لم يحدث، وأوجه تركيزي بالكامل للحركة القادمة.",
                "أنفعل داخلياً وأزيد سرعة وعنف الضربات التالية للتعويض فيختل الـ Rhythm والتوازن التام."
            ],
            index=2
        )

        q3 = st.radio(
            "3. عندما تشاهد منافسك المباشر في القرعة يؤدي كاتا قوية جداً وحصد علامات مرتفعة:",
            [
                "يتسرب الشك إلى نفسي وأبدأ بمقارنة مستواي بمستواه وأشعر بأن فرص الفوز أصبحت ضعيفة.",
                "أتحمس بشكل عدائي مبالغ فيه وأقرر تفجير الحركات بأقصى طاقة حتى لو فقدت نظافة التكنيك.",
                "أعزل تركيزي عن نقاط المنافسين وأعلم أن تركيزي على أداء حركاتي بإتقان هو الفيصل الوحيد."
            ],
            index=2
        )

        q4 = st.radio(
            "4. عند سماع صيحات الجمهور أو توجيهات مفاجئة بصوت عالٍ أثناء أداء الكاتا:",
            [
                "يتشتت انتباهي البصري والسمعي للحظة وأشعر بارتباك في التوقيت والانتقال الحركي.",
                "أمتلك نفق تركيز ضيق (Tunnel Vision) ولا أسمع أو أرى سوى مسار حركتي الافتراضية.",
                "تزيد الأصوات من تهوري وتدفعني للاستعراض المبالغ فيه على حساب الدقة الفنية."
            ],
            index=1
        )

        q5 = st.radio(
            "5. روتين ليلة البطولة قبل الخلود للنوم:",
            [
                "أواجه صعوبة في الاستغراق بالنوم بسبب توارد سيناريوهات الأخطاء أو هاجس الهزيمة.",
                "أسهر طويلاً بسبب فرط التفكير والحماس المفرط للميدالية والتتويج ولا تهدأ طاقتي.",
                "أطبق روتين تنفس هادئ مع تخيل كاتا ناجحة ومتكاملة، وأنام نوماً عميقاً ومريحاً."
            ],
            index=1
        )

        submit_btn = st.form_submit_button("📊 تحليل نتائج اللاعب وإصدار البرنامج التدريبي فوراً")

    if submit_btn:
        st.success(f"تم تحليل استمارة البطل: {name} بنجاح!")
        st.markdown("---")

        # التحليل النفسي الذكي
        somatic_anxiety = "برودة بالأطراف" in q1
        over_arousal = "طاقة وحماس مفرط" in q1 or "أسهر طويلاً" in q5
        reaction_to_error = "أنفعل داخلياً" in q2 or "أفقد التركيز" in q2
        self_focus = "أعزل تركيزي" in q3
        tunnel_vision = "Tunnel Vision" in q4

        tab1, tab2, tab3 = st.tabs(["🧠 التشخيص والتحليل النفسي", "🏠 برنامج التدريب المنزلي (للبطل)", "🥋 برنامج التدريب الميداني (مع المدرب)"])

        with tab1:
            st.subheader("📊 الملف النفسي للاعب:")
            c1, c2, c3 = st.columns(3)
            c1.metric("الكاتا المستهدفة", kata)
            c2.metric("الحزام والدرجة", rank)
            c3.metric("الفئة العمرية", age)

            st.markdown("#### 🔍 نقاط القوة:")
            if self_focus:
                st.write("✅ **عزل ممتاز للمنافسين:** قدرة عالية على عدم التأثر بنقاط المنافس والتركيز على ذاته.")
            if tunnel_vision:
                st.write("✅ **بؤرة تركيز قوية:** يمتلك تركيزاً حاداً يحميه من تشتت صيحات الجمهور وأصوات القاعة.")

            st.markdown("#### ⚠️ التحديات الواجب علاجها:")
            if somatic_anxiety:
                st.write("⚠️ **قلق استباقي وتوتر بدني (Somatic Anxiety):** تسارع النبض وبرودة الأطراف قبل 10 دقائق من النزول ناتج عن التفكير في النتيجة أو نسيان الحركات.")
            if "أنفعل داخلياً" in q2:
                st.write("⚠️ **رد فعل تعويضي مندفع:** الانفعال بعد الاهتزاز المفاجئ ومحاولة التعويض بالقوة الزائدة يؤدي لاختلال الرتم وتفشيخ الوقفات.")
            if "أسهر طويلاً" in q5:
                st.write("⚠️ **استثارة عصبية زائدة ليلة البطولة (Over-Excitement):** فرط التفكير في الميدالية يستهلك الطاقة العصبية قبل بدء المنافسات.")

        with tab2:
            st.subheader("🏠 برنامج التدريب العقلي في المنزل (يطبقه اللاعب يومياً):")
            st.markdown(f"""
            1. **بروتوكول التنفس الترددي (4 - 4 - 4 - 4 Box Breathing):**
               * **التطبيق:** 10 دقائق يومياً قبل النوم مباشرة للتخلص من السهر وفرط التفكير في الميداليات.
               * شهيق 4 ثوانٍ - كتم النفس 4 ثوانٍ - زفير 4 ثوانٍ - ثبات 4 ثوانٍ (يهدئ الجهاز العصبي السمبثاوي فوراً).
            2. **التخيل الحركي الموجه لكاتا ({kata}):**
               * استلقاء في مكان هادئ وتخيل أداء الكاتا بالكامل بـ **العرض البطيء** مع التركيز على ثبات الوقفات ونظافة الـ Kime وليس سرعة الحركات.
            3. **قاعدة الـ 3 ثوانٍ الذهنية (Reset Rule):**
               * تدريب الدماغ على نسيان أي حركة سابقة انتهت، وتكرار كلمة سر داخلية (مثل: **«زانشين»**) لإعادة ضبط النبض.
            """)

        with tab3:
            st.subheader("🥋 برنامج التدريب العملي في النادي (مع المدرب):")
            st.markdown(f"""
            1. **محاكاة ارتباك الأداء (Error Inoculation Training):**
               * أثناء أداء كاتا **{kata}** في التمرين، يقوم المدرب بإعطاء صيحة مفاجئة أو لمس اللاعب لإحداث خلل متعمد، والمطلوب من اللاعب عدم تغيير سرعته أو انفعاله والاستمرار بنفس الرتم دون تسريع تعويضي.
            2. **روتين الـ 10 دقائق قبل البساط (Pre-Performance Routine):**
               * تدريب اللاعب على تدفئة الأطراف بحركات ديناميكية خفيفة بدلاً من الضرب المفرط المنهك، مع ارتداء الجاكيت وتمرين الزفير الطويل لخفض ضربات القلب.
            3. **تثبيت رتم الكاتا (Metronome Training):**
               * تدريب أداء كاتا {kata} باستخدام إيقاع صوتي ثابت (عد تنازلي أو تصفيق منتظم) لمنع الاندفاع العنيف والتأكيد على وضوح الوقفات الانتقالية.
            """)

        # حفظ السجل
        log_entry = {
            "اللاعب": name,
            "السن": age,
            "الحزام": rank,
            "الكاتا": kata,
            "قلق الإحماء": "نعم" if somatic_anxiety else "لا",
            "اندفاع التعويض": "نعم" if reaction_to_error else "لا",
            "سهر ليلة البطولة": "نعم" if "أسهر طويلاً" in q5 else "لا",
            "تاريخ التسجيل": time.strftime("%Y-%m-%d %H:%M")
        }
        pd.DataFrame([log_entry]).to_csv("athletes_evaluations.csv", mode="a", header=not os.path.exists("athletes_evaluations.csv"), index=False, encoding="utf-8-sig")

# ----------------- 2. الجيم الذهني (رد الفعل الحقيقي) -----------------
elif app_mode == "🎮 الجيم الذهني (رد الفعل والثبات الحقيقي)":
    st.title("🧠 اختبار الثبات وسرعة الاستجابة اللحظية")
    st.write("قياس حقيقي مباشر بالمللي ثانية على شاشة جهازك.")

    col1, col2 = st.columns(2)
    with col1:
        player_name = st.text_input("اسم البطل:", placeholder="اكتب اسمك هنا...")
    with col2:
        level = st.selectbox("المستوى التدريبي:", ["المستوى 1: عادي (2-4 ثوانٍ)", "المستوى 2: تحدي (1.5-3 ثوانٍ)", "المستوى 3: احترافي فجائي (1-2.5 ثوانٍ)"])

    if "المستوى 1" in level:
        min_w, max_w = 2000, 4000
    elif "المستوى 2" in level:
        min_w, max_w = 1500, 3000
    else:
        min_w, max_w = 1000, 2500

    st.markdown("---")

    if not player_name:
        st.info("👋 اكتب اسمك أولاً في الأعلى للانطلاق في التحدي!")
    else:
        st.subheader(f"🥋 تحدي سرعة الاستجابة للبطل: {player_name}")
        
        game_html = f"""
        <!DOCTYPE html>
        <html dir="rtl">
        <head>
            <style>
                #box {{
                    width: 100%;
                    height: 260px;
                    border-radius: 18px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    color: white;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    font-size: 24px;
                    font-weight: bold;
                    cursor: pointer;
                    user-select: none;
                    text-align: center;
                    transition: background-color 0.1s ease;
                    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
                    padding: 15px;
                }}
                .idle {{ background-color: #1e3a8a; }}
                .waiting {{ background-color: #dc2626; }}
                .ready {{ background-color: #16a34a; }}
                .result {{ background-color: #0f172a; }}
                #subtext {{ font-size: 16px; margin-top: 10px; font-weight: normal; }}
            </style>
        </head>
        <body>
            <div id="box" class="idle" onclick="handleClick()">
                <div id="mainText">اضغط هنا لبدء التحدي 🥋</div>
                <div id="subtext">(ادخل وضع الاستعداد YOI)</div>
            </div>

            <script>
                let state = "idle";
                let timer = null;
                let startTime = 0;
                let minWait = {min_w};
                let maxWait = {max_w};

                function handleClick() {{
                    let box = document.getElementById("box");
                    let main = document.getElementById("mainText");
                    let sub = document.getElementById("subtext");

                    if (state === "idle" || state === "result") {{
                        state = "waiting";
                        box.className = "waiting";
                        main.innerText = "🛑 اثبت مكانك وتماسك!";
                        sub.innerText = "لا تلمس الشاشة أبداً حتى تتحول للأخضر...";

                        let delay = Math.floor(Math.random() * (maxWait - minWait + 1)) + minWait;
                        timer = setTimeout(() => {{
                            state = "ready";
                            box.className = "ready";
                            main.innerText = "💥 انطلق الآن! اضغط فوراً!";
                            sub.innerText = "كيااااي!";
                            startTime = performance.now();
                        }}, delay);

                    }} else if (state === "waiting") {{
                        clearTimeout(timer);
                        state = "result";
                        box.className = "waiting";
                        main.innerText = "❌ تسرع واندفاع (Over-Arousal)!";
                        sub.innerText = "لمست الشاشة قبل الإشارة الخضراء. اضغط لإعادة المحاولة بهدوء.";

                    }} else if (state === "ready") {{
                        let reactionTime = Math.round(performance.now() - startTime);
                        state = "result";
                        box.className = "result";
                        main.innerText = "🎯 زمن الاستجابة: " + reactionTime + " مللي ثانية";

                        let feedback = "";
                        if (reactionTime < 250) feedback = "🔥 سرعة استثنائية وانفجارية!";
                        else if (reactionTime < 380) feedback = "⚡ تركيز ممتاز ورد فعل عالي!";
                        else if (reactionTime < 500) feedback = "👍 استجابة جيدة ولكن تحتاج يقظة أعلى.";
                        else feedback = "⏳ تردد طفيف، ركز أكثر في المحاولة القادمة.";

                        sub.innerText = feedback + " (اضغط لتكرار التحدي)";
                    }}
                }}
            </script>
        </body>
        </html>
        """
        components.html(game_html, height=300)

# ----------------- 3. قسم التحكم العصبي (Go / No-Go) -----------------
elif app_mode == "🎯 اختبار القرار والتحكم العصبي (Go / No-Go)":
    st.title("🎯 اختبار التحكم في الاندفاع (Go / No-Go)")
    st.write("اختبار عصبي لقياس القدرة على كبح الحركة عند ظهور إشارة الخداع مقابل الضغط السريع عند ظهور إشارة الهجوم.")

    p_name = st.text_input("اسم البطل:", placeholder="اكتب اسمك هنا...", key="gonogo_name")
    
    if p_name:
        gonogo_html = """
        <!DOCTYPE html>
        <html dir="rtl">
        <head>
            <style>
                #gobox {{
                    width: 100%;
                    height: 280px;
                    border-radius: 18px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    color: white;
                    font-family: sans-serif;
                    cursor: pointer;
                    text-align: center;
                    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
                    user-select: none;
                }}
                .start {{ background: #1e293b; }}
                .strike {{ background: #15803d; font-size: 50px; }}
                .hold {{ background: #b91c1c; font-size: 50px; }}
                .score {{ background: #0f172a; font-size: 24px; }}
                #info {{ font-size: 18px; margin-top: 10px; font-weight: normal; }}
            </style>
        </head>
        <body>
            <div id="gobox" class="start" onclick="boxClick()">
                <div id="title">اضغط لبدء جولة الـ 5 إشارات 🥋</div>
                <div id="info">اضرب عند الأخضر (👊) واثبت تماماً عند الأحمر (🛑)</div>
            </div>

            <script>
                let round = 0;
                let active = false;
                let currentType = "";
                let score = 0;
                let responded = false;
                let testTimer = null;

                function boxClick() {{
                    let b = document.getElementById("gobox");
                    let t = document.getElementById("title");
                    let inf = document.getElementById("info");

                    if (!active && round === 0) {{
                        score = 0;
                        nextSignal();
                    }} else if (active) {{
                        if (currentType === "strike") {{
                            if (!responded) {{
                                score += 20;
                                responded = true;
                                t.innerText = "✅ ضربة في وقتها!";
                            }}
                        }} else if (currentType === "hold") {{
                            score -= 20;
                            t.innerText = "❌ اندفعت في الخداع!";
                            responded = true;
                        }}
                    }}
                }}

                function nextSignal() {{
                    let b = document.getElementById("gobox");
                    let t = document.getElementById("title");
                    let inf = document.getElementById("info");

                    if (round >= 5) {{
                        active = false;
                        b.className = "score";
                        t.innerText = "🏆 النتيجة النهائية: " + Math.max(0, score) + " / 100";
                        inf.innerText = "اضغط للبدء من جديد";
                        round = 0;
                        return;
                    }}

                    round++;
                    active = false;
                    b.className = "start";
                    t.innerText = "استعد... (جولة " + round + " من 5)";
                    inf.innerText = "ركز ولا تتعجل";

                    let delay = Math.floor(Math.random() * 1500) + 1200;
                    setTimeout(() => {{
                        active = true;
                        responded = false;
                        let isStrike = Math.random() > 0.4;
                        if (isStrike) {{
                            currentType = "strike";
                            b.className = "strike";
                            t.innerText = "👊 اضرب!";
                            inf.innerText = "المس الشاشة فوراً!";
                        }} else {{
                            currentType = "hold";
                            b.className = "hold";
                            t.innerText = "🛑 اثبت مكانك!";
                            inf.innerText = "إياك أن تلمس الشاشة!";
                        }}

                        setTimeout(() => {{
                            if (currentType === "hold" && !responded) {{
                                score += 20;
                            }}
                            nextSignal();
                        }}, 900);

                    }}, delay);
                }}
            </script>
        </body>
        </html>
        """
        components.html(gonogo_html, height=320)

# ----------------- 4. قسم اختبار التطور التتبعي -----------------
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

# سجل التقييمات المحفوظة في القائمة الجانبية
st.sidebar.markdown("---")
with st.sidebar.expander("📁 سجل استمارات اللاعبين المسجلة"):
    if os.path.exists("athletes_evaluations.csv"):
        st.dataframe(pd.read_csv("athletes_evaluations.csv", encoding="utf-8-sig"))
    else:
        st.write("لا توجد استمارات مسجلة بعد.")
