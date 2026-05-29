(function () {
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const supportsHover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

    const selectors = [
        '.login-container',
        '.reg-card',
        '.camera-card',
        '.reset-card',
        '.panel',
        '.exam-card',
        '.stat-tile',
        '.topic-card',
        '.status-banner',
        '.profile-modal-card',
        '.card',
        '.profile-band',
        '.stat-card',
        '.year-card',
        '.live-card',
        '.modal',
        '.qcard',
        '.review',
        '.analysis-card',
        '.question-card',
        '.modal-card'
    ];

    const allCards = () => document.querySelectorAll(selectors.join(','));

    function resetCard(card) {
        card.classList.remove('tilt-active');
        card.style.transform = '';
    }

    function bindCard(card) {
        if (!card || card.dataset.tiltBound === '1') {
            return;
        }

        card.dataset.tiltBound = '1';
        card.classList.add('tilt-surface');

        if (prefersReducedMotion || !supportsHover) {
            return;
        }

        card.addEventListener('pointermove', function (event) {
            const rect = card.getBoundingClientRect();
            if (!rect.width || !rect.height) {
                return;
            }

            const x = (event.clientX - rect.left) / rect.width;
            const y = (event.clientY - rect.top) / rect.height;
            const rotateY = (x - 0.5) * 12;
            const rotateX = (0.5 - y) * 12;

            card.classList.add('tilt-active');
            card.style.transform = `perspective(1200px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateY(-4px)`;
        });

        card.addEventListener('pointerleave', function () {
            resetCard(card);
        });

        card.addEventListener('pointercancel', function () {
            resetCard(card);
        });
    }

    function initTiltEffects() {
        allCards().forEach(bindCard);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTiltEffects);
    } else {
        initTiltEffects();
    }

    window.addEventListener('pageshow', initTiltEffects);
})();
