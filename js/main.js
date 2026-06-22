// ============================================================
//   BURGER KING BREAKFAST MENU  –  main.js
// ============================================================

(function () {
  'use strict';

  /* -----------------------------------------------------------
     SIDEBAR TOGGLE (hamburger)
  ----------------------------------------------------------- */
  const sidebar   = document.getElementById('sidebar');
  const overlay   = document.getElementById('overlay');
  const hamBtn    = document.getElementById('hamburgerBtn');

  function openSidebar()  { sidebar?.classList.add('open');   overlay?.classList.add('active'); }
  function closeSidebar() { sidebar?.classList.remove('open'); overlay?.classList.remove('active'); }

  hamBtn?.addEventListener('click', openSidebar);
  overlay?.addEventListener('click', closeSidebar);

  /* -----------------------------------------------------------
     EXPANDABLE NAV SECTIONS
  ----------------------------------------------------------- */
  document.querySelectorAll('.nav-section-header').forEach(header => {
    header.addEventListener('click', () => {
      const children = header.nextElementSibling;
      const isOpen   = header.classList.contains('open');

      // Close all
      document.querySelectorAll('.nav-section-header.open').forEach(h => {
        h.classList.remove('open');
        h.nextElementSibling?.classList.remove('open');
      });

      // Toggle clicked
      if (!isOpen) {
        header.classList.add('open');
        children?.classList.add('open');
      }
    });
  });

  // Auto-open section that contains the active link
  const activeLink = document.querySelector('.nav-link.active, .nav-top-link.active');
  if (activeLink) {
    const parentChildren = activeLink.closest('.nav-children');
    const parentHeader   = parentChildren?.previousElementSibling;
    if (parentHeader) {
      parentHeader.classList.add('open');
      parentChildren.classList.add('open');
    }
  }

  /* -----------------------------------------------------------
     SIDEBAR SEARCH FILTER
  ----------------------------------------------------------- */
  const sidebarSearch = document.getElementById('sidebarSearch');
  sidebarSearch?.addEventListener('input', () => {
    const q = sidebarSearch.value.toLowerCase().trim();
    document.querySelectorAll('.nav-link').forEach(link => {
      const text  = link.textContent.toLowerCase();
      const match = !q || text.includes(q);
      link.style.display = match ? '' : 'none';
    });
    // If searching, open all sections
    if (q) {
      document.querySelectorAll('.nav-section-header').forEach(h => {
        h.classList.add('open');
        h.nextElementSibling?.classList.add('open');
      });
    }
  });

  /* -----------------------------------------------------------
     MENU PAGE SEARCH / FILTER
  ----------------------------------------------------------- */
  const menuSearch    = document.getElementById('menuSearchInput');
  const menuCount     = document.getElementById('menuCount');
  const noResults     = document.getElementById('noResults');
  const allCards      = document.querySelectorAll('.menu-card[data-name]');
  const catSections   = document.querySelectorAll('.category-section');

  function filterMenu() {
    if (!menuSearch) return;
    const q = menuSearch.value.toLowerCase().trim();
    let visible = 0;

    allCards.forEach(card => {
      const name = card.dataset.name.toLowerCase();
      const show = !q || name.includes(q);
      card.style.display = show ? '' : 'none';
      if (show) visible++;
    });

    // Hide empty category sections
    catSections.forEach(section => {
      const hasVisible = Array.from(section.querySelectorAll('.menu-card')).some(c => c.style.display !== 'none');
      section.style.display = hasVisible ? '' : 'none';
    });

    if (menuCount) menuCount.textContent = `${visible} item${visible !== 1 ? 's' : ''}`;
    if (noResults) noResults.style.display = visible === 0 ? 'block' : 'none';
  }

  menuSearch?.addEventListener('input', filterMenu);

  /* -----------------------------------------------------------
     SCROLL FADE-IN ANIMATION
  ----------------------------------------------------------- */
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

  /* -----------------------------------------------------------
     CONTACT FORM (prevent default, show toast)
  ----------------------------------------------------------- */
  const contactForm = document.getElementById('contactForm');
  contactForm?.addEventListener('submit', e => {
    e.preventDefault();
    showToast('✅ Message sent! We\'ll respond within 30 days.');
    contactForm.reset();
  });

  function showToast(msg) {
    const t = document.createElement('div');
    t.textContent = msg;
    Object.assign(t.style, {
      position: 'fixed',
      bottom: '28px',
      right: '28px',
      background: '#1C1C1C',
      border: '1px solid #FF6B00',
      color: '#F0F0F0',
      padding: '14px 22px',
      borderRadius: '10px',
      fontFamily: 'Inter, sans-serif',
      fontSize: '0.88rem',
      boxShadow: '0 8px 32px rgba(0,0,0,0.5)',
      zIndex: '9999',
      animation: 'fadeInUp 0.3s ease',
    });
    document.body.appendChild(t);
    setTimeout(() => { t.style.opacity = '0'; t.style.transition = 'opacity 0.3s'; setTimeout(() => t.remove(), 300); }, 4000);
  }

  /* -----------------------------------------------------------
     SMOOTH ANCHOR SCROLLING
  ----------------------------------------------------------- */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        closeSidebar();
      }
    });
  });

})();
