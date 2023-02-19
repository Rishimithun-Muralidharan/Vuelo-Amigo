/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 300,
    // reset: true
});

sr.reveal('#main-logo, .footer__container, .description-card, .message-card');
sr.reveal('.footer__info, #get_start-button', {delay: 400});