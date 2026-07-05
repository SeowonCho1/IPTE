(function () {
  var pageId = document.body.getAttribute('data-page-id') || location.pathname;
  var storageKey = 'ipte-understand:' + pageId;

  function loadState() {
    try { return JSON.parse(localStorage.getItem(storageKey) || '{}'); }
    catch (e) { return {}; }
  }
  function saveState(state) {
    localStorage.setItem(storageKey, JSON.stringify(state));
  }

  var state = loadState();
  var checkboxes = Array.prototype.slice.call(document.querySelectorAll('.understand-check'));
  var total = checkboxes.length;
  var rateValueEl = document.getElementById('urate-value');
  var rateDetailEl = document.getElementById('urate-detail');
  var toggleBtn = document.getElementById('toggle-unclear-btn');

  function updateRate() {
    var uncheckedCount = checkboxes.filter(function (cb) { return !cb.checked; }).length;
    var rate = total ? Math.round((uncheckedCount / total) * 100) : 100;
    if (rateValueEl) rateValueEl.textContent = rate + '%';
    if (rateDetailEl) rateDetailEl.textContent = '(이해 ' + uncheckedCount + ' / 전체 ' + total + ')';
  }

  function markCard(cb) {
    var card = cb.closest('.topic-card');
    if (card) card.classList.toggle('marked-unclear', cb.checked);
  }

  function applyFilter() {
    document.querySelectorAll('.topic-card').forEach(function (card) {
      var hasUnclear = card.classList.contains('marked-unclear') ||
        !!card.querySelector('.topic-card.marked-unclear');
      card.classList.toggle('filtered-hidden', !hasUnclear);
      if (hasUnclear) {
        var el = card.parentElement;
        while (el) {
          if (el.tagName === 'DETAILS') el.open = true;
          el = el.parentElement;
        }
      }
    });
  }

  function clearFilter() {
    document.querySelectorAll('.topic-card.filtered-hidden').forEach(function (card) {
      card.classList.remove('filtered-hidden');
    });
  }

  checkboxes.forEach(function (cb) {
    var tid = cb.getAttribute('data-tid');
    cb.checked = !!state[tid];
    markCard(cb);
    cb.addEventListener('change', function () {
      state[tid] = cb.checked;
      saveState(state);
      markCard(cb);
      updateRate();
      if (document.body.classList.contains('filter-active')) applyFilter();
    });
  });

  if (toggleBtn) {
    toggleBtn.addEventListener('click', function () {
      var active = document.body.classList.toggle('filter-active');
      toggleBtn.classList.toggle('active', active);
      toggleBtn.textContent = active ? '전체 토픽 보기' : '🔖 이해 못한 토픽만 보기';
      if (active) applyFilter(); else clearFilter();
    });
  }

  updateRate();
})();
