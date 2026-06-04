if (!window.CooldownCartAddGuard) {
  window.CooldownCartAddGuard = {
    recentAdds: [],
    originalFetch: window.fetch.bind(window),
    windowMs: 3000,

    fingerprint(formData) {
      if (!(formData instanceof FormData)) return '';

      return [
        formData.get('id'),
        formData.get('Size'),
        formData.get('Color')
      ].filter(Boolean).join('|');
    },

    record(formData) {
      const fingerprint = this.fingerprint(formData);
      if (!fingerprint) return;

      const now = Date.now();
      this.recentAdds = this.recentAdds.filter((add) => now - add.time < this.windowMs);
      this.recentAdds.push({ fingerprint, time: now });
    },

    isDuplicateAppAdd(url, init) {
      const requestUrl = new URL(url, window.location.origin);
      if (requestUrl.pathname !== `${routes.cart_add_url}.js`) return false;
      if (!init || init.method?.toUpperCase() !== 'POST') return false;

      const fingerprint = this.fingerprint(init.body);
      if (!fingerprint) return false;

      const now = Date.now();
      this.recentAdds = this.recentAdds.filter((add) => now - add.time < this.windowMs);

      return this.recentAdds.some((add) => add.fingerprint === fingerprint);
    }
  };

  window.fetch = function(input, init) {
    const url = typeof input === 'string' ? input : input?.url;

    if (url && window.CooldownCartAddGuard.isDuplicateAppAdd(url, init)) {
      return Promise.resolve(new Response(JSON.stringify({ ok: true }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      }));
    }

    return window.CooldownCartAddGuard.originalFetch(input, init);
  };
}

if (!customElements.get('product-form')) {
  customElements.define('product-form', class ProductForm extends HTMLElement {
    constructor() {
      super();

      this.form = this.querySelector('form');
      if (!this.form) return;

      const variantInput = this.form.querySelector('[name=id]');
      if (variantInput) variantInput.disabled = false;

      this.form.addEventListener('submit', this.onSubmitHandler.bind(this));
      this.cart = document.querySelector('cart-notification') || document.querySelector('cart-drawer');
      this.onSubmitButtonInteraction = this.onSubmitButtonInteraction.bind(this);

      this.bindSubmitButton();
      window.setTimeout(() => this.bindSubmitButton(), 0);
      window.setTimeout(() => this.bindSubmitButton(), 500);

      this.buttonObserver = new MutationObserver(() => this.bindSubmitButton());
      this.buttonObserver.observe(this, { childList: true, subtree: true });
    }

    bindSubmitButton() {
      const submitButton = this.querySelector('[type="submit"], button[name="add"]');
      if (!submitButton || submitButton === this.submitButton) return;

      this.submitButton = submitButton;
      this.submitButton.addEventListener('pointerup', this.onSubmitButtonInteraction, { capture: true });
      this.submitButton.addEventListener('click', this.onSubmitButtonInteraction, { capture: true });

      if (document.querySelector('cart-drawer')) this.submitButton.setAttribute('aria-haspopup', 'dialog');
    }

    onSubmitButtonInteraction(evt) {
      this.submitButton = evt.currentTarget;

      if (evt.button !== 0) return;
      if (!this.submitButton.classList.contains('cart-add')) return;

      if (this.captureSubmitInProgress) {
        evt.preventDefault();
        evt.stopImmediatePropagation();
        return;
      }

      if (this.submitButton.disabled || this.submitButton.getAttribute('aria-disabled') === 'true') return;

      this.captureSubmitInProgress = true;
      evt.preventDefault();
      evt.stopImmediatePropagation();
      this.onSubmitHandler(evt);
    }

    onSubmitHandler(evt) {
      evt.preventDefault();
      this.bindSubmitButton();
      if (!this.submitButton) return;

      if (this.submitButton.getAttribute('aria-disabled') === 'true') return;

      this.handleErrorMessage();

      this.submitButton.setAttribute('aria-disabled', true);
      this.submitButton.classList.add('loading');
      this.querySelector('.loading-overlay__spinner')?.classList.remove('hidden');

      const config = fetchConfig('javascript');
      config.headers['X-Requested-With'] = 'XMLHttpRequest';
      delete config.headers['Content-Type'];

      const formData = new FormData(this.form);
      if (this.cart) {
        formData.append('sections', this.cart.getSectionsToRender().map((section) => section.id));
        formData.append('sections_url', window.location.pathname);
        this.cart.setActiveElement(document.activeElement);
      }
      config.body = formData;
      window.CooldownCartAddGuard?.record(formData);

      fetch(`${routes.cart_add_url}`, config)
        .then((response) => response.json())
        .then((response) => {
          if (response.status) {
            this.handleErrorMessage(response.description);

            const soldOutMessage = this.submitButton.querySelector('.sold-out-message');
            if (!soldOutMessage) return;
            this.submitButton.setAttribute('aria-disabled', true);
            this.submitButton.querySelector('span').classList.add('hidden');
            soldOutMessage.classList.remove('hidden');
            this.error = true;
            return;
          } else if (!this.cart) {
            window.location = window.routes.cart_url;
            return;
          }

          this.error = false;
          const quickAddModal = this.closest('quick-add-modal');
          if (quickAddModal) {
            document.body.addEventListener('modalClosed', () => {
              setTimeout(() => { this.cart.renderContents(response) });
            }, { once: true });
            quickAddModal.hide(true);
          } else {
            this.cart.renderContents(response);
          }
        })
        .catch((e) => {
          console.error(e);
        })
        .finally(() => {
          this.captureSubmitInProgress = false;
          this.submitButton.classList.remove('loading');
          if (this.cart && this.cart.classList.contains('is-empty')) this.cart.classList.remove('is-empty');
          if (!this.error) this.submitButton.removeAttribute('aria-disabled');
          this.querySelector('.loading-overlay__spinner')?.classList.add('hidden');
        });
    }

    handleErrorMessage(errorMessage = false) {
      this.errorMessageWrapper = this.errorMessageWrapper || this.querySelector('.product-form__error-message-wrapper');
      if (!this.errorMessageWrapper) return;
      this.errorMessage = this.errorMessage || this.errorMessageWrapper.querySelector('.product-form__error-message');

      this.errorMessageWrapper.toggleAttribute('hidden', !errorMessage);

      if (errorMessage) {
        this.errorMessage.textContent = errorMessage;
      }
    }
  });
}
