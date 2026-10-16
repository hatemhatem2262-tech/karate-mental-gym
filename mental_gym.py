import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import time
import os

st.set_page_config(page_title="الجيم الذهني للكاراتيه - كابتن حاتم", page_icon="🥋", layout="wide")

st.sidebar.title("🥋 بوابة الإعداد النفسي")
app_mode = st.sidebar.radio(
    "اختر القسم:",
    [
        "📋 استبيان الإعداد النفسي والخطط التدريبية",
        "🎮 الجيم الذهني (رد الفعل والثبات الحقيقي)",
        "🎯 اختبار القرار والتحكم العصبي (Go / No-Go)",
        "📈 اختبار التطور التتبعي (بعد فترة تدريب)",
        "📖 دليل البطل (طريقة اللعب)"
    ]
)

# ----------------- 1. قسم استبيان الإعداد النفسي -----------------
if app_mode == "📋 استبيان الإعداد النفسي والخطط التدريبية":
    st.title("📋 استبيان الأداء الذهني والتنافسي — ناشئين وشباب")
    st.markdown("**برنامج التحليل السلوكي ومواجهة الضغوط التنافسية — إشراف: كابتن حاتم**")
    st.info("💡 أدخل بيانات اللاعب وإجاباته من الاستمارة الورقية، ثم اضغط على زر التحليل بالأسفل.")

    with st.form("athlete_profile_form"):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            name = st.text_input("اسم اللاعب:")
        with col2:
            age = st.text_input("السن (سنة الميلاد):")
        with col3:
            rank = st.text_input("الدرجة / الحزام:")
        with col4:
            kata = st.text_input("الكاتا الأساسية:")

        st.markdown("---")
        st.subheader("📝 إجابات الاستبيان التنافسي:")

        q1 = st.radio(
            "1. في منطقة الإحماء الرسمية قبل الصعود للبساط بـ 5 إلى 10 دقائق:",
            [
                "برودة بالأطراف، تسارع نبضات القلب، اضطراب بالمعدة، وتخوف من نسيان الحركات أو سوء الأداء.",
                "طاقة وحماس مفرط، رغبة في التسريع والضرب بقوة في الإحماء دون أخذ راحة كافية أو تنظيم نفس.",
                "إحساس بالثقل أو الخمول وضعف الاستثارة العصبية وصعوبة في إشعال الحافز الداخلي للمباراة.",
                "ثبات وانضباط، تركيز كامل على إيقاع الكاتا والتنفس المنتظم مع استرجاع ذهني هادئ للتكنيك."
            ]
        )

        q2 = st.radio(
            "2. أثناء أداء الكاتا الرسمية أمام لجنة الحكام، حدث اهتزاز مفاجئ في وقفة أو حركة:",
            [
                "أفقد التركيز فوراً، وتسيطر علي فكرة أن المباراة ضاعت، فينعكس الارتباك على الحركات المتبقية.",
                "أستمر فوراً بنفس الهدوء والإيقاع وكأن شيئاً لم يحدث، وأوجه تركيزي بالكامل للحركة القادمة.",
                "أنفعل داخلياً وأزيد سرعة وعنف الضربات التالية للتعويض فيختل الـ Rhythm والتوازن التام."
            ]
        )

        q3 = st.radio(
            "3. عندما تشاهد منافسك المباشر في القرعة يؤدي كاتا قوية جداً وحصد علامات مرتفعة:",
            [
                "يتسرب الشك إلى نفسي وأبدأ بمقارنة مستواي بمستواه وأشعر بأن فرص الفوز أصبحت ضعيفة.",
                "أتحمس بشكل عدائي مبالغ فيه وأقرر تفجير الحركات بأقصى طاقة حتى لو فقدت نظافة التكنيك.",
                "أعزل تركيزي عن نقاط المنافسين وأعلم أن تركيزي على أداء حركاتي بإتقان هو الفيصل الوحيد."
            ]
        )

        q4 = st.radio(
            "4. عند سماع صيحات الجمهور أو توجيهات مفاجئة بصوت عالٍ أثناء أداء الكاتا:",
            [
                "يتشتت انتباهي البصري والسمعي للحظة وأشعر بارتباك في التوقيت والانتقال الحركي.",
                "أمتلك نفق تركيز ضيق (Tunnel Vision) ولا أسمع أو أرى سوى مسار حركتي الافتراضية.",
                "تزيد الأصوات من تهوري وتدفعني للاستعراض المبالغ فيه على حساب الدقة الفنية."
            ]
        )

        q5 = st.radio(
            "5. روتين ليلة البطولة قبل الخلود للنوم:",
            [
                "أواجه صعوبة في الاستغراق بالنوم بسبب توارد سيناريوهات الأخطاء أو هاجس الهزيمة.",
                "أسهر طويلاً بسبب فرط التفكير والحماس المفرط للميدالية والتتويج ولا تهدأ طاقتي.",
                "أطبق روتين تنفس هادئ مع تخيل كاتا ناجحة ومتكاملة، وأنام نوماً عميقاً ومريحاً."
            ]
        )

        submit_btn = st.form_submit_button("📊 تحليل نتائج اللاعب وإصدار البرامج التدريبية فوراً")

    if submit_btn:
        if not name:
            st.warning("⚠️ يرجى كتابة اسم اللاعب أولاً لحفظ بياناته وإصدار الخطة.")
        else:
            st.success(f"تم تحليل استمارة البطل: {name} بنجاح!")
            st.markdown("---")

            somatic_anxiety = "برودة بالأطراف" in q1
            over_arousal = "طاقة وحماس مفرط" in q1 or "أسهر طويلاً" in q5
            reaction_to_error = "أنفعل داخلياً" in q2 or "أفقد التركيز" in q2
            self_focus = "أعزل تركيزي" in q3
            tunnel_vision = "Tunnel Vision" in q4

            home_plan_text = f"""🥋 برنامج التدريب العقلي في المنزل (يطبقه اللاعب يومياً)
إشراف: كابتن حاتم
--------------------------------------------------
اسم البطل: {name}
السن: {age}  |  الدرجة: {rank}  |  الكاتا الأساسية: {kata}
تاريخ الإصدار: {time.strftime('%Y-%m-%d')}
--------------------------------------------------

1. بروتوكول التنفس الترددي (Box Breathing 4-4-4-4):
* التطبيق: 10 دقائق يومياً قبل النوم مباشرة للتخلص من السهر وفرط التفكير في الميداليات.
* الطريقة: شهيق هادئ (4 ثوانٍ) - كتم النفس (4 ثوانٍ) - زفير تفريغي (4 ثوانٍ) - ثبات (4 ثوانٍ).
* الهدف: تهدئة الجهاز العصبي السمبثاوي وخفض نبضات القلب السريعة.

2. التخيل الحركي الموجه لكاتا ({kata}):
* التطبيق: 3 إلى 5 مرات أسبوعياً في مكان هادئ مع إغماض العينين.
* الطريقة: تخيل أداء كاتا ({kata}) بالكامل بالعرض البطيء.
* التركيز: ثبات الوقفات، كتم الاندفاع، ونظافة الـ Kime في نهاية كل حركة.

3. قاعدة الـ 3 ثوانٍ الذهنية (Reset Rule):
* تدريب الدماغ على نسيان أي حركة سابقة انتهت أو حدث فيها اهتزاز.
* تكرار كلمة سر داخلية مثل: «زانشين» لإعادة ضبط النبض والتركيز على الحركة التالية فقط بنسبة 100%."""

            dojo_plan_text = f"""🥋 خطة التدريب الميداني والفني في النادي (خاص بالمدرب)
إشراف: كابتن حاتم
--------------------------------------------------
اسم البطل: {name}
السن: {age}  |  الدرجة: {rank}  |  الكاتا الأساسية: {kata}
تاريخ الإصدار: {time.strftime('%Y-%m-%d')}
--------------------------------------------------

1. محاكاة ارتباك الأداء (Error Inoculation Training):
* أثناء أداء كاتا ({kata}) في التمرين، إعطاء صيحة مفاجئة أو لمس مفاجئ للاعب لإحداث خلل متعمد.
* المطلوب: عدم الانفعال التعويضي، والاستمرار بنفس الرتم والتنفس دون تسريع الضربات التالية.

2. روتين الـ 10 دقائق قبل الصعود للبساط (Pre-Performance Routine):
* إلزام اللاعب بتدفئة الأطراف بحركات ديناميكية خفيفة وارتداء الجاكيت لمنع برودة الأطراف.
* منع الضرب العنيف والمفرط في الإحماء لتوفير الطاقة العصبية.

3. تثبيت إيقاع الكاتا بالعد المنتظم (Metronome Training):
* أداء كاتا ({kata}) بعداد صوتي منتظم لضبط الـ Rhythm والتأكيد على وضوح الوقفات الانتقالية."""

            # أزرار تنزيل الورق بشكل منفصل
            st.subheader("🖨️ تنزيل وطباعة البرامج في أوراق منفصلة:")
            c_p1, c_p2 = st.columns(2)
            with c_p1:
                st.download_button(
                    label="📄 تنزيل ورقة تدريب المنزل للبطل (PDF/Text)",
                    data=home_plan_text,
                    file_name=f"تدريب_منزلي_{name}.txt",
                    mime="text/plain"
                )
            with c_p2:
                st.download_button(
                    label="🥋 تنزيل خطة تدريب النادي للمدرب (PDF/Text)",
                    data=dojo_plan_text,
                    file_name=f"خطة_نادي_{name}.txt",
                    mime="text/plain"
                )

            st.markdown("---")
            t1, t2, t3 = st.tabs(["🧠 التشخيص النفسي", "🏠 برنامج المنزل", "🥋 برنامج النادي"])
            with t1:
                st.subheader(f"الملف النفسي للبطل: {name}")
                if self_focus: st.write("✅ **عزل ممتاز للمنافسين:** تركيز داخلي عالي.")
                if tunnel_vision: st.write("✅ **تركيز بؤري قوي:** حماية من تشتت صيحات الجمهور.")
                if somatic_anxiety: st.write("⚠️ **قلق استباقي وتوتر بدني:** برودة أطراف وتسارع نبض.")
                if "أنفعل داخلياً" in q2: st.write("⚠️ **اندفاع تعويضي:** تسريع مفرط بعد الاهتزاز يخل بالرتم.")
                if "أسهر طويلاً" in q5: st.write("⚠️ **استثارة زائدة ليلة البطولة:** تفكير مفرط في الميدالية يسبب قلة النوم.")

            with t2:
                st.text(home_plan_text)

            with t3:
                st.text(dojo_plan_text)

            # حفظ اللاعب تلقائياً في السجل
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
    col1, col2 = st.columns(2)
    with col1:
        player_name = st.text_input("اسم البطل:")
    with col2:
        level = st.selectbox("المستوى التدريبي:", ["المستوى 1: عادي", "المستوى 2: تحدي", "المستوى 3: احترافي"])

    min_w, max_w = (2000, 4000) if "1" in level else ((1500, 3000) if "2" in level else (1000, 2500))

    if player_name:
        game_html = f"""
        <!DOCTYPE html>
        <html dir="rtl">
        <head>
            <style>
                #box {{ width: 100%; height: 250px; border-radius: 15px; display: flex; flex-direction: column; justify-content: center; align-items: center; color: white; font-family: sans-serif; font-size: 22px; font-weight: bold; cursor: pointer; user-select: none; }}
                .idle {{ background-color: #1e3a8a; }}
                .waiting {{ background-color: #dc2626; }}
                .ready {{ background-color: #16a34a; }}
                .result {{ background-color: #0f172a; }}
            </style>
        </head>
        <body>
            <div id="box" class="idle" onclick="handleClick()">
                <div id="t">اضغط للبدء 🥋</div>
                <div style="font-size:15px;margin-top:8px;" id="s">(وضع الاستعداد)</div>
            </div>
            <script>
                let state = "idle", timer, start;
                function handleClick() {{
                    let b = document.getElementById("box"), t = document.getElementById("t"), s = document.getElementById("s");
                    if(state === "idle" || state === "result") {{
                        state = "waiting"; b.className = "waiting"; t.innerText = "🛑 اثبت مكانك!"; s.innerText = "لا تلمس حتى تصبح خضراء...";
                        timer = setTimeout(() => {{
                            state = "ready"; b.className = "ready"; t.innerText = "💥 اضرب فوراً!"; s.innerText = "كيااااي!";
                            start = performance.now();
                        }}, Math.floor(Math.random() * ({max_w} - {min_w} + 1)) + {min_w});
                    }} else if(state === "waiting") {{
                        clearTimeout(timer); state = "result"; b.className = "waiting"; t.innerText = "❌ تسرع واندفاع!"; s.innerText = "اضغط للمحاولة بهدوء.";
                    }} else if(state === "ready") {{
                        let rt = Math.round(performance.now() - start);
                        state = "result"; b.className = "result"; t.innerText = "🎯 رد الفعل: " + rt + " ms"; s.innerText = "اضغط للتكرار";
                    }}
                }}
            </script>
        </body>
        </html>
        """
        components.html(game_html, height=290)

# ----------------- 3. قسم التحكم العصبي (Go / No-Go) -----------------
elif app_mode == "🎯 اختبار القرار والتحكم العصبي (Go / No-Go)":
    st.title("🎯 اختبار التحكم في الاندفاع (Go / No-Go)")
    p_name = st.text_input("اسم البطل:", key="gng")
    if p_name:
        gonogo_html = """
        <!DOCTYPE html>
        <html dir="rtl">
        <head>
            <style>
                #g {{ width: 100%; height: 260px; border-radius: 15px; display: flex; flex-direction: column; justify-content: center; align-items: center; color: white; font-family: sans-serif; cursor: pointer; user-select: none; font-size: 32px; font-weight: bold; background: #1e293b; }}
            </style>
        </head>
        <body>
            <div id="g" onclick="c()">
                <div id="m">اضغط لبدء التحدي 🥋</div>
                <div style="font-size:16px;margin-top:10px;" id="sub">اضرب عند الأخضر واثبت عند الأحمر</div>
            </div>
            <script>
                let r = 0, on = false, kind = "", pts = 0;
                function c() {
                    let g = document.getElementById("g"), m = document.getElementById("m");
                    if(!on && r === 0) { pts = 0; nxt(); }
                    else if(on) {
                        if(kind === "s") { pts += 20; m.innerText = "✅ ضربة في وقتها!"; on = false; }
                        else { pts -= 20; m.innerText = "❌ اندفاع في الخداع!"; on = false; }
                    }
                }
                function nxt() {
                    let g = document.getElementById("g"), m = document.getElementById("m"), sub = document.getElementById("sub");
                    if(r >= 5) { g.style.background = "#0f172a"; m.innerText = "النتيجة: " + Math.max(0, pts) + " / 100"; sub.innerText = "اضغط للبدء من جديد"; r = 0; on = false; return; }
                    r++; on = false; g.style.background = "#1e293b"; m.innerText = "استعد (" + r + "/5)"; sub.innerText = "";
                    setTimeout(() => {
                        on = true;
                        let s = Math.random() > 0.4;
                        kind = s ? "s" : "h";
                        g.style.background = s ? "#15803d" : "#b91c1c";
                        m.innerText = s ? "👊 اضرب!" : "🛑 اثبت مكانك!";
                        setTimeout(() => { if(kind === "h" && on) pts += 20; nxt(); }, 900);
                    }, Math.floor(Math.random() * 1200) + 1000);
                }
            </script>
        </body>
        </html>
        """
        components.html(gonogo_html, height=300)

# ----------------- 4. قسم اختبار التطور التتبعي -----------------
elif app_mode == "📈 اختبار التطور التتبعي (بعد فترة تدريب)":
    st.title("📈 مقياس التطور الذهني التتبعي")
    t_name = st.text_input("اسم اللاعب:")
    q1 = st.radio("س1: الوقوف على خط البداية أمام الحكام:", ["ما زلت أشعر بتسارع ضربات القلب", "أصبحت أسيطر على نفسي بتمارين التنفس"])
    q2 = st.radio("س2: عند حدوث اهتزاز بسيط في الكاتا:", ["أتوتر وأتأثر", "أطبق قاعدة الـ 3 ثوانٍ وأكمل بثبات"])
    q3 = st.radio("س3: الالتزام بتمارين التنفس في المنزل:", ["أمارسها نادراً", "أمارسها بانتظام"])
    if st.button("تسجيل قياس التطور"):
        if t_name:
            sc = (35 if "أصبحت" in q1 else 0) + (35 if "أطبق" in q2 else 0) + (30 if "بانتظام" in q3 else 0)
            st.metric("معدل التطور الذهني:", f"{sc}%")

# ----------------- 5. دليل البطل -----------------
elif app_mode == "📖 دليل البطل (طريقة اللعب)":
    st.title("📖 دليل البطل: طريقة خوض التحديات الذهنية")
    st.write("شرح كامل لقواعد التدريب والتحكم في الاندفاع ورد الفعل السريع.")

st.sidebar.markdown("---")
with st.sidebar.expander("📁 سجل استمارات اللاعبين المسجلة"):
    if os.path.exists("athletes_evaluations.csv"):
        st.dataframe(pd.read_csv("athletes_evaluations.csv", encoding="utf-8-sig"))
    else:
        st.write("لا توجد استمارات مسجلة بعد.")
