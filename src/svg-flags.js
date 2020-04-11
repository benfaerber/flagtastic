window.addEventListener('DOMContentLoaded', () => {
  updateFlags();
});

function updateFlags() {
  let flags = [...document.querySelectorAll('.fl')];
  flags.forEach(flag => {
    if (flag.childElementCount === 0) {
      let classList = [...flag.classList];
      let iso = classList.find(elem => elem.includes('fl-'));
      iso = iso.replace('fl-', '');
      createFlag(iso, flag);
    }
  })
}

function createFlag(iso, parent) {
  parent.innerHTML = svgs[iso];
}

const flagCss = '.fl{margin:10px}.fl svg{width:64px}.fl-xs svg{width:16px}.fl-sm svg{width:32px}.fl-md svg{width:64px}.fl-lg svg{width:128px}.fl-xl svg{width:256px}';
function injectFlagStyles() {
  let style = document.createElement('style');
  style.innerHTML = flagCss;
  document.head.appendChild(style);
}