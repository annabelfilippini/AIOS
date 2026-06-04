(() => {
  const swatchRootSelector = '.globo-swatch-product-detail';
  let polishTimer;

  function optionLabel(option) {
    const input = option.querySelector('input');
    const button = option.querySelector('.globo-style--button');
    const label = option.dataset.cooldownOptionLabel ||
      button?.getAttribute('aria-label') ||
      button?.getAttribute('title') ||
      button?.textContent ||
      option.getAttribute('data-value') ||
      option.getAttribute('title') ||
      input?.getAttribute('aria-label') ||
      input?.value ||
      option.textContent ||
      '';

    return label.trim().replace(/\s+/g, ' ');
  }

  function preserveOptionLabels() {
    document.querySelectorAll(`${swatchRootSelector} .select-option`).forEach((option) => {
      if (!option.dataset.cooldownOptionLabel) {
        const label = optionLabel(option);
        if (label) option.dataset.cooldownOptionLabel = label;
      }
    });
  }

  function syncSelectedLabels() {
    document.querySelectorAll(`${swatchRootSelector} .swatch--gl`).forEach((group) => {
      const heading = group.querySelector('.name-option');
      if (!heading) return;

      let selectedOption = group.querySelector('.select-option input:checked')?.closest('.select-option');
      if (!selectedOption && group.dataset.selectedOptionName) {
        selectedOption = [...group.querySelectorAll('.select-option')].find((option) => optionLabel(option) === group.dataset.selectedOptionName);
      }
      if (!selectedOption) {
        selectedOption = group.querySelector('.select-option.available') || group.querySelector('.select-option');
      }

      group.querySelectorAll('.globo-style--button').forEach((button) => {
        button.removeAttribute('aria-current');
        button.removeAttribute('title');
      });

      const selectedLabel = selectedOption ? optionLabel(selectedOption) : '';
      const selectedButton = selectedOption?.querySelector('.globo-style--button');
      if (selectedButton) selectedButton.setAttribute('aria-current', 'true');

      let valueLabel = heading.querySelector('.selected-option-name');
      if (!valueLabel) {
        valueLabel = document.createElement('span');
        valueLabel.className = 'selected-option-name';
        valueLabel.setAttribute('aria-live', 'polite');
        heading.append(valueLabel);
      }

      valueLabel.textContent = selectedLabel ? ` - ${selectedLabel}` : '';
    });
  }

  function cleanVariantChrome() {
    preserveOptionLabels();
    document.querySelectorAll(`${swatchRootSelector} [title]`).forEach((node) => node.removeAttribute('title'));
    document.querySelectorAll(`${swatchRootSelector} [required]`).forEach((node) => {
      node.removeAttribute('required');
      node.removeAttribute('aria-required');
    });
    document.querySelectorAll(`${swatchRootSelector} *`).forEach((node) => {
      if (node.textContent.trim() === 'This field is required') node.hidden = true;
    });
  }

  function selectSingleColorOption() {
    document.querySelectorAll(`${swatchRootSelector} ul.value.g-variant-color-detail`).forEach((list) => {
      const options = [...list.querySelectorAll('.select-option')].filter((option) => {
        return option.offsetParent !== null && !option.hidden;
      });
      const selectedInput = list.querySelector('.select-option input:checked');

      if (options.length !== 1 || selectedInput) return;

      const option = options[0];
      const input = option.querySelector('input');
      const button = option.querySelector('.globo-style--button');
      const group = option.closest('.swatch--gl');

      if (input?.disabled || option.classList.contains('globo-out-of-stock')) return;

      if (group) group.dataset.selectedOptionName = optionLabel(option);

      if (button) {
        button.click();
      } else if (input) {
        input.click();
      }

      if (input && !input.checked) {
        input.checked = true;
        input.dispatchEvent(new Event('change', { bubbles: true }));
      }
    });
  }

  function cleanDescription() {
    document.querySelectorAll('.product__description p').forEach((paragraph) => {
      paragraph.innerHTML = paragraph.innerHTML
        .replace(/[🏃📱💨🔥✨♀️\u200d\ufe0f]/gu, '')
        .replace(/<br\s*\/?>/gi, ' ');
    });
  }

  function refreshPdpPolish() {
    preserveOptionLabels();
    selectSingleColorOption();
    syncSelectedLabels();
    cleanVariantChrome();
    cleanDescription();
  }

  document.addEventListener('click', (event) => {
    const option = event.target.closest(`${swatchRootSelector} .select-option`);
    if (!option) return;

    const group = option.closest('.swatch--gl');
    if (group) group.dataset.selectedOptionName = optionLabel(option);

    window.setTimeout(refreshPdpPolish, 50);
    window.setTimeout(refreshPdpPolish, 300);
  });

  document.addEventListener('change', (event) => {
    const option = event.target.closest(`${swatchRootSelector} .select-option`);
    if (!option) return;

    const group = option.closest('.swatch--gl');
    if (group) group.dataset.selectedOptionName = optionLabel(option);

    window.setTimeout(refreshPdpPolish, 50);
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', refreshPdpPolish);
  } else {
    refreshPdpPolish();
  }

  window.setTimeout(refreshPdpPolish, 500);
  window.setTimeout(refreshPdpPolish, 1200);

  if (document.body) {
    const observer = new MutationObserver(() => {
      window.clearTimeout(polishTimer);
      polishTimer = window.setTimeout(refreshPdpPolish, 50);
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }
})();
