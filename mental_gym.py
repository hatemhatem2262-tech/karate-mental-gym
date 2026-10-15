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
        "🎮 الجيم الذهني (رد الفعل والثبات الحقيقي)",
        "🎯 اختبار القرار والتحكم العصبي (Go / No-Go)",
        "📈 اختبار التطور التتبعي (بعد فترة تدريب)",
        "📖 دليل البطل (طريقة اللعب)"
    ]
)

# ----------------- 1. قسم دليل البطل -----------------
if app_mode == "📖 دليل البطل (طريقة اللعب)":
    st.title("📖 دليل البطل: كيف تخوض التحدي الذهني؟")
    st.markdown("""
    ### أهلاً بك يا بطل المستقبل! 🥋
    هذا التدريب مصمم خصيصاً لتقوية **أعصابك وثباتك الداخلي** وسرعة رد فعلك الفعلي تحت الضغط العصبي.
    
    ---
    #### 🚦 التمرين الأول: اختبار الثبات ورد الفعل الفوري:
    1. **الشاشة الحمراء:** لا تلمس الشاشة نهائياً! اللمس في الأحمر يعني تسرعاً وتشتتاً وخصم نقاط فورية.
    2. **الشاشة الخضراء:** أول ما تتحول الشاشة للأخضر، المس المربع بأقصى سرعة ممكنة.
    * العداد يقيس بالمللي ثانية الحقيقية داخل جهازك مباشرة دون أي تأخير إنترنت.

    ---
    #### 🎯 التمرين الثاني: اختبار القرار والتحكم (Go / No-Go):
    * ستظهر إشارات متتالية وسريعة:
      * **علامة اللكمة (👊) أو الخضراء:** اضرب فوراً!
      * **علامة التوقف (🛑) أو الخداع:** اثبت تماماً ولا تلمس الشاشة.
    * هذا الاختبار يدربك على كبح الاندفاع التلقائي والسيطرة التامة على ردود أفعالك أثناء الكاتا والقتال.
    """)

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
        
        # كود تفاعلي بالـ JavaScript لحساب زمن رد الفعل الحقيقي في المتصفح محلياً
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
                #gobox {
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
                }
                .start { background: #1e293b; }
                .strike { background: #15803d; font-size: 50px; }
                .hold { background: #b91c1c; font-size: 50px; }
                .score { background: #0f172a; font-size: 24px; }
                #info { font-size: 18px; margin-top: 10px; font-weight: normal; }
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

                function boxClick() {
                    let b = document.getElementById("gobox");
                    let t = document.getElementById("title");
                    let inf = document.getElementById("info");

                    if (!active && round === 0) {
                        score = 0;
                        nextSignal();
                    } else if (active) {
                        if (currentType === "strike") {
                            if (!responded) {
                                score += 20;
                                responded = true;
                                t.innerText = "✅ ضربة في وقتها!";
                            }
                        } else if (currentType === "hold") {
                            score -= 20;
                            t.innerText = "❌ اندفعت في الخداع!";
                            responded = true;
                        }
                    }
                }

                function nextSignal() {
                    let b = document.getElementById("gobox");
                    let t = document.getElementById("title");
                    let inf = document.getElementById("info");

                    if (round >= 5) {
                        active = false;
                        b.className = "score";
                        t.innerText = "🏆 النتيجة النهائية: " + Math.max(0, score) + " / 100";
                        inf.innerText = "اضغط للبدء من جديد";
                        round = 0;
                        return;
                    }

                    round++;
                    active = false;
                    b.className = "start";
                    t.innerText = "استعد... (جولة " + round + " من 5)";
                    inf.innerText = "ركز ولا تتعجل";

                    let delay = Math.floor(Math.random() * 1500) + 1200;
                    setTimeout(() => {
                        active = true;
                        responded = false;
                        let isStrike = Math.random() > 0.4;
                        if (isStrike) {
                            currentType = "strike";
                            b.className = "strike";
                            t.innerText = "👊 اضرب!";
                            inf.innerText = "المس الشاشة فوراً!";
                        } else {
                            currentType = "hold";
                            b.className = "hold";
                            t.innerText = "🛑 اثبت مكانك!";
                            inf.innerText = "إياك أن تلمس الشاشة!";
                        }

                        setTimeout(() => {
                            if (currentType === "hold" && !responded) {
                                score += 20;
                            }
                            nextSignal();
                        }, 900);

                    }, delay);
                }
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
