{
  // Mobile menu
  const btn = document.querySelector('.menu-btn');
  const menu = document.getElementById('mobile-menu');
  if (btn && menu) {
    btn.addEventListener('click', () => {
      const open = menu.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
  }

  // Contact form: sends through Web3Forms once the real key is in place
  const form = document.getElementById('contact-form');
  if (form) {
    const msg = form.querySelector('.form-msg');
    const show = (t) => { msg.textContent = t; msg.classList.add('show'); };
    form.addEventListener('submit', async (ev) => {
      ev.preventDefault();
      const key = form.querySelector('[name=access_key]').value;
      if (key.indexOf('AT_LAUNCH') !== -1) {
        show('Preview only: the form will be connected to Jia\'s email at launch.');
        return;
      }
      const btnS = form.querySelector('button[type=submit]');
      btnS.disabled = true;
      try {
        const res = await fetch(form.action, { method: 'POST', body: new FormData(form) });
        const data = await res.json();
        if (data.success) { form.reset(); show('Thank you! Your message was sent. Jia will get back to you soon.'); }
        else show('Sorry, something went wrong. Please call or email instead.');
      } catch (e) {
        show('Sorry, something went wrong. Please call or email instead.');
      }
      btnS.disabled = false;
    });
  }
}
