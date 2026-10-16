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
    st.info("💡 أدخل بيانات اللاعب وإجاباته بدقة للحصول على خطة تدريبية مخصصة 100% لحالته الفردية.")

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

        submit_btn = st.form_submit_button("📊 تحليل نتائج اللاعب وإصدار البرامج التدريبية المخصصة")

    if submit_btn:
        if not name:
            st.warning("⚠️ يرجى كتابة اسم اللاعب أولاً لحفظ بياناته وإصدار الخطة.")
        else:
            st.success(f"تم تحليل استمارة البطل: {name} بنجاح!")
            st.markdown("---")

            # --- محرك التحليل الديناميكي المخصص ---
            home_drills = []
            dojo_drills = []
            strengths = []
            weaknesses = []

            # تحليل السؤال 1 (الإحماء والحالة العصبية)
            if "برودة بالأطراف" in q1:
                weaknesses.append("قلق منافسة بدني (Somatic Anxiety) يسبب انقباض الأوعية وبرودة الأطراف وتسارع النبض.")
                home_drills.append("• تمرين التنفس العميق المهدئ (4-7-8): شهيق 4 ثوانٍ، كتم 7 ثوانٍ، زفير بطيء 8 ثوانٍ لتهدئة ضربات القلب.")
                dojo_drills.append(f"• روتين تدفئة ديناميكي خاص: إلزام اللاعب بارتداء الجاكيت وتدفئة اليدين والقدمين بحركات مركبة خفيفة مع تجنب الضرب الانفجاري المفرط قبل البساط.")
            elif "طاقة وحماس مفرط" in q1:
                weaknesses.append("استثارة عصبية زائدة وتفريغ مبكر للطاقة في الإحماء مما يؤدي لنفاذ الـ Kime على البساط.")
                home_drills.append("• تدريب ضبط الإيقاع الذهني: الاستماع إلى إيقاع هادئ وتخيل أداء الكاتا بتركيز على الوقفات والهدوء بين كل حركة وحركة.")
                dojo_drills.append(f"• كبح طاقة الإحماء: منع اللاعب من تكرار كاتا ({kata}) كاملة في الإحماء؛ يكتفي فقط بمراجعة الوقفات وتمرين الزفير الطويل لتهدئة الجهاز العصبي.")
            elif "إحساس بالثقل" in q1:
                weaknesses.append("نقص الاستثارة العصبية (Under-arousal) ودخول البساط بجسد خامل ورد فعل بطيء.")
                home_drills.append("• التخيل التحفيزي: استرجاع أفضل لحظات الفوز والتتويج وسماع صوت الكياي القوي لتحفيز هرمونات النشاط.")
                dojo_drills.append(f"• إحماء تنشيطي انفجاري (Pylometrics): قفزات سريعة متتالية مع ضرب كياي عالي وقصير قبل الدخول بدقيقتين لتنبيه الجهاز العصبي المركزي.")
            else:
                strengths.append("ثبات وانضباط عصبي عالي في منطقة الإحماء.")
                home_drills.append("• الحفاظ على روتين التنفس الحالي مع مراجعة كاتا متوازنة ذهنياً.")
                dojo_drills.append("• تثبيت روتين الإحماء الناجح دون تغيير.")

            # تحليل السؤال 2 (التعامل مع الخطأ والاهتزاز)
            if "أفقد التركيز" in q1 or "أفقد التركيز" in q2:
                weaknesses.append("صدمة الخطأ (Catastrophic Thinking): التفكير في أن المباراة ضاعت بمجرد حدوث اهتزاز بسيط.")
                home_drills.append("• تمرين قاعدة الـ 3 ثوانٍ (Reset): تكرار سيناريو خطأ تخيلي في البيت، والتدرب على أخذ نفس وإطلاق كلمة سر (مثل: «زانشين») لنسيان الخطأ فوراً.")
                dojo_drills.append(f"• تدريب التشتيت المفاجئ: أثناء أداء كاتا ({kata})، يقوم المدرب بمقاطعة اللاعب أو تصعيب حركته، والمطلوب منه استكمال الكاتا بتركيز وقوة فورية.")
            elif "أنفعل داخلياً" in q2:
                weaknesses.append("اندفاع تعويضي عنيف: محاولة تعويض الخطأ بالقوة والتسريع مما يخل بالرتم وميزان الكاتا.")
                home_drills.append(f"• تدريب التخيل البطيء لـ ({kata}): أداء الكاتا في الخيال بنصف السرعة للتأكيد على عمق الوقفات وثبات نقلات الثقل.")
                dojo_drills.append(f"• تدريب المترونوم الصوتي: إلزام اللاعب بأداء كاتا ({kata}) على توقيت إيقاعي ثابت، بحيث إذا أخطأ يُمنع تماماً من تسريع الحركات التالية.")
            else:
                strengths.append("مرونة نفسية وقدرة ممتازة على التجاوز السريع للأخطاء دون ارتباك.")

            # تحليل السؤال 3 (التعامل مع المنافسين)
            if "يتسرب الشك" in q3:
                weaknesses.append("المقارنة الهدامة وتشتت التركيز الخارجي بمستوى ودرجات المنافسين.")
                home_drills.append("• توكيدات الكفاءة الذاتية: كتابة 3 نقاط تميز يمتلكها اللاعب في كاتا الخاصة به وتكرارها يومياً قبل النوم.")
                dojo_drills.append("• عزل المنافسين: منع اللاعب من متابعة جولات منافسيه المباشرين في البطولة، وتوجيهه للتركيز في حيزه الخاص فقط.")
            elif "أتحمس بشكل عدائي" in q3:
                weaknesses.append("توتر عدائي مفرط يؤدي إلى تشنج العضلات وفقدان نظافة التكنيك وجودة الحركات.")
                home_drills.append("• تمرين استرخاء العضلات التدريجي (PMR): شد وإرخاء عضلات الكتفين والذراعين للشعور بالانسيابية.")
                dojo_drills.append("• تدريب الانسيابية قبل الانفجار: التركيز في التمرين على بدء الحركة بارتخاء تام والشد (Kime) في أجزاء الثانية الأخيرة فقط.")
            else:
                strengths.append("عزل ذهني احترافي لنقاط المنافسين وتركيز ذاتي كامل على التكنيك الشخصي.")

            # تحليل السؤال 4 (صيحات الجمهور)
            if "يتشتت انتباهي" in q4 or "تزيد الأصوات" in q4:
                weaknesses.append("حساسية للمؤثرات الخارجية والضوضاء مما يربك التوقيت والانتقال الحركي.")
                dojo_drills.append(f"• تدريب محاكاة ضجيج الصالات: تشغيل أصوات جمهور وصيحات حكام بصوت مرتفع في صالة النادي أثناء أداء كاتا ({kata}) لتدريب التركيز البؤري الضيق.")
            else:
                strengths.append("امتلاك تركيز بؤري ضيق ومحكم (Tunnel Vision) يحميه من أي مشتت خارجي.")

            # تحليل السؤال 5 (ليلة البطولة والنوم)
            if "أواجه صعوبة" in q5:
                weaknesses.append("قلق ليلة النزال وسيناريوهات الفشل الذهنية.")
                home_drills.append("• تمرين التخيل الإيجابي الموجه: الاستلقاء قبل النوم وتخيل سيناريو الصعود لمنصة التتويج وتحية الحكام بثقة وهدوء.")
            elif "أسهر طويلاً" in q5:
                weaknesses.append("استثارة ذهنية وفرط تفكير بالميدالية يسرق طاقة النوم والراحة العصبية.")
                home_drills.append("• بروتوكول تفريغ الدماغ: كتابة كل الأفكار والخطط في ورقة وإغلاقها قبل النوم بساعة، مع منع شاشات الهاتف.")
            else:
                strengths.append("روتين نوم متزن ونضج ذهني ممتاز ليلة البطولة.")

            # صياغة بطاقة المنزل المستقلة
            home_plan_text = f"""==================================================
🥋 بطاقة التدريب العقلي والمنزلي للبطل
إشراف الكابتن: حاتم
==================================================
اسم البطل: {name}
السن: {age}  |  الحزام: {rank}  |  الكاتا الأساسية: {kata}
تاريخ الإصدار: {time.strftime('%Y-%m-%d')}
--------------------------------------------------
🎯 الواجبات الذهنية والتنفسية في المنزل (تطبق يومياً):

""" + "\n\n".join(home_drills) + f"""

--------------------------------------------------
💡 كلمة السر للبطل {name}:
«ثباتك في هدوء أنفاسك ونظافة وقفاتك.. ركز في نفسك وتجاهل كل ما حولك»
=================================================="""

            # صياغة خطة النادي الميدانية المستقلة
            dojo_plan_text = f"""==================================================
🥋 الخطة الفنية والميدانية للمدرب داخل الصالة
إشراف الكابتن: حاتم
==================================================
اللاعب: {name}  |  الكاتا المستهدفة: {kata}
الدرجة: {rank}  |  السن: {age}
تاريخ الإصدار: {time.strftime('%Y-%m-%d')}
--------------------------------------------------
🔍 التقييم التشخيصي السريع:
* نقاط القوة: {', '.join(strengths) if strengths else 'قيد التأسيس والتطوير'}
* نقاط الضعف المعالجة: {', '.join(weaknesses)}

--------------------------------------------------
🥋 التوجيهات والتدريبات العملية في النادي:

""" + "\n\n".join(dojo_drills) + f"""
=================================================="""

            # أزرار التنزيل والطباعة المنفصلة
            st.subheader("🖨️ تنزيل وطباعة البرامج في أوراق منفصلة:")
            c_p1, c_p2 = st.columns(2)
            with c_p1:
                st.download_button(
                    label="📄 تنزيل ورقة تدريب المنزل للبطل (ورقة مستقلة)",
                    data=home_plan_text,
                    file_name=f"تدريب_منزلي_{name}.txt",
                    mime="text/plain"
                )
            with c_p2:
                st.download_button(
                    label="🥋 تنزيل خطة تدريب النادي للمدرب (ورقة مستقلة)",
                    data=dojo_plan_text,
                    file_name=f"خطة_نادي_{name}.txt",
                    mime="text/plain"
                )

            st.markdown("---")
            t1, t2, t3 = st.tabs(["🧠 التشخيص النفسي", "🏠 برنامج المنزل المخصص", "🥋 برنامج النادي الميداني"])
            with t1:
                st.subheader(f"الملف النفسي والتشخيص للبطل: {name}")
                st.markdown("#### 💪 نقاط القوة المكتشفة:")
                if strengths:
                    for s in strengths: st.write(f"✅ {s}")
                else:
                    st.write("يحتاج إلى بناء الثقة والتركيز من الصفر.")
                
                st.markdown("#### ⚠️ التحديات الواجب علاجها فوراً:")
                for w in weaknesses: st.write(f"⚠️ {w}")

            with t2:
                st.text(home_plan_text)

            with t3:
                st.text(dojo_plan_text)

            # حفظ السجل
            log_entry = {
                "اللاعب": name,
                "السن": age,
                "الحزام": rank,
                "الكاتا": kata,
                "أبرز نقاط الضعف": " | ".join(weaknesses[:2]),
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
