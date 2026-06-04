(function () {
  function updateBundleDiscountCopy(root) {
    var walker = document.createTreeWalker(
      root || document.body,
      NodeFilter.SHOW_TEXT,
      null
    );

    while (walker.nextNode()) {
      var node = walker.currentNode;
      if (!node.nodeValue || node.nodeValue.indexOf("10% discount") === -1) continue;

      node.nodeValue = node.nodeValue.replace(/10% discount/g, "20% discount");
    }
  }

  function initializeBundleCopyFix() {
    updateBundleDiscountCopy(document.body);

    var observer = new MutationObserver(function (mutations) {
      mutations.forEach(function (mutation) {
        mutation.addedNodes.forEach(function (node) {
          if (node.nodeType === Node.TEXT_NODE) {
            if (node.nodeValue && node.nodeValue.indexOf("10% discount") !== -1) {
              node.nodeValue = node.nodeValue.replace(/10% discount/g, "20% discount");
            }
            return;
          }

          if (node.nodeType === Node.ELEMENT_NODE) {
            updateBundleDiscountCopy(node);
          }
        });
      });
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeBundleCopyFix);
  } else {
    initializeBundleCopyFix();
  }
})();
