(function () {
  const lang = document.documentElement.lang === "en" ? "en" : "fr";

  const copy = {
    fr: {
      progress: (n, total) => `Question ${n} sur ${total}`,
      next: "Suivant",
      prev: "Précédent",
      results: "Voir mes résultats",
      start: "Commencer le diagnostic",
      answers: ["Pas du tout", "Peu", "Moyennement", "Plutôt bien", "Tout à fait"],
      cats: { growth: "Croissance", innovation: "Innovation", rse: "RSE", ai: "IA" },
      questions: [
        { text: "Votre marque a-t-elle une mission et un positionnement clairs et différenciants ?", category: "growth" },
        { text: "Votre portefeuille de produits est-il optimisé et rentable sur l'ensemble des SKUs ?", category: "growth" },
        { text: "Vos parts de marché évoluent-elles positivement sur les 2 dernières années ?", category: "growth" },
        { text: "Vos équipes marketing sont-elles alignées sur une stratégie commune et des KPIs partagés ?", category: "growth" },
        { text: "Disposez-vous d'un pipeline d'innovation structuré avec des projets à différents horizons ?", category: "innovation" },
        { text: "Votre taux de succès des lancements produits dépasse-t-il 50% ?", category: "innovation" },
        { text: "Votre process d'innovation permet-il un time-to-market compétitif ?", category: "innovation" },
        { text: "L'innovation génère-t-elle plus de 20% de votre chiffre d'affaires ?", category: "innovation" },
        { text: "Vos engagements RSE sont-ils intégrés dans votre stratégie business ?", category: "rse" },
        { text: "La RSE génère-t-elle de la préférence marque mesurable chez vos consommateurs ?", category: "rse" },
        { text: "Vos collaborateurs sont-ils mobilisés et fiers de vos engagements durables ?", category: "rse" },
        { text: "Mesurez-vous le ROI de vos initiatives RSE sur le business ?", category: "rse" },
        { text: "Utilisez-vous l'IA générative pour créer du contenu marketing (textes, visuels, vidéos) ?", category: "ai" },
        { text: "Avez-vous des outils d'analyse de données augmentés par l'IA pour vos insights consommateurs ?", category: "ai" },
        { text: "Vos équipes marketing sont-elles formées aux outils d'IA et les utilisent-elles quotidiennement ?", category: "ai" },
        { text: "L'IA vous permet-elle d'automatiser des tâches répétitives et de gagner en productivité ?", category: "ai" }
      ],
      recos: {
        growth: { title: "Priorité : IQ-Growth · UNLOCK™", text: "Votre croissance et votre positionnement sont le levier le plus urgent. Un sprint de 2 à 4 semaines peut clarifier where to play et how to win.", href: "missions.html#growth", cta: "Découvrir IQ-Growth" },
        innovation: { title: "Priorité : IQ-Innovation · CREATE™", text: "Votre pipeline innovation manque de structure. CREATE™ transforme les idées dispersées en moteur de croissance prévisible.", href: "missions.html#innovation", cta: "Découvrir IQ-Innovation" },
        rse: { title: "Priorité : IQ-RSE · SUSTAIN™", text: "Vos engagements existent mais ne créent pas encore d'avantage concurrentiel. SUSTAIN™ aligne RSE, ADN de marque et business.", href: "missions.html#rse", cta: "Découvrir IQ-RSE" },
        ai: { title: "Priorité : IQ-AI · AMPLIFY™", text: "L'IA n'est pas encore un avantage compétitif pour vos équipes. AMPLIFY™ passe de l'expérimentation à l'intégration.", href: "missions.html#ai", cta: "Découvrir IQ-AI" },
        excellence: { title: "Belle maturité — approfondissons", text: "Vos scores sont solides. Un échange permettra d'identifier le prochain palier : scale, international, ou industrialisation IA.", href: "contact.html", cta: "Échanger 30 minutes" }
      }
    },
    en: {
      progress: (n, total) => `Question ${n} of ${total}`,
      next: "Next",
      prev: "Previous",
      results: "See my results",
      start: "Start the diagnostic",
      answers: ["Not at all", "Slightly", "Moderately", "Quite well", "Completely"],
      cats: { growth: "Growth", innovation: "Innovation", rse: "CSR", ai: "AI" },
      questions: [
        { text: "Does your brand have a clear, differentiated mission and positioning?", category: "growth" },
        { text: "Is your product portfolio optimized and profitable across SKUs?", category: "growth" },
        { text: "Have your market shares moved positively over the last 2 years?", category: "growth" },
        { text: "Are marketing teams aligned on a shared strategy and KPIs?", category: "growth" },
        { text: "Do you have a structured innovation pipeline across time horizons?", category: "innovation" },
        { text: "Does your product launch success rate exceed 50%?", category: "innovation" },
        { text: "Does your innovation process enable a competitive time-to-market?", category: "innovation" },
        { text: "Does innovation generate more than 20% of your revenue?", category: "innovation" },
        { text: "Are CSR commitments integrated into your business strategy?", category: "rse" },
        { text: "Does CSR create measurable brand preference among consumers?", category: "rse" },
        { text: "Are employees mobilized and proud of your sustainability agenda?", category: "rse" },
        { text: "Do you measure the business ROI of CSR initiatives?", category: "rse" },
        { text: "Do you use generative AI to create marketing content (copy, visuals, video)?", category: "ai" },
        { text: "Do you use AI-augmented analytics for consumer insights?", category: "ai" },
        { text: "Are marketing teams trained on AI tools and using them daily?", category: "ai" },
        { text: "Does AI automate repetitive tasks and improve productivity?", category: "ai" }
      ],
      recos: {
        growth: { title: "Priority: IQ-Growth · UNLOCK™", text: "Growth and positioning are your most urgent lever. A 2–4 week sprint can clarify where to play and how to win.", href: "missions.html#growth", cta: "Explore IQ-Growth" },
        innovation: { title: "Priority: IQ-Innovation · CREATE™", text: "Your innovation pipeline needs structure. CREATE™ turns scattered ideas into a predictable growth engine.", href: "missions.html#innovation", cta: "Explore IQ-Innovation" },
        rse: { title: "Priority: IQ-CSR · SUSTAIN™", text: "Commitments exist but are not yet a competitive advantage. SUSTAIN™ aligns CSR, brand DNA and business.", href: "missions.html#rse", cta: "Explore IQ-CSR" },
        ai: { title: "Priority: IQ-AI · AMPLIFY™", text: "AI is not yet a competitive advantage for your teams. AMPLIFY™ moves from experiments to integration.", href: "missions.html#ai", cta: "Explore IQ-AI" },
        excellence: { title: "Strong maturity — let's go deeper", text: "Your scores are solid. A conversation will identify the next step: scale, international, or AI industrialization.", href: "contact.html", cta: "Book 30 minutes" }
      }
    }
  }[lang];

  const questions = copy.questions;
  const answers = new Array(questions.length).fill(0);
  let current = 0;

  const intro = document.getElementById("introScreen");
  const container = document.getElementById("questionsContainer");
  const result = document.getElementById("resultContainer");
  const fill = document.getElementById("progressFill");
  const progressText = document.getElementById("progressText");
  const progressWrap = document.querySelector(".diag-progress");

  function start() {
    intro.style.display = "none";
    progressWrap.style.display = "block";
    renderQuestions();
    show(0);
  }

  function renderQuestions() {
    container.innerHTML = questions.map((q, i) => `
      <div class="q-card" id="q-${i}">
        <div class="tag">${copy.cats[q.category]} · ${i + 1}/${questions.length}</div>
        <h2 class="section-title">${q.text}</h2>
        <div class="options">
          ${copy.answers.map((label, idx) => `
            <div class="option" data-q="${i}" data-v="${idx + 1}">${label}</div>
          `).join("")}
        </div>
        <div class="nav-q">
          ${i > 0 ? `<button class="btn btn-secondary" data-prev>${copy.prev}</button>` : "<span></span>"}
          <button class="btn btn-primary" data-next disabled>${i === questions.length - 1 ? copy.results : copy.next}</button>
        </div>
      </div>
    `).join("");

    container.querySelectorAll(".option").forEach((el) => {
      el.addEventListener("click", () => {
        const i = Number(el.dataset.q);
        const v = Number(el.dataset.v);
        answers[i] = v;
        el.parentElement.querySelectorAll(".option").forEach((o) => o.classList.remove("selected"));
        el.classList.add("selected");
        container.querySelector(`#q-${i} [data-next]`).disabled = false;
      });
    });
    container.querySelectorAll("[data-next]").forEach((btn) => btn.addEventListener("click", next));
    container.querySelectorAll("[data-prev]").forEach((btn) => btn.addEventListener("click", prev));
  }

  function show(i) {
    current = i;
    container.querySelectorAll(".q-card").forEach((c, idx) => c.classList.toggle("active", idx === i));
    fill.style.width = ((i + 1) / questions.length * 100) + "%";
    progressText.textContent = copy.progress(i + 1, questions.length);
  }

  function next() {
    if (current < questions.length - 1) show(current + 1);
    else finish();
  }
  function prev() { if (current > 0) show(current - 1); }

  function avg(start) {
    return (answers[start] + answers[start + 1] + answers[start + 2] + answers[start + 3]) / 4;
  }

  function finish() {
    container.innerHTML = "";
    progressWrap.style.display = "none";
    const scores = { growth: avg(0), innovation: avg(4), rse: avg(8), ai: avg(12) };
    const average = (scores.growth + scores.innovation + scores.rse + scores.ai) / 4;
    const weakest = Object.entries(scores).sort((a, b) => a[1] - b[1])[0][0];
    const reco = average >= 4 ? copy.recos.excellence : copy.recos[weakest];
    const pct = (n) => Math.round((n / 5) * 100);

    result.innerHTML = `
      <div class="result-card">
        <div class="tag">${lang === "en" ? "Your result" : "Votre résultat"}</div>
        <h2>${reco.title}</h2>
        <p class="muted" style="margin:12px 0 24px">${reco.text}</p>
        <div class="stats">
          ${Object.keys(scores).map((k) => `
            <div class="stat"><b>${pct(scores[k])}%</b><span>${copy.cats[k]}</span></div>
          `).join("")}
        </div>
        <div class="hero-actions" style="margin-top:24px">
          <a class="btn btn-primary" href="${reco.href}">${reco.cta}</a>
          <a class="btn btn-secondary" href="contact.html">${lang === "en" ? "Talk to Gérald" : "Parler à Gérald"}</a>
        </div>
      </div>
    `;
  }

  document.getElementById("startBtn")?.addEventListener("click", start);
  if (progressWrap) progressWrap.style.display = "none";
})();
