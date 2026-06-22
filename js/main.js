// ============================================================
//   BURGER KING BREAKFAST MENU  –  main.js
// ============================================================
(function () {
  'use strict';

  /* --- SIDEBAR TOGGLE --- */
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('overlay');
  const hamBtn  = document.getElementById('hamburgerBtn');
  function openSidebar()  { sidebar?.classList.add('open');    overlay?.classList.add('active'); }
  function closeSidebar() { sidebar?.classList.remove('open'); overlay?.classList.remove('active'); }
  hamBtn?.addEventListener('click', openSidebar);
  overlay?.addEventListener('click', closeSidebar);

  /* --- EXPANDABLE NAV SECTIONS --- */
  document.querySelectorAll('.nav-section-header').forEach(header => {
    header.addEventListener('click', () => {
      const children = header.nextElementSibling;
      const isOpen   = header.classList.contains('open');
      document.querySelectorAll('.nav-section-header.open').forEach(h => { h.classList.remove('open'); h.nextElementSibling?.classList.remove('open'); });
      if (!isOpen) { header.classList.add('open'); children?.classList.add('open'); }
    });
  });
  const activeLink = document.querySelector('.nav-link.active');
  if (activeLink) {
    const parentChildren = activeLink.closest('.nav-children');
    const parentHeader   = parentChildren?.previousElementSibling;
    if (parentHeader) { parentHeader.classList.add('open'); parentChildren.classList.add('open'); }
  }

  /* --- SIDEBAR SEARCH --- */
  const sidebarSearch = document.getElementById('sidebarSearch');
  sidebarSearch?.addEventListener('input', () => {
    const q = sidebarSearch.value.toLowerCase().trim();
    document.querySelectorAll('.nav-link').forEach(link => { link.style.display = !q || link.textContent.toLowerCase().includes(q) ? '' : 'none'; });
    if (q) { document.querySelectorAll('.nav-section-header').forEach(h => { h.classList.add('open'); h.nextElementSibling?.classList.add('open'); }); }
  });

  /* --- MENU PAGE SEARCH --- */
  const menuSearch  = document.getElementById('menuSearchInput');
  const menuCount   = document.getElementById('menuCount');
  const noResults   = document.getElementById('noResults');
  const allCards    = document.querySelectorAll('.menu-card[data-name]');
  const catSections = document.querySelectorAll('.category-section');
  function filterMenu() {
    if (!menuSearch) return;
    const q = menuSearch.value.toLowerCase().trim();
    let visible = 0;
    allCards.forEach(card => { const show = !q || card.dataset.name.toLowerCase().includes(q); card.style.display = show ? '' : 'none'; if (show) visible++; });
    catSections.forEach(section => { section.style.display = Array.from(section.querySelectorAll('.menu-card')).some(c => c.style.display !== 'none') ? '' : 'none'; });
    if (menuCount) menuCount.textContent = `${visible} item${visible !== 1 ? 's' : ''}`;
    if (noResults) noResults.style.display = visible === 0 ? 'block' : 'none';
  }
  menuSearch?.addEventListener('input', filterMenu);

  /* --- FAQ ACCORDION --- */
  document.querySelectorAll('.faq-question').forEach(q => {
    q.addEventListener('click', () => {
      const answer = q.nextElementSibling;
      const isOpen = q.classList.contains('open');
      document.querySelectorAll('.faq-question.open').forEach(oq => { oq.classList.remove('open'); oq.nextElementSibling?.classList.remove('open'); });
      if (!isOpen) { q.classList.add('open'); answer?.classList.add('open'); }
    });
  });

  /* --- SCROLL FADE IN --- */
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); } });
  }, { threshold: 0.08 });
  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

  /* --- CONTACT FORM --- */
  const contactForm = document.getElementById('contactForm');
  contactForm?.addEventListener('submit', e => { e.preventDefault(); showToast('✅ Message sent! We\'ll respond within 30 days.'); contactForm.reset(); });

  function showToast(msg) {
    const t = document.createElement('div');
    t.textContent = msg;
    Object.assign(t.style, { position:'fixed', bottom:'28px', right:'28px', background:'#1C1C1C', border:'1px solid #FF6B00', color:'#F0F0F0', padding:'14px 22px', borderRadius:'10px', fontFamily:'Inter,sans-serif', fontSize:'0.88rem', boxShadow:'0 8px 32px rgba(0,0,0,0.5)', zIndex:'9999', opacity:'1', transition:'opacity 0.3s' });
    document.body.appendChild(t);
    setTimeout(() => { t.style.opacity = '0'; setTimeout(() => t.remove(), 300); }, 4000);
  }

  /* --- SMOOTH ANCHOR SCROLL --- */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth', block: 'start' }); closeSidebar(); }
    });
  });
})();
