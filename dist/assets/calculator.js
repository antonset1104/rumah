(() => {
  'use strict';
  const form = document.getElementById('calculator');
  const result = document.getElementById('result');
  if (!form || !result) return;

  const lang = form.dataset.lang === 'en' ? 'en' : 'id';
  const kind = form.dataset.kind;
  const fmt = (n, digits = 2) => new Intl.NumberFormat(lang === 'id' ? 'id-ID' : 'en-US', {
    maximumFractionDigits: digits,
    minimumFractionDigits: digits,
  }).format(n);
  const value = (name) => Number(form.elements.namedItem(name).value);
  const row = (label, number, unit, digits = 2) => {
    const item = document.createElement('div');
    item.className = 'result-row';
    const name = document.createElement('span');
    name.textContent = label;
    const amount = document.createElement('b');
    amount.textContent = `${fmt(number, digits)} ${unit}`;
    item.append(name, amount);
    return item;
  };
  const labels = lang === 'id' ? {
    gross: 'Dinding kotor', net: 'Dinding bersih', litres: 'Cat teoritis',
    order: 'Luas pesanan', boxes: 'Kotak utuh', actual: 'Cakupan kotak',
    badOpenings: 'Luas bukaan harus lebih kecil daripada luas dinding.',
    badNumber: 'Periksa angka: ukuran dan cakupan harus lebih dari nol.',
    notePaint: 'Bulatkan pembelian ke ukuran kaleng yang tersedia; periksa lagi daya sebar label dan kondisi permukaan.',
    noteTile: 'Jumlah kotak dibulatkan ke atas. Periksa pola, potongan tepi, stok, dan cakupan pada kemasan.',
  } : {
    gross: 'Gross walls', net: 'Net walls', litres: 'Theoretical paint',
    order: 'Order area', boxes: 'Whole boxes', actual: 'Box coverage',
    badOpenings: 'Openings must be smaller than the gross wall area.',
    badNumber: 'Check the numbers: dimensions and coverage must be above zero.',
    notePaint: 'Round a purchase to available can sizes; recheck label coverage and surface condition.',
    noteTile: 'Boxes are rounded up. Check layout, edge cuts, stock and package coverage.',
  };

  const showError = (message) => {
    result.replaceChildren();
    const title = document.createElement('strong');
    title.textContent = '—';
    const detail = document.createElement('p');
    detail.textContent = message;
    result.append(title, detail);
  };
  const show = (headline, rows, note) => {
    result.replaceChildren();
    const title = document.createElement('strong');
    title.textContent = headline;
    const list = document.createElement('div');
    list.className = 'result-rows';
    rows.forEach((item) => list.append(item));
    const detail = document.createElement('p');
    detail.textContent = note;
    result.append(title, list, detail);
  };

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    if (kind === 'cat') {
      const length = value('length');
      const width = value('width');
      const height = value('height');
      const openings = value('openings');
      const coats = value('coats');
      const coverage = value('coverage');
      if (![length, width, height, openings, coats, coverage].every(Number.isFinite) ||
          Math.min(length, width, height, coats, coverage) <= 0 || openings < 0) {
        showError(labels.badNumber); return;
      }
      const gross = 2 * (length + width) * height;
      if (openings >= gross) { showError(labels.badOpenings); return; }
      const net = gross - openings;
      const litres = net * coats / coverage;
      show(`${fmt(litres)} L`, [
        row(labels.gross, gross, 'm²'),
        row(labels.net, net, 'm²'),
        row(labels.litres, litres, 'L'),
      ], labels.notePaint);
    } else if (kind === 'keramik') {
      const area = value('floor-area');
      const allowance = value('allowance');
      const boxCoverage = value('box-coverage');
      if (![area, allowance, boxCoverage].every(Number.isFinite) ||
          Math.min(area, boxCoverage) <= 0 || allowance < 0 || allowance > 100) {
        showError(labels.badNumber); return;
      }
      const order = area * (1 + allowance / 100);
      const boxes = Math.ceil(order / boxCoverage);
      show(`${fmt(boxes, 0)} ${lang === 'id' ? 'kotak' : 'boxes'}`, [
        row(labels.order, order, 'm²'),
        row(labels.boxes, boxes, lang === 'id' ? 'kotak' : 'boxes', 0),
        row(labels.actual, boxes * boxCoverage, 'm²'),
      ], labels.noteTile);
    }
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'use_home_calculator', {tool_name: kind, page_language: lang});
    }
  });
})();
