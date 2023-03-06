/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 300,
    // reset: true
});

sr.reveal('#main-logo, .footer__container, .description-card, .message-card');
sr.reveal('.footer__info', {delay: 400});
sr.reveal('#get_start-button', {delay: 500});