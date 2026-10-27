
const menuToggle = document.querySelector(".menu-toggle");
const siteNav = document.querySelector(".site-nav");

const progressBar = document.createElement("div");
progressBar.className = "reading-progress";
document.body.prepend(progressBar);

const updateProgress = () => {
  const scrollable = document.documentElement.scrollHeight - window.innerHeight;
  progressBar.style.width = `${scrollable > 0 ? (window.scrollY / scrollable) * 100 : 0}%`;
};
window.addEventListener("scroll", updateProgress, { passive: true });
updateProgress();

menuToggle?.addEventListener("click", () => {
  const isOpen = siteNav.classList.toggle("open");
  menuToggle.setAttribute("aria-expanded", String(isOpen));
  menuToggle.setAttribute("aria-label", isOpen ? "Close navigation" : "Open navigation");
});

document.querySelectorAll(".site-nav a").forEach((link) => {
  link.addEventListener("click", () => {
    siteNav.classList.remove("open");
    menuToggle?.setAttribute("aria-expanded", "false");
  });
});

const currentPath = window.location.pathname.replace(/\/index\.html$/, "/");
document.querySelectorAll(".site-nav a").forEach((link) => {
  const href = link.getAttribute("href");
  if (!href || href.startsWith("http") || href.startsWith("#")) return;
  const target = new URL(href, window.location.href).pathname.replace(/\/index\.html$/, "/");
  link.classList.toggle("current", target === currentPath);
});

document.querySelectorAll("a[href]").forEach((link) => {
  const href = link.getAttribute("href");
  if (!href || href.startsWith("#") || href.startsWith("http") || href.startsWith("mailto:")) return;
  link.addEventListener("click", (event) => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    document.body.classList.add("is-leaving");
    window.setTimeout(() => {
      window.location.href = href;
    }, 190);
  });
});

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 },
);

document.querySelectorAll(".reveal").forEach((element) => revealObserver.observe(element));

const tabs = document.querySelectorAll(".dash-tab");
const panels = document.querySelectorAll(".dash-content");
const title = document.querySelector(".tab-title");
const titles = {
  overview: "Good morning, Alex",
  transactions: "Your transaction history",
  security: "Your security overview",
  settings: "Workspace settings",
};

tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    const selected = tab.dataset.tab;
    tabs.forEach((item) => item.classList.toggle("active", item === tab));
    panels.forEach((panel) => panel.classList.toggle("hidden", panel.dataset.content !== selected));
    if (title && selected in titles) title.innerHTML = `${titles[selected]} <span>✦</span>`;
  });
});

document.querySelectorAll('a[href^="#"]').forEach((link) => {
  link.addEventListener("click", (event) => {
    const target = document.querySelector(link.getAttribute("href"));
    if (!target) return;
    event.preventDefault();
    target.scrollIntoView({ behavior: "smooth", block: "start" });
  });
});

document.querySelectorAll(".copy-code").forEach((button) => {
  button.addEventListener("click", async () => {
    const code = button.closest(".code-card")?.querySelector("code")?.textContent;
    if (!code) return;
    try {
      await navigator.clipboard.writeText(code);
      const original = button.textContent;
      button.textContent = "Copied";
      window.setTimeout(() => {
        button.textContent = original;
      }, 1400);
    } catch {
      button.textContent = "Select manually";
    }
  });
});

document.querySelectorAll(".docs-toc a").forEach((link) => {
  link.addEventListener("click", () => {
    document.querySelectorAll(".docs-toc a").forEach((item) => item.classList.remove("active"));
    link.classList.add("active");
  });
});

const tocSections = document.querySelectorAll(".docs-content section[id]");
if (tocSections.length) {
  const tocObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const activeLink = document.querySelector(`.docs-toc a[href="#${entry.target.id}"]`);
        if (!activeLink) return;
        document.querySelectorAll(".docs-toc a").forEach((item) => item.classList.remove("active"));
        activeLink.classList.add("active");
      });
    },
    { rootMargin: "-20% 0px -65% 0px" },
  );
  tocSections.forEach((section) => tocObserver.observe(section));
}

const faqItems = document.querySelectorAll(".faq-list details");
if (faqItems.length) {
  const search = document.createElement("input");
  search.className = "faq-search";
  search.type = "search";
  search.placeholder = "Search questions...";
  search.setAttribute("aria-label", "Search frequently asked questions");
  document.querySelector(".faq-list")?.prepend(search);
  search.addEventListener("input", () => {
    const query = search.value.toLowerCase().trim();
    faqItems.forEach((item) => {
      item.hidden = query && !item.textContent.toLowerCase().includes(query);
    });
  });
}

const featureFilters = document.querySelectorAll(".feature-filter");
const featureCards = document.querySelectorAll(".detail-card");
if (featureFilters.length && featureCards.length) {
  const categories = ["user", "user", "user", "admin", "system", "system"];
  featureCards.forEach((card, index) => {
    if (!card.dataset.category) card.dataset.category = categories[index] || "system";
  });
  featureFilters.forEach((filter) => {
    filter.addEventListener("click", () => {
      const selected = filter.dataset.filter;
      featureFilters.forEach((item) => item.classList.toggle("active", item === filter));
      featureCards.forEach((card) => {
        const visible = selected === "all" || card.dataset.category === selected;
        card.hidden = !visible;
      });
    });
  });
}

document.querySelectorAll(".hero-card, .feature-card, .detail-card").forEach((card) => {
  card.addEventListener("pointermove", (event) => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const bounds = card.getBoundingClientRect();
    const x = (event.clientX - bounds.left) / bounds.width - 0.5;
    const y = (event.clientY - bounds.top) / bounds.height - 0.5;
    card.style.transform = `perspective(700px) rotateX(${y * -3}deg) rotateY(${x * 3}deg) translateY(-4px)`;
  });
  card.addEventListener("pointerleave", () => {
    card.style.transform = "";
  });
});

const footer = document.querySelector(".site-footer");
if (footer) {
  const favicon = document.querySelector('link[rel="icon"]');
  const assetBase = favicon?.href || document.currentScript?.src || window.location.href;
  const logoUrl = new URL("logo-circle.png", new URL(".", assetBase)).href;
  const docsPage = document.body.classList.contains("docs-page");
  const homeUrl = docsPage ? "../" : "#top";
  footer.innerHTML = `
    <div class="footer-main">
      <a class="brand" href="${homeUrl}" aria-label="Bank With High Functionalities home">
        <img src="${logoUrl}" alt="">
        <span>Bank<span class="brand-dot">.</span>HF</span>
      </a>
      <p>Designed for learning. Built for Windows.<br><b>Simulation only.</b></p>
      <button class="footer-toggle" type="button" aria-expanded="false">Explore the site <span>＋</span></button>
    </div>
    <div class="footer-panel" hidden>
      <div><span class="mini-label">DISCOVER</span><a href="${homeUrl}">Home</a><a href="${docsPage ? "../features/" : "features/"}">Capabilities</a><a href="${docsPage ? "../architecture/" : "architecture/"}">Architecture</a></div>
      <div><span class="mini-label">LEARN</span><a href="${docsPage ? "../getting-started/" : "getting-started/"}">Get started</a><a href="${docsPage ? "../faqs/" : "faqs/"}">FAQ</a><a href="${docsPage ? "../security/" : "security/"}">Security</a></div>
      <div><span class="mini-label">OPEN SOURCE</span><a href="https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities" target="_blank" rel="noreferrer">GitHub ↗</a><span class="footer-note">© 2026 Bank With High Functionalities</span></div>
    </div>
  `;
  const footerToggle = footer.querySelector(".footer-toggle");
  const footerPanel = footer.querySelector(".footer-panel");
  footerToggle?.addEventListener("click", () => {
    const expanded = footerToggle.getAttribute("aria-expanded") === "true";
    footerToggle.setAttribute("aria-expanded", String(!expanded));
    footerToggle.querySelector("span").textContent = expanded ? "＋" : "－";
    footerPanel.hidden = expanded;
  });
}
